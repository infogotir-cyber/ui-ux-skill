# Secuencia post-agendamiento (agendó → llamada) — GOTIR comercial

> Pedido por Mariano el 20 agosto 2026 (madrugada, antes de dormir): analizar qué le llega hoy a un
> lead entre el momento en que agenda la llamada y la llamada en sí (hoy incluye, en teoría, un
> video para que lo vea antes), y proponer correcciones para que lleguen a la llamada educados,
> realmente interesados, con presupuesto y con timing de menos de 6 meses. Se pidió usar todo el
> conocimiento de ventas disponible: el curso Mapa Antifugas (`mapa-antifugas-curso.md`, mismo
> directorio) y el libro "Vendes o Vendes" (Grant Cardone, *Sell or Be Sold*).
>
> Distinto del "mini-funnel pre-llamada" de `patrones-apertura-conversacion.md`: ese cubre la
> **apertura de la conversación**, antes de que exista una cita agendada. Este documento cubre lo
> que pasa **después de agendar y antes de la llamada** — es la siguiente etapa del mismo embudo,
> con su propia fuga.

## 1. Qué existe hoy realmente (verificado en vivo, no supuesto)

> **Corrección (20 agosto 2026, misma madrugada)**: la primera versión de esta sección concluía que
> no había ningún video automatizado — **esa conclusión era incorrecta**. Se basó en los exports de
> WhatsApp que Mariano había compartido para el análisis del mini-funnel de apertura
> (`patrones-apertura-conversacion.md`), que resultaron estar **truncados** — empezaban varios días
> *después* del momento real de agendamiento, así que nunca llegaron a incluir el mensaje
> automático que se manda justo al agendar. Mariano pidió específicamente revisar la conversación
> real de un caso reciente (Florencia Cuaranta) para confirmarlo, y ahí apareció. Se volvió a
> chequear Demelis y Karen (2 de los 3 casos usados en la versión anterior de este documento)
> directo contra la API de conversaciones de GHL (no contra el export), y el mismo mensaje
> automático aparece en los tres, con fecha real de envío coincidente con el momento de agendar.
> Queda todo lo de abajo como la versión corregida.

Se verificó contra la API de conversaciones de GHL (`GET /conversations/{id}/messages`, que expone
`source: workflow` para los mensajes disparados por automatizaciones, a diferencia de `source: api`
para lo que Mariano escribe a mano desde su teléfono) para tres casos reales: **Florencia Cuaranta**
(agendó 19 ago, el caso que Mariano pidió revisar), **Demelis Celis** (agendó 3 ago) y **Karen
Quijije** (agendó 24 jun).

**Sí existe una secuencia automática real al agendar, y funciona bien.** En los tres casos, en el
mismo segundo en que se crea la cita (evento `TYPE_ACTIVITY_APPOINTMENT`), se disparan 4 mensajes
con `source: workflow`:

1. **WhatsApp** (`{WA#1}`, `status: delivered` confirmado): *"Hola [Nombre] 😊 Gracias por agendar
   tu llamada con el equipo de GOTIR. Antes de nuestra llamada te dejamos un video corto de Mariano
   donde te cuenta quiénes somos y cómo trabajamos. En la llamada vamos a ver tu situación, fechas,
   opciones según tu caso y responder todas tus dudas. 📌 Busca estar en un lugar tranquilo y con
   buena conexión. Si no puedes asistir, avisános y la reprogramamos sin problema. ¡Nos vemos
   pronto! 🙌 Equipo GOTIR"* — con un **archivo de video real adjunto** (`.mp4` alojado en GHL, no
   un link a la landing), es decir, se reproduce directo en el chat de WhatsApp sin que el lead
   tenga que salir a un navegador.
2. **Email** con el mismo contenido, algo más largo, con bullets de qué se cubre en la llamada.
3. **SMS/WhatsApp de confirmación de fecha/hora** (`"Tu asesoría gratuita ha sido agendada
   correctamente el [fecha] [hora]"`).
