#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "mcp>=1.2.0,<2.0.0",
#   "httpx>=0.27",
#   "python-dotenv>=1.0",
# ]
# ///
"""Servidor MCP propio contra la API de GoHighLevel (GHL) para mariano-os.

Expone lectura y escritura sobre contactos, oportunidades/pipelines,
calendarios y formularios de la location de GOTIR en GHL.

Regla de escritura (ver mariano-os/CLAUDE.md, "Regla de creacion/escritura"):
toda tool que crea o modifica datos en GHL requiere que quien la llama pase
confirm=True. Si confirm=False (default), la tool devuelve un resumen de lo
que HARIA sin ejecutar nada — el llamador (Claude, en cualquier direccion de
mariano-os) tiene que describirle la accion a Mariano y esperar su
confirmacion explicita antes de volver a llamar la tool con confirm=True.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Literal

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(REPO_ROOT / ".env")

GHL_TOKEN = os.environ.get("GHL_PRIVATE_INTEGRATION_TOKEN")
GHL_LOCATION_ID = os.environ.get("GHL_LOCATION_ID")
GHL_API_VERSION = "2021-07-28"
GHL_BASE_URL = "https://services.leadconnectorhq.com"
# En las sesiones remotas de Claude Code (claude.ai/code) el trafico HTTPS
# pasa por un proxy que retermina TLS con su propia CA (ver
# /root/.ccr/README.md) — httpx no confia en ella salvo que se le pase
# explicito como `verify`. No dependemos de que SSL_CERT_FILE le llegue al
# subproceso (el launcher de MCP puede no heredar el environ completo):
# chequeamos directamente el path fijo del bundle. Si no existe (ej. Mariano
# corriendo esto en su propia maquina, sin este proxy), usamos el bundle
# default de certifi (verify=True) para una conexion TLS normal.
_CCR_CA_BUNDLE = Path(os.environ.get("SSL_CERT_FILE", "/root/.ccr/ca-bundle.crt"))
TLS_VERIFY: str | bool = str(_CCR_CA_BUNDLE) if _CCR_CA_BUNDLE.exists() else True

mcp = FastMCP("ghl")


class GHLConfigError(RuntimeError):
    pass


class GHLAPIError(RuntimeError):
    pass


async def ghl_request(
    method: str,
    path: str,
    params: dict[str, Any] | None = None,
    json_body: dict[str, Any] | None = None,
    location_param: str | None = "locationId",
    api_version: str | None = None,
) -> dict[str, Any]:
    if not GHL_TOKEN:
        raise GHLConfigError(
            "Falta GHL_PRIVATE_INTEGRATION_TOKEN. Tiene que estar en el .env de la "
            "raiz del repo (nunca versionado) — pedile el Private Integration Token "
            "de GHL a Mariano y guardalo ahi antes de reintentar."
        )
    if not GHL_LOCATION_ID:
        raise GHLConfigError("Falta GHL_LOCATION_ID en el .env de la raiz del repo.")

    params = dict(params or {})
    # La mayoria de los endpoints de GHL v2 esperan "locationId" (camelCase),
    # pero /opportunities/search es una excepcion documentada de la propia API
    # de GHL y exige "location_id" (snake_case) — de ahi este parametro.
    # Algunos endpoints (ej. GET /contacts/:id/notes) no aceptan locationId
    # de ninguna forma (ni body ni query) — pasar location_param=None para
    # esos casos y que no se agregue nada.
    if location_param is not None:
        params.setdefault(location_param, GHL_LOCATION_ID)

    headers = {
        "Authorization": f"Bearer {GHL_TOKEN}",
        # Casi todos los endpoints usan GHL_API_VERSION, pero algunos (ej.
        # POST /conversations/messages) exigen una version distinta —
        # api_version permite pisarla para esos casos puntuales.
        "Version": api_version or GHL_API_VERSION,
        "Accept": "application/json",
    }

    async with httpx.AsyncClient(
        base_url=GHL_BASE_URL, timeout=30.0, verify=TLS_VERIFY
    ) as client:
        resp = await client.request(
            method, path, params=params, json=json_body, headers=headers
        )

    if resp.status_code >= 400:
        try:
            detail = resp.json().get("message", resp.text)
        except Exception:
            detail = resp.text
        raise GHLAPIError(
            f"GHL API devolvio {resp.status_code} en {method} {path}: {detail}. "
            "Si dice 'not authorized for this scope', el Private Integration Token "
            "no tiene ese permiso habilitado — hay que agregarlo desde la "
            "configuracion de la Private Integration en GHL y pedir un token nuevo."
        )
    if not resp.text:
        return {}
    return resp.json()


def _fmt_list(items: list[str]) -> str:
    return ", ".join(items) if items else "—"


# ---------------------------------------------------------------------------
# Contactos
# ---------------------------------------------------------------------------


@mcp.tool()
async def ghl_search_contacts(query: str = "", limit: int = 20) -> str:
    """Busca contactos de GOTIR en GHL por nombre, email o telefono.

    Usa esto para encontrar el contact_id de una persona antes de leer su
    detalle completo o de crear una oportunidad asociada a ella.

    Args:
        query: Texto libre para buscar (nombre, email o telefono). Vacio =
            lista los contactos mas recientes sin filtrar.
        limit: Maximo de resultados a devolver (1-100, default 20).
    """
    limit = max(1, min(limit, 100))
    data = await ghl_request(
        "GET", "/contacts/", params={"query": query, "limit": limit}
    )
    contacts = data.get("contacts", [])
    if not contacts:
        return "No se encontraron contactos con ese criterio."

    lines = [f"{len(contacts)} contacto(s):"]
    for c in contacts:
        name = c.get("contactName") or f"{c.get('firstName', '')} {c.get('lastName', '')}".strip()
        lines.append(
            f"- {name or '(sin nombre)'} | id={c.get('id')} | "
            f"email={c.get('email') or '—'} | tel={c.get('phone') or '—'} | "
            f"tags=[{_fmt_list(c.get('tags', []))}] | fuente={c.get('source') or '—'}"
        )
    return "\n".join(lines)


@mcp.tool()
async def ghl_get_contact(contact_id: str) -> str:
    """Trae el detalle completo de un contacto de GHL por su id.

    Args:
        contact_id: id del contacto (lo devuelve ghl_search_contacts).
    """
    data = await ghl_request("GET", f"/contacts/{contact_id}")
    c = data.get("contact", data)
    return (
        f"Nombre: {c.get('contactName') or c.get('firstName')}\n"
        f"Email: {c.get('email') or '—'}\n"
        f"Telefono: {c.get('phone') or '—'}\n"
        f"Tipo: {c.get('type') or '—'}\n"
        f"Fuente: {c.get('source') or '—'}\n"
        f"Tags: {_fmt_list(c.get('tags', []))}\n"
        f"Pais: {c.get('country') or '—'}\n"
        f"Alta: {c.get('dateAdded') or '—'}\n"
        f"Ultima actualizacion: {c.get('dateUpdated') or '—'}\n"
        f"id: {c.get('id')}"
    )


@mcp.tool()
async def ghl_create_contact(
    first_name: str,
    last_name: str = "",
    email: str = "",
    phone: str = "",
    tags: list[str] | None = None,
    source: str = "",
    confirm: bool = False,
) -> str:
    """Crea un contacto nuevo en GHL. Requiere confirmacion explicita de Mariano.

    Regla del sistema: llama esta tool primero con confirm=False (o sin
    pasarlo) para ver el resumen de lo que se va a crear, describiselo a
    Mariano tal cual, y solo volve a llamarla con confirm=True despues de que
    el confirme explicitamente.

    Args:
        first_name: Nombre del contacto.
        last_name: Apellido.
        email: Email de contacto.
        phone: Telefono en formato internacional (ej. +34600000000).
        tags: Lista de tags a asignarle.
        source: Fuente/origen del contacto (ej. "WhatsApp JARVIS").
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    tags = tags or []
    body = {
        "locationId": GHL_LOCATION_ID,
        "firstName": first_name,
        "lastName": last_name or None,
        "email": email or None,
        "phone": phone or None,
        "tags": tags,
        "source": source or None,
    }
    body = {k: v for k, v in body.items() if v not in (None, "")}

    if not confirm:
        return (
            "NO EJECUTADO (falta confirmacion). Se crearia un contacto con:\n"
            f"  nombre: {first_name} {last_name}\n"
            f"  email: {email or '—'}\n"
            f"  telefono: {phone or '—'}\n"
            f"  tags: {_fmt_list(tags)}\n"
            f"  fuente: {source or '—'}\n"
            "Describile esto a Mariano y volve a llamar con confirm=True solo si el confirma."
        )

    data = await ghl_request("POST", "/contacts/", json_body=body)
    c = data.get("contact", data)
    return f"Contacto creado: {c.get('id')} — {first_name} {last_name}".strip()


