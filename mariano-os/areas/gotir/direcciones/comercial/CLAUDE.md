# GOTIR — Comercial (CLAUDE.md)

> Última actualización de este documento: **14 agosto 2026**.
> Todo lo que sigue viene de: (a) los documentos de contexto del proyecto comercial de GOTIR
> (estructura de llamada, plantilla Fathom, criterio comercial de Mariano, detección de nivel
> de conciencia, baseline de julio 2026, contexto de precios/servicios) y (b) una inspección
> directa del workflow de n8n conectado (`n8n.gotir.es`), hecha hoy para verificar qué existe
> realmente vs. qué se había hablado pero no se construyó. Donde no hay dato confirmado, se
> dice explícitamente "no confirmado" en vez de inventar.

---

## 0. Quién es quién / cómo leer esto

- **Mariano**: único responsable del área comercial de GOTIR (setter, closer, seguimiento). Fundador de GOTIR. Capacidad real: ~2-3 llamadas comerciales por día. También lidera un área ministerial (Impact Global / New Life / Ruge) — eso comparte infraestructura de automatización (ClickUp) pero **no es parte del negocio GOTIR**, se menciona en la sección 4 solo porque aparece en el mismo workflow de n8n.
- **Colaboradores externos mencionados**: Sebastián y María — **María confirmada como María García Serrano** (`mariagarciaserranoabogada@gmail.com`, ver sección 5.3.1) — (abogados, estancia por estudios, 250€ por caso), Gisella (visado de estudios desde origen, arma grupo de WhatsApp cuando faltan ≤6 meses para la presentación).
- **Situación de fondo que explica casi todas las decisiones de abajo**: presión financiera actual + Mariano es el único cuello de botella comercial. Cualquier propuesta nueva debe protegerle tiempo, no consumírselo.

---

## 1. Plan maestro comercial

### 1.1 Servicios y por qué se recalibraron

**Prioritarios ahora (se gestionan de punta a punta):**
- Estancias por estudios
- Visados de estudios (desde origen)
- Modificaciones/renovaciones de estancia a residencia de trabajo

**No prioritarios (se venden como lead directo, no se gestionan más):** nómada digital, no lucrativa, emprendedor, arraigos.

**Por qué se sacaron esos servicios**: no era un tema de rentabilidad en el papel — era que el modelo de derivarlos a abogados externos a cambio de 30% si cerraban generaba mucho esfuerzo propio (Ads, llamadas) sin control del resultado. Los abogados externos estaban saturados, hacían poco seguimiento, y los leads se enfriaban. Criterio de fondo explícito de Mariano: **no vale la pena sostener un servicio donde GOTIR pone el esfuerzo y el riesgo pero no controla la ejecución ni el resultado.**

Con estancia por estudios pasó una versión más leve del mismo problema: el modelo anterior tenía un grupo de WhatsApp con compromiso de respuesta <24hs, lo cual generaba mucha carga operativa y fricción cuando los clientes no entregaban documentación a tiempo. Se recalibró a un modelo con **menos acompañamiento directo de Mariano** y más derivación a Sebastián/María/Gisella, para proteger su tiempo para lo único que solo él puede hacer: **vender y cerrar**.

> Principio general de Mariano: el tiempo de Mariano es el recurso más escaso de GOTIR ahora mismo — cualquier decisión de servicio o proceso debe protegerlo, no consumirlo en tareas que otros pueden hacer.

### 1.2 Precios y estructura de cada servicio

**Estancia por estudios (dentro de España)**
- GOTIR hace la "primera parte": lead, venta, contrato, plataforma propia con requisitos y agente virtual, matriculación a curso, seguro, certificado médico.
- Sebastián/María hacen la "segunda parte" por 250€: presentación, dudas 1 a 1, seguimiento hasta TIE (sin recursos de reposición incluidos).
- **Precio al cliente: 825€ en dos cuotas, o 750€ en pago único.** De ese total, 250€ van al abogado.
- Comisiones extra por cliente: ~250€ por matriculación a curso, 40-60€ por seguro de salud, 15€ por certificado médico.

**Visado de estudios desde origen (ej. Argentina)**
- GOTIR hace la "primera parte"; Gisella arma el grupo de WhatsApp y hace seguimiento hasta el TIE (crea el grupo cuando faltan ≤6 meses para la presentación).
- **Precio: 668€, repartido 50/50** (primer 50% al inicio, segundo 50% cerca de la presentación).
- **Reparto confirmado 17 agosto 2026**: de cada cuota de 334€ (el 50% del total), **la mitad es
  para Gisella y la otra mitad para GOTIR** — o sea, 167€/167€ por cuota, 334€/334€ en el total del
  servicio. No estaba especificado antes cuánto se llevaba Gisella, solo que hacía la "segunda
  parte"; ahora queda con el monto exacto.
- Deja menos margen directo que la estancia, pero suma comisión de curso y seguro (el certificado médico se hace en origen, sin comisión).

**Requisitos clave — estancia por estudios**
- Formación de grado superior, universitaria o con aval universitario, más de 6 meses, presencial o semipresencial, con título al finalizar.
- Pasaporte vigente, antecedentes penales apostillados, certificado médico, seguro de salud.
- Fondos demostrables: **~7.200€** (600€/mes × duración de la formación).
- Presentación del expediente con al menos 60 días de anticipación al inicio del curso.
- Resolución del expediente: entre 1 y 5 meses. Se puede estudiar sin resolución aprobada, pero no se puede trabajar en blanco hasta la aprobación.
- Rechazo del expediente (poco frecuente, salvo error en la presentación): dos años de irregularidad antes de poder tramitar un arraigo; no se devuelven honorarios ni el pago de la formación.

### 1.3 Capacidad y prioridad actual

- Mariano es setter + closer + seguimiento, solo. ~2-3 llamadas comerciales/día es el techo real.
- Prioridad explícita dada la situación financiera ajustada: **cerrar leads ya interesados y generar nuevos vía marketing, por encima de** reestructurar todo el CRM o hacer nurturing de la base histórica de +2.000 contactos. Eso queda para más adelante — no es que se haya descartado, es que no es la prioridad ahora.

### 1.4 Herramientas del flujo comercial actual

