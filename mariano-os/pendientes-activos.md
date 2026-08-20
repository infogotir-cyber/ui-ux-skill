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
   - Recordado: 2 veces (19/20 ago 2026; 20 ago, chequeo diario 20:00).

### GOTIR — urgente

0. **Promo en USDT/Binance ofrecida a Javier Maddia, vence viernes 21 ago**
   - Detectado 19 ago revisando la llamada del 18 ago (73 min, familia de 3, ~2.475€ potenciales).
     Mariano ya envió por correo una promoción agresiva por pagar en USDT vía Binance, con fecha
     límite este viernes — el cliente además prefiere pagar así.
   - **Contradice directamente** la política de centralización de pagos que Mariano fijó el 14 ago
     (todo en euros, sin cripto, sin dólares — ver `areas/gotir/CLAUDE.md`, "Política de
     centralización de pagos").
   - Estado: **abierto, urgente por la fecha límite — vence MAÑANA, viernes 21 ago**. Sin confirmar
     si fue una excepción deliberada o un olvido de la política.
   - Recordado: 2 veces (19 ago 2026; 20 ago, chequeo diario 20:00).

1. **Nazareth Rengel — no-show del 18 ago sin reconexión todavía**
   - Referida por Jesús Mosquera. La nota en GHL dice "pendiente contactar para reagendar" pero no
     hay evidencia de que se le haya escrito, a diferencia de Yeraldin (mismo día, misma situación,
     ya recontactada). Ya pasaron 2 días.
   - Estado: **abierto**. Recordado: 2 veces (19 ago 2026; 20 ago, chequeo diario 20:00).

### GOTIR — decisión pendiente, la más importante de todas

**Elegir una de las 3 propuestas de sistema comercial completo**
   - Mariano pidió juntar todo el análisis del día (Mapa Antifugas, mini-funnel, secuencia
     post-agendamiento, bandeja de mensajes sin responder) en 3 propuestas de sistema comercial
     completas para elegir una: **Propuesta 1 (Copiloto)**, **Propuesta 2 (Filtro Automático, con
     bot)**, **Propuesta 3 (Reglas que se cumplen solas)**. Detalle completo, comparación y
     recomendación en `direcciones/comercial/propuestas-sistema-comercial.md`.
   - Hallazgo a confirmar antes de avanzar con la Propuesta 2 si la elige: ya existen workflows
     publicados en GHL llamados "Bot setter", "Bot closer", "Bot para clientes" y "Proximo follow up
     bot closer" — sin documentar, sin confirmar si están activos.
   - Estado: **abierto, esperando que Mariano elija**. Ninguna de las 3 empieza a construirse hasta
     que decida.
   - Recordado: 2 veces (20 ago 2026; 20 ago, chequeo diario 20:00).

### GOTIR — prioritarios (marcados así por Mariano, 20 ago 2026 madrugada)

0. **Secuencia post-agendamiento (agendó → llamada) — corregida tras revisión pedida por Mariano**
   - Área: GOTIR comercial.
   - **Corrección importante (20 ago 2026, madrugada)**: el primer análisis decía que el video
     pre-llamada no estaba automatizado — eso era **incorrecto**, basado en exports de WhatsApp
     truncados que no llegaban hasta el día real de agendamiento. Mariano pidió específicamente
     revisar el caso real de Florencia Cuaranta (+34600806842) contra la API de GHL, y ahí se
     confirmó: **sí existe** un mensaje automático de WhatsApp con video real adjunto (`.mp4`,
     entrega confirmada) + email, disparado al instante de agendar — verificado también en Demelis
     y Karen, mismos resultados. Lo que sigue faltando (esto sí es real): nada de lo automático pide
     una respuesta activa, y las 3 preguntas de precalificación (modalidad/timing/presupuesto)
     siguen siendo 100% manuales. Detalle completo en
     `direcciones/comercial/secuencia-post-agendamiento.md`, sección 1.
   - Estado: **bloqueado (esperando a Mariano)** — falta un ajuste chico (agregar "respondé listo"
     al mensaje que ya existe) + 2 pasos nuevos (precalificación 24-48hs antes, confirmación de
     asistencia el día de la cita), a mano en el builder de GHL. También revisar el pie "Nuhka AI
     Consulting" que aparece en los emails automáticos — probablemente no es intencional.
   - Recordado: 3 veces (20 ago 2026, madrugada — 2 mensajes seguidos; 20 ago, chequeo diario 20:00).

1. **Mini-funnel pre-llamada (Fragmentos) — texto listo, falta cargarlo en GHL**
   - Ver ítem completo más abajo en esta misma sección — se re-marca acá como prioritario a pedido
     explícito de Mariano (20 ago 2026 madrugada), junto con el ítem 0 de arriba. Los dos tocan el
     mismo tramo del embudo (antes de la llamada) y conviene resolverlos juntos cuando Mariano
     tenga tiempo de entrar al builder de GHL.

### GOTIR

1. **Mini-chat / bandeja unificada para responder mensajes de TikTok**
   - Área: GOTIR (comercial/marketing).
   - Mencionado por Mariano: antes del 19 ago 2026 (fecha exacta no registrada — él mismo señaló el
     19 ago que lo había pedido y nunca se retomó).
   - Estado: **abierto**, sin dueño ni plan todavía.
   - Recordado: 3 veces (19 ago 2026, chequeo diario 20:00; 20 ago, chequeo diario 20:00).
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
   - Estado: **bloqueado (esperando a Mariano) — texto ya terminado (20 ago 2026)**. Se analizaron
     10 conversaciones reales, se armó la secuencia de 9 mensajes y se confirmó que GHL no permite
     crear Fragmentos por API (probado contra el endpoint real, no solo asumido — ver
     `direcciones/comercial/patrones-apertura-conversacion.md`, sección "Fragmentos de GHL"). El
     texto final de los 9 Fragmentos, listo para copiar y pegar, está en la sección "Textos finales"
     del mismo documento. Falta que Mariano los cargue a mano en GHL (Conversaciones → Fragmentos) —
     no hay nada más que este sistema pueda avanzar hasta que eso pase.
   - Recordado: 4 veces (19 ago 2026, chequeo diario 20:00; 20 ago 2026; 20 ago, chequeo diario
     20:00).

### Ministerio (Ruge y otros)

3. **Inventario físico de Ruge — documento definitivo ya cargado, quedan 2 puntos abiertos**
   - Estado: **en curso**. Mariano corrigió y subió el excel final
     (`Ruge_tareas_por_persona_DEFINITIVO_19ago2026.xlsx`) y se sincronizó lo relevante a ClickUp
     — detalle completo en `areas/ministerio/CLAUDE.md`, sección "Documento definitivo — corrección
     de Mariano". El reto de los platos de cartón quedó resuelto en 70 (confirmado por él mismo).
   - Quedan 2 sin resolver, Mariano dijo que los corrobora él mismo: (a) paños pequeños, linterna
     de cabeza, martillo y el detalle de los 3 maletines rotos — sin ítem claro en el sistema; (b)
     si las banderas de tribu están completas.
   - Recordado: 1 vez (20 ago, chequeo diario 20:00).

---

## Hechos (quedan un tiempo como registro antes de limpiarse)

- ~~Post-mortem obligatorio de venta perdida en el checklist "después de colgar"~~ — agregado a
  `areas/gotir/direcciones/comercial/CLAUDE.md`, sección 2, paso 6, el 19 agosto 2026.