@mcp.tool()
async def ghl_update_contact(
    contact_id: str,
    first_name: str = "",
    last_name: str = "",
    email: str = "",
    phone: str = "",
    tags: list[str] | None = None,
    confirm: bool = False,
) -> str:
    """Actualiza campos de un contacto existente en GHL. Requiere confirmacion.

    Solo los campos que se pasen (no vacios) se actualizan; el resto queda
    igual. Misma regla que ghl_create_contact: primero confirm=False para
    mostrarle el cambio a Mariano, despues confirm=True si el aprueba.

    Args:
        contact_id: id del contacto a actualizar.
        first_name: Nuevo nombre (vacio = no cambiar).
        last_name: Nuevo apellido (vacio = no cambiar).
        email: Nuevo email (vacio = no cambiar).
        phone: Nuevo telefono (vacio = no cambiar).
        tags: Nueva lista completa de tags (None = no cambiar; reemplaza, no suma).
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    body = {
        "firstName": first_name or None,
        "lastName": last_name or None,
        "email": email or None,
        "phone": phone or None,
        "tags": tags,
    }
    body = {k: v for k, v in body.items() if v not in (None, "")}

    if not body:
        return "No se paso ningun campo para actualizar."

    if not confirm:
        return (
            f"NO EJECUTADO (falta confirmacion). Se actualizaria el contacto {contact_id} con:\n"
            + "\n".join(f"  {k}: {v}" for k, v in body.items())
            + "\nDescribile esto a Mariano y volve a llamar con confirm=True solo si el confirma."
        )

    await ghl_request("PUT", f"/contacts/{contact_id}", json_body=body)
    return f"Contacto {contact_id} actualizado."


@mcp.tool()
async def ghl_list_contact_notes(contact_id: str) -> str:
    """Lista las notas ya cargadas en un contacto de GHL (ej. resumenes de llamadas anteriores).

    Usa esto antes de armar un mensaje de seguimiento o un resumen nuevo,
    para no repetir contexto que ya esta cargado. Cae bajo el scope
    "contacts.readonly" (GET /contacts/:contactId/notes), ya habilitado.

    Args:
        contact_id: id del contacto (lo devuelve ghl_search_contacts).
    """
    data = await ghl_request("GET", f"/contacts/{contact_id}/notes", location_param=None)
    notes = data.get("notes", [])
    if not notes:
        return "Este contacto no tiene notas cargadas."
    lines = [f"{len(notes)} nota(s):"]
    for n in notes:
        # bodyText es la version en texto plano; body trae HTML (notas que
        # vienen de Fathom, por ejemplo) — se prefiere bodyText si existe.
        texto = n.get("bodyText") or n.get("body", "")
        lines.append(
            f"--- {n.get('dateAdded') or '(sin fecha)'} (note_id={n.get('id')}) ---\n{texto}"
        )
    return "\n".join(lines)


@mcp.tool()
async def ghl_add_contact_note(
    contact_id: str,
    note: str,
    confirm: bool = False,
) -> str:
    """Agrega una nota al contacto en GHL (ej. resumen de una llamada). Requiere confirmacion.

    Pensada para el proceso de "despues de colgar" documentado en
    direcciones/comercial/CLAUDE.md: pegar el resumen de la llamada (formato
    Fathom) como nota del contacto. Misma regla que el resto de las tools de
    escritura: primero confirm=False para mostrarle el texto a Mariano,
    despues confirm=True si el aprueba.

    NOTA TECNICA (17 agosto 2026): usa el mismo scope "contacts.write" que ya
    esta habilitado en el token actual (POST /contacts/:contactId/notes cae
    bajo ese scope segun la doc oficial de GHL, no existe un scope separado
    de "notas") — no hace falta ningun permiso nuevo. Probada de punta a
    punta contra un contacto real, funciona.

    Args:
        contact_id: id del contacto al que se le agrega la nota.
        note: Texto completo de la nota.
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    if not note.strip():
        return "No se paso texto para la nota."

    if not confirm:
        return (
            f"NO EJECUTADO (falta confirmacion). Se agregaria esta nota al contacto {contact_id}:\n"
            f"---\n{note}\n---\n"
            "Describile esto a Mariano y volve a llamar con confirm=True solo si el confirma."
        )

    data = await ghl_request(
        "POST", f"/contacts/{contact_id}/notes", json_body={"body": note}
    )
    n = data.get("note", data)
    return f"Nota agregada al contacto {contact_id} (note_id={n.get('id', '?')})."