4. **Email de confirmación de fecha/hora**, formato similar.

Además, hay **recordatorios adicionales cerca de la llamada** ("Te recordamos que tenés tu llamada
agendada con el equipo de GOTIR...") que también aparecen de forma consistente el día antes y el
día de la cita en los tres casos — con `source: api`/`app` en vez de `workflow`, así que
probablemente vienen del sistema nativo de recordatorios de citas de GHL a nivel de cuenta (no del
campo `notifications` del calendario específico, que sigue devolviendo vacío — el recordatorio debe
estar configurado en otro lado, a nivel de Configuración del negocio, no por calendario).

**Detalle menor a revisar, no crítico**: los emails automáticos (los 4 revisados) terminan con el
pie *"Nuhka AI Consulting"* debajo del logo de GOTIR — no parece intencional, probablemente quedó
del proveedor/plantilla que armó estos templates. Vale la pena que lo revises y lo cambies por la
marca de GOTIR si no es a propósito.

## 1.1 Lo que sigue sin estar resuelto (esto sí se mantiene de la versión anterior)

Con el video ya cubierto, el problema real no es "no llega contenido" — es que **nada de lo que
llega automático pide una respuesta activa ni precalifica**:

- Los 4 mensajes automáticos y los recordatorios son **unidireccionales** — informan, no piden
  confirmación. Nadie sabe si el lead realmente vio el video o si va a poder asistir hasta que
  Mariano se lo pregunta a mano en el chat (lo cual, según los mismos exports, a veces pasa recién
  al momento de la llamada — ver el caso de Karen más abajo, sección 2).
- **Las 3 preguntas de precalificación (modalidad, timing, presupuesto) siguen sin estar en ningún
  automatismo** — en los tres casos revisados, esas preguntas las hace Mariano a mano, en tiempo
  real, dentro de la conversación — a veces antes de la llamada (Demelis), a veces literalmente
  mientras la persona ya está por conectarse (Karen, sección 2 abajo).
- El video que llega automático es genérico ("quiénes somos y cómo trabajamos"), no el mismo video
  con los requisitos (`landing.gotir.es/estancias`) que Mariano manda a mano después en la
  conversación — son dos piezas de contenido distintas, y la segunda (la que realmente educa sobre
  requisitos/precios) sigue siendo 100% manual.

## 2. Por qué esto importa (cruzando con el Mapa Antifugas y Vendes o Vendes)

Con el contenido ya resuelto (sección 1), la fuga real que queda es de **compromiso y filtro**, no
de información:

- **Mapa Antifugas, zona 1 (antes del presupuesto)**: la apertura ya estaba en ámbar por falta de
  guion fijo (sección 8.1 de `CLAUDE.md`). El contenido pre-llamada ya llega automático y bien
  producido (sección 1) — eso no es la fuga. La fuga hermana en este mismo tramo es que nada de lo
  automático pide una respuesta ni filtra, así que sigue dependiendo 100% de que Mariano lo haga a
  mano, y con timing inconsistente (ver caso Karen abajo).
- **El 41,2% de no-show del baseline de julio (sección 3.1)** sigue siendo coherente con esto: los
  4 mensajes automáticos y los recordatorios informan, pero **ninguno pide una confirmación activa**
  de que la persona va a estar — no hay ningún mecanismo que aumente el compromiso real de
  presentarse más allá de recibir un aviso.
- **Vendes o Vendes (Grant Cardone)** — dos ideas centrales del libro aplican directo acá:
  1. **"Los compradores son mentirosos" / no confiar en la palabra pasiva, buscar compromiso
     activo**: un recordatorio que solo informa la hora no compromete a nadie. Cardone insiste en
     que hay que pedir una confirmación activa — que la persona *responda* algo, no que reciba un
     mensaje y listo. Hoy el flujo automático de GOTIR entrega contenido bien producido, pero es
     100% pasivo — nunca pide una respuesta.
  2. **Calificar antes de invertir tiempo escaso**: Mariano tiene capacidad real de 2-3 llamadas
     comerciales por día (sección 1.3 de `CLAUDE.md`) — el recurso más escaso del negocio. Cardone
     es explícito en que no calificar antes de la reunión es el error más caro que puede cometer un
     vendedor con tiempo limitado: se termina invirtiendo el mismo tiempo en un lead sin
     presupuesto/timing/interés real que en uno listo para cerrar. Hoy, entre agendar y la llamada,
     no hay ningún filtro automático — la precalificación (cuando pasa) la hace Mariano a mano,
     dentro del tiempo que le queda antes de la llamada, no siempre con margen (caso Karen: el
     video de requisitos se lo pidió justo cuando ella ya estaba por conectarse a la videollamada,
     "Ya te llamo" → "Te pido que antes de unirte... veas el video" en el mismo minuto).

## 3. Secuencia corregida propuesta

Pensada en 3 momentos, cada uno con un propósito distinto — no es "mandar más mensajes", es que
cada mensaje haga un trabajo específico que hoy no se está haciendo:

### Momento 1 — Inmediatamente al agendar (ya existe, solo falta un agregado)

**No hace falta crear nada nuevo acá** — el mensaje de WhatsApp con el video ya se dispara solo y
funciona bien (sección 1). Un solo cambio: agregarle al final el pedido explícito de una respuesta
activa, en vez de dejarlo como aviso pasivo:

> Hola {{contact.first_name}} 😊 Gracias por agendar tu llamada con el equipo de GOTIR. Antes de
> nuestra llamada te dejamos un video corto de Mariano donde te cuenta quiénes somos y cómo
> trabajamos. En la llamada vamos a ver tu situación, fechas, opciones según tu caso y responder
> todas tus dudas.
>
> 📌 Busca estar en un lugar tranquilo y con buena conexión. Si no puedes asistir, avisános y la
> reprogramamos sin problema.
>
> **Cuando termines de ver el video, respondé "listo" acá mismo** — así sabemos que llegás
> preparado/a a la llamada.
>
> ¡Nos vemos pronto! 🙌 Equipo GOTIR

El "respondé 'listo'" no es cosmético — es el mecanismo de compromiso activo que falta hoy (punto
1 de Cardone arriba). Da además una señal medible: si a las 24hs no respondió "listo", ya se sabe
que no vio el video sin tener que preguntarlo en el Momento 2. Esto se edita directo en el paso de
WhatsApp que ya existe en el workflow ("Llamada agendada" o "Nueva reunión agendada", confirmar
cuál al abrirlo) — no hace falta un paso nuevo.

### Momento 2 — Precalificación explícita (24-48hs antes, o al día siguiente de agendar si la cita es más lejana)

Esto es lo que hoy no existe en ningún lado del embudo post-agendamiento: las 3 preguntas que
determinan si el lead cumple el perfil que Mariano quiere en la llamada (quiere estancia por
estudios / puede con el presupuesto / viaja en menos de 6 meses) — mismas preguntas de fondo que
el mini-funnel de apertura (`patrones-apertura-conversacion.md`), pero acá con el objetivo
distinto de **filtrar antes de gastar el slot de llamada**, no de abrir la conversación:

> {{contact.first_name}}, para preparar bien tu llamada del {{appointment.date}}, contame 3 cositas
> rápidas:
>
> 1) ¿Confirmás que te interesa la modalidad de estancia por estudios (no visado desde tu país, ni
> otro trámite)?
> 2) ¿Tenés fecha o ventana de viaje dentro de los próximos 6 meses?
> 3) Los montos que viste en el video (~7.200€ de fondos + curso + seguro) — ¿te resultan
> alcanzables en el corto plazo?

