# Pendientes activos — mariano-os

> Creado 19 agosto 2026, a pedido explícito de Mariano: quiere que el sistema deje de depender de
> que él se acuerde de las cosas y empiece a recordarle activamente lo que quedó sin resolver, las
> veces que haga falta. Vive en la raíz porque cruza cualquier área (GOTIR, ministerio/Ruge,
> empresarial, personal) — no es solo un archivo de GOTIR.

## Cómo usar este archivo

- Cualquier cosa que Mariano mencione como "esto hay que hacerlo" se agrega acá en el momento, no se
  espera a que la conversación termine ni a que él lo repita.
- Campo **Recordado**: sube en 1 cada vez que se le vuelve a mencionar sin que haya avanzado. Sirve
  para ver qué lleva más tiempo estancado y merece más insistencia.
- **Estado**: `abierto` / `en curso` / `bloqueado (esperando a X)` / `hecho`.
- Un ítem pasa a `hecho` solo cuando Mariano lo confirma explícitamente — nunca por inferencia (ej.
  "probablemente ya lo hizo").
- Los ítems `hecho` se dejan tachados un tiempo como registro antes de limpiarse.
- El chequeo diario (ver `areas/gotir/direcciones/comercial/CLAUDE.md`, sección 9) lee este archivo
  y vuelve a mencionar todo lo que siga `abierto` o `en curso`.

---

## Abiertos

### GOTIR — urgente, bloqueante

**WhatsApp sin proveedor conectado tras la migración de reseller de GHL — bloquea TODO envío automático por WhatsApp**
   - Detectado 19/20 ago 2026, investigando el caso de Regina Lucia Epifanio (ver más abajo).
     Mariano confirmó la causa real: el proveedor que les daba GHL como reseller ("God High
     Level") dejó de darles servicio y los migró directo a una cuenta de Go High Level — y en esa
     migración **no quedó conectado ningún proveedor de WhatsApp** (ni el genérico anterior ni el
     oficial de Meta Business).
   - Impacto: cualquier automatización de GHL que mande WhatsApp (`{WA#1}`, notificaciones a
     colaboradores, seguimientos) **no entrega nada**, aunque el registro de ejecución la marque
     como "Ejecutado" — no tira error visible, simplemente no sale. El canal de email no está
     afectado (sí funciona).
   - Esto explica retroactivamente el caso de Sebastián Gimenez (17 ago) que había quedado sin
     resolver — mismo problema de fondo, no una casualidad aislada.
   - Estado: **abierto, requiere acción directa de Mariano en GHL** (no se puede resolver por API)
     — reconectar el proveedor de WhatsApp (genérico con QR, o pasar al oficial de Meta Business).
   - Recordado: 1 vez (19/20 ago 2026).

### GOTIR — urgente

0. **Promo en USDT/Binance ofrecida a Javier Maddia, vence viernes 21 ago**
   - Detectado 19 ago revisando la llamada del 18 ago (73 min, familia de 3, ~2.475€ potenciales).
     Mariano ya envió por correo una promoción agresiva por pagar en USDT vía Binance, con fecha
     límite este viernes — el cliente además prefiere pagar así.
   - **Contradice directamente** la política de centralización de pagos que Mariano fijó el 14 ago
     (todo en euros, sin cripto, sin dólares — ver `areas/gotir/CLAUDE.md`, "Política de
     centralización de pagos").
   - Estado: **abierto, urgente por la fecha límite**. Sin confirmar si fue una excepción deliberada
     o un olvido de la política. Recordado: 1 vez (19 ago 2026).

1. **Nazareth Rengel — no-show del 18 ago sin reconexión todavía**
   - Referida por Jesús Mosquera. La nota en GHL dice "pendiente contactar para reagendar" pero no
     hay evidencia de que se le haya escrito, a diferencia de Yeraldin (mismo día, misma situación,
     ya recontactada). Ya pasó más de un día.
   - Estado: **abierto**. Recordado: 1 vez (19 ago 2026).

### GOTIR

1. **Mini-chat / bandeja unificada para responder mensajes de TikTok**
   - Área: GOTIR (comercial/marketing).
   - Mencionado por Mariano: antes del 19 ago 2026 (fecha exacta no registrada — él mismo señaló el
     19 ago que lo había pedido y nunca se retomó).
   - Estado: **abierto**, sin dueño ni plan todavía.
   - Recordado: 2 veces (19 ago 2026, chequeo diario 20:00).
   - Falta definir: ¿GHL ya centraliza Instagram/WhatsApp — también permite TikTok, o hace falta
     otra herramienta? Confirmar con Mariano el volumen real de mensajes de TikTok antes de decidir
     la solución.

2. **Corregir/mejorar el mini-funnel pre-llamada que ya existe**
   - Área: GOTIR comercial.
   - Qué es: **confirmado por Mariano (19 ago 2026)** — no es un proceso nuevo, es corregir el
     mini-funnel pre-llamada que ya existe (mencionado en `direcciones/comercial/CLAUDE.md` sección
     6.2, cubre SABE/QUIERE/PUEDE/CUÁNDO) para que la persona llegue a la llamada sabiendo
     requisitos y precios con más claridad de la que hoy logra.
   - Mencionado por Mariano: antes del 19 ago 2026, sin seguimiento; retomado y aclarado el 19 ago.
   - Estado: **abierto** — falta que Mariano diga qué específicamente está fallando hoy en ese
     mini-funnel (¿no llega el contenido?, ¿llega pero no queda claro?, ¿falta algún dato concreto
     como precio o requisito?) antes de poder proponer una corrección puntual.
   - Recordado: 2 veces (19 ago 2026, chequeo diario 20:00).

### Ministerio (Ruge y otros)

3. **Inventario físico de Ruge — documento definitivo ya cargado, quedan 2 puntos abiertos**
   - Estado: **en curso**. Mariano corrigió y subió el excel final
     (`Ruge_tareas_por_persona_DEFINITIVO_19ago2026.xlsx`) y se sincronizó lo relevante a ClickUp
     — detalle completo en `areas/ministerio/CLAUDE.md`, sección "Documento definitivo — corrección
     de Mariano". El reto de los platos de cartón quedó resuelto en 70 (confirmado por él mismo).
   - Quedan 2 sin resolver, Mariano dijo que los corrobora él mismo: (a) paños pequeños, linterna
     de cabeza, martillo y el detalle de los 3 maletines rotos — sin ítem claro en el sistema; (b)
     si las banderas de tribu están completas.

---

## Hechos (quedan un tiempo como registro antes de limpiarse)

- ~~Post-mortem obligatorio de venta perdida en el checklist "después de colgar"~~ — agregado a
  `areas/gotir/direcciones/comercial/CLAUDE.md`, sección 2, paso 6, el 19 agosto 2026.
