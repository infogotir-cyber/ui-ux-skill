# Propuestas de sistema comercial — GOTIR (20 agosto 2026)

> Pedido por Mariano: juntar todo el análisis del día (Mapa Antifugas actualizado, mini-funnel de
> apertura, secuencia post-agendamiento, y el pedido nuevo de una bandeja de mensajes sin responder
> con seguimiento basado en notas) en 3 propuestas completas de sistema comercial, de punta a punta,
> para elegir una. Versión visual publicada como artifact — este documento es la versión persistida
> en el sistema, mismo contenido.
>
> **Actualización (20 ago 2026, más tarde el mismo día)**: se agregó el estándar permanente de
> técnica de venta (sección 12 de `CLAUDE.md`, disparado por el caso de seguimiento a Sara Sofía) —
> todo mensaje que cualquiera de las tres propuestas genere (borrador para aprobar, guion de bot, o
> lo que sea) pasa por ese checklist antes de salir. Se anota abajo, dentro de cada propuesta, cómo
> aplica específicamente.
>
> **Segunda actualización (20 ago 2026, misma tarde)**: Mariano pidió una cuarta propuesta que
> combine lo mejor de la 1 (Copiloto) y la 3 (Reglas que se cumplen solas), con criterio de experto
> en ventas/marketing y con todo lo que este sistema ya sabe de GOTIR. Es la **Propuesta 4 — Motor +
> Copiloto**, abajo, después de la 3. No reemplaza a las otras tres — se agrega como una cuarta
> opción real, probablemente la más completa de las cuatro.

## El diagnóstico del que parten las tres (no cambia entre propuestas)

- **Capa 1 (proceso): verde.** El guion de llamada (sección 2 de `CLAUDE.md`), el manejo de
  objeciones y el cierre ya están a un nivel alto — no es ahí donde se pierde plata.
- **Capa 2 (ejecución): no aplica.** Mariano es setter + closer + seguimiento, solo.
- **Capa 3 (sostén/dependencia): rojo.** Ninguna regla ya escrita se cumple sola — depende de que
  Mariano se acuerde, cada vez, en cada caso. Es la causa raíz de casi todas las fugas en rojo
  (sección 8.2 de `CLAUDE.md`).
- Evidencia dura: baseline julio 2026 — 249 leads, 22,5% completó formulario, 41,2% no-show de las
  llamadas agendadas, 40% se enfría después de la llamada realizada, 0 ventas identificadas en esa
  cohorte (sección 3.1 de `CLAUDE.md`).

## Propuesta 1 — El Copiloto

**Filosofía**: Mariano sigue hablando personalmente con cada lead — su forma de vender (rapport
genuino, transparencia sobre riesgos) es la ventaja real, no se toca. El sistema se encarga de que
nunca se le pase nadie.

- **Mecanismo central**: el chequeo diario que ya existe (mañana/noche, sección 9 de `CLAUDE.md`)
  se convierte en un centro de mando — revisa toda conversación con mensaje entrante sin responder,
  cruza notas e historial real, y arma un borrador de respuesta por persona, ordenado por tiempo de
  espera. Mariano aprueba, edita o rechaza — nunca se manda nada sin que lo vea primero, mismo
  criterio que ya rige para GHL.
- **Qué se automatiza**: los 2 mensajes que faltan en la secuencia post-agendamiento (confirmación
  activa + precalificación, ver `secuencia-post-agendamiento.md`); los 9 Fragmentos del mini-funnel
  de apertura (`patrones-apertura-conversacion.md`); la detección y priorización de mensajes sin
  responder.
- **Qué sigue siendo de Mariano**: escribir/aprobar cada respuesta real, la llamada entera.
- **Se construye con**: lo que ya existe — los 2 Routines diarios, Fragmentos, 2 pasos nuevos en el
  workflow de GHL. Sin herramientas nuevas.
