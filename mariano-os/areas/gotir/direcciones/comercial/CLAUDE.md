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
- **Colaboradores externos mencionados**: Sebastián y María (abogados, estancia por estudios, 250€ por caso), Gisella (visado de estudios desde origen, arma grupo de WhatsApp cuando faltan ≤6 meses para la presentación).
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
3. Crear tarea en GHL con la próxima acción + fecha exacta acordada en la Fase 5
4. Si se detectó un bloqueo nuevo o un diferenciador que funcionó bien, anotarlo — sirve para afinar el guion con el tiempo

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
- **GOTIR** (`6CRhAWYRRL8gMpwwdOyi`) — tipo colectivo, slots de 60 min. Candidato más probable al
  "[link]" de agendar llamada que se menciona en la sección 1.5/2 de este documento, a confirmar.
- **Asesoría GOTIR** (`Sl5Of5SLsAgTrwxhwoAE`) — tipo personal, slots de 60 min.
- **Mariano Barcelona** (`DaiTSbSX6zMA7wIclOgw`) — personal, 30 min.
- Calendarios personales de: Sabrina Navarro, Pamela Jordan, Micol Navarro, Jonathan Barrionuevo,
  Rocío Jury (30-60 min c/u).

  **Identidades resueltas en gran parte (17 agosto 2026)**, cruzando contra `GET /users/` de GHL (se
  habilitó el scope `users.readonly` ese mismo día):
  - **Sabrina Navarro** (`sabriinavarro.sn@gmail.com`) — sigue como usuario **admin activo** en GHL
    (`deleted: false`), pese a que `CLAUDE.md` raíz dice que ya no trabaja en GOTIR. Esto confirma
    que el calendario no es un error de configuración — la cuenta en sí sigue viva. Sigue sin
    confirmarse si es un resabio administrativo sin dar de baja o si todavía colabora de alguna
    forma — no asumir ninguna de las dos, preguntarle a Mariano directamente.
  - **Pamela Jordan** (`comercial.gotir@gmail.com`) — admin activa. El email sugiere que está en el
    área comercial, coherente con tener su propio calendario de citas — sin confirmar el rol exacto.
  - **Micol Navarro** (`micolnavarro7@gmail.com`) — admin activa. Sin más contexto sobre su rol.
  - **Jonathan Barrionuevo** — **no aparece en la lista de usuarios de GHL** (ni activo ni dado de
    baja) pese a tener un calendario propio configurado — a diferencia de los otros tres, esto no se
    pudo resolver con este método. Sigue sin identificar, confirmar con Mariano.

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
- "Apostilla" y "Alquiler IberoLocations" no están descritos como servicios/trámites en la sección
  1.1 de este documento (que solo lista estancias/visados de estudios y modificación de residencia
  de trabajo como prioritarios) — confirmar con Mariano qué son y si son servicios activos o leads
  de algo distinto (ej. Alquiler IberoLocations podría no ser ni siquiera un trámite de inmigración).
- "Carolina Chapo" y "María García Serrano" no coinciden por nombre completo con los colaboradores
  ya documentados en la sección 0 (Sebastián, María, Gisella). **Actualización 17 agosto 2026**: se
  confirmó vía `GET /users/` que ambas son usuarias reales y activas en GHL — "Chapo abogados"
  (`visados@carolinachapo.com`, rol `user`) y "María García Serrano"
  (`mariagarciaserranoabogada@gmail.com` — el email dice literalmente "abogada", rol `user`). Esto
  confirma que son estudios de abogados externos reales, coherente con el patrón de colaboración con
  estudios ya documentado en la sección 0. **Sigue sin confirmarse** si "María García Serrano" es la
  misma "María" del dúo Sebastián/María de 250€/caso — el apellido no coincide con nada ya escrito,
  así que se sigue sin asumir, solo se corrobora que es una abogada real, no un dato inventado.

### 5.3.1 Usuarios de GHL (traído en vivo 17 agosto 2026, vía `GET /users/`)

