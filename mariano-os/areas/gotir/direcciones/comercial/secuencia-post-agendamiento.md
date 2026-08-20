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

Se investigaron dos fuentes: la configuración real del calendario "Asesoría GOTIR"
(`Sl5Of5SLsAgTrwxhwoAE`) vía API, y las conversaciones reales de Demelis, Karen y Gladys (las 3 del
grupo de 10 analizadas para el mini-funnel que ya habían agendado por formulario antes de escribir).

- **El calendario en sí no tiene notificaciones nativas configuradas** — `GET /calendars/{id}`
  devuelve `"notifications": []`, vacío. La confirmación/recordatorio que sí llega ("Hola [Nombre],
  Te recordamos que tenés tu llamada agendada con el equipo de GOTIR. [fecha] [hora]") viene de un
  workflow aparte (candidatos por nombre, sin poder confirmar el contenido interno por la
  limitación de API ya conocida — sección 5.5 de `CLAUDE.md`: `GET /workflows/{id}` da 404): **"Llamada
  agendada"** o **"Nueva reunión agendada"**, ambos publicados. Es un mensaje de solo confirmación —
  no incluye video, no incluye requisitos, no pregunta nada.
- **El video y el pedido de verlo antes de la llamada NO están automatizados — son 100% manuales,
  escritos por Mariano en el momento**, con timing muy inconsistente según la evidencia real:
  - **Gladys** (10 ago): agendó para "el día de hoy", la automática de confirmación llegó a las
    18:50, y Mariano pidió ver el video **a las 18:53**, tres minutos después — prácticamente en
    el momento, sin margen real para que lo vea con calma antes de la llamada.
  - **Karen** (25 jun): la automática de confirmación llegó para una cita de las 8:00, pero el
    pedido del video ("antes de unirte a la llamada") lo mandó Mariano **a las 15:11-15:12**, justo
    cuando ella escribió "Ya te llamo" — es decir, el video se pidió **al momento de entrar a la
    llamada**, no antes. Esto anula por completo el propósito del video (que llegue con contexto
    previo) — en la práctica se lo mandó para verlo *durante* el tiempo que se demoraba en conectar,
    no como preparación.
  - **Demelis** (7 ago): acá sí hubo más margen — agendó a las 14:02, la automática llegó a las
    16:00, y Mariano preguntó por el video recién a las 16:05 ("¿has podido ver el vídeo que había
    antes de agendar?"), dando a entender que el video se pide *antes de agendar*, no después —
    contradice lo que Mariano cree hoy (que llega automático post-agendamiento).

**Conclusión empírica, la más importante de este análisis**: no hay ninguna automatización que
mande el video ni las preguntas de precalificación en la ventana entre agendar y la llamada. Todo
depende de que Mariano esté disponible, se acuerde, y lo escriba a mano — y cuando lo hace, en 2 de
3 casos revisados fue tan cerca de la hora de la llamada que perdió su función de preparar con
anticipación. Es el mismo patrón de "capa 3 sin respaldo sistémico" ya diagnosticado en la sección
8.2 de `CLAUDE.md` — pero acá aplicado a un tramo del embudo que hasta hoy no se había mirado.

## 2. Por qué esto importa (cruzando con el Mapa Antifugas y Vendes o Vendes)

- **Mapa Antifugas, zona 1 (antes del presupuesto)**: la apertura ya estaba en ámbar por falta de
  guion fijo (sección 8.1 de `CLAUDE.md`). Esto agrega una fuga hermana en el mismo tramo del
  embudo: el contenido educativo que debería llegar antes de la llamada no llega de forma
  consistente ni con anticipación real.
- **El 41,2% de no-show del baseline de julio (sección 3.1)** es exactamente el síntoma esperable de
  esto: si nadie confirma activamente que la persona va a estar en la llamada, y si el único
  contacto entre agendar y la hora es un mensaje pasivo de "te recordamos", no hay ningún mecanismo
  que aumente el compromiso real de presentarse.
- **Vendes o Vendes (Grant Cardone)** — dos ideas centrales del libro aplican directo acá:
  1. **"Los compradores son mentirosos" / no confiar en la palabra pasiva, buscar compromiso
     activo**: un recordatorio que solo informa la hora no compromete a nadie. Cardone insiste en
     que hay que pedir una confirmación activa — que la persona *responda* algo, no que reciba un
     mensaje y listo. Hoy el flujo de GOTIR es 100% pasivo de este lado.
  2. **Calificar antes de invertir tiempo escaso**: Mariano tiene capacidad real de 2-3 llamadas
     comerciales por día (sección 1.3 de `CLAUDE.md`) — el recurso más escaso del negocio. Cardone
     es explícito en que no calificar antes de la reunión es el error más caro que puede cometer un
     vendedor con tiempo limitado: se termina invirtiendo el mismo tiempo en un lead sin
     presupuesto/timing/interés real que en uno listo para cerrar. Hoy, entre agendar y la llamada,
     no hay ningún filtro — la precalificación (cuando pasa) ocurre *dentro* de la llamada ya
     gastada, no antes.

## 3. Secuencia corregida propuesta

Pensada en 3 momentos, cada uno con un propósito distinto — no es "mandar más mensajes", es que
cada mensaje haga un trabajo específico que hoy no se está haciendo:

### Momento 1 — Inmediatamente al agendar (automatizable, dispara el workflow existente)

Mantener el mensaje de confirmación que ya existe, pero **agregarle en el mismo envío** (o
inmediatamente después, mismo workflow) el video y el pedido explícito de una respuesta activa —
no una sugerencia pasiva:

> Hola {{contact.first_name}}, quedó confirmada tu asesoría gratuita con GOTIR para el
> {{appointment.date}} a las {{appointment.time}}.
>
> Antes de la llamada, mirá este video de 6 minutos — ahí te cuento el proceso completo y los
> requisitos, así llegamos a la llamada directo a resolver tu caso puntual, sin perder tiempo en lo
> general:
> https://landing.gotir.es/estancias
>
> Cuando lo termines, respondé "listo" acá mismo — así sé que llegaste preparado/a.

El "respondé 'listo'" no es cosmético — es el mecanismo de compromiso activo que falta hoy (punto
1 de Cardone arriba). Da además una señal medible: si a las 24hs no respondió "listo", ya se sabe
que no vio el video sin tener que preguntarlo en el Momento 2.

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
