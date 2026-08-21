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

**Elegida: Propuesta 4 (Motor + Copiloto) del sistema comercial — falta empezar a construir**
   - Mariano pidió juntar todo el análisis del día (Mapa Antifugas, mini-funnel, secuencia
     post-agendamiento, bandeja de mensajes sin responder) en propuestas de sistema comercial
     completas: **Propuesta 1 (Copiloto)**, **Propuesta 2 (Filtro Automático, con bot)**,
     **Propuesta 3 (Reglas que se cumplen solas)**, y **Propuesta 4 (Motor + Copiloto, agregada 20
     ago 2026 más tarde a pedido explícito, combina lo mejor de la 1 y la 3 con el estándar de
     venta de sección 12 tejido adentro)**. Detalle completo en
     `direcciones/comercial/propuestas-sistema-comercial.md`.
   - **Mariano confirmó la Propuesta 4 el 20 ago 2026** (misma tarde) — quedó una duda resuelta en
     el momento: confirmó que el copiloto (Capa 2) no es solo para retomar en frío, sino que arma
     un borrador cada vez que hay un mensaje sin responder, en cualquier punto de la conversación,
     turno por turno hasta que cierra — ya aclarado en el documento.
   - Se construye en 3 fases, cada una útil sola: **Fase A** (campo obligatorio de próxima
     acción con hora exacta + etiqueta automática de "esperando respuesta" en GHL), **Fase B**
     (conectar Fathom → GHL vía la rama de n8n ya diseñada), **Fase C** (el chequeo diario se
     convierte en el copiloto real).
   - **Fase A en curso (20/21 ago 2026)** — Mariano pidió arrancarla y ejecutarla solo. 2 de 3
     piezas resueltas por API sin pedirle nada: custom field "Próxima acción - Fecha y hora exacta"
     en la oportunidad (id `kjYi4hnJFKwwZi63jydV`) y custom field "Esperando respuesta desde" en el
     contacto (id `qLXajIzazssOvAsseqT4`), más el checklist post-llamada y el chequeo nocturno ya
     ajustados para usarlos. **Falta 1 pieza — bloqueada por un límite real de la API de GHL, no
     por falta de autorización**: el workflow que detecte automáticamente un mensaje sin responder
     y llene el campo — GHL no tiene ningún endpoint para crear ni editar la lógica de un workflow
     (límite ya confirmado antes, sección 5.5 de `direcciones/comercial/CLAUDE.md`). Spec funcional
     lista en `direcciones/comercial/CLAUDE.md`, sección 13, para cuando Mariano tenga ~10 minutos
     en el builder de GHL — es el único paso manual que queda de toda la Fase A.
   - Hallazgo aparte, no bloqueante para la Propuesta 4: ya existen workflows publicados en GHL
     llamados "Bot setter", "Bot closer", "Bot para clientes" y "Proximo follow up bot closer" —
     eran relevantes solo si se elegía la Propuesta 2, que no fue la elegida.
   - **Pendiente separado, todavía sin ejecutar a propósito**: Mariano preguntó si se puede aplicar
     esto en retroactivo a todos los clientes que escribieron y no se les respondió en los últimos
     meses. Es técnicamente posible, pero no se ejecutó — motivo completo en
     `direcciones/comercial/CLAUDE.md` sección 13.5 (choca con la decisión ya tomada de priorizar
     leads activos sobre nurturing histórico de +2.000 contactos, generaría demasiados borradores
     de golpe para que Mariano revise, y en rigor es una capacidad de la Fase C, que todavía no
     existe). Recomendación dada: acotarlo a los últimos 30 días cuando llegue el momento, no a
     "todos, meses".
   - Estado: **Fase A en curso (2/3 hecho), Fase B y C sin empezar**.
   - Recordado: 1 vez (20 ago 2026, tras la elección).

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