@mcp.tool()
async def ghl_create_task(
    contact_id: str,
    title: str,
    due_date: str,
    body: str = "",
    confirm: bool = False,
) -> str:
    """Crea una tarea de seguimiento asociada a un contacto en GHL. Requiere confirmacion.

    Pensada para la "proxima accion + fecha" que pide la regla de oro
    comercial (direcciones/comercial/CLAUDE.md) despues de cada llamada.
    Misma regla de confirmacion que el resto de las tools de escritura.

    NOTA TECNICA (17 agosto 2026): mismo caso que ghl_add_contact_note — usa
    el scope "contacts.write" ya habilitado, sin permisos nuevos. Probada de
    punta a punta contra un contacto real, funciona (la respuesta viene
    envuelta en {"task": {...}}, ya contemplado en el parseo).

    Args:
        contact_id: id del contacto al que se le asocia la tarea.
        title: Titulo corto de la tarea (ej. "Seguimiento Frank Sojo").
        due_date: Fecha limite en formato ISO 8601 (ej. "2026-08-19T10:00:00+02:00").
        body: Descripcion/detalle de la tarea (opcional).
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    if not title.strip():
        return "Falta el titulo de la tarea."
    if not due_date.strip():
        return "Falta la fecha limite de la tarea."

    payload = {"title": title, "dueDate": due_date, "completed": False}
    if body:
        payload["body"] = body

    if not confirm:
        return (
            f"NO EJECUTADO (falta confirmacion). Se crearia esta tarea para el contacto {contact_id}:\n"
            f"  titulo: {title}\n"
            f"  fecha limite: {due_date}\n"
            f"  detalle: {body or '—'}\n"
            "Describile esto a Mariano y volve a llamar con confirm=True solo si el confirma."
        )

    data = await ghl_request(
        "POST", f"/contacts/{contact_id}/tasks", json_body=payload
    )
    t = data.get("task", data)
    return f"Tarea creada para el contacto {contact_id} (task_id={t.get('id', '?')})."


# ---------------------------------------------------------------------------
# Pipelines / oportunidades
# ---------------------------------------------------------------------------


@mcp.tool()
async def ghl_list_pipelines() -> str:
    """Lista los pipelines comerciales de GOTIR en GHL y sus etapas, con ids.

    Usa esto primero para saber que pipeline_id/stage_id pasarle a
    ghl_search_opportunities, ghl_create_opportunity o ghl_update_opportunity.
    """
    data = await ghl_request("GET", "/opportunities/pipelines")
    pipelines = data.get("pipelines", [])
    lines = []
    for p in pipelines:
        lines.append(f"# {p.get('name')} (pipeline_id={p.get('id')})")
        for s in sorted(p.get("stages", []), key=lambda s: s.get("position", 0)):
            lines.append(f"  - {s.get('name')} (stage_id={s.get('id')})")
    return "\n".join(lines) if lines else "No hay pipelines configurados."


@mcp.tool()
async def ghl_search_opportunities(
    pipeline_id: str = "",
    stage_id: str = "",
    contact_id: str = "",
    status: Literal["open", "won", "lost", "abandoned", "all"] = "open",
    query: str = "",
    limit: int = 20,
) -> str:
    """Busca oportunidades comerciales en GHL con filtros combinables.

    Usa ghl_list_pipelines primero para conseguir pipeline_id/stage_id validos.

    Args:
        pipeline_id: Filtra por pipeline (ej. "Pre-venta"). Vacio = todos.
        stage_id: Filtra por etapa dentro del pipeline. Vacio = todas.
        contact_id: Filtra oportunidades de un contacto especifico.
        status: "open" (default), "won", "lost", "abandoned" o "all".
        query: Texto libre (busca por nombre de la oportunidad o del contacto).
        limit: Maximo de resultados (1-100, default 20).
    """
    limit = max(1, min(limit, 100))
    params: dict[str, Any] = {"limit": limit}
    if pipeline_id:
        params["pipeline_id"] = pipeline_id
    if stage_id:
        params["pipeline_stage_id"] = stage_id
    if contact_id:
        params["contact_id"] = contact_id
    if status != "all":
        params["status"] = status
    if query:
        params["q"] = query

    data = await ghl_request(
        "GET", "/opportunities/search", params=params, location_param="location_id"
    )
    opps = data.get("opportunities", [])
    if not opps:
        return "No se encontraron oportunidades con ese criterio."

    lines = [f"{len(opps)} oportunidad(es):"]
    for o in opps:
        contact = o.get("contact") or {}
        lines.append(
            f"- {o.get('name')} | id={o.get('id')} | valor={o.get('monetaryValue')} EUR | "
            f"status={o.get('status')} | pipeline_id={o.get('pipelineId')} | "
            f"stage_id={o.get('pipelineStageId')} | contacto={contact.get('name') or o.get('contactId')} | "
            f"fuente={o.get('source') or '—'} | ult. cambio etapa={o.get('lastStageChangeAt') or '—'}"
        )
    return "\n".join(lines)


@mcp.tool()
async def ghl_get_opportunity(opportunity_id: str) -> str:
    """Trae el detalle completo de una oportunidad por su id.

    Args:
        opportunity_id: id de la oportunidad (lo devuelve ghl_search_opportunities).
    """
    data = await ghl_request("GET", f"/opportunities/{opportunity_id}")
    o = data.get("opportunity", data)
    contact = o.get("contact") or {}
    return (
        f"Nombre: {o.get('name')}\n"
        f"Valor: {o.get('monetaryValue')} EUR\n"
        f"Status: {o.get('status')}\n"
        f"pipeline_id: {o.get('pipelineId')}\n"
        f"stage_id: {o.get('pipelineStageId')}\n"
        f"Contacto: {contact.get('name') or o.get('contactId')} (contact_id={o.get('contactId')})\n"
        f"Fuente: {o.get('source') or '—'}\n"
        f"Creada: {o.get('createdAt') or '—'}\n"
        f"Ultimo cambio de etapa: {o.get('lastStageChangeAt') or '—'}\n"
        f"id: {o.get('id')}"
    )


@mcp.tool()
async def ghl_create_opportunity(
    pipeline_id: str,
    stage_id: str,
    name: str,
    contact_id: str,
    monetary_value: float = 0,
    status: Literal["open", "won", "lost", "abandoned"] = "open",
    confirm: bool = False,
) -> str:
    """Crea una oportunidad nueva en un pipeline de GHL. Requiere confirmacion.

    Usa ghl_list_pipelines para conseguir pipeline_id/stage_id, y
    ghl_search_contacts para conseguir contact_id, antes de llamar esto.

    Args:
        pipeline_id: id del pipeline (de ghl_list_pipelines).
        stage_id: id de la etapa inicial dentro del pipeline.
        name: Nombre de la oportunidad (ej. "Juan Perez - Visado estudios").
        contact_id: id del contacto asociado.
        monetary_value: Valor monetario estimado en EUR (0 = sin definir).
        status: Estado inicial, normalmente "open".
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    body = {
        "locationId": GHL_LOCATION_ID,
        "pipelineId": pipeline_id,
        "pipelineStageId": stage_id,
        "name": name,
        "contactId": contact_id,
        "status": status,
    }
    if monetary_value:
        body["monetaryValue"] = monetary_value

    if not confirm:
        return (
            "NO EJECUTADO (falta confirmacion). Se crearia esta oportunidad:\n"
            f"  nombre: {name}\n"
            f"  pipeline_id: {pipeline_id} / stage_id: {stage_id}\n"
            f"  contacto: {contact_id}\n"
            f"  valor: {monetary_value or '—'} EUR | status: {status}\n"
            "Describile esto a Mariano y volve a llamar con confirm=True solo si el confirma."
        )

    data = await ghl_request("POST", "/opportunities/", json_body=body)
    o = data.get("opportunity", data)
    return f"Oportunidad creada: {o.get('id')} — {name}"