- **Fathom** (notetaker): graba y resume llamadas con plantilla personalizada de 11 secciones (texto exacto de la plantilla en la sección 6.1 de este documento).
- **GHL (GoHighLevel)**: CRM. Hoy el resumen de Fathom se pega **manualmente** en la nota del contacto; se aplica manualmente una etiqueta de temperatura (🔥 Caliente / Templado / Frío); se crea manualmente una tarea con la próxima acción y fecha exacta. Ver sección 4 para el estado real de automatización de esto (spoiler: no está automatizado todavía, solo hay un placeholder en n8n).
- **Regla de oro repetida en todos los documentos de proceso**: ninguna llamada debe terminar sin una próxima acción concreta, con fecha y responsable definidos. Es el principal punto de fuga de oportunidades detectado hasta ahora (confirmado también como el error #1 en la llamada con Hector, ver sección 3.2).

### 1.5 Detección de nivel de conciencia del lead (antes de agendar)

Objetivo: no tratar igual a alguien que recién llega y a alguien que ya comparó y está por decidir, para proteger las 2-3 llamadas diarias disponibles para los leads con mayor probabilidad real de avanzar.

**Pregunta (formulario o primer WhatsApp):**
> "Para ayudarte mejor, contame: ¿es la primera vez que buscás información sobre estudiar/vivir en España, o ya estuviste comparando opciones?"

Opciones: *Es la primera vez que investigo* / *Ya leí/comparé un poco, tengo dudas* / *Ya comparé varias opciones y estoy por decidir*.

**Camino según la respuesta:**

- **"Primera vez" (nivel 1-2 — no agendar todavía)**: se dispara contenido educativo (cómo funciona el proceso + requisitos + costes) antes de ofrecer el calendario.
  > "Genial, empecemos por lo básico así no te pierdas nada importante. Te mando 2 cositas cortas: cómo funciona el proceso y qué necesitás para calificar. Después de verlas, si te sigue interesando, coordinamos la llamada."

- **"Ya comparé, dudas" (nivel 2-3 — educación corta + agendar)**:
  > "Perfecto, te mando un resumen rápido de cómo trabajamos y las cifras concretas que necesitás — así llegás a la llamada con todo claro y la aprovechamos al máximo. Reservá tu horario acá: [link]"

- **"Ya comparé, listo" (nivel 3-4 — directo a agendar)**:
  > "Buenísimo, entonces vayamos directo a lo importante. Reservá tu llamada acá y ahí resolvemos lo que te falte para decidir: [link]"

**Por qué importa**: el error más caro es tratar a alguien del nivel 1 igual que a alguien del nivel 4 — al del nivel 1 se lo agobia si se le vende de entrada, y al del nivel 4 se lo pierde si se lo obliga a pasar por contenido educativo que ya no necesita.

### 1.6 Problema estructural identificado (estacionalidad)

Fuerte estacionalidad (pico en verano europeo) por la creencia de que solo se puede iniciar en septiembre, cuando varios centros ofrecen inicio mensual. Esto no tiene todavía una solución de proceso definida en los documentos — queda como problema identificado, no resuelto.

---

## 2. Estructura de llamada de ventas (las 5 fases)

Objetivo de la llamada: convertirla en una conversación que resuelve la decisión, no en una presentación. La persona ya llega con información (por el mini-funnel pre-llamada); el trabajo en la llamada es personalizar, resolver el bloqueo real, y cerrar.

### FASE 1 — Apertura y encuadre (2 min)

No arrancar con "contame tu caso" en frío — se pierde el control de la llamada. Encuadrar primero.

> "Hola [nombre], ¿cómo estás? Antes de arrancar te cuento cómo va a ser esta llamada: primero quiero entender bien tu situación — de dónde venís, cuándo te gustaría viajar, qué es lo que más te preocupa — y con eso te armo el camino más conveniente para vos. Al final vemos los próximos pasos concretos. ¿Te parece? ¿Cuánto tiempo tenés hoy?"

Por qué funciona: fija expectativas (que va a terminar en una decisión, no solo información), y preguntar el tiempo disponible permite ajustar el ritmo — si tiene 15 min en vez de 30, se va directo al bloqueo principal.

### FASE 2 — Descubrimiento profundo (8-10 min)

Ya se tiene SABE/QUIERE/PUEDE/CUÁNDO del formulario y del contenido pre-llamada. Acá no se repregunta eso — se profundiza el por qué emocional, que es lo que de verdad cierra.

Preguntas clave:
- "¿Qué es lo que más te ilusiona de este proyecto?" (conecta con la motivación real, no solo el trámite)
- "¿Qué es lo que más te frena o te preocupa hoy?" (da el bloqueo principal antes de que aparezca como objeción)
- "¿Ya hablaste de esto con tu pareja/familia, o falta esa conversación?" (anticipa la objeción #1 antes de que aparezca al final)
- "¿Estuviste mirando otras opciones además de nosotros?" (si dice que sí, preguntar qué le gustó y qué le faltó — información de oro para el pitch)
- "¿Cómo pensás manejar el tema de los pagos — ya tenés los fondos disponibles, o van a depender de vender algo, juntar, o hacerlo desde el país de origen?" (esto saca a la luz remesas, tipo de cambio, liquidez real, ANTES de armar precios y financiación — no a mitad de la propuesta, cuando ya se suena reactivo en vez de haberlo previsto)

Anotar mentalmente (o en la ficha post-llamada) el bloqueo principal real — no el que dice al final para colgar cortés, sino el que aparece en el medio de la conversación.

### FASE 3 — Presentar la solución a medida (5-7 min)

Nunca un pitch genérico. Reflejar literalmente lo que dijo en la Fase 2.

> "Con lo que me contás, esto es lo que te recomiendo: [trámite específico], porque [conecta directamente con su motivación de la Fase 2]. Así funciona el proceso con nosotros: [breve, 3-4 pasos, sin abrumar con detalle que ya vio en el contenido pre-llamada]."

Regla: si ya vio el contenido educativo antes de la llamada, no repetirlo entero acá — solo lo específico a su caso. Repetir información que ya tiene es la forma más rápida de perder su atención y alargar la llamada sin necesidad.

Mencionar el precio sin rodeos, en el mismo tono que todo lo demás (ya lo vio en el contenido previo, así que no es sorpresa): "La inversión total es de [precio], en [opciones de pago]." Decirlo con naturalidad, sin bajar el volumen ni acelerar el ritmo, transmite seguridad.

**Regla importante — fragmentar, no descargar todo junto**: si hay varias opciones (ciudades, cursos, formaciones), no presentarlas todas de corrido en un solo bloque largo. Dar máximo 2 opciones por vez y hacer una pausa con una pregunta corta antes de seguir: "¿de estas dos, cuál te resuena más?" o "¿esto te queda claro hasta acá?". Cuando la persona recibe mucha información junta y sin pausas, el precio al final se siente más pesado de lo que es — no porque sea caro, sino porque llegó saturada.

### FASE 4 — Manejo de objeciones (anticipadas, no reactivas)

**"Tengo que hablarlo con mi pareja/familia"** — no dejarlo abierto ("ok, avisame"). Cerrar con fecha concreta:
> "Totalmente entendible. ¿Cuándo creés que van a poder hablarlo? [espera respuesta] Perfecto, te escribo el [día] a las [hora] para ver cómo quedó. Mientras tanto te mando un resumen para que se lo puedas mostrar directamente."

**"Estoy comparando con otra gestoría/opción"** — no atacar a la competencia. Preguntar qué le importa comparar y diferenciarse en eso:
> "Me parece bien que compares, es una decisión importante. ¿Qué es lo que más estás mirando — precio, tiempo del proceso, o el acompañamiento? [ajustar respuesta a lo que diga]. Lo que nosotros hacemos distinto es [diferenciador real: ej. seguimos con el abogado hasta el TIE, o el precio incluye X]."

**"No tengo el dinero ahora / necesito juntar"** — no descartarlo ni empujarlo. Segmentar el timing real:
> "¿Aproximadamente en cuánto tiempo estimás que podrías tenerlo? [según la respuesta: si es corto plazo, ofrecer dejar reservado el proceso o el pago en dos cuotas; si es largo plazo, pasar a nurturing con fecha de reactivación]."

### FASE 5 — Cierre (3-5 min)

Si está listo para avanzar:
> "Por lo que hablamos, tiene mucho sentido arrancar ahora. Te mando el link de pago/contrato ahora mismo mientras seguimos hablando — ¿lo revisamos juntos?"

Hacer el pago o la firma **en vivo, durante la llamada**, siempre que sea posible — la tasa de cierre baja mucho si se deja para "después".

**Invitación directa a decidir (no saltearla)**: aunque no haya certeza de que va a decir que sí, siempre preguntar directamente antes de pasar al fallback de "próxima acción". No dejar que el silencio o un comentario tipo "es una inversión fuerte" se interprete como un no automático:
> "Con todo lo que hablamos, ¿qué te parece si arrancamos ahora con el 50%? Te puedo tener todo listo en minutos."

Si responde con dudas, ahí sí se pasa a resolver la objeción puntual (Fase 4) o al fallback de abajo — pero primero invitarlo a decidir, no asumir que no está listo.

**Si no cierra hoy (cualquier motivo)**: nunca terminar la llamada sin estas tres cosas explícitas:
1. Próxima acción concreta (qué va a hacer el asesor o qué va a hacer el cliente)
2. Fecha exacta (no "en unos días" — un día y hora concretos)
3. Quién la ejecuta (asesor o cliente)

> "Perfecto, entonces quedamos así: vos hablás con tu pareja este fin de semana, y yo te escribo el lunes a las 10am para ver cómo siguió todo. ¿Te sirve ese horario?"

### Después de colgar (con Fathom + GHL)

1. Copiar el resumen de Fathom → pegar en nota del contacto
2. Aplicar etiqueta de temperatura (Caliente / Templado / Frío)
3. Crear tarea en GHL con la próxima acción + fecha exacta acordada en la Fase 5. **Agregado 20/21
   agosto 2026**: además cargar la misma fecha y hora en el campo de la oportunidad "Próxima acción
   - Fecha y hora exacta" (ver sección 13) — la tarea es para el recordatorio operativo, el campo es
   para que quede visible directo en la tarjeta de la oportunidad y para que el chequeo de la noche
   (sección 9.1) lo pueda auditar sin tener que abrir cada tarea.
4. Si se detectó un bloqueo nuevo o un diferenciador que funcionó bien, anotarlo — sirve para afinar el guion con el tiempo
5. **Agregado 18 agosto 2026**: marcar el estado real de la cita en GHL (`showed` si se realizó,
   `noshow` si no se presentó) — ver mecanismo completo y por qué es un paso nuevo en la sección
   "Tracking de no-show" más abajo. Sin este paso, el panel de estadísticas de Mariano no refleja
   la realidad.
6. **Agregado 19 agosto 2026, a pedido explícito de Mariano tras el curso de Mapa Antifugas**: si la
   llamada no terminó en venta, completar un post-mortem corto en la misma nota del contacto — dónde
   se frenó, qué dijo el cliente, qué se cree que pasó realmente, qué señal hubo, qué se haría
   diferente la próxima vez (ver sección 8.1, "aprendizaje de ventas perdidas"). Deja de ser un
   análisis ocasional tipo caso Hector — es parte obligatoria del checklist para **toda** venta
   perdida, no solo la que se estudia en detalle. Ver sección 9 para el mecanismo que ayuda a que
   este paso (y el resto de este checklist) no dependa solo de que Mariano se acuerde.

**Regla de oro de toda la llamada**: no es "explicar bien el trámite" — es hacer que la persona sienta que la escuchaste antes de venderle algo. El pitch genérico se puede replicar en cualquier gestoría; la conversación personalizada, no.

---

## 3. Precedente de julio 2026

### 3.1 Baseline del embudo — cohorte julio 2026

Análisis manual de los leads nuevos de julio 2026, usado como línea base para medir mejoras futuras del proceso comercial.

**Volumen y conversión por etapa:**
- 249 leads nuevos entraron al CRM en julio 2026.
- 22,5% completó el formulario.
- De los que completaron formulario, 85,7% fue cualificado (= 19,3% del total de leads del mes).
- De una reconstrucción manual de 34 llamadas: 44,1% se realizaron y 41,2% resultó en no-show.
- De las llamadas realizadas, 40% dejó de responder después (seguimiento perdido).
- **0 ventas identificadas** de esta cohorte específica al momento del análisis.
- Nota importante: los ~6.821€ de ingresos de julio **no** vienen de esta cohorte — vienen de clientes y comisiones de meses anteriores. Julio no generó ventas propias todavía identificadas al momento de este análisis.

**Dónde están las fugas (de mayor a menor en números absolutos):**
1. **Formulario (22,5% de conversión)**: la fuga más grande en términos absolutos — de 249 leads, menos de 1 de cada 4 llega siquiera a completar el formulario.
2. **No-show (41,2%)**: de los que sí agendan, 4 de cada 10 no se presentan a la llamada.
3. **Seguimiento post-llamada (40% deja de responder)**: de los que sí tuvieron la conversación, una porción significativa se enfría después sin resolución.

**Para qué sirve este dato**: es el punto de comparación. Cuando se implementen mejoras (plantilla de Fathom, próxima acción con fecha, guion de llamada, detección de nivel de conciencia), se vuelve a medir la misma cohorte de un mes y se compara contra esta base — para ver si de verdad se está moviendo la aguja, en vez de asumir que algo "funciona" sin datos.

### 3.1.1 Tracking de no-show — mecanismo real encontrado y corregido (18 agosto 2026)

Mariano quiere poder sacar estadísticas de no-show por país/tipo de lead (para dejar de perder
tiempo con perfiles que no suelen conectarse), y notó que el panel que armó dice "no show" pero no
reflejaba nada. Investigado en vivo:

- **El campo real es `appointmentStatus` de cada cita** en GHL (`confirmed` / `showed` / `noshow` /
  `cancelled`), parte del objeto de la cita del calendario (`GET/PUT
  /calendars/events/appointments/{id}`) — no es una etiqueta de contacto ni nada que se cargue a
  mano en otro lado. El panel de Mariano casi seguro lee de este campo.
- **Causa raíz de por qué el panel salía vacío**: nadie estaba actualizando este campo después de
  cada llamada — se confirmó en vivo el 18 ago que las 3 citas del día (incluida la que sí se
  realizó) seguían en `confirmed`, el valor por default al agendar, nunca se habían tocado. Por
  eso el baseline de julio (sección 3.1, 41,2% no-show) tuvo que reconstruirse **a mano**, revisando
  34 llamadas una por una — el dato real existía, pero no en el campo que el panel consulta.
- **Corregido**: se agregó el paso 5 al checklist de "Después de colgar" (arriba) — marcar
  `showed`/`noshow` en cada cita es ahora parte del proceso estándar, no opcional.
- **Herramienta agregada (21 agosto 2026)**: hasta la llamada con Florencia Cuaranta, este paso se
  hacía a mano en la UI de GHL porque el servidor MCP no tenía una tool para tocar
  `appointmentStatus`. Se agregó `ghl_update_appointment_status` (`mariano-os/mcp-servers/ghl/server.py`,
  ver detalle técnico en `CLAUDE.md` raíz) — ya se puede marcar `showed`/`noshow` directo desde acá,
  sin entrar a GHL.
- **Conteo arranca desde el 18 de agosto de 2026** (decisión explícita de Mariano) — no se
  reconstruyó el historial previo a esa fecha para las estadísticas por país/fuente, porque salvo
  reconstrucción manual como la de julio, el campo no tiene datos confiables de antes. Casos reales
  del 18 ago ya corregidos como ejemplo del mecanismo: Javier Maddia (`showed`), Yeraldin Coba
  (`noshow` — dejó una nota en el propio formulario de reserva avisando que el horario asignado por
  el widget probablemente no le iba a funcionar por diferencia horaria y pidiendo coordinar por
  WhatsApp antes — nadie lo vio, vale la pena revisar si el widget de reserva está exponiendo bien
  esas notas a quien gestiona el calendario), Nazareth Rengel (`noshow`, sin nota, sin explicación
  aparente, referida por Jesús Mosquera).
- **Cómo sacar las estadísticas cuando haga falta**: cruzar `ghl_list_calendar_events` (calendario
  `Sl5Of5SLsAgTrwxhwoAE`, "Asesoría GOTIR") filtrando por `appointmentStatus=noshow` en el rango de
  fechas pedido, contra el campo `Pais` y la fuente (`Fuente`) de cada contacto — no hace falta una
  tool nueva, se arma con las que ya existen. Todavía no hay suficiente volumen desde el 18 ago para
  sacar conclusiones — retomar cuando Mariano pida el corte.

### 3.2 La llamada con Hector (analizada el 13 de agosto 2026)

Hector: fisioterapeuta venezolano interesado en Ourense. Esta llamada se usó como caso de estudio real para el criterio comercial de Mariano.

**Cómo manejó Mariano la transparencia sobre riesgos** (lo que se debe mantener): fue explícito sobre limitaciones reales antes de que se convirtieran en problema — que Ourense es una ciudad pequeña sin cursos válidos cerca, que una de las opciones de curso técnicamente requiere presencialidad en Madrid aunque en la práctica casi nadie va, que no sabe si la normativa sanitaria española le va a pedir un curso adicional para su actividad. En ningún momento inventó una respuesta que no tenía — cuando no sabía algo (regulación sanitaria de fisioterapia), lo dijo directamente y sugirió cómo averiguarlo.

> Principio: la confianza se construye siendo el que avisa los riesgos antes de que aparezcan, no el que los minimiza para cerrar más rápido. Nunca inventar una respuesta legal o técnica que no se domina — decir "no lo sé, así lo puedes confirmar" es preferible a arriesgar la credibilidad de GOTIR.

**Cómo manejó el precio frente a una economía inestable (Venezuela)**: no bajó el precio ni minimizó el valor, pero mostró empatía genuina (habla desde su propia experiencia emigrando de Argentina) y ofreció flexibilidad real: pago en cuotas, opción de cripto para evitar las pérdidas de las casas de cambio, descuentos que él mismo negocia con escuelas/proveedores. Encuadre siempre "esto es una inversión, no un gasto — hacerlo mal después sale más caro" — nunca a la defensiva ante la objeción de precio.

> Principio: la objeción de precio en economías inestables casi nunca es sobre el valor del servicio — es sobre la logística real del dinero (remesas, tipo de cambio, liquidez). Resolver la logística importa más que argumentar el precio.

> **⚠️ Actualización de política — 14 agosto 2026, NO repetir la parte de cripto/dólares de acá en
> adelante**: Mariano confirmó que la opción de cripto ofrecida en esta llamada fue una decisión
> puntual tomada en un momento de necesidad de liquidez urgente, no una práctica que quiera
> mantener. Decidió centralizar todos los cobros de GOTIR en euros, a cuentas de la empresa en
> España (Stripe/PayPal vía GHL, todo facturado por Holded) — sin dólares, sin pesos argentinos, ni
> criptomonedas, ni para pagos a proveedores ni como opción de pago para clientes. El resto del
> criterio de esta llamada (transparencia sobre riesgos, resolver la logística del dinero antes que
> el precio, ofrecer flexibilidad real) sigue vigente — lo que cambió específicamente es *qué*
> formas de pago están sobre la mesa, no el criterio de fondo. Ver `areas/gotir/CLAUDE.md`, sección
> "Política de centralización de pagos".

**Errores identificados a corregir (de esta llamada específica):**
1. **Terminó la llamada sin próxima acción + fecha + responsable** — quedó abierto a que el cliente decida cuándo volver a escribir. Este es el error que más plata cuesta y el que menos cuesta corregir.
2. Entregó mucha información de golpe (3 ciudades, 3 cursos, precios, financiación) sin pausas de confirmación — probablemente contribuyó a que el precio se sintiera más pesado de lo que era.
3. No indagó la logística de pago/fondos (remesas desde Venezuela, liquidez atada a la venta de un carro) durante el descubrimiento — salió a mitad de la propuesta, cuando ya era más difícil de anticipar.
4. No hizo una invitación directa a decidir/cerrar — ofreció el descuento y la opción de cripto pero nunca preguntó explícitamente "¿arrancamos ahora?".

**Lo que Mariano hace bien y debe mantenerse:**
- Rapport genuino desde su propia historia migratoria, no como técnica sino porque es real.
- Paciencia real con interrupciones de la vida del cliente (llamadas de familia, niños) sin perder el hilo comercial.
- Reencuadre de precio como inversión sin ponerse defensivo ni ceder en el valor del servicio.
- Ofrecer soluciones concretas a los obstáculos que el cliente plantea, dentro de las formas de pago vigentes en euros (Stripe/PayPal vía GHL, transferencia, Bizum) — antes se citaba "pago con tarjeta vs. cripto" como ejemplo de esto, pero la opción de cripto ya no aplica desde la política de centralización de pagos (ver nota arriba).

**Por qué sigue siendo relevante hoy**: los errores #1 y #2 de esta llamada son exactamente los mismos patrones que la estructura de llamada (sección 2) y el baseline de julio (sección 3.1) ya habían identificado como las fugas más caras (falta de próxima acción concreta, saturación de información antes del precio). Esta llamada es la evidencia concreta y con nombre propio de un problema que hasta entonces era solo un patrón estadístico — por eso se usa como caso de referencia al entrenar/revisar el criterio comercial.

---

## 4. n8n — estado real de la automatización comercial/GHL

**Esta sección se verificó hoy (14 agosto 2026) directamente contra la instancia de n8n conectada (`n8n.gotir.es`), no es un resumen de lo hablado — es lo que efectivamente existe en este momento.**

### 4.1 El único workflow relacionado

- **Nombre**: `JARVIS - Go High Level`
- **ID**: `HYsCGgQAorF5t5Yq`
- **Estado**: activo
- **Creado**: 13 mayo 2026 · **Última actualización**: 13 agosto 2026
- **Trigger**: Webhook POST en `n8n.gotir.es`, path de producción `/webhook/72842a61-a720-4af4-b68b-6ec97222bfa0`. Sin credenciales requeridas en el webhook.
- **Qué es realmente**: no es un workflow comercial de GOTIR específico. Es un asistente personal general tipo "JARVIS" (con personalidad de mayordomo elegante, habla en español, llama "señor" al usuario) que enruta cualquier mensaje entrante a distintos módulos según intención detectada. GHL es **uno de los módulos posibles**, no el propósito del workflow.

### 4.2 Cómo funciona el enrutamiento

1. `Detectar Intención` (GPT-4o-mini) clasifica el mensaje entrante en una de ~19 intenciones posibles (incluye `calendar_create`, `whatsapp_send`, `email_send`, `ghl_pipeline`, `ghl_contact`, `ghl_metrics`, `task_create`, `search_web`, `payment_register`, `report_metrics`, `general_chat`, etc.).
2. `Parsear Intención` (Code) limpia la respuesta del modelo.
3. `Router de Intenciones` (Switch) enruta según coincidencia de texto (ej. todo lo que contenga `ghl_` va a una rama; `calendar_` a otra).

### 4.3 Lo que SÍ está construido y funcionando

- **Google Calendar** (calendario `info.gotir@gmail.com`): consultar próximos eventos (`calendar_query`), crear evento (`calendar_create`, extrae título/fecha/hora vía GPT-4o-mini y llama a la API de Google Calendar), modificar/reprogramar evento (`calendar_reschedule`, busca el evento por palabra clave en un rango de -7 a +60 días y lo actualiza). Las tres ramas tienen nodos reales de `n8n-nodes-base.googleCalendar`, no placeholders.
- **"Vida OS" → ClickUp**: interpreta un mensaje dictado por Mariano y lo convierte en una o varias tareas de ClickUp vía HTTP request a la API de ClickUp (`POST /api/v2/list/{list_id}/task`). **Esto es para la vida personal/ministerial de Mariano, no para GOTIR comercial** — los `list_id` mapeados son: seguimiento pastoral de líderes/parejas ministeriales (`901220315594`), grupos de amistad FM4.1-4.6 (`901220315596`), alumnos/ciclos de New Life (`901220315606`), tareas operativas de New Life (`901220315608`), logística de Ruge (`901220315541`), inventario/compras de Ruge (`901220315543`), preparación del evento Ruge (`901220315548`), salud personal (`901220315615`), desarrollo personal/vida espiritual (`901220315621`). Se incluye acá solo porque vive en el mismo workflow — no confundir con automatización de GOTIR.
- **Chat general** (fallback): si no matchea ninguna intención, responde con GPT-4o en el tono JARVIS.
- **Búsqueda**: `search_maps` arma un link de Google Maps; `search_web` devuelve un link de búsqueda de Google (no tiene API de búsqueda real conectada, es un link, no una búsqueda ejecutada).

### 4.4 Lo que NO está construido (y esto es lo importante para GOTIR)

- **`Placeholder — GHL`** (rama que matchea cualquier intención que contenga `ghl_` genérico): es literalmente un nodo de código que devuelve el texto fijo *"🏢 Módulo de Go High Level — Este módulo está en construcción. Necesitas configurar tu API key de GHL para activarlo."* No llama a ninguna API de GHL. No lee ni escribe nada en el CRM.
- **`Placeholder — Métricas`**: mismo patrón, texto fijo *"📊 Módulo de Métricas — Este módulo está en construcción. Necesitas configurar tu API key de Go High Level para ver las métricas del pipeline."*
- **`Placeholder — WhatsApp`**, **`Placeholder — Email`**, **`Placeholder — Instagram`**, **`Placeholder — Pagos`**, **`Placeholder — Audio`**: mismo patrón, todos con mensajes de "en construcción", ninguno conectado a una API real.
- **Detalle específico que vale la pena registrar**: el router de intenciones tiene reglas ya definidas para intenciones de GHL mucho más finas — `ghl_pipeline_read`, `ghl_pipeline_edit`, `ghl_calendar_read`, `ghl_calendar_create`, `ghl_conversation_read`, `ghl_conversation_reply`, `ghl_payment_link` — pero en las conexiones del workflow, **las siete ramas no están conectadas a ningún nodo**. Es decir: alguien (probablemente Mariano armando esto con ayuda de IA) ya pensó la granularidad de lo que se querría automatizar de GHL, pero ninguna de esas ramas específicas tiene lógica detrás — ni siquiera el placeholder genérico. Si el router clasifica un mensaje en, por ejemplo, `ghl_pipeline_edit`, ese mensaje no produce ninguna respuesta.

### 4.5 Conclusión honesta sobre el estado de la automatización comercial

**No existe, a día de hoy, ninguna automatización real entre GOTIR y GHL.** Todo lo que hay es: (1) un stub de mensaje "en construcción" para intenciones genéricas de GHL, y (2) siete ramas de intención más específicas ya nombradas en el router pero completamente sin conectar. El flujo real de Fathom → GHL sigue siendo 100% manual (copiar resumen, aplicar etiqueta, crear tarea a mano), tal como está descrito en la sección 1.4.

**Pendiente explícito si se quiere avanzar esto**: conectar credenciales de API de GHL en n8n, y decidir qué rama construir primero — dado que ya existe el desglose de intenciones (pipeline read/edit, calendar read/create, conversation read/reply, payment link), lo más barato sería empezar por la que más tiempo le ahorra a Mariano hoy (candidata obvia: automatizar el paso de "pegar resumen de Fathom + etiqueta + tarea" descrito en la sección 1.4/2, ya que es la regla de oro repetida en todos los documentos de proceso). Esto no está decidido — es una lectura de lo que ya está armado, no una instrucción confirmada por Mariano.

---

## 5. Estructura de GHL (pipelines, etapas, campos, automatizaciones)

**Conexión en vivo confirmada y datos traídos directamente de la API (14 agosto 2026)**: se
construyó un servidor MCP propio contra la API de GHL (ver `CLAUDE.md` raíz, sección "Herramientas
conectadas") y se usó para leer en vivo, hoy, la estructura real de pipelines, calendarios y
formularios de la location de GOTIR (`utTdf7grGmBznkERpPNM`). Todo lo de abajo es dato real leído de
la API, no dictado por Mariano ni inferido — reemplaza la versión anterior de esta sección, que
tenía la estructura incompleta porque solo había lo que Mariano recordaba de memoria.

### 5.1 Pipelines (las 3 reales — se confirma que sí eran 3, resolviendo la duda de Mariano)

**Pre-venta** (`pipeline_id=wf2UkzEcz6TSyQHoJYgW`) — cubre desde que entra un lead hasta que paga:
1. New lead /sin clasificar (`95da0f11-a578-4360-bdfc-6bb249ec11a4`)
2. Cuailficado *(sic — así está escrito en GHL, con typo)* (`a24a7ae4-8ac9-4530-a9e2-cdb7f5ac5697`)
3. Agendar llamada (`670b647d-17ff-429e-9a0c-d5a5ca729bb1`)
4. Llamada agendada (`7c6f52a5-4dfa-442d-b75f-97235880f89c`)
5. Llamada realizada (`4e7eeff5-c042-4b7f-8c38-9273464ec476`)
6. Información y contrato enviado (`3c1d2e47-61e2-44fc-81c4-1121772aa309`)
7. Pronto pago (`695a4517-14f2-4cf0-8dcd-ff5a02be6e54`)
8. Pagado (`c677f784-81f8-41e7-b60c-132a6aa3fb9f`)

Nota: el nombre real es "**Pre-venta**" (con guion), no "Preventa" como se había anotado antes por
dictado. No hay una etapa separada de "completó el formulario" — parece estar implícita entre "New
lead" y "Cuailficado", a confirmar con Mariano si le interesa desagregarla.

**Proveedores** (`pipeline_id=ldCkueEhaKZP531O7hP7`) — esta es la "tercera pipeline" que Mariano no
recordaba en la sesión anterior. Por el nombre y las etapas, coincide con el flujo de colaboración
con abogados/partners externos descrito en "Contexto operativo adicional" de `areas/gotir/CLAUDE.md`
(ej. los 250€ que GOTIR paga a Sebastián/María por la "segunda parte", o comisiones a estudios
colaboradores) — **a confirmar con Mariano**, no asumido:
1. Lead enviado (`1f4b21fe-e4b6-40c5-aa0c-14919881d66b`)
2. En contacto con partner (`0d9dec7a-14e2-4667-b2a8-e3063c00aaec`)
3. Confirmado (`a856f893-1145-4f4d-aba3-49d3eccb0a6c`)
4. Compra realizada/ Comisión pendiente (`a21f3617-5fa9-48ff-8064-a3442197972b`)
5. Comisión pagada (`55734f75-bc63-4465-ba26-bdcdc1b37eac`)
6. Cerrado (`ad51ba97-f557-46ef-a518-8d0fb31281e2`)

**Seguimiento** (`pipeline_id=kqSbO3AkmyMF0ECNxwe4`) — arranca cuando el cliente ya pagó y se le da
el servicio:
1. Nuevo cliente (derivar) (`96eeffca-a783-4425-8486-02f488072ed1`)
2. En proceso (`5849b57c-55d3-421a-90af-92eff35d0129`)
3. Presentado en evaluación (`4846e062-8901-45f2-af48-5d3e4bdae33f`)
4. Resolución (`aaac3a31-b0f4-49ed-93ea-dc99173d8736`)
5. Recurso (`b34a63b3-520c-44a3-867d-17e68b7b3a10`)
6. Trámites posteriores (`1711e597-a87b-489a-92dc-106143666115`)
7. Renovación (`0c035bff-b386-4c5f-954e-3aa4c455b690`)
8. En pausa (`4cbcf458-760f-4f2e-9767-ab406dd41d33`)
9. Cerrado (`7228583e-f565-452c-aac8-469c3e1a3b20`)

### 5.2 Calendarios

8 calendarios configurados. Solo el propósito de dos es deducible con confianza del nombre; el resto
queda anotado tal cual, **sin asumir para quién es cada uno**:
- **GOTIR** (`6CRhAWYRRL8gMpwwdOyi`) — tipo colectivo, slots de 60 min.
- **Asesoría GOTIR** (`Sl5Of5SLsAgTrwxhwoAE`) — tipo personal, slots de 60 min. **Confirmado (17 ago
  2026) directamente por Mariano: es el calendario real que usa para agendar las llamadas
  comerciales** (`asesoria.gotir@gmail.com`, el mismo usuario con el que atendió la llamada con
  Frank Sojo el 17 ago — la nota completa de esa llamada vive en GHL, en el contacto de Frank, no
  duplicada acá) — resuelve el "[link]" de agendar llamada mencionado en la sección 1.5/2.
  **Alias confirmado (19/20 ago 2026): de cara al público/en la web aparece como "Asesoría Punto
  Migratoria" — es el mismo calendario, no uno distinto.**
- **Mariano Barcelona** (`DaiTSbSX6zMA7wIclOgw`) — personal, 30 min.
- Calendarios personales de: Sabrina Navarro, Pamela Jordan, Micol Navarro, Jonathan Barrionuevo,
  Rocío Jury (30-60 min c/u).

  **Identidades resueltas (17 agosto 2026)**, cruzando contra `GET /users/` de GHL (se habilitó el
  scope `users.readonly` ese mismo día) y confirmadas directamente por Mariano:
  - **Sabrina Navarro** (`sabriinavarro.sn@gmail.com`) — cuenta activa, **se deja tal cual a
    propósito**: trabajó en GOTIR antes. **Corrección (21 ago 2026)**: no son pareja actualmente
    ("de momento", en palabras de Mariano) — sí lo fueron, y él tiene la expectativa/esperanza de
    que vuelvan a estarlo en el futuro. Sigue teniendo la expectativa de que colabore en GOTIR más
    adelante, por eso prefiere no borrar el perfil por ahora. Tratar como información personal, con
    mucha discreción.
  - **Pamela Jordan** — era **closer** (cerraba ventas), igual que Jonathan Barrionuevo — **ya no
    trabaja ni va a trabajar con GOTIR**. Mariano pidió borrar su perfil de GHL — **hecho el 17
    agosto 2026** (`DELETE /users/`, confirmado por la API, con efecto en unos minutos).
  - **Micol Navarro** (`micolnavarro7@gmail.com`) — es **hermana de Sabrina Navarro**. Colabora de
    vez en cuando con marketing y edición de videos. Mariano prefiere que su perfil **siga activo**
    — no borrar. **Es trabajo pago** (confirmado 17 ago 2026): cobra poco, pero Mariano le paga por
    cada trabajo que hace — no es una colaboración gratuita/informal. Cualquier tarea nueva que se le
    pida (ej. editar un directo) implica un pago pendiente a registrar en
    `direcciones/finanzas/CLAUDE.md` cuando se confirme el monto.
  - **Jonathan Barrionuevo** — era **closer** también, ya no trabaja ni va a trabajar con GOTIR. No
    tenía cuenta activa en `GET /users/` — nada que borrar por ese lado, el calendario que le quedó
    es un resabio visual sin cuenta detrás.
  - **Belén Campana** (`adm.gotir.es@gmail.com`) — era la mano derecha de Mariano, lo ayudaba en
    todo; ya no trabaja ni va a trabajar con GOTIR. **No es la misma persona que "Juliana"**
    (ministerio, organización distinta). Perfil borrado el 17 agosto 2026, mismo proceso que Pamela.

### 5.3 Formularios (10 reales, por primera vez con nombres y IDs completos)

- Formulario 1 - Visados Estudios (`rvGrrKqC76JAltyuoGuL`)
- Formulario 2 - Estancias Estudios (`6mANHohxrOLt15EvQeA0`)
- Formulario 3 - Otros trámites (`P6m1nOByHjzbE2noLwqW`)
- Información post venta (`SWmA6ppCjrTKnDE8yXuT`)
- Webinar Presencial (`GM828vWiRRchNBZ9cqHa`)
- Datos de facturación (`YrHyk4NpBIqxf59EoH0S`)
- Apostilla (`QRMGOiQAmFzQIyPpAr8N`)
- Alquiler IberoLocations (`ZU7dDir39vlrXpwM104o`)
- Trámites derivados a Carolina Chapo (`55wG5sKZYkvxxAOqcJSZ`)
- Trámites derivados a María García Serrano (`2HHoJ2flDrSkb3jAGwPg`)

Los 3 primeros coinciden con lo esperado por la sección 1 (visados/estancias por estudios + otros
trámites). El resto trae información nueva que **no estaba documentada y no se debe asumir**:
- "Apostilla" y "Alquiler IberoLocations" — **resuelto 17 agosto 2026**: ninguno es un trámite
  migratorio de los descritos en la sección 1.1, son servicios/leads aparte.
  - **Apostilla**: Mariano dijo que **ya no tiene sentido** — servicio descontinuado. Pendiente
    borrarlo del builder de GHL — **no se pudo hacer por API**, la API pública de GHL no ofrece
    endpoint para borrar formularios (mismo límite que ya existe para crearlos, ver `CLAUDE.md`
    raíz) — hay que borrarlo a mano en el builder.
  - **Alquiler IberoLocations**: formulario real y activo — conecta con **IberoLocations**, una
    empresa externa que busca alquileres a pedido para los clientes, sobre todo en Madrid. No es un
    trámite migratorio, es un servicio complementario de vivienda.
- "Carolina Chapo" y "María García Serrano" — **resuelto 17 agosto 2026**: ambas son usuarias reales
  y activas en GHL — "Chapo abogados" (`visados@carolinachapo.com`, rol `user`) y "María García
  Serrano" (`mariagarciaserranoabogada@gmail.com`, rol `user`). **Mariano confirmó directamente que
  María García Serrano ES la misma "María" del dúo Sebastián/María** (250€/caso, estancia por
  estudios, sección 0/1.2) — de ahora en más referirse a ella con el apellido completo cuando haga
  falta precisión. Carolina Chapo queda como colaboradora externa nueva, sin más contexto todavía.

### 5.3.1 Usuarios de GHL (traído en vivo 17 agosto 2026, vía `GET /users/`)

Lista completa de usuarios de la location, útil como referencia cruzada para identificar personas
que aparecen en calendarios/formularios/pipelines sin contexto:
- Mariano Barcelona — `info.gotir@gmail.com` (admin)
- Asesoria GOTIR — `asesoria.gotir@gmail.com` (admin) — cuenta genérica de asesoría comercial.
- Clientes GOTIR — `clientes@gotir.es` (admin) — cuenta genérica de cara al cliente.
- ~~Belén Campana~~ — perfil **borrado el 17 agosto 2026** (ver 5.2), ya no aparece en `GET /users/`.
- ~~Pamela Jordan~~ — perfil **borrado el 17 agosto 2026** (ver 5.2), ya no aparece en `GET /users/`.
- Micol Navarro — `micolnavarro7@gmail.com` (admin) — ver 5.2.
- Sabrina Navarro — `sabriinavarro.sn@gmail.com` (admin) — ver 5.2.
- Rocío Jury — `rociojury@gmail.com` (admin) — mismo nombre y apellido que la discípula de FM4.3 en
  ministerio; no confirmado si es la misma persona colaborando también en GOTIR, aunque es plausible.
- Agustin Zaya — `agustinzaya@exxoweb.com` (admin) — dominio `exxoweb.com` confirma que es de
  **Exxo**, la agencia de marketing ya documentada en `areas/gotir/CLAUDE.md`.
- Gisela Justribo — `licgisellajustribo@gmail.com` (admin) — probablemente la misma "Gisella"
  (visado de estudios desde origen, arma grupo de WhatsApp) ya documentada en la sección 0, con
  variante de ortografía del nombre ("Gisela" vs. "Gisella") — el prefijo "lic" en el email
  (licenciada) es coherente, pero no se confirma al 100% sin que Mariano lo diga.
- Wilmen Mendoza — `wilmenmendoza@yahoo.com` (user) — el especialista en visados de Venezuela
  mencionado en la llamada con Frank Sojo (17 ago) — confirma que es un usuario real de GHL, no solo
  una mención verbal.
- Chapo abogados — `visados@carolinachapo.com` (user) — ver arriba.
- María García Serrano — `mariagarciaserranoabogada@gmail.com` (user) — ver arriba.

### 5.4 Lo que sigue sin poder verse (limitación real de la API, no de este sistema)

Los campos personalizados de contacto/oportunidad no se pudieron traer en esta pasada — el servidor
MCP de GHL hoy no tiene una tool dedicada a listar campos personalizados (ver limitaciones conocidas
en `CLAUDE.md` raíz). Si hace falta ese detalle, hay que agregar esa tool al servidor.

**Actualización 18 agosto 2026**: esto ya no es cierto del todo — se confirmó en vivo que
`GET /locations/{locationId}/customFields` sí funciona con el token actual (no hacía falta una tool
nueva del servidor MCP, alcanzó con `curl` directo). Ver 5.5 abajo para lo que se encontró.

No se debe inventar automatizaciones de GHL que no estén confirmadas por Mariano o vistas en vivo —
lo de arriba es pipelines/calendarios/formularios reales, pero no dice nada de qué automatizaciones
(si las hay) mueven contactos entre etapas. **Actualización 18 agosto 2026**: esto también dejó de
ser cierto para el caso concreto de la sección 5.5 — se confirmó en vivo, vía
`GET /workflows/?locationId=...`, que sí existen automatizaciones reales en GHL (separadas del
workflow de n8n/JARVIS descrito en la sección 4, que es un sistema completamente distinto). Seguir
sin inventar nada que no esté confirmado así, pero ya no asumir que "no hay automatizaciones de GHL"
en general — lo que no hay es visibilidad automática de todo el listado, hay que ir confirmando
workflow por workflow a medida que aparecen en la conversación.

### 5.5 Automatización de derivación de partners/influencers (descubierto y armado 18 agosto 2026)

Mecanismo real que ya funcionaba para Jesús Mosquera y Nasla Espinosa, no documentado hasta ahora.
Encontrado en vivo vía API cuando Mariano pidió sumar a una colaboradora nueva (Pri Rocha) — no es
parte del workflow de n8n/JARVIS de la sección 4, es 100% nativo de GHL (Automation → Workflows),
por eso no aparecía ahí.

**Limitación real y permanente de la API de GHL confirmada acá** (para no reintentar en el futuro):
`GET /workflows/` solo devuelve id/nombre/status de cada workflow — **no expone el detalle interno**
(condiciones, ramas, acciones) ni por ese endpoint ni por `GET /workflows/{id}` (404, no existe).
Tampoco hay forma de editar un workflow por API. Todo lo de adentro de un workflow (agregar una
rama, cambiar un mensaje) es exclusivamente manual, en el builder de GHL — este sistema puede leer
la lista de workflows y los custom fields, pero no puede tocar la lógica de automatización él mismo.

**El campo que decide todo**: custom field de contacto **"Canal referencia (Dr)"**
(id `buvxaVIkvbHPOmzSz01C`, `fieldKey=contact.canal_referencia_dr`, tipo `SINGLE_OPTIONS`/dropdown).
Opciones actuales (18 agosto 2026, después de agregar a Pri Rocha):
Jesús Mosquera, Nasla Espinosa (con "s" — ojo, no "Espinoza"), Wilmen Mendoza, **Pri Rocha**, Un
Centro de estudios me pasó el contacto, Un amigo o familiar, Instagram, TikTok, Facebook, Sitio Web,
Otro. (Existe un segundo campo parecido, "Canal referencia (Dr) (copy) (copy)"
`NOoOqoYPg9wzUgFT1YzE`, con solo las opciones genéricas de canal — no es el que usan los
influencers, no confundirlos.)

**El workflow que manda el aviso**: **"Notificacion influencers"**
(`16b4bde7-31c5-4c6c-adcd-45503adc6f30`, publicado). Estructura (confirmada visualmente por
Mariano, no por API): un nodo **Condition** con una rama por influencer (`"Canal referencia (Dr)"
Es "<nombre>"`), cada rama conectada a un nodo **Internal Notification** configurado como:
`Tipo de notificación = SMS`, `Para tipo de usuario = Custom Number`, número de teléfono directo del
influencer en `A número personalizado` (no son usuarios de GHL, son números externos), con un
mensaje que usa variables (`Contact.Full Name`, `Opportunity.Stage Name`) para avisar en vivo. Una
rama final `None` cubre "ninguna condición se cumplió".

**Pri Rocha agregada 18 agosto 2026** — colaboradora nueva, consultora de inmigración portuguesa,
tiene una empresa similar a GOTIR enfocada en asesoría para vivir en Portugal y para gente que
quiere venir a España con visado de estudios. No puede firmar ni presentar trámites como abogada en
España, por eso deriva esos casos a GOTIR en vez de llevarlos ella. Colabora en dos frentes:
- **Estancias por estudios** → sus clientes completan el "Formulario 2 - Estancias Estudios"
  (`6mANHohxrOLt15EvQeA0`).
- **Nómada digital presentado desde España** → sus clientes completan el formulario **"Trámites
  derivados a María García Serrano"** (`2HHoJ2flDrSkb3jAGwPg`) — Mariano lo estaba editando en vivo
  (18 ago) para agregarle el campo "Canal referencia (Dr)" (no existía en ese formulario todavía).

Teléfono de Pri Rocha: **+351 969 515 147** (código de país de Portugal), ya cargado como
`A número personalizado` en la rama nueva de "Notificacion influencers".

Pasos ejecutados 18 agosto 2026 (mitad por API de este sistema, mitad manual por Mariano en el
builder de GHL, porque la API no permite lo segundo):
1. Agregada la opción "Pri Rocha" al dropdown "Canal referencia (Dr)" — hecho por este sistema vía
   `PUT /locations/{locationId}/customFields/{id}` con body `{"options": [...]}` (**ojo**: el GET
   devuelve el array como `picklistOptions`, pero el PUT lo espera como `options` — nombres
   distintos entre lectura y escritura del mismo campo, confirmado por prueba y error, un 422
   "property picklistOptions should not exist" delató el nombre correcto).
2. Mariano agregó el campo "Canal referencia (Dr)" al formulario de María García Serrano a mano
   (builder de GHL, no hay endpoint de API para editar formularios — límite ya conocido).
3. Mariano agregó la rama nueva "Pri Rocha" al Condition de "Notificacion influencers", con su
   Internal Notification (SMS, Custom Number, +351 969 515 147), a mano en el builder — mismo
   límite de API.

**Bug encontrado y corregido el mismo día**: al probar el formulario de María García Serrano, llegó
una notificación interna que decía *"Nuevo cliente en pipeline de proveedores — Test Testing,
interesado en una asesoría con **Carolina Chapo**"* — texto equivocado. Causa: el formulario
"Trámites derivados a María García Serrano" se armó duplicando el de Carolina Chapo (existe un
workflow análogo, **"Carolina Chapo - tramites"**, `61519076-1516-4760-8ce9-62cf8ce54262`, que hace
lo mismo para los leads de Carolina Chapo, dentro del pipeline "Proveedores") — el nodo Internal
Notification de **"María García Serrano - tramites"** (`25d94447-e6c5-4852-a13e-0b83b6417017`)
había quedado con el nombre "Carolina Chapo" escrito fijo en el texto del mensaje en vez de
actualizarse al duplicar. Mariano lo corrigió a mano, cambiando el texto a "María García Serrano".
**Lección para la próxima vez que se duplique un formulario/workflow de un partner para armar el de
otro**: revisar todo texto estático (no solo el trigger) por nombres hardcodeados que hayan quedado
del original — no alcanza con que el trigger dispare bien, el contenido del mensaje también hay que
revisarlo entero.

**Pendiente de confirmar**: no se verificó si el workflow "María García Serrano - tramites" tiene
más de un nodo Internal Notification (podría haber otro con el mismo problema sin corregir) ni si
hay otros textos estáticos en el resto del workflow con el mismo error — revisarlo completo la
próxima vez que se abra.

### 5.6 Cierre del caso Pri Rocha (18 agosto 2026) — dos caminos, dos workflows

Continuación de 5.5. Mariano aclaró que Pri Rocha deriva dos tipos de cliente por caminos
distintos, y cada uno necesitó su propia solución:

- **Estancias por estudios** → formulario "Estancias Estudios", cierra Mariano, pasa por el
  pipeline **Pre-venta**. Ya cubierto por la rama "Pri Rocha" agregada a "Notificacion
  influencers" (sección 5.5) — el campo "Canal referencia (Dr)" ya existía en ese formulario
  (confirmado por Mariano). **No se probó de punta a punta con un envío real** (las pruebas del
  día fueron todas por el formulario de María) — queda pendiente de probar cuando surja un caso
  real o una prueba dedicada.
- **Nómada digital** → formulario "Trámites derivados a María García Serrano", pipeline
  **Proveedores**. No lo cubre "Notificacion influencers" (trigger scopeado a cambios de etapa en
  Pre-venta, nunca se dispara para Proveedores). Se armó un workflow nuevo y separado en vez de
  tocar "María García Serrano - tramites" (para no arriesgar la secuencia ya en producción):
  **"Notificar Pri Rocha Nomada Digital"** (`c3d18da5-4813-4414-85d7-b97b78e326fe`, publicado) —
  mismo trigger (Form Submitted = ese formulario) que el workflow existente, corre en paralelo,
  con Condition ("Canal referencia (Dr)" es "Pri Rocha") → Internal Notification (SMS, Custom
  Number, +351969515147) → FINAL. **Probado con éxito** (18 ago, 20:04 UTC) — el SMS llegó.

**Corrección de número (18 agosto 2026)**: durante las pruebas se descubrió que `+34603289674`
(documentado antes como "el WhatsApp de GOTIR") es en realidad la línea laboral personal de
Mariano — la centralita real termina en **3469** (`+34604363469`). Ver corrección completa en
`CLAUDE.md` raíz, sección de herramientas conectadas / GHL.

**Bug menor pendiente, no bloqueante**: el SMS de "Notificar Pri Rocha Nomada Digital" salió desde
`+34603289674` (línea de Mariano) en vez de la centralita (`...3469`), a pesar de que el nodo
Internal Notification tiene la misma configuración que los que sí usan la centralita (Jesús/Nasla/
Wilmen). Diagnóstico agotado por API: el campo de workflow "Número de origen" (Configuración →
Detalles del remitente) está vacío en AMBOS workflows (el que funciona bien y el nuevo) y muestra
"No Data" — no hay números cargados en absoluto en "Sistema telefónico" de GHL. No se encontró
registro de conversación/mensaje vía API para el número de Pri Rocha (los envíos a "Custom Number"
no generan un contacto/conversación rastreable). **Sin resolver** — próximos pasos sugeridos: (a)
revisar la pestaña "Registros de ejecución" del workflow para ver si GHL expone ahí el número real
usado, o (b) contactar soporte de GHL, ya que dos workflows con configuración idéntica dan
resultados distintos — probablemente algo a nivel de cuenta que la API pública no expone. No
bloquea el uso real (el mensaje sí llega), es un detalle de imagen de marca a corregir cuando haya
tiempo.

**Aclaración sobre pruebas repetidas con el mismo contacto (18 agosto 2026)**: al probar dos veces
con el mismo teléfono/email pero distinto nombre, GHL matcheó al mismo contact_id existente
(`dhZ4EyB1jWVm3ui4TPGX`) en vez de crear uno nuevo — como ese contacto ya había entrado una vez a
"María García Serrano - tramites", no volvió a dispararse (comportamiento default de GHL: sin
reingreso a menos que se habilite explícitamente), mientras que sí entró a
"Notificar Pri Rocha Nomada Digital" por ser su primera vez ahí. **No es un bug** — con clientes
reales (teléfono/email genuinamente nuevos) el workflow de María se dispara normal para cada uno.

---

## 6. Piezas sueltas (todo lo demás que no encajó arriba)

### 6.1 Plantilla exacta de Fathom (pegada en el engranaje de resumen)

Estructura del resumen, exactamente en este orden, con estos títulos literales. Si un dato no se mencionó en la llamada, se escribe "No mencionado" en vez de omitir la sección. No se deben inventar datos que no se mencionaron explícitamente en la llamada. Cada línea debe caber en una sola frase.

```
ORIGEN
- Cómo nos conoció / referencia:

SITUACIÓN GEOGRÁFICA
- Ciudad/país de origen:
- Ciudad de destino en España (o "sin definir"):

TIMING
- Fecha tentativa de viaje o entrada a Schengen:

SITUACIÓN LABORAL
- Trabaja actualmente (sí/no, tipo de trabajo):
- Posibilidad de trabajar online desde España:

FORMACIÓN
- Nivel/título/qué estudió:

CURSO
- Curso elegido o "necesita asesoramiento":

UNIDAD FAMILIAR
- Viaja solo/pareja/familia/con menores (edades si aplica):

RESUMEN DEL CASO
- 2-3 frases con lo esencial de lo hablado:

TEMPERATURA
- Caliente / Templado / Frío / No oportunidad:

BLOQUEO PRINCIPAL
- Motivo concreto por el que todavía no compra:

PRÓXIMA ACCIÓN
- Acción concreta:
- Fecha:
- Responsable (GOTIR / Cliente):
```

### 6.2 Notas sueltas de contexto (no encajan en una sección propia)

- El contenido "pre-llamada" (mini-funnel) ya cubre SABE/QUIERE/PUEDE/CUÁNDO antes de que Mariano entre a la llamada — esto es lo que permite que la Fase 2 de la llamada vaya directo al "por qué emocional" en vez de repreguntar lo básico. No hay documento separado que describa el contenido de ese mini-funnel más allá de lo que se infiere de su función.
- El criterio de "no inventar respuestas legales/técnicas" (sección 3.2) es explícitamente más amplio que solo la llamada con Hector — es un principio general de Mariano sobre cómo se construye credibilidad, aplicable a cualquier caso donde la normativa no esté 100% clara (ej. requisitos sanitarios específicos por profesión, casos migratorios atípicos).
- El baseline de julio (sección 3.1) es una **reconstrucción manual**, no un reporte automático del CRM — esto importa porque significa que hoy no hay un dashboard o proceso recurrente que genere estos números solo; alguien tiene que rearmarlos a mano cada vez que se quiera comparar un mes contra este baseline.
- Los ~6.821€ de ingresos de julio, para que no se malinterprete en el futuro: **no** son la métrica de éxito de las mejoras de proceso que se están implementando ahora (guion, plantilla Fathom, próxima acción con fecha, detección de nivel de conciencia) — esas mejoras se miden contra los números de conversión por etapa (formulario, no-show, seguimiento perdido) de una cohorte nueva, no contra ingresos de meses anteriores.

### 6.3 Revisión de pipeline persona por persona (iniciada 17 agosto 2026)

Mariano pidió revisar uno por uno los contactos activos en pipeline ("llamar hoy" y similares) antes
de mandar mensajes o mover etapas, con instrucción explícita de ritmo: **preguntar de a una persona
por vez**, no procesar la lista entera de una — "vale anda preguntandome de a uno y te digo si tengo
nota o si se algo de esa persona o no". También pidió, antes de esto, limpiar del pipeline los casos
que no deberían estar ahí (notas reales que Mariano tiene en WhatsApp pero nunca subió a GHL).

**Regla permanente agregada 17 agosto 2026, tras el caso de Sebastián Gimenez**: antes de proponerle
a Mariano cualquier mensaje de seguimiento nuevo para un contacto, usar `ghl_read_conversation` para
leer el historial real del chat — no alcanza con las notas de GHL ni con lo que Mariano recuerda de
memoria (con Sebastián había un mensaje manual reciente que no estaba en ningún lado más que en el
chat real). Esta tool no transcribe notas de voz de WhatsApp (limitación de entorno, ver
`CLAUDE.md` raíz) — si el último mensaje relevante es un audio, hay que pedirle a Mariano que
cuente el contenido, como ya se viene haciendo.

**Caso 1 — Sebastián Gimenez** (`contact_id=Ma0BBzRU86lESAKjiHqd`) — **resuelto 17 agosto 2026**:
- Mariano no tenía notas propias en WhatsApp para este caso — se armó el mensaje de seguimiento
  leyendo las notas ya cargadas en GHL (vía `ghl_list_contact_notes`) más sus tags (`reunion-agendada`,
  `🔥caliente`, `requiere seguimiento`, `wa: +34603289674`).
- Al revisar la conversación real (`GET /conversations/search`) apareció contexto que no estaba en
  las notas: el 13 de agosto Mariano ya le había escrito manualmente por WhatsApp *"Seba, ya te envié
  el correo, me confirmas si te llegó bien?"*, sin respuesta desde entonces.
- Mariano aprobó mandar el mensaje igual con el texto original (sin ajustarlo para mencionar ese
  correo) y dio la orden explícita de enviarlo de verdad: *"Mandalo así desde el numero de whatsapp
  que yo uso."*
- **Intento de envío 17 agosto 2026 — FALLÓ, no le llegó a Sebastián**: `POST /conversations/messages`
  devolvió `201` dos veces (`message_id=FpWxhGezl7IgaxeIKGa2` sin `conversationProviderId`, después
  `message_id=3Dtvm8SM0KR2fRYnmt3r` agregando el `conversationProviderId` de la conversación existente
  por si hacía falta rutear el mensaje) — un `201` de GHL **no significa entrega real**. Mariano
  confirmó mirando el panel de Conversaciones de GHL que los 3 intentos (los 2 por API + un
  "Try again" manual de él) quedaron con ⚠️ y "Try again", y el compositor mostraba **"WhatsApp no
  está conectado. Conectar WhatsApp."** — el canal de WhatsApp de esta location (una integración *no
  oficial*, no la Business Platform de Meta, según aclaró Mariano) estaba desconectado en ese momento,
  nada que ver con el body del request. El texto del mensaje (arriba) **no llegó a Sebastián todavía**.
  Queda pendiente reconectar el canal (botón "Conectar WhatsApp" en GHL, probablemente re-vincular por
  QR) o que Mariano lo mande manualmente desde su teléfono como hizo el 13 de agosto.
- Se detectó además un contacto duplicado de esta misma persona (`contact_id=6do6xCQ4rBwytUBIrzWz`,
  tag "cualificado visado", sin notas ni oportunidad propia) — **pendiente de decidir con Mariano**,
  prioridad baja (a diferencia del duplicado de Regina Epifanio, este no tiene datos reales cargados
  que se puedan perder).

**Caso 2 — Enrique Eduardo Aguilar** (`contact_id=Q5FBh8Be5ujYviVJVg6c`, oportunidad
`id=1hf61joLaDSIMWZMAtyW`, 670€) — **en curso 17 agosto 2026**:
- Primera confusión real a tener en cuenta: Mariano mezcló dos veces las notas de este caso con las
  de otro lead distinto, **Enrique Esmilse Donna** (`contact_id=h5lkSakInpSPfQ33coQQ`, el mismo que
  estaba pendiente en `direcciones/finanzas/CLAUDE.md` sección 1.1 — ese pendiente queda resuelto,
  es este contacto). Se distinguieron por evidencia técnica: teléfono de Donna con código de
  Argentina (+549, coincide con "Viedma, Río Negro") vs. teléfono de Aguilar con código de Brasil
  (+55, coincide con "Natal, Brasil" — confirmado también porque el email de Aguilar tiene "1957",
  su año de nacimiento, 69 años en 2026). **Si en el futuro aparecen notas de "Enrique" sin apellido
  claro, verificar código de país del teléfono antes de asumir a cuál de los dos pertenecen.**
- Perfil real (dado por Mariano, ya cargado como nota en GHL): 69 años, ciudadano estadounidense
  jubilado, argentino de nacimiento (madre española), ex personal trainer, vive en Natal (Brasil)
  con esposa brasileña. Gasista y plomero matriculado en Argentina (quiere curso RITE acá); también
  camionero especializado en cargas peligrosas/frío — pendiente que Mariano averigüe sobre el CAP.
  Vendría solo primero, después su esposa. Destino: Ciudad Real. Sin el dinero suficiente todavía.
  Sugerencia ya dada: estancia por estudios (ISIE o Maude), viviendo en Rafelbuñol.
- **No tiene notas ni conversación real en GHL para leer** (`ghl_read_conversation` solo trae
  mensajes automáticos: recordatorios de cita, confirmaciones — nada de una conversación real). El
  contexto real vino de un audio de WhatsApp que Mariano escuchó y resumió (ver limitación de
  transcripción de audio en `CLAUDE.md` raíz): Enrique está juntando el dinero para viajar y **quedó
  en llamar él mismo a Mariano cuando llegue a noviembre 2026** (su fecha tentativa de viaje) con el
  dinero completo — compromiso atado a esa fecha puntual, no abierto. Por eso no correspondía un
  mensaje de seguimiento activo ahora (iría en contra de lo que el propio cliente pidió) — en cambio
  se preparó nota completa + tarea de chequeo preventivo para el 26 de octubre de 2026 (antes de
  noviembre, por si no llamó). **Pendiente de confirmación de Mariano para cargar ambas en GHL.**

**Pendiente — resto de la lista "llamar hoy"** (mismo ritmo, uno a la vez, preguntando antes de
actuar en cada caso): Héctor Ojeda (825€, ya tiene una retrospectiva de llamada documentada — ver
sección 3), Luisana Junguittu (825€), Felipe Nogues Martinena (670€), Samuel Salgan (670€), Maria
Taly Navarro, Marylaura Guerrero (750€).

---

## 7. Abierto / pendiente de confirmar por Mariano

Lista honesta de lo que este documento *no* puede responder todavía porque no hay fuente confiable:

- ~~Estructura real de GHL (pipelines, etapas, campos custom, automatizaciones existentes)~~ —
  **resuelto en gran parte el 14 agosto 2026** (ver sección 5): pipelines, etapas y formularios ya
  están confirmados en vivo contra la API. Quedan sub-pendientes puntuales, todos nuevos, surgidos
  de leer los datos reales:
  - Confirmar el propósito de la pipeline **Proveedores** (¿es el flujo de comisiones a
    Sebastián/María/estudios colaboradores, u otra cosa?) — sección 5.1.
  - ~~Confirmar quiénes son Pamela Jordan, Micol Navarro, Jonathan Barrionuevo y Belén Campana~~ —
    **resuelto por completo 17 agosto 2026**: los cuatro eran/son colaboradores identificados (ver
    sección 5.2). Pamela y Belén, ex-closer y ex-mano derecha respectivamente, con perfiles ya
    borrados de GHL a pedido de Mariano. Micol (hermana de Sabrina) sigue activa colaborando en
    marketing/edición. Sabrina Navarro se deja activa a propósito, es información personal — ver 5.2.
  - ~~Confirmar qué son los formularios "Apostilla" y "Alquiler IberoLocations"~~ — **resuelto 17
    agosto 2026**: Apostilla descontinuado (pendiente borrarlo a mano en el builder, sin endpoint de
    API); Alquiler IberoLocations es un servicio real de vivienda con una empresa externa — sección
    5.3.
  - ~~Si "Carolina Chapo" / "María García Serrano" son colaboradores nuevos~~ — **resuelto 17 agosto
    2026**: ambas son usuarias reales de GHL. **María García Serrano es la "María" del dúo
    Sebastián/María**, confirmado por Mariano — sección 5.3.
  - Campos personalizados de contacto/oportunidad: la API no se pudo consultar todavía (el servidor
    MCP no tiene tool para eso) — sección 5.4.
- Contenido exacto del mini-funnel pre-llamada (qué recibe el lead antes de agendar, más allá de su propósito general).
- Si existe o no una solución definida para el problema de estacionalidad (sección 1.6) — identificado, no resuelto.
- Qué rama de GHL priorizar para automatizar primero en n8n (sección 4.5) — hay una lectura razonable pero no es una decisión confirmada.
- Cualquier cambio de precio o servicio que se hable en conversaciones futuras: por instrucción del proyecto, un cambio mencionado en una conversación no se trata como permanente hasta que se actualice el documento de contexto de precios/servicios correspondiente.

---

## 8. Sistema Comercial Antifugas — plan GOTIR (19 agosto 2026)

Mariano compartió por WhatsApp el curso completo (dictado, transcripción de voz) del framework "Mapa
Antifugas" de Facundo Prado. Texto fuente, limpio y reorganizado, en `mapa-antifugas-curso.md`, mismo
directorio — no se duplica el contenido acá, solo la aplicación concreta a GOTIR.

### 8.1 Autoauditoría con evidencia real (no estimada)

Antes de tener el curso completo ya se había hecho un primer mapa contra la evidencia ya documentada
en este archivo (baseline julio 2026, llamada Hector, caso Yeraldin) — resultado: **3 verde, 4
ámbar, 4 rojo** de 11 puntos, publicado como artifact para Mariano el mismo 19 agosto. El framework
que se usó ya coincidía en estructura con el curso completo, así que la evaluación no cambia de
fondo — se afina acá con el vocabulario exacto del curso:

- **Zona 1, antes del presupuesto — resultado general: ámbar.** Indagación y generación de deseo en
  verde (Fase 2 y 3 de la estructura de llamada, sección 2, son de lo más fuerte del proceso).
  Apertura en ámbar — existe el guion de nivel de conciencia (sección 1.5), pero no está confirmado
  que se aplique siempre a todo lead entrante. **Recuperación temprana en rojo** — no existe ningún
  proceso para retomar consultas que quedan sin respuesta en los primeros mensajes; el módulo de
  WhatsApp del workflow de n8n sigue siendo un placeholder (sección 4.4).
- **Zona 2, durante la decisión — resultado general: rojo.** Estructura persuasiva en verde (la regla
  de "fragmentar, no descargar todo junto" de la Fase 3 es la misma idea que el curso describe para
  evitar presupuestos genéricos). Presupuesto persuasivo y prevención de objeciones/cierre en ámbar —
  el guion existe (Fases 3-5), pero la única llamada real analizada en detalle (Hector) tuvo
  exactamente las dos fallas que este bloque mide: nunca hubo invitación explícita a decidir, y no
  hubo un presupuesto escrito para mostrarle a la pareja. **Continuidad post presupuesto en rojo, con
  dato duro**: 40% de las llamadas realizadas en julio 2026 dejó de responder después (sección 3.1).
- **Zona 3, después del presupuesto — resultado general: rojo, la más débil de las tres.**
  **Seguimiento con intención en rojo** — es, literalmente, el mismo punto que este documento ya
  nombraba antes de conocer el framework como "el principal punto de fuga de oportunidades detectado
  hasta ahora" (sección 1.4) y el error #1 de la llamada con Hector (sección 3.2). **Recuperación de
  abandonados en rojo, por decisión explícita** — la prioridad actual es cerrar leads activos por
  sobre hacer nurturing de la base histórica de +2.000 contactos (sección 1.3); correcto dado el
  cuello de botella actual, pero sigue siendo una fuga real con volumen grande dormido. Aprendizaje de
  ventas perdidas en ámbar — hay cultura real de esto (Hector como caso de estudio, el bug de no-show
  corregido en vivo el 18 ago, sección 3.1.1), pero es caso por caso, no un paso obligatorio después
  de cada venta perdida.

**Zona que más está costando ventas hoy: zona 3, después del presupuesto.** Coincide con lo que el
propio curso predice como "la fuga más visible", y con lo que este documento ya venía señalando antes
de conocer el framework completo.

**Las 2 fugas prioritarias** (mismo criterio del curso: no corregir 20 cosas a la vez):
1. Cerrar llamadas sin próxima acción + fecha + responsable — aparece tres veces en la evidencia:
   como regla ya escrita (sección 1.4), como error nombrado en la llamada con Hector (sección 3.2), y
   como motor del 40% de seguimiento perdido (sección 3.1).
2. Contexto del lead que se pierde entre agendar y la llamada — caso real: Yeraldin Coba dejó una
   nota en el formulario de reserva avisando que el horario asignado no le iba a funcionar por
   diferencia horaria y pidiendo coordinar por WhatsApp; nadie la vio; quedó `noshow` (sección 3.1.1).

### 8.2 Las 3 capas aplicadas a GOTIR — el diagnóstico que más importa

Esta es la parte del curso que más cambia la lectura de todo lo de arriba. El mapa antifugas mide
**capa 1 (proceso)** — y en esa capa GOTIR no está mal: la estructura de llamada (sección 2) es de lo
más maduro del negocio, con guiones específicos para descubrimiento, objeciones y cierre.

El curso separa dos capas más, y ahí está el punto real:

- **Capa 2 (ejecución — ¿el equipo lo ejecuta de forma consistente?) prácticamente no aplica hoy**:
  Mariano es setter + closer + seguimiento, solo (sección 1.3) — no hay equipo con interpretaciones
  distintas del proceso, hay una sola persona. Esto no es una fuga en sí, pero **significa que toda
  la responsabilidad de la capa 2 recae también en la capa 3.**
- **Capa 3 (liderazgo/dependencia) es, hoy, la causa raíz real de casi todas las fugas en rojo de
  arriba.** No hay ningún mecanismo que sostenga el proceso sin que Mariano lo recuerde en el
  momento: la "regla de oro" de próxima acción con fecha vive en un documento, no en un campo
  obligatorio de GHL; la nota de Yeraldin quedó invisible porque nadie revisó el formulario antes de
  la cita, no porque faltara un guion; el tracking de no-show estuvo roto semanas porque nadie
  actualizaba un campo, no porque el proceso no lo contemplara (sección 3.1.1). El propio n8n lo
  confirma en la práctica: el módulo de GHL sigue siendo un placeholder (sección 4.4) — hoy **nada
  automatiza lo que Mariano ya sabe que tiene que hacer**, todo depende de que se acuerde, cada vez.

**Conclusión de fondo**: las fugas de GOTIR no son un problema de proceso mal diseñado (capa 1 está
bien) ni de un equipo que ejecuta distinto (capa 2 no aplica, es una sola persona) — son un problema
de **capa 3 sin ningún respaldo sistémico**. La solución no es "escribir mejor el proceso" (ya está
bien escrito) ni "entrenar mejor al vendedor" (es Mariano, ya lo sabe) — es **convertir las reglas
que ya existen en obligaciones que el sistema hace cumplir solo**, para que sobrevivan sin que
Mariano tenga que sostenerlas activamente en cada caso.

### 8.3 Plan de mejora priorizado (actualizado con la lectura de capas)

Mismo plan de 5 pasos ya compartido con Mariano (artifact del 19 ago), reordenado con la capa 3 como
criterio explícito de diseño — cada acción de abajo es, en el fondo, "mover una regla de la cabeza de
Mariano a un campo/automatización que no dependa de que se acuerde":

1. **Campo obligatorio de próxima acción en GHL** — no una regla en un documento, un campo que hay
   que llenar para poder cerrar la tarea de la llamada. Dueño: Mariano. Esfuerzo: bajo. Cuándo: ya.
2. **Chequeo de la nota de reserva antes de cada llamada agendada** — confirmar si el widget de GHL
   expone la nota del cliente de forma visible; si no, agregar 5 minutos de revisión antes de cada
   cita. Dueño: Mariano. Esfuerzo: bajo. Cuándo: esta semana.
3. **Automatizar Fathom → GHL** — el paso donde vive la fuga #1, hoy 100% manual (secciones 1.4 y
   4.5). El router de n8n ya tiene las intenciones de GHL mapeadas sin conectar (sección 4.4) — es la
   rama más barata de construir primero. Esto es, literalmente, mover la capa 3 de la memoria de
   Mariano a una automatización. Dueño: IT/n8n. Esfuerzo: medio. Cuándo: próximas semanas.
4. **Pieza de presupuesto escrito y persuasivo** — resuelve la objeción "lo tengo que hablar en casa"
   con algo concreto en la mano, no un resumen improvisado. Dueño: Mariano + Marketing. Esfuerzo:
   medio. Cuándo: este mes.
5. **Recorrido mínimo de recuperación para presupuestos de los últimos 30 días** (no la base
   histórica completa de +2.000 — eso sigue sin ser prioridad, sección 1.3) — volumen chico, tibio, no
   frío. Dueño: Mariano. Esfuerzo: medio. Cuándo: después del paso 1.

**Confirmado 19 agosto 2026**: Mariano pidió agregar el post-mortem de venta perdida como paso
obligatorio — ya está como paso 6 del checklist "después de colgar" (sección 2).

---

## 9. Chequeo diario proactivo y sistema de pendientes (19 agosto 2026)

Mariano pidió explícitamente pasar de un sistema reactivo (el sistema responde lo que se le
pregunta) a uno proactivo: que el sistema le recuerde las llamadas del día, las tareas que quedaron
sin resolver, y todo lo que él mencionó como necesario y después no se volvió a tocar — porque está
solo sosteniendo todas las áreas de GOTIR (y del resto de su vida) y es normal que se le pasen cosas
con la cabeza en tantos frentes a la vez. Motivación textual suya: quiere que el sistema actúe "como
director general de todas las áreas, pero también como una especie de secretario" que todos los días
le diga qué sigue pendiente — no solo cuando él se acuerda de preguntar.

### 9.1 Mecanismo: dos Routines, mañana y noche

Se configuraron **dos** Routines (triggers programados) hacia esta misma conversación —
complementarias, no duplicadas:

**Chequeo de la mañana** (`trig_01Us5mDwAASHmmzEqxsihfig`, agregada 19 ago 2026, a pedido explícito
de Mariano) — dispara a las **08:00 hora de España** (06:00 UTC en horario de verano). Mirada hacia
adelante, corta: qué citas tiene agendadas hoy, qué pendientes de `pendientes-activos.md` vencen hoy
o mañana (esos primero), y si hay algo de Ruge con fecha cercana. No repite el detalle completo del
chequeo de la noche anterior — es el arranque del día, no un resumen.

**Chequeo de la noche** (`trig_01VqNHfVMi8jzMLpvfcXVHvn`, creada 19 ago 2026) — dispara a las
**20:00 hora de España** (18:00 UTC en horario de verano — revisar el offset en ambas Routines
cuando España pase a horario de invierno, a fines de octubre 2026). Mirada hacia atrás, sobre lo que
pasó en el día:

1. Consulta `ghl_list_calendar_events` del calendario "Asesoría GOTIR" (`Sl5Of5SLsAgTrwxhwoAE`) para
   las citas del día.
2. Para cada una, le pregunta a Mariano cómo fue, si ya cargó el resumen de Fathom, si aplicó la
   etiqueta de temperatura, si creó la tarea de próxima acción con fecha, y si marcó `showed`/
   `noshow` — y si no cerró, si hizo el post-mortem (sección 2, pasos 1-6). **Agregado 20/21 agosto
   2026**: también consulta el campo de la oportunidad "Próxima acción - Fecha y hora exacta"
   (sección 13) para cada llamada del día — si está vacío o solo tiene fecha sin hora, lo señala
   como pendiente sin esperar a que Mariano lo note solo. Esto es lo que hoy hace cumplir el "campo
   obligatorio" de la Fase A de la Propuesta 4 (sección 13) — GHL no tiene forma de bloquear por API
   que se cierre una llamada sin llenarlo, así que el chequeo cumple esa función mientras no exista
   un mecanismo nativo.
3. Lee `pendientes-activos.md` (raíz de `mariano-os/`) y vuelve a mencionar cualquier ítem que siga
   `abierto` o `en curso` — **las veces que haga falta**, no una sola vez y listo.
4. Si la ventana de aprendizaje de 20 llamadas (sección 9.2) sigue abierta, pide el resumen/
   transcripción de las llamadas del día que todavía no se haya recibido.

Las dos son chequeos cortos y directos, no un cuestionario largo — el objetivo es que Mariano no
tenga que acordarse de nada, no sumarle otra carga.

### 9.2 Ventana de aprendizaje — primeras 20 llamadas con transcripción

A pedido de Mariano, durante al menos 20 llamadas va a compartir el resumen/transcripción (Fathom)
de cada una para que el sistema registre patrones: preguntas frecuentes de los clientes, errores
recurrentes de Mariano en la llamada, y ajustes sugeridos al guion (sección 2). El registro vive en
`patrones-llamadas.md`, mismo directorio — se actualiza cada vez que llega una transcripción nueva.

**Contador: 0/20 llamadas registradas al 19 agosto 2026.**

### 9.3 `pendientes-activos.md` — qué es y cómo se usa

Vive en la raíz de `mariano-os/` (no solo GOTIR), porque cubre cualquier compromiso que Mariano
mencione como necesario en cualquier área — incluido ministerio/Ruge, a pedido explícito suyo el 19
de agosto. Cada ítem registra: fecha en que se mencionó, área, descripción, estado, y cuántas veces
ya se le recordó. Regla simple: si un ítem sigue abierto, se vuelve a mencionar en el chequeo diario
— nunca se asume que un solo recordatorio alcanza. Un ítem sale de la lista solo cuando Mariano
confirma que está hecho, no por inferencia.

**Ya cargados ahí (19 agosto 2026), señalados por Mariano como pedidos previos que se perdieron sin
seguimiento:**
- Mini-chat/bandeja unificada para responder mensajes de TikTok.
- Proceso de precalificación antes de la llamada (que el lead llegue sabiendo requisitos y precios) —
  a confirmar si es lo mismo que el "mini-funnel pre-llamada" ya mencionado en la sección 6.2, o algo
  distinto.

---

## 10. Caso Regina Lucia Epifanio (19/20 agosto 2026) — duplicado de oportunidad y WhatsApp caído

### 10.1 El duplicado de contacto/oportunidad

Mariano había pedido hace unos días mover a Regina a "ganada" tras confirmar que Gisela le pasa el
50% de un pago recibido directo (visado de estudios desde origen, 668€). Al revisar, existían **dos
contactos distintos** con el mismo nombre:
- `vXvPgYTIctXeNlM6juoh` — **Regina Lucia Epifanio**, el contacto real (email, teléfono argentino,
  conversación real con Mariano desde su WhatsApp personal +34603289674).
- `OvKjvt9MQvLiS2R6ofDG` — **"REGINA EPIFANIO"** (sin "Lucia"), un contacto que en realidad quedó
  de una **prueba de la conexión MCP-GHL el 14 de agosto** (ver `CLAUDE.md` raíz, "se creó una
  oportunidad real (Regina Epifanio) después del fix") — no es un lead real duplicado, es un
  resabio de testing.

Ambos terminaron con una oportunidad de "Visado" (668€) cada uno, lo que generó la confusión de
Mariano marcando primero la equivocada como ganada. **Resuelto 19/20 ago**: Mariano borró la
oportunidad de "Estancia" (825€, otro trámite, sin relación) y la oportunidad del contacto de
prueba (`bmu3mMXm0aVco9buvdAv`, la que había quedado abandonada). Queda **una sola oportunidad real**:
"Regina Lucia Epifanio - Visado" (`Q4OXfkauBNkLO5ibprGz`), status `won`, etapa Pagado.

**Lección para no repetir**: cuando aparezca un contacto con nombre casi idéntico a uno real y sin
teléfono/email/conversación real cargada, sospechar que es un resabio de prueba de este sistema
(sección técnica de `CLAUDE.md` raíz) antes de asumir que es un duplicado de lead genuino.

### 10.2 Automatización de contrato — sí se dispara, pero WhatsApp no entrega nada

El workflow nativo de GHL **"Pago realizado- contrato"** (`4e156779-b873-46dc-888b-896c3abcbb5f`,
publicado) sí se disparó correctamente al mover la oportunidad a ganada/Pagado — confirmado en el
"Registro de ejecución" de GHL (Create/Update Opportunity → Send Documents & Contracts → tags →
Finished, todo "Ejecutado"). Y en la conversación real del contacto aparecen efectivamente un email
con el link al contrato (`sendlink.co`, llegó a `reginaepi01@gmail.com`) y un mensaje `{WA#1}`
(código correcto que le dice a la centralita de GOTIR que mande por WhatsApp, no un error de
plantilla — **no tocar ni "arreglar" ese código, funciona bien**).

**Pero nada llegó por WhatsApp.** Causa real, confirmada por Mariano: **la empresa que les daba
GHL como reseller dejó de darles servicio y los migró directo a una cuenta de Go High Level propia
— y en esa migración no quedó conectado ningún proveedor de WhatsApp** (ni el genérico anterior con
QR, ni el oficial de Meta Business). El workflow y el `{WA#1}` funcionan perfecto; simplemente no
hay ningún canal de WhatsApp activo ahora mismo para que la centralita entregue nada. GHL marca el
paso como "Ejecutado" igual, sin ningún error visible — el mismo patrón ya visto con Sebastián
Gimenez el 17 de agosto (ver sección 6.3), que en retrospectiva es casi seguro el mismo problema de
fondo, no un caso aislado.

**RESUELTO (21 agosto 2026)**: Mariano identificó al reseller anterior como **"Trindia"** (nombre
oído por dictado, ortografía sin confirmar) y reconectó el canal de WhatsApp con un proveedor
nuevo, **GoGHL.ai** (`app.goghl.ai`) — mismo tipo de integración no oficial que la anterior, no la
WhatsApp Business Platform de Meta. Los 4 números de GOTIR ya están dados de alta ahí y muestran
"Conectado" en el panel:
- **WhatsApp #1** — `+34604363469`, marcado **Predeterminado** — es la centralita real de GOTIR,
  coincide con lo ya documentado (`CLAUDE.md` raíz, tag `wa: +34604363469`) — es el número al que
  apunta `{WA#1}` en los workflows.
- **WhatsApp #2** — `+34603289674`, "Mariano Barcelona - GOTIR" — coincide con la línea laboral
  personal de Mariano ya documentada, y con el `fromNumber` hardcodeado en la tool
  `ghl_send_message` del servidor MCP — sigue siendo válido.
- **WhatsApp #3** — `+34634194829`, etiquetado **"Pamela Jordan - GOTIR"**.
- **WhatsApp #4** — `+5493512594563` (número argentino), etiquetado **"Belén Campana GOTIR"**.

**Pendiente de confirmar con Mariano, no asumido**: Pamela Jordan y Belén Campana ya no trabajan ni
van a trabajar con GOTIR (ver sección 5.2) — sus usuarios de GHL ya fueron borrados el 17 agosto,
pero estos dos números de WhatsApp con sus nombres siguen conectados y activos en GoGHL.ai. No se
sabe si son líneas que GOTIR sigue usando bajo otro criterio (ej. reasignadas a otra persona) o si
quedaron así por la migración y convendría desconectarlas/renombrarlas — preguntarle a Mariano.

**Límite real de esta revisión**: la API de GHL no expone el detalle interno de los workflows (ver
sección 5.5 más abajo — límite ya confirmado antes), así que no se puede auditar por API si cada
automatización usa el número de WhatsApp correcto. Lo que sí se pudo confirmar: los números que
SÍ están hardcodeados en código propio de este sistema (`{WA#1}` en los workflows de GHL y el
`fromNumber` de `ghl_send_message`) coinciden con números reales y conectados. El resto de la
revisión (¿hay algún workflow en el builder de GHL que todavía apunte a un canal de WhatsApp viejo
o roto?) tiene que hacerse a mano en el builder — no hay forma de confirmarlo por API.

**Impacto real: todo lo que dependa de WhatsApp está caído** — mensajes de contrato, seguimientos,
notificaciones a colaboradores (Notificacion influencers, etc.) — hasta que Mariano reconecte un
proveedor. El canal de email no está afectado. Esto no se puede resolver por API (ni la de GHL ni
la de n8n dan acceso para tocar workflows o conectar canales de mensajería) — **requiere que
Mariano entre a GHL → Conversaciones/Configuración y reconecte el proveedor de WhatsApp**, un canal
genérico con QR o el oficial de Meta Business. Registrado como pendiente urgente y bloqueante en
`pendientes-activos.md`.

### 10.3 Límites de API confirmados en este caso (para no reintentar)

- `GET /workflows/{id}` y cualquier variante de detalle/ejecuciones de un workflow → 404, la API
  pública de GHL no expone la lógica interna de un workflow ni su historial (coincide con el límite
  ya documentado en `CLAUDE.md` raíz, sección de herramientas conectadas).
- Los tools de n8n disponibles en esta sesión (`execute_workflow`, `get_workflow_details`,
  `search_workflows`) **no incluyen crear ni editar workflows** — solo ejecutar y listar los que ya
  existen. No hay credencial de API de n8n cargada en este entorno (`.env` no tiene ninguna
  variable `N8N_*`) para intentarlo por HTTP directo tampoco.
- Sí funciona (y fue lo que permitió avanzar el diagnóstico): `GET /workflows/?locationId=...` por
  curl directo (mismo patrón ya usado en sección 5.5) para listar nombre/estado de los workflows
  existentes — así se encontró "Pago realizado- contrato" entre 17 workflows reales de la cuenta.

---

## 11. Mapa Antifugas — actualización viva (20 agosto 2026)

Mariano pidió explícitamente que este análisis se mantenga como práctica estándar, no como un
ejercicio de una sola vez — cada vez que haya evidencia real nueva (una llamada, un caso como el de
Regina), hay que releer el semáforo de la sección 8 a la luz de esa evidencia, no repetirlo sin
cambios. Esta sección es la versión más reciente; la sección 8 queda como el análisis original del
19 ago, sin reescribirla.

**Conclusión de fondo con la evidencia acumulada hasta hoy**: no hay una fuga de habilidad
comercial. La llamada con Javier Maddia (sección "Autoauditoría", zona 1) sigue siendo la prueba de
que el guion funciona bien ejecutado. Las fugas reales están en dos lugares distintos:

1. **Capa 3 (dependencia de que Mariano se acuerde), sin cambios respecto al 19 ago**: funcionó con
   Yeraldin (se revisó el chat real, se encontró el motivo real, se recontactó) pero no con
   Nazareth, mismo día, mismo tipo de caso — el mecanismo existe pero no es sistemático todavía.
   Mismo patrón con Javier: la continuidad post-presupuesto fue excelente (resumen y promo el mismo
   día), pero no hay evidencia de una tarea con fecha concreta de seguimiento — depende de que
   Mariano se acuerde del viernes 21 ago sin nada que se lo recuerde por fuera de este sistema.
2. **Una capa nueva que el curso no contempla — "capa 0", el canal en sí**: el caso Regina (sección
   10) mostró que la infraestructura de WhatsApp está caída (sin proveedor conectado tras la
   migración del reseller) y que GHL no avisa cuando esto pasa — un paso de automatización puede
   figurar "Ejecutado" sin haber entregado nada. Ningún ajuste de proceso o de guion importa si el
   mensaje no sale físicamente. Explica retroactivamente el caso de Sebastián Gimenez también.

**Semáforo actualizado (reemplaza el de la sección 8.1 mientras no haya evidencia más nueva)**:
- Zona 1 (antes del presupuesto): **ámbar**. Indagación y generación de deseo siguen en verde.
  Recuperación temprana sube de rojo a **ámbar** — funcionó una vez (Yeraldin), no la otra
  (Nazareth, sigue sin recontactar al cierre de este análisis).
- Zona 2 (durante la decisión): **rojo en conjunto, con una mejora real**. Continuidad post
  presupuesto sube de rojo a **ámbar** — Javier es el primer caso real donde funcionó bien. El
  problema de esa llamada no fue de seguimiento, fue la promo en USDT que contradice la política de
  pagos (pendiente urgente, vence 21 ago — ver `pendientes-activos.md`).
- Zona 3 (después del presupuesto): sigue siendo la más débil, sin cambios — seguimiento con
  intención en rojo, recuperación de abandonados en rojo (por decisión, no por descuido), aprendizaje
  en ámbar (post-mortem ya obligatorio desde el 19 ago).

**Las 2 fugas prioritarias, actualizadas**:
1. **Infraestructura de WhatsApp caída** — pasa a ser la fuga #1 por encima de cualquier otra,
   porque mientras no se resuelva, ningún ajuste de proceso llega a ejecutarse de verdad.
2. **Seguimiento con intención sin sistema** — Nazareth sin recontactar, deadline de Javier (21 ago)
   sin una tarea con fecha que lo sostenga.

**Regla para las próximas veces que se actualice este análisis**: no repetir el mapa completo de
cero — anclar cada actualización a evidencia real nueva (una llamada, un caso, un dato duro), igual
que se hizo acá, y dejar constancia de qué cambió y qué se mantiene igual.

---

## 12. Estándar de expertise en ventas — instrucción permanente (20 agosto 2026)

Mariano pidió explícitamente que esto deje de ser algo puntual (una corrección sobre un mensaje de
Sara Sofía) y pase a ser un estándar permanente: **todo mensaje de seguimiento, toda propuesta de
mini-funnel, todo guion de llamada o cualquier otro output de venta que este sistema proponga tiene
que estar fundamentado en técnica de venta real de referentes reconocidos** — no en intuición
genérica. Verificado y actualizado el 20 de agosto de 2026 contra fuentes reales (no solo
conocimiento de entrenamiento) — ver fuentes al final de esta sección.

### 12.1 Por qué se agregó esto (caso real que lo disparó)

Mariano pidió un mensaje de seguimiento para Sara Sofía (no respondía hacía 1h+). La primera
versión propuesta acá decía *"quería saber cómo vas pensando... quería asegurarme de que esté todo
bien de tu lado"* — sonaba razonable, pero tenía dos fallas clásicas y caras: era un genérico
**"checking in"** (sin motivo real para escribir hoy) y sonaba **necesitado** (proyectaba que
Mariano esperaba por ella, no que tenía el control). Mariano lo notó y pidió que de ahora en más se
verifique explícitamente contra técnica de venta real antes de proponer cualquier mensaje — no
alcanza con que "suene bien".

### 12.2 Referentes a tener en cuenta (marco de trabajo, no cita textual)

No inventar citas literales de estos autores — usarlos como marco de criterio, y decir
explícitamente cuando algo es una aplicación de un principio general, no una frase exacta del
libro:

- **Grant Cardone, *Sell or Be Sold / Vendes o Vendes*** — el referente que Mariano nombra
  explícitamente. Ideas centrales aplicables acá: los compradores no son transparentes por default
  (no tomar el silencio como la última palabra, pero tampoco como excusa para insistir sin
  criterio); **lenguaje asuntivo** una vez que ya hubo intención real mostrada (hablar de *cómo* se
  avanza, no de *si* se avanza); **nunca proyectar necesidad** — el vendedor con más opciones
  cierra más, así que el mensaje debe sonar a que Mariano tiene el control, no a que está
  esperando una respuesta; persistencia real en el seguimiento (la mayoría de las ventas se pierden
  por abandonar el contacto demasiado pronto, no por un "no" real del cliente).
- **Robert Cialdini, *Influence*** — escasez y urgencia **siempre reales, nunca inventadas** (esto
  ya es un principio propio de Mariano, documentado en la sección 3.2 — Cialdini lo respalda con
  evidencia: la urgencia fabricada se detecta y quema confianza); prueba social y compromiso/
  consistencia (recordarle a alguien lo que ya dijo que quería, en vez de lo que no cumplió).
- **Chris Voss, *Never Split the Difference*** — preguntas calibradas en vez de cerradas
  agresivas; dar una **salida fácil** ("si preferís más tiempo, decime y no hay drama") reduce la
  presión percibida y, contraintuitivamente, mejora la tasa de respuesta real — no es debilidad, es
  técnica.
- Aplicar con criterio, no como checklist rígido — el objetivo es que el mensaje sea efectivo y
  genuino, no que mencione los tres autores en cada línea.

### 12.3 Consenso actualizado 2026 (verificado por búsqueda web el 20 ago 2026, no solo memoria)

Contra fuentes de venta B2B/B2C actuales (Apollo, Artisan, dialmycalls, ex.plo.re — ver enlaces
abajo), el consenso moderno confirma y matiza lo de arriba:

- **Un solo CTA cerrado y de fricción mínima** (pregunta binaria o de una palabra) supera casi el
  doble en tasa de respuesta a un mensaje con 3+ opciones abiertas — no dar de más para elegir.
  Ejemplo de CTA cerrado: "¿Opción 2 o 3? Respondé con el número."
  Ejemplo de CTA cerrado: "¿Te viene bien el jueves a las 10?"
- **Estructura recomendada del primer follow-up**: gancho de contexto (algo real de lo ya hablado)
  + motivo concreto para escribir hoy (no "cómo estás") + un detalle específico + un solo CTA
  cerrado + una salida fácil. Menos de ~125 palabras.
- **El cierre moderno es consultivo, no de alta presión** — el comprador de 2026 detecta
  manipulación y se aleja apenas la huele. El cierre tiene que sentirse como el paso natural de un
  proceso bien llevado (coherente con la "regla de oro" ya documentada en la sección 2: "hacer que
  la persona sienta que la escuchaste antes de venderle algo"), no como un truco al final.
- **Nunca mencionar que el cliente incumplió un plazo que él mismo puso** ("dijiste que en 2hs
  ibas a responder") — resta autoridad y suena a reclamo, no a seguimiento comercial.

### 12.4 Checklist a aplicar en todo mensaje de seguimiento, guion o funnel de ahora en más

1. ¿Tiene un motivo concreto para escribir *hoy*, o es un "checking in" genérico? (si es lo
   segundo, reescribir).
2. ¿El lenguaje asume que avanza (si ya mostró intención real), o pregunta tentativamente "¿querés
   seguir?"?
3. ¿El CTA es uno solo, cerrado, y de fricción mínima — o le estoy dando 3+ opciones abiertas?
4. ¿La urgencia que uso es real (cupos, fechas, plazos genuinos) o la estoy inventando?
5. ¿Incluye una salida fácil que baje la presión percibida?
6. ¿Menciono algún incumplimiento del cliente? Si sí, sacarlo.
7. ¿Es corto? (segundo mensaje en adelante, más corto todavía que el primero).

Este checklist aplica a: mensajes de seguimiento post-llamada, mensajes de recuperación de
no-shows/fríos, el mini-funnel pre-llamada (`patrones-apertura-conversacion.md`), la secuencia
post-agendamiento (`secuencia-post-agendamiento.md`), y cualquier ajuste futuro al guion de llamada
(sección 2 de este documento).

**Fuentes verificadas 20 agosto 2026** (búsqueda web, no solo memoria de entrenamiento):
- [8 Sales Closing Techniques That Actually Work (2026) — Wave Connect](https://wavecnct.com/blogs/sales-closing-techniques)
- [What Are the Best Closing Techniques in Sales? 2026 — Apollo](https://www.apollo.io/insights/closing-techniques-in-sales)
- [7 effective follow-up techniques to close more sales — Artisan AI](https://www.artisan.co/blog/follow-up-techniques-in-sales)
- [10 Follow-Up Text Message Templates That Keep Leads Engaged — DialMyCalls](https://www.dialmycalls.com/blog/follow-up-text-message-templates)
- [Follow-Up Best Practices for Sales Pros: 15 Rules — ex.plo.re](https://ex.plo.re/crm/follow-up-best-practices/)

---

## 13. Propuesta 4 (Motor + Copiloto) — Fase A ejecutada (20/21 agosto 2026)

Mariano eligió la Propuesta 4 (`direcciones/comercial/propuestas-sistema-comercial.md`) y pidió
explícitamente empezar por la Fase A y ejecutarla solo, sin pedirle confirmación paso a paso. Esto
es lo que se hizo y lo que quedó, en detalle honesto:

### 13.1 Hecho por API, sin intervención de Mariano

Dos custom fields nuevos creados en vivo contra la API de GHL (`POST
/locations/{locationId}/customFields`, mismo endpoint ya usado antes solo para editar campos
existentes — funcionar para creación no estaba confirmado hasta ahora, quedó probado):

- **"Próxima acción - Fecha y hora exacta"** — `model=opportunity`, `dataType=TEXT`, id
  `kjYi4hnJFKwwZi63jydV`, `fieldKey=opportunity.prxima_accin__fecha_y_hora_exacta` (GHL le sacó los
  acentos al generar el fieldKey automáticamente, es normal, no afecta el nombre visible). Tipo
  TEXT a propósito, no DATE — así admite el string completo "día/mes hora" en un solo campo visible
  en la tarjeta de la oportunidad, sin depender de que el selector de fecha de GHL soporte hora.
  Resuelve directamente el patrón confirmado 2/2 en `patrones-llamadas.md` (próxima acción sin hora
  exacta).
- **"Esperando respuesta desde"** — `model=contact`, `dataType=DATE`, id `qLXajIzazssOvAsseqT4`,
  `fieldKey=contact.esperando_respuesta_desde`. Vive en el contacto (no en la oportunidad) porque el
  estado "está esperando que le responda" es de la conversación, no de un trámite puntual. Queda
  vacío hasta que el mecanismo de 13.2 lo llene.

### 13.2 Lo que NO se pudo hacer por API — límite real, no un tema de confirmación

La "etiqueta automática" de la Propuesta 4 (que detecte solo un mensaje entrante sin responder y
llene el campo de arriba) requiere un **Workflow de GHL con trigger de mensaje entrante** —
Automation → Workflows. Ya está documentado como límite duro en la sección 5.5: `GET /workflows/`
no expone la lógica interna, y **no existe ningún endpoint para crear ni editar workflows**. No es
que falte confirmación de Mariano — es que la API pública de GHL, hoy, no ofrece ningún camino para
que este sistema arme esa lógica él solo, con o sin autorización.

**Spec funcional para cuando Mariano tenga ~10 minutos en el builder** (no son instrucciones de UI
paso a paso, porque la interfaz puede cambiar — es lo que el workflow tiene que lograr):
1. Un workflow que dispare con el trigger nativo de "mensaje entrante / Customer Replied", y como
   acción setee el custom field de contacto "Esperando respuesta desde" = fecha/hora del trigger.
2. Un segundo workflow (o una segunda rama) que dispare cuando sale un mensaje de Mariano hacia ese
   contacto (manual o vía `ghl_send_message`) y vacíe ese mismo campo — así el campo solo tiene
   valor mientras de verdad hay algo sin responder.
3. Opcional pero recomendado: que el primer workflow también aplique una etiqueta simple
   "Esperando respuesta" al contacto (no hace falta que la etiqueta tenga la fecha adentro del
   texto, para eso ya está el custom field) — sirve para poder filtrar contactos en GHL a simple
   vista, no solo por campo.
Mientras este mecanismo no exista, el campo "Esperando respuesta desde" queda creado pero inerte —
no se completa solo todavía.

### 13.3 Qué se ajustó en el proceso existente para no depender de la Fase A completa

Dos cambios que **sí pudo hacer este sistema solo**, sin builder de GHL, para que la Fase A ya
empiece a sumar aunque el mecanismo de 13.2 no esté armado:
- El paso 3 de "Después de colgar" (sección 2) ahora incluye cargar el campo de la oportunidad,
  además de la tarea de GHL.
- El chequeo de la noche (sección 9.1) ahora también audita ese campo por cada llamada del día — es
  la forma de que "campo obligatorio" sea real en la práctica (nadie deja de llenarlo sin que se
  note) mientras GHL no ofrezca una manera de bloquearlo a nivel de plataforma.

### 13.4 Frecuencia del chequeo de mensajes pendientes (pregunta de Mariano, 20 ago 2026)

Hoy, el único mecanismo que revisa mensajes/pendientes es el par de Routines de la sección 9.1 —
**dos veces por día** (08:00 y 20:00 hora de España). Hasta que la Fase C (el copiloto que arma
borradores) exista, esa es la cadencia real. Una vez que la Fase C esté construida, tiene sentido
subir la frecuencia (ej. cada 2-3 horas en horario laboral) porque ahí sí habría valor en enterarse
antes — pero no antes, porque hoy el chequeo no arma nada automáticamente, solo pregunta.

### 13.5 Sobre hacer esto retroactivo a mensajes de meses anteriores (pregunta de Mariano, 20 ago 2026)

Es técnicamente posible (barrer todos los contactos con `ghl_search_contacts` + leer cada
conversación con `ghl_read_conversation`), pero **no se ejecutó sin antes dejarlo anotado acá**, por
tres motivos concretos, no por seguir pidiendo permiso porque sí:
1. **Ya existe una decisión explícita de Mariano en sentido contrario** (sección 1.3): priorizar
   cerrar leads activos por sobre hacer nurturing de la base histórica de +2.000 contactos — un
   barrido retroactivo completo de "todos los clientes... en los últimos meses" es exactamente ese
   nurturing, a una escala mucho mayor que el "recorrido mínimo de 30 días" que la sección 8.3 (punto
   5) ya había acotado a propósito.
2. El diseño central de la propia Propuesta 4 es que Mariano ve y aprueba cada mensaje antes de que
   salga — un barrido de "todos, meses" generaría potencialmente cientos de borradores para revisar
   de una sola vez, un volumen que compite directo con el objetivo de protegerle el tiempo
   (sección 0), lo opuesto a lo que la Propuesta 4 busca.
3. Es, en rigor, una capacidad de la **Fase C** (el copiloto que arma los borradores), que todavía
   no está construida — antes de barrer meses de historial hace falta que el mecanismo que arma cada
   respuesta ya esté probado con volumen chico y reciente.

**Recomendación, no ejecutada todavía**: cuando llegue el momento, acotar el primer barrido
retroactivo a algo mucho más chico que "todos, meses" — por ejemplo, presupuestos/llamadas de los
últimos 30 días (mismo criterio que sección 8.3), y ahí sí revisar los resultados juntos antes de
decidir si vale la pena ir más atrás. Queda anotado como paso futuro en `pendientes-activos.md`, no
descartado.