**Por qué importa hacerlo acá y no solo en la llamada**: si las respuestas muestran que no hay
timing, no hay presupuesto, o la modalidad no es la que interesa, Mariano todavía está a tiempo de
decidir con criterio — reagendar más adelante, derivar a contenido, o simplemente saber de entrada
que esa llamada no es prioritaria y usar mejor sus 2-3 slots diarios. Hoy esa misma información
recién aparece **dentro** de la llamada ya gastada (ver casos Demelis y Gladys, donde el freno de
presupuesto apareció después de todo el bloque de requisitos, no antes).

### Momento 3 — Confirmación de asistencia (misma mañana o 2-3 horas antes)

Objetivo puntual: bajar el 41,2% de no-show con un pedido de confirmación activo, no un
recordatorio pasivo:

> {{contact.first_name}}, nos vemos hoy a las {{appointment.time}} 🙌🏻 ¿Confirmás que vas a poder
> estar? Si surgió algo y no llegás, avisame acá mismo y te reagendo sin problema — pero necesito
> saberlo antes, así aprovecho ese horario si vos no podés.

La última frase ("aprovecho ese horario si vos no podés") no es solo cortesía — es la misma lógica
de escasez real que ya aplica Mariano en la llamada (Fase 5, invitación directa a decidir): nombrar
el costo de oportunidad genera más probabilidad de respuesta que un simple "te esperamos".