Lista completa de usuarios de la location, útil como referencia cruzada para identificar personas
que aparecen en calendarios/formularios/pipelines sin contexto:
- Mariano Barcelona — `info.gotir@gmail.com` (admin)
- Asesoria GOTIR — `asesoria.gotir@gmail.com` (admin) — cuenta genérica de asesoría comercial.
- Clientes GOTIR — `clientes@gotir.es` (admin) — cuenta genérica de cara al cliente.
- Belén Campana — `adm.gotir.es@gmail.com` (admin) — el email sugiere administración de GOTIR;
  **no confirmado** si es la misma "Juliana" mencionada como única persona del área administrativa
  de la iglesia en el contexto de ministerio (son organizaciones distintas — iglesia vs. GOTIR — así
  que probablemente NO sea la misma persona; se anota la duda solo por si acaso, sin asumir nada).
- Pamela Jordan — `comercial.gotir@gmail.com` (admin) — ver 5.2.
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

No se debe inventar automatizaciones de GHL que no estén confirmadas por Mariano o vistas en vivo —
lo de arriba es pipelines/calendarios/formularios reales, pero no dice nada de qué automatizaciones
(si las hay) mueven contactos entre etapas.

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

---

## 7. Abierto / pendiente de confirmar por Mariano

Lista honesta de lo que este documento *no* puede responder todavía porque no hay fuente confiable:

- ~~Estructura real de GHL (pipelines, etapas, campos custom, automatizaciones existentes)~~ —
  **resuelto en gran parte el 14 agosto 2026** (ver sección 5): pipelines, etapas y formularios ya
  están confirmados en vivo contra la API. Quedan sub-pendientes puntuales, todos nuevos, surgidos
  de leer los datos reales:
  - Confirmar el propósito de la pipeline **Proveedores** (¿es el flujo de comisiones a
    Sebastián/María/estudios colaboradores, u otra cosa?) — sección 5.1.
  - ~~Confirmar quiénes son Pamela Jordan, Micol Navarro y Jonathan Barrionuevo~~ — **resuelto en
    parte el 17 agosto 2026** vía `GET /users/`: Pamela Jordan y Micol Navarro son usuarias admin
    reales de GHL (ver sección 5.2), aunque su rol exacto sigue sin confirmar. **Jonathan
    Barrionuevo sigue sin identificar** — no aparece ni siquiera en la lista de usuarios de GHL.
    **Sabrina Navarro**: confirmado que su cuenta sigue activa (no dada de baja) — falta confirmar
    si realmente sigue colaborando o es un resabio administrativo — sección 5.2.
  - Confirmar qué son los formularios **"Apostilla"** y **"Alquiler IberoLocations"** (no encajan en
    los servicios descritos en la sección 1.1) — sección 5.3.
  - ~~Si "Carolina Chapo" / "María García Serrano" son colaboradores nuevos~~ — **resuelto en parte
    el 17 agosto 2026**: ambas son usuarias reales de GHL, "María García Serrano" confirmada como
    abogada por su propio email. Sigue sin confirmar si es la misma "María" del dúo Sebastián/María
    — sección 5.3.
  - Confirmar si **Belén Campana** (`adm.gotir.es@gmail.com`, admin de GHL) es la misma "Juliana"
    del área administrativa de la iglesia mencionada en el contexto de Graduación New Life —
    probablemente no, son organizaciones distintas, pero queda la duda anotada sin resolver —
    sección 5.3.1.
  - Campos personalizados de contacto/oportunidad: la API no se pudo consultar todavía (el servidor
    MCP no tiene tool para eso) — sección 5.4.
- Contenido exacto del mini-funnel pre-llamada (qué recibe el lead antes de agendar, más allá de su propósito general).
- Si existe o no una solución definida para el problema de estacionalidad (sección 1.6) — identificado, no resuelto.
- Qué rama de GHL priorizar para automatizar primero en n8n (sección 4.5) — hay una lectura razonable pero no es una decisión confirmada.
- Cualquier cambio de precio o servicio que se hable en conversaciones futuras: por instrucción del proyecto, un cambio mencionado en una conversación no se trata como permanente hasta que se actualice el documento de contexto de precios/servicios correspondiente.