- **Cómo aplica el estándar de venta (sección 12 de `CLAUDE.md`)**: acá es donde más rinde — cada
  borrador que se arma para que Mariano apruebe pasa primero por el checklist de 7 puntos (motivo
  real para escribir hoy, lenguaje asuntivo si corresponde, CTA único y cerrado, urgencia real,
  salida fácil, sin mencionar incumplimientos, corto). Es la misma corrección que se le hizo al
  mensaje de Sara Sofía — con esta propuesta, esa corrección pasa a aplicarse siempre, antes de que
  Mariano vea el borrador, no solo cuando él la pide.
- **Límite real**: si el volumen de leads crece fuerte, Mariano sigue siendo quien escribe cada
  respuesta — la lista se prioriza mejor, pero no se achica sola.
- **Riesgo**: bajo.

## Propuesta 2 — El Filtro Automático

**Filosofía**: un bot de WhatsApp hace la apertura y el mini-funnel completo (modalidad, timing,
presupuesto) y agenda solo, sin depender de que Mariano esté disponible en el momento. El lead le
llega ya calificado — la parte que solo él puede hacer bien (confianza, cierre).

- **Hallazgo importante, ya revisado (25 agosto 2026)**: en la cuenta de GHL existen 4 workflows
  publicados llamados **"Bot setter"** (`79ded9c9-20ed-40e7-b403-fec2add1895e`, v31), **"Bot
  closer"** (`95b6fd4f-8363-4306-b574-9669b37c8172`, v4), **"Bot para clientes"**
  (`eafe5f36-86e1-4949-9ece-54c78edf78cf`, v5) y **"Proximo follow up bot closer"**
  (`dcaa56ee-e8a6-4355-8a8a-44dbe9b05ffa`, v5). Se abrió **"Bot setter"** en el builder (el de más
  versiones, 31 — sugería que había trabajo real hecho ahí) para ver su lógica real: es solo 2
  pasos — trigger "El cliente ha respondido" filtrado por `Has Tag includes "mariano"` → acción
  Webhook (POST) a `https://n8n.gotir.es/webhook/fce352e8-8edf-447c-9b54-c2c2b...` con el mensaje,
  nombre, teléfono, canal, etiquetas y email del contacto. O sea que "Bot setter" no contesta nada
  él solo — es un router que reenvía el mensaje a una automatización de n8n para que esa sea la que
  responda. **Ese webhook está muerto**: se buscó en `n8n.gotir.es` (revisado por Mariano
  directamente) y no existe ningún workflow con ese path — ni con las herramientas de n8n
  disponibles en este entorno (que hoy solo ven el workflow "JARVIS - Go High Level", con un
  webhook de path distinto, `72842a61...`) ni en la cuenta real de n8n de Mariano. Conclusión:
  "Bot setter" es un intento anterior abandonado a mitad de camino, no algo reutilizable — no vale
  la pena seguir esa punta. **"Bot closer"**, **"Bot para clientes"** y **"Proximo follow up bot
  closer"** quedan sin revisar todavía (no se llegó a abrirlos), así que no están descartados de la
  misma forma, pero tampoco hay nada que indique que resuelven esto — revisarlos solo si conviene
  antes de construir de cero.
- **Decisión (25 agosto 2026)**: en vez de rescatar nada de GHL, **el bot se construye nuevo, desde
  cero, directo en n8n** (mismo criterio que la Fase B de la Propuesta 4 — sección 13.6 de
  `CLAUDE.md` — construir ahí en vez de intentar reparar una rama vieja a medio hacer). Mariano
  decidió además, antes de este hallazgo, ir por un puente corto: probar el mini-funnel manual
  (los 9 Fragmentos de `patrones-apertura-conversacion.md`, ya listos para pegar en GHL) con los
  próximos 3-5 leads reales, y recién con eso validado en vivo pasar a automatizarlo como bot en
  n8n. Construcción real del bot: pendiente, se retoma en una próxima sesión.