@mcp.tool()
async def ghl_update_opportunity(
    opportunity_id: str,
    stage_id: str = "",
    status: Literal["", "open", "won", "lost", "abandoned"] = "",
    monetary_value: float = -1,
    name: str = "",
    confirm: bool = False,
) -> str:
    """Mueve de etapa y/o actualiza una oportunidad existente. Requiere confirmacion.

    Este es el tool para "mover a Fulano a la etapa X del pipeline". Solo los
    campos pasados se actualizan.

    Args:
        opportunity_id: id de la oportunidad a modificar.
        stage_id: Nuevo stage_id (vacio = no cambiar etapa).
        status: Nuevo status ("open"/"won"/"lost"/"abandoned", vacio = no cambiar).
        monetary_value: Nuevo valor en EUR (-1 = no cambiar).
        name: Nuevo nombre (vacio = no cambiar).
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    body: dict[str, Any] = {}
    if stage_id:
        body["pipelineStageId"] = stage_id
    if status:
        body["status"] = status
    if monetary_value >= 0:
        body["monetaryValue"] = monetary_value
    if name:
        body["name"] = name

    if not body:
        return "No se paso ningun campo para actualizar."

    if not confirm:
        return (
            f"NO EJECUTADO (falta confirmacion). Se actualizaria la oportunidad {opportunity_id} con:\n"
            + "\n".join(f"  {k}: {v}" for k, v in body.items())
            + "\nDescribile esto a Mariano y volve a llamar con confirm=True solo si el confirma."
        )

    await ghl_request("PUT", f"/opportunities/{opportunity_id}", json_body=body)
    return f"Oportunidad {opportunity_id} actualizada."


# ---------------------------------------------------------------------------
# Calendarios
# ---------------------------------------------------------------------------


@mcp.tool()
async def ghl_list_calendars() -> str:
    """Lista los calendarios configurados en GHL (nombre, tipo, duracion de slot, id)."""
    data = await ghl_request("GET", "/calendars/")
    calendars = data.get("calendars", [])
    if not calendars:
        return "No hay calendarios configurados."
    lines = []
    for c in calendars:
        lines.append(
            f"- {c.get('name')} | id={c.get('id')} | tipo={c.get('calendarType')} | "
            f"slot={c.get('slotDuration')} {c.get('slotDurationUnit')}"
        )
    return "\n".join(lines)


@mcp.tool()
async def ghl_list_calendar_events(calendar_id: str, start_date: str, end_date: str) -> str:
    """Lista citas/eventos de un calendario en un rango de fechas.

    NOTA: esta llamada requiere que el Private Integration Token tenga el
    scope de eventos de calendario habilitado en GHL — si devuelve un error
    de "not authorized for this scope", ese scope falta en el token actual
    y hay que agregarlo desde la configuracion de la Private Integration.

    Args:
        calendar_id: id del calendario (de ghl_list_calendars).
        start_date: Fecha de inicio en formato YYYY-MM-DD.
        end_date: Fecha de fin en formato YYYY-MM-DD.
    """
    import datetime as _dt

    start_ms = int(_dt.datetime.fromisoformat(start_date).timestamp() * 1000)
    end_ms = int(_dt.datetime.fromisoformat(end_date).timestamp() * 1000)

    data = await ghl_request(
        "GET",
        "/calendars/events",
        params={"calendarId": calendar_id, "startTime": start_ms, "endTime": end_ms},
    )
    events = data.get("events", [])
    if not events:
        return "No hay eventos en ese rango."
    lines = [f"{len(events)} evento(s):"]
    for e in events:
        lines.append(
            f"- {e.get('title')} | id={e.get('id')} | inicio={e.get('startTime')} | "
            f"fin={e.get('endTime')} | status={e.get('appointmentStatus')} | "
            f"contacto={e.get('contactId')}"
        )
    return "\n".join(lines)


@mcp.tool()
async def ghl_create_appointment(
    calendar_id: str,
    contact_id: str,
    start_time: str,
    end_time: str,
    title: str = "",
    confirm: bool = False,
) -> str:
    """Agenda una cita en un calendario de GHL. Requiere confirmacion explicita.

    Args:
        calendar_id: id del calendario (de ghl_list_calendars).
        contact_id: id del contacto para el que se agenda.
        start_time: Inicio en formato ISO 8601 (ej. "2026-08-20T15:00:00+02:00").
        end_time: Fin en formato ISO 8601.
        title: Titulo de la cita (opcional).
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    body = {
        "locationId": GHL_LOCATION_ID,
        "calendarId": calendar_id,
        "contactId": contact_id,
        "startTime": start_time,
        "endTime": end_time,
        "title": title or None,
    }
    body = {k: v for k, v in body.items() if v not in (None, "")}

    if not confirm:
        return (
            "NO EJECUTADO (falta confirmacion). Se agendaria:\n"
            f"  calendario: {calendar_id}\n"
            f"  contacto: {contact_id}\n"
            f"  desde: {start_time} hasta: {end_time}\n"
            f"  titulo: {title or '—'}\n"
            "Describile esto a Mariano y volve a llamar con confirm=True solo si el confirma."
        )

    data = await ghl_request("POST", "/calendars/events/appointments", json_body=body)
    a = data.get("event", data)
    return f"Cita creada: {a.get('id')}"


