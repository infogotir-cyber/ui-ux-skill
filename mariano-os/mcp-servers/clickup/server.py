#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "mcp>=1.2.0,<2.0.0",
#   "httpx>=0.27",
#   "python-dotenv>=1.0",
# ]
# ///
"""Servidor MCP propio contra la API REST de ClickUp para mariano-os.

Por que existe (18 agosto 2026): el conector oficial mcp.clickup.com (OAuth)
tiene un limite propio de MCP separado del limite general de la API — 300
llamadas / 24hs en planes Unlimited/Business, ventana movil, sin resetear
rapido — que dejo el sync diario de Ruge bloqueado mas de un dia. Ese limite
de "MCP" solo aplica al servidor alojado por ClickUp; llamando directo a
api.clickup.com con un token personal se usa el limite normal de la API REST
(100 req/min en Business, ver developer.clickup.com/docs/rate-limits), que
alcanza sobrado para cientos de tareas por dia. Este servidor hace eso.

Regla de escritura para ClickUp (ver mariano-os/CLAUDE.md, "Regla de
creacion/escritura"): a diferencia de GHL, ClickUp se puede crear/modificar
DIRECTO, sin pedir confirmacion previa — instruccion explicita de Mariano.
Por eso estas tools no tienen parametro confirm, a diferencia de las de GHL.
"""

from __future__ import annotations

import asyncio
import os
import time
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(REPO_ROOT / ".env")

CLICKUP_TOKEN = os.environ.get("CLICKUP_API_TOKEN")
# Team/Workspace ID de GOTIR en ClickUp, documentado en mariano-os/CLAUDE.md.
# Se puede pisar con la env var si algun dia hace falta apuntar a otro team.
CLICKUP_TEAM_ID = os.environ.get("CLICKUP_TEAM_ID", "90121963418")
CLICKUP_BASE_URL = "https://api.clickup.com/api/v2"

# Mismo mecanismo que mcp-servers/ghl/server.py: en las sesiones remotas de
# Claude Code el trafico HTTPS pasa por un proxy que retermina TLS con su
# propia CA — httpx no confia en ella salvo que se le pase explicito como
# `verify`. Se chequea el path fijo del bundle en vez de depender de que
# SSL_CERT_FILE le llegue al subproceso (el launcher de MCP puede no heredar
# el environ completo).
_CCR_CA_BUNDLE = Path(os.environ.get("SSL_CERT_FILE", "/root/.ccr/ca-bundle.crt"))
TLS_VERIFY: str | bool = str(_CCR_CA_BUNDLE) if _CCR_CA_BUNDLE.exists() else True

mcp = FastMCP("clickup")


class ClickUpConfigError(RuntimeError):
    pass


class ClickUpAPIError(RuntimeError):
    pass


# ---------------------------------------------------------------------------
# Pacing: nos quedamos bien por debajo del limite real de la API (100/min en
# Business) para no volver a pisar un 429 nunca — sin esto, una tanda de
# tareas en loop dispara todas las llamadas en rafaga como paso con el MCP
# oficial. No es un rate limiter sofisticado, alcanza con espaciar llamadas.
# ---------------------------------------------------------------------------
_MIN_INTERVAL_SECONDS = 0.7  # ~85 req/min como techo, con margen sobre 100/min
_last_request_at = 0.0
_pacing_lock = asyncio.Lock()


async def _pace() -> None:
    global _last_request_at
    async with _pacing_lock:
        wait = _last_request_at + _MIN_INTERVAL_SECONDS - time.monotonic()
        if wait > 0:
            await asyncio.sleep(wait)
        _last_request_at = time.monotonic()