- **Cómo resuelve la bandeja sin responder**: el bot responde en segundos, siempre — nadie queda en
  silencio literal, incluso si Mariano está en una llamada o durmiendo. Solo le llega la
  conversación cuando el bot ya calificó, o cuando el lead pide explícitamente un humano.
- **Qué se automatiza**: apertura + las 3 preguntas de calificación; entrega de requisitos
  fragmentada con pausas (mismo guion ya escrito); agendamiento directo si califica.
- **Qué sigue siendo de Mariano**: conversaciones con matices/objeciones de precio/casos atípicos
  (el bot deriva, no improvisa); la llamada entera.
- **Se construye con**: GHL Workflow AI nativo (o revisar los bots existentes) + reglas de
  escalamiento a humano.
- **Cómo aplica el estándar de venta (sección 12 de `CLAUDE.md`)**: acá es donde más pesa el riesgo
  — el bot no tiene calidez humana que compense un guion débil, así que cada mensaje fijo (apertura,
  calificación, recordatorios) tiene que pasar el checklist **antes de publicarse**, no caso por
  caso como en la Propuesta 1. Si el guion del bot cae en "checking in" genérico o pide 3+ opciones
  abiertas en vez de un CTA cerrado, el problema se multiplica por cada lead que lo recibe, no se
  corrige uno por uno. Esto sube el esfuerzo de diseño inicial, pero es no-negociable si se elige
  esta ruta.
- **Límite real**: un bot mal calibrado puede sonar genérico justo donde el diferencial de GOTIR es
  sonar genuino — necesita pruebas reales antes de soltarlo con leads de verdad.
- **Riesgo**: medio-alto.

## Propuesta 3 — Reglas que se cumplen solas

**Filosofía**: ataca directamente la capa 3 diagnosticada como causa raíz. No agrega contenido
nuevo — convierte cada regla de oro ya escrita en un campo obligatorio, una etiqueta automática o
una lista viva dentro de GHL, para que no dependa de la memoria de Mariano.

- **Cómo resuelve la bandeja sin responder**: un workflow etiqueta automáticamente todo contacto con
  mensaje entrante sin respuesta después de N horas ("Esperando respuesta desde: [fecha]"). Esa
  etiqueta arma una lista viva dentro de GHL que Mariano puede abrir en cualquier momento, no solo
  cuando habla con este sistema — el chequeo diario la lee igual que hoy lee
  `pendientes-activos.md`.
- **Qué se automatiza**: Fathom → GHL (resumen, etiqueta de temperatura, tarea de próxima acción) —
  hoy 100% manual, y ya está mapeado sin conectar en n8n (sección 4.4/4.5 de `CLAUDE.md`); marcado
  de showed/no-show por evento; campo obligatorio de próxima acción; la etiqueta de "esperando
  respuesta".
- **Qué sigue siendo de Mariano**: escribir cada mensaje — esta ruta no toca contenido, garantiza
  que nada quede invisible; decidir a quién priorizar.
- **Se construye con**: workflows + campos obligatorios en GHL, más conectar la rama de n8n ya
  diseñada y sin usar.
- **Cómo aplica el estándar de venta (sección 12 de `CLAUDE.md`)**: no aplica directo — esta
  propuesta no genera texto de venta, solo garantiza que Mariano vea a tiempo a quién tiene que
  escribirle. El checklist sigue siendo responsabilidad de Mariano al redactar cada mensaje (o de
  este sistema, si Mariano pide ayuda puntual con uno) — esta ruta no lo automatiza.
- **Límite real**: no reduce el tiempo que toma escribir cada respuesta — garantiza que nada se
  pierde, pero las horas del día siguen siendo las mismas.
- **Riesgo**: bajo.

## Propuesta 4 — Motor + Copiloto (lo mejor de la 1 y la 3)