3. **Inventario de Ruge — cambio de fuente de verdad (21 ago 2026): ahora se trabaja sobre el excel
   de Marco Jurado, no sobre los derivados "por persona"**
   - Estado: **en curso**. Mariano avisó que Marco Jurado (dueño real del inventario) quiere que se
     use su propio excel por ítem/comisión de ahora en más
     (`areas/ministerio/recursos/INVENTARIO_2026_RUGE_actualizado_21ago2026.xlsx`) — los archivos
     "por persona" (incluido `Ruge_tareas_por_persona_DEFINITIVO_19ago2026.xlsx`, que hasta ayer
     era la fuente de verdad) quedan deprecados como documento de trabajo activo. Detalle completo
     en `areas/ministerio/CLAUDE.md`, sección "Cambio de fuente de verdad — Marco Jurado retoma el
     inventario maestro".
   - **Regla nueva**: no se le agregan columnas al excel de Marco Jurado — fecha límite y encargado
     puntual (cuando no está claro en "Régimen de tenencia") se siguen trackeando en
     `ruge_reparto_lookup.md`/acá, cruzando por nombre de ítem. Falta reconciliar ese lookup (202
     ítems) contra el excel nuevo (~230 ítems) — se va a ir haciendo tarea por tarea con Mariano,
     no de una sola vez.
   - De los 2 puntos que quedaban abiertos: **"banderas de tribu" aparece 5/5 en el excel nuevo**
     (`PROPIEDAD`, `ALMACEN RUGE`) — parece resuelto, pendiente que Mariano lo confirme
     explícitamente (no se marca `hecho` por inferencia). El detalle de los "3 maletines rotos"
     apareció asociado a "COCINAS PORTATILES DE GAS" (ya `GESTIONADO`/`OK` como ítem, el maletín
     roto en sí sigue sin resolver). Paños pequeños, linterna de cabeza y martillo siguen sin
     rastro en ningún excel — Mariano dijo que los corrobora él mismo.
   - Recordado: 2 veces (20 ago, chequeo diario 20:00; 21 ago, cambio de fuente).

4. **Graduación New Life (1 sept 2026) — lista de coordinaciones propias de Mariano, como pilar**
   - Detalle completo en `areas/ministerio/CLAUDE.md`, sección "Graduación New Life", ítems 4/6-11/14.
   - Pendientes suyos, sin hacer todavía: escribirle a **Jenny Rodríguez** preguntando si va a haber
     edecanes; recordarle a **Impact Worship/David Valera** que prepare canciones (previsto para
     unos días antes del 1 sept, no ahora); seguimiento con **Carlos Prado** (rol de producción/
     servicio) y con **Margot** (rol de servidores); pedirle a **Costa Rica** cuál va a ser la
     prédica del pastor ese día; definir **quién paga la entrada (15€) de Lisandro, Luisa y
     Jessica** (Iván Paredes ya quedó resuelto — no va, sin drama); confirmar que **Lurbin** termine
     de comprar la decoración y le reporte el gasto total (para saber si Mariano tiene que poner
     dinero extra más allá de los 25€ ya definidos para los globos); asegurarse de que el resto de
     los graduandos efectivamente paguen los 15€.
   - **Agregado 21 ago 2026, más tarde**: (a) el regalito que Lurbin quiere "sembrar" para los
     graduados está esperando confirmación de los pastores, sin resolver; (b) reparto del
     seguimiento de pago — Mariano hace seguimiento a los líderes **Paola (Huanucci) y Diego**
     (nuevo, sin más contexto todavía) para sus propios estudiantes, y él mismo directamente para
     que **Paulina, Jacobo y Lisandro** paguen (Lisandro es el mismo caso de arriba sin poder
     pagar — no confirmado si esto significa que Mariano lo va a cubrir él).
   - Estado: **abierto**, varios sub-ítems en paralelo.
   - Recordado: 2 veces (21 ago 2026, dos actualizaciones el mismo día).

5. **Grupo de Madrid — Marianne y Yorlenny en riesgo de no ir al Lanzamiento (5 sept 2026)**
   - Detalle completo en `areas/ministerio/CLAUDE.md`, sección "Grupo de Madrid". Mariano tiene
     llamada **hoy (21 ago 2026)** con Yorlenny, Marianne y Jenny (su pareja ministerial en Madrid)
     para visionarlas — las dos manifestaron querer renunciar por el costo de viajar a Valencia.
   - Estado: **abierto, esperando el resultado de la llamada de hoy** — decisión pastoral, este
     sistema no participa, solo espera que Mariano cuente cómo quedó.
   - Recordado: 1 vez (21 ago 2026).

6. **Asignar a Emiliano Ortiz y Litzy a un grupo FM4 (4.1, 4.2 o 4.3)**
   - Detalle completo en `areas/ministerio/CLAUDE.md`, sección "Campaña de evangelización rumbo al
     Encuentro". Los dos fueron por primera vez a Noches de Vida el 20 ago 2026; Mariano dijo que
     los va a repartir más adelante, sin fecha concreta todavía.
   - Estado: **abierto**, sin urgencia declarada.
   - Recordado: 1 vez (21 ago 2026).

---

## Hechos (quedan un tiempo como registro antes de limpiarse)

- ~~Post-mortem obligatorio de venta perdida en el checklist "después de colgar"~~ — agregado a
  `areas/gotir/direcciones/comercial/CLAUDE.md`, sección 2, paso 6, el 19 agosto 2026.