@mcp.tool()
async def ghl_update_appointment_status(
    appointment_id: str,
    status: Literal["confirmed", "showed", "noshow", "cancelled", "invalid"],
    confirm: bool = False,
) -> str:
    """Marca el estado real de una cita (showed/noshow/etc.) en GHL. Requiere confirmacion.

    Pensada para el paso 5 del checklist "Despues de colgar"
    (direcciones/comercial/CLAUDE.md): marcar `showed` si la llamada se
    realizo o `noshow` si el contacto no se presento, en el campo real que
    lee el panel de estadisticas de Mariano (`appointmentStatus` del evento
    de calendario, PUT /calendars/events/appointments/{id} — ver seccion
    3.1.1 de ese documento, que hasta ahora este paso se hacia solo a mano en
    la UI de GHL porque el servidor no tenia esta tool).

    NOTA TECNICA: usa el scope `calendars/events.write`, ya habilitado en el
    token (mismo scope que usa la lectura de `ghl_list_calendar_events`).

    Args:
        appointment_id: id de la cita (lo devuelve ghl_list_calendar_events).
        status: nuevo estado — "confirmed", "showed", "noshow", "cancelled" o "invalid".
        confirm: Poner True solo despues de que Mariano confirmo la accion.
    """
    if not confirm:
        return (
            f"NO EJECUTADO (falta confirmacion). Se marcaria la cita {appointment_id} como "
            f"'{status}'.\nDescribile esto a Mariano y volve a llamar con confirm=True solo "
            "si el confirma."
        )

    await ghl_request(
        "PUT",
        f"/calendars/events/appointments/{appointment_id}",
        json_body={"appointmentStatus": status},
    )
    return f"Cita {appointment_id} marcada como '{status}'."