**Filosofía**: la Propuesta 1 protege la calidad de cada mensaje pero no garantiza que nada se
pierda; la Propuesta 3 garantiza que nada se pierda pero no toca la calidad de lo que se escribe.
Son dos mitades del mismo problema, no dos caminos que compitan — esta propuesta las junta en tres
capas que se apoyan una en la otra: una **red** que hace cumplir sola las reglas de oro ya
escritas (de la 3), un **copiloto** que lee esa red y arma cada mensaje real (de la 1), y el
**estándar de venta** (sección 12) como filtro obligatorio antes de que cualquier texto llegue a
los ojos de Mariano. Ataca la causa raíz (capa 3 del Mapa Antifugas) y protege la voz genuina de
Mariano al mismo tiempo — las dos cosas que, separadas, cada propuesta dejaba sin resolver.

- **Capa 1 — La Red (automática, sin que Mariano tenga que acordarse de nada)**:
  - Fathom → GHL automatizado (resumen a la nota, etiqueta de temperatura, tarea de próxima
    acción) usando la rama de n8n ya diseñada y sin conectar (sección 4.4/4.5 de `CLAUDE.md`).
  - Campo obligatorio de "próxima acción — fecha y hora exacta" en GHL: no se puede cerrar el
    registro de una llamada sin cargarlo. Esto no es solo una buena práctica genérica — resuelve
    directamente el patrón que `patrones-llamadas.md` ya confirmó **2/2** en las dos únicas
    llamadas analizadas hasta ahora (Sara Sofía "hoy mismo", Maryi "la semana que viene", ninguna
    con hora concreta pedida en la llamada misma). Convierte un hallazgo de esta semana en una
    regla que se cumple sola, en vez de depender de que Mariano se acuerde de preguntarlo en la
    Fase 5.
  - Etiqueta automática "Esperando respuesta desde: [fecha]" en cualquier contacto con mensaje
    entrante sin responder tras N horas — arma la lista viva dentro de GHL (mismo mecanismo que ya
    usa la cuenta para "Canal referencia (Dr)" y el workflow "Notificacion influencers", sección
    5.5 — no es tecnología nueva para esta cuenta de GHL, es el mismo patrón aplicado a otro campo).
  - Marcado automático de `showed`/`noshow` por evento de calendario (ya identificado como
    mecanismo real en la sección 3.1.1).
- **Capa 2 — El Copiloto (el chequeo diario que ya existe, mañana/noche, sección 9)**:
  - En vez de que Mariano tenga que salir a buscar quién espera, el chequeo lee directamente la
    lista viva que arma la Capa 1 (etiquetas "esperando respuesta" + tareas de próxima acción
    vencidas), ordenada por urgencia real, no por orden de llegada.
  - Por cada contacto, cruza la nota real + el historial de conversación (`ghl_read_conversation`)
    y arma un borrador de mensaje.
  - **No es un mecanismo de una sola vez para retomar en frío — se dispara cada vez que hay un
    mensaje entrante sin responder**, sin importar en qué punto de la conversación esté: la
    etiqueta "Esperando respuesta desde: [fecha]" de la Capa 1 se vuelve a aplicar cada vez que el
    lead escribe, no solo la primera. El chequeo lee el chat actualizado completo y arma el
    borrador de la *siguiente* respuesta puntual (no repite el mensaje de apertura) — así sea el
    primer contacto en frío, una objeción de precio a mitad de negociación, o un "avisame cuando
    hagas la transferencia" al final. Sigue turno por turno hasta que la oportunidad cierra
    (pasa a Pagado), el lead dice explícitamente que no, o entra en la ventana de "se enfrió" — a
    partir de ahí ya no es un mensaje más, es el caso que se revisa en el post-mortem (sección 2,
    paso 6).
  - Mariano aprueba, edita o rechaza cada borrador — nunca se manda nada sin que lo vea primero,
    mismo criterio que ya rige para GHL en todo el sistema.