## 4. Cómo implementarlo (misma limitación de API ya conocida)

Igual que con los Fragmentos (ver `patrones-apertura-conversacion.md`) y con la lógica interna de
workflows en general (sección 5.5 de `CLAUDE.md`, `GET /workflows/{id}` → 404): esto no se puede
armar por API. Hay que construirlo a mano en el builder de GHL, como pasos nuevos dentro de
**"Llamada agendada"** o **"Nueva reunión agendada"** (el que efectivamente dispara al agendar —
confirmar cuál es al abrirlo), con retrasos (`Wait`) entre cada paso:

1. Paso ya existente: confirmación → reemplazar texto por el del Momento 1.
2. Nuevo paso, `Wait` hasta 24hs antes de la cita (o fijo a "el día siguiente de agendar" si la
   cita queda a más de 2 días) → mensaje del Momento 2.
3. Nuevo paso, `Wait` hasta 2-3 horas antes de la cita → mensaje del Momento 3.

**Sugerencia adicional, no imprescindible para arrancar**: agregar un custom field nuevo tipo
Sí/No, ej. "Precalificado (Dr)", que Mariano marque manualmente si las respuestas del Momento 2 dan
bien — así en el pipeline se ve de un vistazo quién llega listo, sin tener que releer el chat antes
de cada llamada. Queda para una segunda vuelta, después de probar la secuencia base.

## 5. Cómo medir si funciona

Mismo criterio que ya usa el sistema para el resto de las mejoras de proceso (sección 3.1 de
`CLAUDE.md`, "no asumir que algo funciona sin datos"): comparar, para una cohorte de citas nuevas
después de implementar esto, contra el baseline ya existente:
- Tasa de no-show (baseline: 41,2%, julio 2026).
- % de llamadas donde Mariano ya sabe la respuesta a modalidad/timing/presupuesto **antes** de
  empezar la Fase 2 de la llamada (hoy no medido, sería el primer dato de esta métrica).

## 6. Pendiente de decidir con Mariano

- Confirmar cuál de los dos workflows candidatos ("Llamada agendada" o "Nueva reunión agendada") es
  el que realmente dispara al agendar — no se pudo confirmar por API, hay que abrirlo en GHL.
- Si el Momento 2 se manda siempre a horario fijo (ej. "al día siguiente de agendar") o calculado
  dinámicamente contra la fecha de la cita (24-48hs antes) — lo segundo es mejor pero más
  complejo de armar en el builder nativo de GHL; confirmar si vale la pena o si conviene empezar
  simple.
