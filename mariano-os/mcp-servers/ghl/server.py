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
    location_param: str = "locationId",
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
    params.setdefault(location_param, GHL_LOCATION_ID)

    headers = {
        "Authorization": f"Bearer {GHL_TOKEN}",
        "Version": GHL_API_VERSION,
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

    NOTA TECNICA (17 agosto 2026): esta tool es nueva y todavia no se probo
    contra la API real — el Private Integration Token actual no tiene
    habilitado el scope de notas de contacto. Hay que agregarlo desde la
    configuracion de la Private Integration en GHL, pedir un token nuevo, y
    validar esta tool de punta a punta antes de confiar en ella sin revisar
    el resultado a mano en GHL la primera vez.

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

    NOTA TECNICA (17 agosto 2026): tool nueva, todavia no probada contra la
    API real por el mismo motivo que ghl_add_contact_note (falta scope en el
    Private Integration Token). Validar de punta a punta (y revisar el
    resultado a mano en GHL la primera vez) antes de confiar en ella.

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
    t = data if isinstance(data, dict) else {}
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