async def clickup_request(
    method: str,
    path: str,
    params: dict[str, Any] | None = None,
    json_body: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not CLICKUP_TOKEN:
        raise ClickUpConfigError(
            "Falta CLICKUP_API_TOKEN. Tiene que estar en el .env de la raiz del "
            "repo (nunca versionado) — generalo en ClickUp: tu perfil -> My "
            "Settings -> Apps -> Generate (API Token), y guardalo ahi antes de "
            "reintentar."
        )

    await _pace()

    headers = {
        # ClickUp acepta el Personal API Token directo en Authorization, sin
        # esquema "Bearer" (a diferencia de GHL).
        "Authorization": CLICKUP_TOKEN,
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(
        base_url=CLICKUP_BASE_URL, timeout=30.0, verify=TLS_VERIFY
    ) as client:
        resp = await client.request(
            method, path, params=params, json=json_body, headers=headers
        )

    if resp.status_code == 429:
        reset = resp.headers.get("X-RateLimit-Reset")
        reset_msg = f" (X-RateLimit-Reset={reset})" if reset else ""
        raise ClickUpAPIError(
            f"ClickUp devolvio 429 (rate limit) en {method} {path}{reset_msg}. "
            "Esto es la API REST directa (100 req/min en Business) — si esto "
            "aparece, hubo una rafaga real de este proceso o algo mas esta "
            "usando el mismo token en paralelo. No reintentar en loop: avisar "
            "y reprogramar para mas tarde."
        )
    if resp.status_code >= 400:
        try:
            detail = resp.json().get("err", resp.text)
        except Exception:
            detail = resp.text
        raise ClickUpAPIError(
            f"ClickUp API devolvio {resp.status_code} en {method} {path}: {detail}"
        )
    if not resp.text:
        return {}
    return resp.json()


def _fmt_list(items: list[str]) -> str:
    return ", ".join(items) if items else "—"


# ---------------------------------------------------------------------------
# Miembros del workspace
# ---------------------------------------------------------------------------


@mcp.tool()
async def clickup_get_workspace_members() -> str:
    """Lista todos los miembros del workspace de ClickUp de GOTIR, con su user_id.

    Usa esto (o clickup_find_member_by_name para un caso puntual) para
    conseguir los user_id que necesitan clickup_create_task/clickup_update_task
    al asignar tareas.
    """
    data = await clickup_request("GET", "/team")
    teams = data.get("teams", [])
    team = next((t for t in teams if t.get("id") == CLICKUP_TEAM_ID), None)
    if team is None and teams:
        team = teams[0]
    if team is None:
        return "No se encontro el workspace configurado (CLICKUP_TEAM_ID)."

    members = team.get("members", [])
    if not members:
        return "El workspace no tiene miembros."
    lines = [f"{len(members)} miembro(s) del workspace:"]
    for m in members:
        u = m.get("user", m)
        lines.append(
            f"- {u.get('username') or u.get('email')} | user_id={u.get('id')} | "
            f"email={u.get('email') or '—'}"
        )
    return "\n".join(lines)


@mcp.tool()
async def clickup_find_member_by_name(name_or_email: str) -> str:
    """Busca un miembro del workspace por nombre (parcial, case-insensitive) o email exacto.

    Args:
        name_or_email: Texto a buscar en username/email (ej. "Marco" o "julio@gotir.es").
    """
    data = await clickup_request("GET", "/team")
    teams = data.get("teams", [])
    team = next((t for t in teams if t.get("id") == CLICKUP_TEAM_ID), None)
    if team is None and teams:
        team = teams[0]
    if team is None:
        return "No se encontro el workspace configurado (CLICKUP_TEAM_ID)."

    needle = name_or_email.strip().lower()
    matches = []
    for m in team.get("members", []):
        u = m.get("user", m)
        username = (u.get("username") or "").lower()
        email = (u.get("email") or "").lower()
        if needle == email or needle in username:
            matches.append(u)

    if not matches:
        return f"No se encontro ningun miembro que coincida con '{name_or_email}'."
    if len(matches) > 1:
        lines = [f"{len(matches)} coincidencias para '{name_or_email}' (elegi por user_id):"]
        for u in matches:
            lines.append(f"- {u.get('username')} | user_id={u.get('id')} | email={u.get('email')}")
        return "\n".join(lines)

    u = matches[0]
    return f"{u.get('username')} | user_id={u.get('id')} | email={u.get('email') or '—'}"


# ---------------------------------------------------------------------------
# Listas y campos
# ---------------------------------------------------------------------------


@mcp.tool()
async def clickup_get_list(list_id: str) -> str:
    """Trae el detalle de una lista de ClickUp (nombre, espacio, estados configurados).

    Args:
        list_id: id de la lista.
    """
    data = await clickup_request("GET", f"/list/{list_id}")
    statuses = ", ".join(s.get("status", "?") for s in data.get("statuses", []))
    space = data.get("space", {})
    folder = data.get("folder", {})
    return (
        f"Nombre: {data.get('name')}\n"
        f"id: {data.get('id')}\n"
        f"space: {space.get('name')} (id={space.get('id')})\n"
        f"folder: {folder.get('name') or '—'} (id={folder.get('id') or '—'})\n"
        f"tareas: {data.get('task_count', '?')}\n"
        f"estados: {statuses or '—'}"
    )


@mcp.tool()
async def clickup_get_custom_fields(list_id: str) -> str:
    """Lista los custom fields configurados en una lista de ClickUp, con sus id.

    Args:
        list_id: id de la lista.
    """
    data = await clickup_request("GET", f"/list/{list_id}/field")
    fields = data.get("fields", [])
    if not fields:
        return "Esta lista no tiene custom fields configurados."
    lines = [f"{len(fields)} custom field(s):"]
    for f in fields:
        lines.append(f"- {f.get('name')} | id={f.get('id')} | tipo={f.get('type')}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Tareas
# ---------------------------------------------------------------------------


@mcp.tool()
async def clickup_get_task(task_id: str) -> str:
    """Trae el detalle completo de una tarea de ClickUp por su id.

    Args:
        task_id: id de la tarea.
    """
    data = await clickup_request("GET", f"/task/{task_id}")
    assignees = [a.get("username", "?") for a in data.get("assignees", [])]
    return (
        f"Nombre: {data.get('name')}\n"
        f"id: {data.get('id')}\n"
        f"status: {(data.get('status') or {}).get('status', '?')}\n"
        f"assignees: {_fmt_list(assignees)}\n"
        f"due_date: {data.get('due_date') or '—'}\n"
        f"priority: {(data.get('priority') or {}).get('priority', '—')}\n"
        f"list: {(data.get('list') or {}).get('name', '?')}\n"
        f"url: {data.get('url')}"
    )


@mcp.tool()
async def clickup_filter_tasks(
    list_id: str,
    statuses: list[str] | None = None,
    include_closed: bool = False,
    page: int = 0,
) -> str:
    """Lista tareas de una lista de ClickUp, con filtro opcional de status. Paginado (100/pagina).

    Si la respuesta dice "hay mas paginas", volve a llamar con page+1 hasta
    traer todo.

    Args:
        list_id: id de la lista.
        statuses: Filtra por status (ej. ["to do", "en progreso"]). None = todos.
        include_closed: Incluir tareas cerradas/completadas.
        page: Pagina 0-indexada (100 tareas por pagina).
    """
    params: dict[str, Any] = {"page": page, "subtasks": "true"}
    if include_closed:
        params["include_closed"] = "true"
    if statuses:
        params["statuses[]"] = statuses

    data = await clickup_request("GET", f"/list/{list_id}/task", params=params)
    tasks = data.get("tasks", [])
    if not tasks:
        return "No hay tareas que coincidan con ese filtro en esta pagina."

    lines = [f"{len(tasks)} tarea(s) en la pagina {page}:"]
    for t in tasks:
        assignees = [a.get("username", "?") for a in t.get("assignees", [])]
        lines.append(
            f"- {t.get('name')} | id={t.get('id')} | status={(t.get('status') or {}).get('status', '?')} | "
            f"assignees=[{_fmt_list(assignees)}]"
        )
    if not data.get("last_page", True):
        lines.append(f"(hay mas paginas — volve a llamar con page={page + 1})")
    return "\n".join(lines)


@mcp.tool()
async def clickup_create_task(
    list_id: str,
    name: str,
    description: str = "",
    assignees: list[str] | None = None,
    due_date: str = "",
    priority: int = 0,
    status: str = "",
) -> str:
    """Crea una tarea nueva en una lista de ClickUp. Se ejecuta directo, sin confirmacion previa.

    Args:
        list_id: id de la lista donde crear la tarea.
        name: Titulo de la tarea.
        description: Descripcion (markdown soportado).
        assignees: Lista de user_id (de clickup_find_member_by_name) a asignar.
        due_date: Fecha limite en formato YYYY-MM-DD o YYYY-MM-DD HH:MM. Vacio = sin fecha.
        priority: 1=urgente, 2=alta, 3=normal, 4=baja. 0 = sin prioridad.
        status: Status inicial (debe existir en la lista). Vacio = default de la lista.
    """
    import datetime as _dt

    body: dict[str, Any] = {"name": name}
    if description:
        body["markdown_description"] = description
    if assignees:
        body["assignees"] = [int(a) for a in assignees]
    if due_date:
        fmt = "%Y-%m-%d %H:%M" if " " in due_date else "%Y-%m-%d"
        ts = int(_dt.datetime.strptime(due_date, fmt).timestamp() * 1000)
        body["due_date"] = ts
    if priority:
        body["priority"] = priority
    if status:
        body["status"] = status

    data = await clickup_request("POST", f"/list/{list_id}/task", json_body=body)
    return f"Tarea creada: {data.get('id')} — {name} (url={data.get('url')})"


@mcp.tool()
async def clickup_update_task(
    task_id: str,
    name: str = "",
    status: str = "",
    due_date: str = "",
    priority: int = 0,
    assignees_add: list[str] | None = None,
    assignees_rem: list[str] | None = None,
) -> str:
    """Actualiza una tarea existente de ClickUp. Se ejecuta directo, sin confirmacion previa.

    Solo los campos pasados (no vacios/no-cero/no-None) se modifican.

    Args:
        task_id: id de la tarea a actualizar.
        name: Nuevo nombre (vacio = no cambiar).
        status: Nuevo status, debe existir en la lista (vacio = no cambiar).
        due_date: Nueva fecha limite YYYY-MM-DD o YYYY-MM-DD HH:MM (vacio = no cambiar).
        priority: 1=urgente, 2=alta, 3=normal, 4=baja (0 = no cambiar).
        assignees_add: user_id(s) a agregar como asignados.
        assignees_rem: user_id(s) a quitar de asignados.
    """
    import datetime as _dt

    body: dict[str, Any] = {}
    if name:
        body["name"] = name
    if status:
        body["status"] = status
    if due_date:
        fmt = "%Y-%m-%d %H:%M" if " " in due_date else "%Y-%m-%d"
        ts = int(_dt.datetime.strptime(due_date, fmt).timestamp() * 1000)
        body["due_date"] = ts
    if priority:
        body["priority"] = priority
    if assignees_add or assignees_rem:
        body["assignees"] = {
            "add": [int(a) for a in (assignees_add or [])],
            "rem": [int(a) for a in (assignees_rem or [])],
        }

    if not body:
        return "No se paso ningun campo para actualizar."

    await clickup_request("PUT", f"/task/{task_id}", json_body=body)
    return f"Tarea {task_id} actualizada: " + ", ".join(f"{k}" for k in body)


@mcp.tool()
async def clickup_set_custom_field(task_id: str, field_id: str, value: str) -> str:
    """Setea el valor de un custom field en una tarea. Se ejecuta directo, sin confirmacion previa.

    Args:
        task_id: id de la tarea.
        field_id: id del custom field (lo devuelve clickup_get_custom_fields).
        value: Valor a setear (texto/numero como string; para dropdown, el UUID de la opcion).
    """
    await clickup_request(
        "POST", f"/task/{task_id}/field/{field_id}", json_body={"value": value}
    )
    return f"Custom field {field_id} de la tarea {task_id} actualizado."


@mcp.tool()
async def clickup_create_comment(task_id: str, comment_text: str) -> str:
    """Agrega un comentario a una tarea de ClickUp. Se ejecuta directo, sin confirmacion previa.

    Args:
        task_id: id de la tarea.
        comment_text: Texto del comentario.
    """
    data = await clickup_request(
        "POST", f"/task/{task_id}/comment", json_body={"comment_text": comment_text}
    )
    return f"Comentario agregado a la tarea {task_id} (comment_id={data.get('id', '?')})."


if __name__ == "__main__":
    mcp.run()