- **Capa 3 — El Filtro de venta (sección 12 de `CLAUDE.md`, obligatorio, no opcional)**: ningún
  borrador de la Capa 2 llega a los ojos de Mariano sin pasar antes el checklist de 7 puntos
  completo — motivo real para escribir hoy, lenguaje asuntivo si corresponde, CTA único y cerrado,
  urgencia real, salida fácil, sin mencionar incumplimientos, corto. No es una capa aparte que se
  agrega después — está tejida dentro del mecanismo de la Capa 2, **en cada turno de la
  conversación, no solo al primer mensaje**. El checklist es el mismo siempre, pero qué principio
  pesa más cambia según el momento: un mensaje de reactivación en frío se apoya más en "motivo real
  para escribir hoy"; una respuesta a mitad de negociación de precio se apoya más en "sin mencionar
  incumplimientos" y "salida fácil"; un mensaje de cierre ("avisame cuando hagas la transferencia")
  se apoya más en el lenguaje asuntivo.
- **Bonus concreto que ya salió de analizar las dos primeras llamadas de la ventana de
  aprendizaje** (`patrones-llamadas.md`): el bloque de las 3 escuelas en Fase 3 ya se confirmó como
  guion estandarizado, palabra por palabra, en 2/2 llamadas reales el mismo día — cargarlo como
  Fragmento de GHL (mismo mecanismo que ya usan los 9 Fragmentos del mini-funnel de apertura)
  ahorra ~8-10 minutos por llamada sin perder nada, y libera tiempo justo para las fases que sí
  varían por cliente (Fase 2, Fase 4). No es parte central de esta propuesta, pero es del mismo
  espíritu — mover a un sistema lo que ya está probado que funciona igual cada vez.
- **Cómo resuelve la bandeja sin responder**: igual que la Propuesta 3 (etiqueta automática, lista
  viva, nadie queda invisible), pero además el borrador de respuesta ya está armado y filtrado
  cuando Mariano abre el chequeo — no hace falta que él arme el mensaje desde cero, solo que lo
  revise.
- **Qué se automatiza**: todo lo de la Propuesta 3 (Fathom → GHL, campo obligatorio, etiqueta de
  "esperando respuesta", showed/no-show) + todo lo de la Propuesta 1 (los 2 mensajes que faltan en
  la secuencia post-agendamiento, los 9 Fragmentos de apertura, la detección y priorización de
  mensajes sin responder) + el filtro de venta aplicado siempre, no caso por caso.
- **Qué sigue siendo de Mariano**: escribir/aprobar cada respuesta real (nunca se manda nada sin su
  visto bueno), la llamada entera, decidir a quién priorizar cuando dos casos empatan en urgencia.
- **Se construye con**: lo mismo que ya usan la Propuesta 1 y la 3 por separado — no hace falta
  ninguna herramienta nueva. Se construye **por fases**, no de una vez, justamente para que cada
  fase entregue valor real por sí sola sin depender de que las otras estén terminadas:
  1. **Fase A (la más rápida, arranca la red de seguridad ya)**: campo obligatorio de próxima
     acción con hora exacta + etiqueta automática de "esperando respuesta" en GHL. Solo esto ya
     empieza a atacar la capa 3, aunque el copiloto todavía no exista.
     **Estado (20/21 ago 2026): en curso, 2 de 3 piezas resueltas por API sin intervención de
     Mariano** — los dos custom fields creados (próxima acción con hora exacta en la oportunidad, y
     "esperando respuesta desde" en el contacto), más el ajuste del checklist post-llamada y del
     chequeo nocturno para que auditen el campo nuevo. Falta 1 pieza que la API de GHL no permite
     hacer sola (el workflow que detecte automáticamente un mensaje sin responder y llene ese
     campo) — spec funcional lista en `direcciones/comercial/CLAUDE.md`, sección 13, para cuando
     Mariano tenga ~10 minutos en el builder.
  2. **Fase B**: conectar Fathom → GHL vía la rama de n8n ya diseñada y sin usar.
  3. **Fase C**: convertir el chequeo diario en el copiloto real — que lea la lista de la Capa 1 y
     arme los borradores, siempre con el filtro de venta aplicado.
  Cada fase es útil sola — no hay que esperar a las tres para empezar a notar la diferencia.