# ---------------------------------------------------------------------------
# Formularios
# ---------------------------------------------------------------------------


@mcp.tool()
async def ghl_list_forms() -> str:
    """Lista los formularios configurados en GHL (nombre e id).

    NOTA: la API publica de GHL no ofrece un endpoint para crear formularios
    nuevos — solo se pueden listar y leer submissions de los que ya existen
    (se crean a mano en el builder de GHL). Este tool solo cubre lectura.
    """
    data = await ghl_request("GET", "/forms/")
    forms = data.get("forms", [])
    if not forms:
        return "No hay formularios configurados."
    return "\n".join(f"- {f.get('name')} | id={f.get('id')}" for f in forms)


@mcp.tool()
async def ghl_get_form_submissions(form_id: str, limit: int = 20) -> str:
    """Lista las ultimas respuestas (submissions) de un formulario de GHL.

    Args:
        form_id: id del formulario (de ghl_list_forms).
        limit: Maximo de submissions a devolver (1-100, default 20).
    """
    limit = max(1, min(limit, 100))
    data = await ghl_request(
        "GET", "/forms/submissions", params={"formId": form_id, "limit": limit}
    )
    subs = data.get("submissions", [])
    if not subs:
        return "No hay submissions para ese formulario."
    lines = [f"{len(subs)} submission(s):"]
    for s in subs:
        lines.append(
            f"- {s.get('name') or '(sin nombre)'} | email={s.get('email') or '—'} | "
            f"contact_id={s.get('contactId')} | submission_id={s.get('id')}"
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Mensajeria / conversaciones
# ---------------------------------------------------------------------------


@mcp.tool()
async def ghl_send_message(
    contact_id: str,
    message: str,
    channel: Literal["WhatsApp", "SMS", "Email"] = "WhatsApp",
    confirm: bool = False,
) -> str:
    """Manda un mensaje (por defecto WhatsApp) a un contacto de GHL. Requiere confirmacion explicita.

    Sale desde el numero de WhatsApp de GOTIR conectado en GHL (+34603289674,
    el mismo que aparece en el tag "wa: +34603289674" de los contactos que ya
    tuvieron conversacion por ahi) — no hace falta elegir remitente, GHL usa
    el canal ya conectado en la location. Accion IRREVERSIBLE (es un mensaje
    real a un cliente): primero confirm=False para mostrarle a Mariano el
    texto exacto y el destinatario, y solo confirm=True despues de que el
    confirme explicitamente ESE mensaje para ESA persona.

    NOTA TECNICA (17 agosto 2026): POST /conversations/messages exige el
    header Version 2021-04-15 (distinto del default 2021-07-28 que usa el
    resto del servidor) — por eso pasa api_version explicito. El scope
    necesario es "conversations/message.write", ya habilitado en el token.

    ADVERTENCIA IMPORTANTE (probada 17 agosto 2026 con un mensaje real que
    NO llego a destino): esta API devuelve 201 con un message_id apenas
    ACEPTA el pedido en su cola — eso no confirma entrega real. Si el canal
    de WhatsApp de la location esta desconectado (pasa con integraciones no
    oficiales, no la WhatsApp Business Platform de Meta), GHL igual responde
    201 y el mensaje queda visible en el panel de Conversaciones con un
    icono de advertencia y "Try again", sin llegar nunca al contacto. Esta
    tool no puede verificar eso por si sola todavia (falta el scope
    conversations/message.readonly para poder chequear el estado real del
    mensaje despues de mandarlo) — despues de llamarla con confirm=True,
    quien la use tiene que pedirle a Mariano que confirme en el panel de
    GHL (Conversaciones) que el mensaje se ve entregado, no asumir exito
    solo por la respuesta 201 de esta tool.

    ACTUALIZACION (21 agosto 2026): el reseller anterior de GHL dejo de dar servicio y la
    migracion se quedo sin proveedor de WhatsApp conectado (ver
    direcciones/comercial/CLAUDE.md seccion 6/10) — Mariano ya lo reconecto con un proveedor
    nuevo, GoGHL.ai (`app.goghl.ai`), con los 4 numeros reales de GOTIR dados de alta y
    "Conectado" (incluido +34603289674, el que usa esta tool). El problema de fondo debería
    estar resuelto, pero esta tool todavia no se volvio a probar de punta a punta con un envio
    real desde que se reconecto — seguir chequeando el panel de Conversaciones despues de cada
    envio hasta confirmarlo con un caso real.

    Args:
        contact_id: id del contacto destinatario (lo devuelve ghl_search_contacts).
        message: Texto del mensaje a enviar.
        channel: "WhatsApp" (default), "SMS" o "Email".
        confirm: Poner True solo despues de que Mariano confirmo este mensaje puntual.
    """
    if not message.strip():
        return "No se paso texto para el mensaje."

    if not confirm:
        return (
            f"NO EJECUTADO (falta confirmacion). Se mandaria por {channel} al contacto "
            f"{contact_id}:\n---\n{message}\n---\n"
            "Describile esto a Mariano tal cual y volve a llamar con confirm=True solo "
            "si el confirma explicitamente este mensaje para esta persona."
        )

    body = {
        "type": channel,
        "contactId": contact_id,
        "message": message,
    }
    if channel == "WhatsApp":
        body["fromNumber"] = "+34603289674"

    data = await ghl_request(
        "POST",
        "/conversations/messages",
        json_body=body,
        location_param=None,
        api_version="2021-04-15",
    )
    m = data.get("message", data)
    msg_id = m.get("id", data.get("messageId", "?"))
    return (
        f"GHL acepto el mensaje al contacto {contact_id} (message_id={msg_id}), status 2xx. "
        "OJO: esto NO confirma entrega real (ver advertencia en la descripcion de esta tool) — "
        "pedile a Mariano que confirme en el panel de Conversaciones de GHL que el mensaje se "
        "ve entregado antes de darlo por mandado."
    )


@mcp.tool()
async def ghl_read_conversation(contact_id: str, limit: int = 20) -> str:
    """Lee el historial real de mensajes (WhatsApp/SMS/Email) con un contacto de GHL.

    Usa esto SIEMPRE antes de proponerle a Mariano un mensaje de seguimiento
    nuevo para un contacto — instruccion explicita suya (17 agosto 2026): "ve
    al chat de whatsapp y lee que fue lo ultimo se hablo" antes de redactar
    cualquier propuesta. No asumas que las notas de GHL o lo que Mariano
    recuerda de memoria son el ultimo intercambio real.

    NOTA TECNICA: requiere el scope "conversations/message.readonly" (distinto
    del de escritura). Si devuelve 401, ese scope no esta habilitado todavia.

    LIMITACION CONOCIDA (verificada 17 agosto 2026): si un mensaje es un nota
    de voz de WhatsApp (audio), esta tool NO lo transcribe — el entorno de
    Claude Code Remote bloquea por politica de proxy el acceso a los hosts
    donde viven los modelos de transcripcion (Hugging Face, Azure), asi que no
    se pudo montar transcripcion automatica ahi. Esos mensajes se marcan como
    "[audio, sin transcribir]" en la salida — para esos casos hay que seguir
    pidiendole a Mariano que cuente el contenido, como se viene haciendo.

    Args:
        contact_id: id del contacto (lo devuelve ghl_search_contacts).
        limit: maximo de mensajes a traer, del mas reciente al mas viejo (1-100, default 20).
    """
    limit = max(1, min(limit, 100))
    search = await ghl_request(
        "GET", "/conversations/search", params={"contactId": contact_id, "limit": 1}
    )
    convs = search.get("conversations", [])
    if not convs:
        return "Este contacto no tiene ninguna conversacion registrada en GHL."
    conversation_id = convs[0]["id"]

    data = await ghl_request(
        "GET",
        f"/conversations/{conversation_id}/messages",
        params={"limit": limit},
        location_param=None,
    )
    messages = data.get("messages", {}).get("messages", [])
    if not messages:
        return "La conversacion existe pero no tiene mensajes."

    AUDIO_EXT = (".ogg", ".oga", ".opus", ".mp3", ".m4a", ".wav", ".aac", ".amr")
    lines = [f"{len(messages)} mensaje(s) (del mas reciente al mas viejo):"]
    for m in messages:
        direction = "ENTRANTE (contacto)" if m.get("direction") == "inbound" else "saliente (GOTIR)"
        fecha = m.get("dateAdded", "?")
        tipo = m.get("messageType", "?")
        body = (m.get("body") or "").strip()
        attachments = m.get("attachments") or []
        audio_flags = [a for a in attachments if a.lower().endswith(AUDIO_EXT)]
        if audio_flags:
            body = (body + " " if body else "") + f"[audio, sin transcribir: {audio_flags[0]}]"
        if not body:
            # actividades internas (cambio de etapa, cita creada, etc.) sin texto
            activity = m.get("activity", {})
            body = f"(actividad interna: {activity.get('title', tipo)})"
        lines.append(f"--- {fecha} | {direction} | tipo={tipo} ---\n{body}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Usuarios
# ---------------------------------------------------------------------------


@mcp.tool()
async def ghl_list_users() -> str:
    """Lista los usuarios (staff/colaboradores) configurados en la location de GHL."""
    data = await ghl_request("GET", "/users/", params={})
    users = data.get("users", [])
    if not users:
        return "No hay usuarios configurados."
    lines = [f"{len(users)} usuario(s):"]
    for u in users:
        role = u.get("roles", {})
        lines.append(
            f"- {u.get('name')} | id={u.get('id')} | email={u.get('email') or '—'} | "
            f"rol={role.get('role') or '—'} | dado_de_baja={u.get('deleted', False)}"
        )
    return "\n".join(lines)


@mcp.tool()
async def ghl_delete_user(user_id: str, user_name: str, confirm: bool = False) -> str:
    """Borra (da de baja) un usuario de GHL. Requiere confirmacion explicita de Mariano.

    Accion irreversible por API — borrar un usuario no se puede deshacer
    llamando esta misma tool al reves. Misma regla que el resto de las tools
    de escritura: primero confirm=False para mostrarle a Mariano exactamente
    quien se borraria, y solo confirm=True despues de que el confirme
    explicitamente cada persona por nombre.

    Args:
        user_id: id del usuario a borrar (lo devuelve ghl_list_users).
        user_name: nombre del usuario, solo para mostrarlo en el mensaje de
            confirmacion (no se manda a la API).
        confirm: Poner True solo despues de que Mariano confirmo la accion
            para ESTA persona en particular.
    """
    if not confirm:
        return (
            f"NO EJECUTADO (falta confirmacion). Se borraria el usuario '{user_name}' "
            f"(id={user_id}) de GHL — esto NO se puede deshacer.\n"
            "Describile esto a Mariano y volve a llamar con confirm=True solo si el confirma "
            "explicitamente esta persona."
        )

    await ghl_request("DELETE", f"/users/{user_id}")
    return f"Usuario '{user_name}' (id={user_id}) borrado de GHL."


# ---------------------------------------------------------------------------
# Location
# ---------------------------------------------------------------------------


@mcp.tool()
async def ghl_get_location() -> str:
    """Trae los datos generales de la location de GOTIR configurada en GHL."""
    data = await ghl_request("GET", f"/locations/{GHL_LOCATION_ID}")
    loc = data.get("location", data)
    return (
        f"Nombre: {loc.get('name')}\n"
        f"Direccion: {loc.get('address')}, {loc.get('city')}, {loc.get('state')} {loc.get('postalCode')}\n"
        f"Pais: {loc.get('country')}\n"
        f"Zona horaria: {loc.get('timezone')}\n"
        f"Sitio web: {loc.get('website')}\n"
        f"Email: {loc.get('email')}\n"
        f"Telefono: {loc.get('phone')}\n"
        f"Moneda: {loc.get('currency')}\n"
        f"id: {loc.get('id')}"
    )


if __name__ == "__main__":
    mcp.run()
