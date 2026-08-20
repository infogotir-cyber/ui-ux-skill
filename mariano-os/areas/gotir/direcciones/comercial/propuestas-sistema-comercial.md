# Tres propuestas de sistema comercial — GOTIR (20 agosto 2026)

> Pedido por Mariano: juntar todo el análisis del día (Mapa Antifugas actualizado, mini-funnel de
> apertura, secuencia post-agendamiento, y el pedido nuevo de una bandeja de mensajes sin responder
> con seguimiento basado en notas) en 3 propuestas completas de sistema comercial, de punta a punta,
> para elegir una. Versión visual publicada como artifact — este documento es la versión persistida
> en el sistema, mismo contenido.

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
- **Límite real**: si el volumen de leads crece fuerte, Mariano sigue siendo quien escribe cada
  respuesta — la lista se prioriza mejor, pero no se achica sola.
- **Riesgo**: bajo.

## Propuesta 2 — El Filtro Automático

**Filosofía**: un bot de WhatsApp hace la apertura y el mini-funnel completo (modalidad, timing,
presupuesto) y agenda solo, sin depender de que Mariano esté disponible en el momento. El lead le
llega ya calificado — la parte que solo él puede hacer bien (confianza, cierre).

- **Hallazgo importante a confirmar antes de construir nada**: en la cuenta de GHL ya existen
  workflows publicados llamados **"Bot setter"** (`79ded9c9-20ed-40e7-b403-fec2add1895e`), **"Bot
  closer"** (`95b6fd4f-8363-4306-b574-9669b37c8172`), **"Bot para clientes"**
  (`eafe5f36-86e1-4949-9ece-54c78edf78cf`) y **"Proximo follow up bot closer"**
  (`dcaa56ee-e8a6-4355-8a8a-44dbe9b05ffa`) — no están documentados en este sistema y no se sabe si
  están activos, en pausa, o un intento anterior sin terminar. Antes de diseñar esta ruta desde
  cero, revisarlos juntos — podría ser que ya exista media construcción.
- **Cómo resuelve la bandeja sin responder**: el bot responde en segundos, siempre — nadie queda en
  silencio literal, incluso si Mariano está en una llamada o durmiendo. Solo le llega la
  conversación cuando el bot ya calificó, o cuando el lead pide explícitamente un humano.
- **Qué se automatiza**: apertura + las 3 preguntas de calificación; entrega de requisitos
  fragmentada con pausas (mismo guion ya escrito); agendamiento directo si califica.
- **Qué sigue siendo de Mariano**: conversaciones con matices/objeciones de precio/casos atípicos
  (el bot deriva, no improvisa); la llamada entera.
- **Se construye con**: GHL Workflow AI nativo (o revisar los bots existentes) + reglas de
  escalamiento a humano.
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
- **Límite real**: no reduce el tiempo que toma escribir cada respuesta — garantiza que nada se
  pierde, pero las horas del día siguen siendo las mismas.
- **Riesgo**: bajo.

## Comparación lado a lado

| — | Copiloto | Filtro Automático | Reglas que se cumplen solas |
|---|---|---|---|
| Quién habla con el lead | Siempre Mariano | Bot al inicio, Mariano al cerrar | Siempre Mariano |
| Riesgo de sonar genérico | Bajo | Medio | Bajo |
| Resuelve el no-show | Sí, confirmación activa | Sí, y precalifica solo | Sí, vía campo obligatorio |
| Escala más allá de 2-3 llamadas/día | Parcial | Sí | Parcial |
| Tiempo de construcción | Corto | Medio-largo (probar el bot) | Medio |
| Ataca la capa 3 (raíz del problema) | Indirecto | Indirecto | Directo |

## Recomendación (si Mariano pide una opinión)

Empezar por la **Propuesta 3** — no por ser la más ambiciosa, sino porque es la única que ataca
directamente la causa raíz que el propio Mapa Antifugas señaló (capa 3), y porque las otras dos la
necesitan de todos modos: un bot sin campos obligatorios detrás sigue perdiendo casos en silencio, y
un copiloto sin una lista confiable de "quién espera" es solo un chequeo diario más largo.

La Propuesta 1 es la que más rápido se siente en el día a día — si Mariano prefiere resultado
inmediato sobre robustez de fondo, es la de menor riesgo y más rápida de armar en la semana.

La Propuesta 2 es la de mayor techo, pero solo tiene sentido si el volumen de leads lo está
desbordando genuinamente hoy — y antes de construir nada ahí, hay que abrir los workflows "Bot" que
ya existen en la cuenta.

## Pendiente

Mariano tiene que elegir una (o pedir una combinación) antes de que este sistema empiece a construir
nada — ninguna de las tres se ejecuta sola, y cualquier cambio en GHL sigue necesitando confirmación
explícita antes de tocar nada, como en todo el resto del sistema.