- **Límite real**: sigue siendo Mariano quien habla con cada lead y aprueba cada mensaje — si el
  volumen crece mucho más allá de 2-3 llamadas/día, esta propuesta no lo resuelve (para eso está la
  Propuesta 2, el bot). Tampoco es la más rápida de armar de las cuatro — al combinar dos
  mecanismos, el build completo (las 3 fases) toma más que la Propuesta 1 sola, aunque cada fase
  por separado es rápida.
- **Riesgo**: bajo — nada se manda sin aprobación explícita en ningún punto de las tres capas,
  mismo principio no negociable que rige todo el sistema.

## Comparación lado a lado

| — | Copiloto | Filtro Automático | Reglas que se cumplen solas | Motor + Copiloto |
|---|---|---|---|---|
| Quién habla con el lead | Siempre Mariano | Bot al inicio, Mariano al cerrar | Siempre Mariano | Siempre Mariano |
| Riesgo de sonar genérico | Bajo | Medio | Bajo | Bajo |
| Resuelve el no-show | Sí, confirmación activa | Sí, y precalifica solo | Sí, vía campo obligatorio | Sí, campo obligatorio + confirmación activa |
| Escala más allá de 2-3 llamadas/día | Parcial | Sí | Parcial | Parcial (mismo límite que Copiloto) |
| Tiempo de construcción | Corto | Medio-largo (probar el bot) | Medio | Medio, pero por fases — cada fase ya sirve sola |
| Ataca la capa 3 (raíz del problema) | Indirecto | Indirecto | Directo | Directo |
| Aplica el estándar de venta (Cardone/Cialdini/Voss, sección 12) | Sí, en cada mensaje, antes de que Mariano lo vea | Crítico, se diseña una vez en el guion del bot | No aplica — no genera texto de venta | Sí, en cada mensaje, antes de que Mariano lo vea |

## Recomendación (si Mariano pide una opinión)

**Actualizada tras agregar la Propuesta 4**: si Mariano tiene margen para construir por fases (no
todo de una semana), **la Propuesta 4 es la recomendación real** — no porque sea la más vistosa,
sino porque es la única de las cuatro que resuelve las dos cosas que hasta ahora había que elegir
por separado: que nada se pierda (causa raíz, capa 3) y que cada mensaje que sale mantenga el nivel
que ya se le exige desde el caso de Sara Sofía (sección 12). Y como se construye en fases, la
primera (campo obligatorio + etiqueta automática) ya da resultado en días, sin esperar a que el
copiloto completo esté armado.

Si Mariano prefiere no comprometerse a las tres fases todavía y quiere algo más chico para empezar
ya: **Propuesta 3** sigue siendo la apuesta más segura y rápida para atacar la causa raíz sola — es,
de hecho, la Fase A + B de la Propuesta 4, así que elegirla no es un camino perdido, es empezar la
Propuesta 4 sin comprometerse todavía a la Fase C (el copiloto).

La **Propuesta 1** sigue siendo la que más rápido se siente en el día a día si lo que más le importa
a Mariano es la calidad de cada mensaje individual, sin tocar todavía la infraestructura de GHL — la
diferencia con la 4 es que la 1 sola no resuelve el problema de fondo de "qué pasa si me olvido de
revisar".

La **Propuesta 2** es la de mayor techo, pero solo tiene sentido si el volumen de leads lo está
desbordando genuinamente hoy — y antes de construir nada ahí, hay que abrir los workflows "Bot" que
ya existen en la cuenta.

## Pendiente

Mariano tiene que elegir una (o confirmar que la 4 es la elegida, con o sin construir las tres fases
de una) antes de que este sistema empiece a construir nada — ninguna de las cuatro se ejecuta sola,
y cualquier cambio en GHL sigue necesitando confirmación explícita antes de tocar nada, como en todo
el resto del sistema.
