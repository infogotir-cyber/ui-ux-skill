# CLAUDE.md — Área Ministerio (Impact Global)
*Última actualización: 14 agosto 2026*

## Rol de este documento
Sos el **director de ministerio** de Mariano. Esta es el área con más terreno operativo ya andado
de las cuatro — tiene estructura completa en ClickUp, historial real de discípulos, un evento en
curso (Tarde Profética) y un evento futuro clave (Lanzamiento 5 sept). Tratá este documento como la
memoria de largo plazo del área: lo que Mariano ya decidió, por qué lo decidió, y qué sigue
pendiente de confirmar.

## 1. Quién es Mariano en este rol
- Líder en la iglesia Impact Global, parte de los primeros 12 del pastor (modelo de liderazgo
  basado en Jesús: discipular a 12, que cada uno discipule a otros 12, y así sucesivamente).
- Lidera la red de jóvenes **FM4** (grupos de amistad FM4.1 a FM4.6).
- Objetivo de temporada: completar sus 12 discípulos directos abriendo FM4.6 con una pareja nueva.
  A partir de ahí, los nuevos líderes empiezan a discipular a sus propios discípulos (crecimiento
  multiplicativo, no solo lineal).
- Es también pilar/coordinador de **New Life** para TODA la iglesia (no solo sus discípulos) — vela
  por el proceso de los estudiantes de todos los códigos/grupos, no solo los suyos.
- Es responsable de logística en la próxima edición de **Ruge** (1-4 octubre 2026).

## 2. Estructura en ClickUp
**Workspace/Team ID:** `90121963418` — **Space:** "Espacio del equipo [ES]" ID `90128772215`

### Folder: Liderazgo — Mis 12 y Grupos (ID `901212988012`)
- **Lista "Discípulos (seguimiento pastoral)"** — ID `901220315594`
  - Una tarea padre por pareja ministerial (FM4.1–4.5), con una subtarea individual por persona
    (el estado pastoral se lleva por persona, no por pareja) — Mariano prefiere el seguimiento
    pastoral individual, no por pareja en conjunto, porque uno puede estar bien y el otro no.
  - Campo "Estado pastoral" (Drop Down) — field_id `875bf9cf-3296-4ccd-89ba-0fffce5f9109`
    - Bien: `b0e0661c-7869-4cc7-9341-6b6b26d153e3`
    - Atención: `cf1d8fa3-ea3d-4170-be85-1a851334c30d`
    - Prioritario: `9f4a08bb-ddcd-4066-844a-f62a27fe18a1`
  - **Limitación técnica conocida:** la API de ClickUp no permite vaciar un campo Drop Down una vez
    seteado (solo cambiarlo a otra opción). Si un campo quedó mal cargado por error, hay que
    avisarle a Mariano para que lo vacíe manualmente desde la app — no intentes forzarlo con la API.
  - Tareas padre por grupo:
    - FM4.1 — `869ehn2by` → subtareas: Adrián Caro `869ehnatm` (⚠️ tiene el campo "Estado pastoral"
      en "Bien" cargado por error sin base real — pendiente que Mariano lo vacíe a mano), Ingrid
      Guaño `869ehnbdg`.
    - FM4.2 — `869ehn2ed` → subtareas: Diego Villavicencio `869ej5cv3`, Rebeca Lema `869ej5cx2`.
    - FM4.3 — `869ehn2h6` → subtareas: Rocío Jury `869ej5czy`, Jacobo Marulanda `869ej5d3c`.
    - FM4.4 — `869ehn2kh` → subtareas: Lisandro Tapia `869ej5d5t`, Paulina Soto `869ej5d98`.
    - FM4.5 — `869ehn2nq` → subtareas: David Valera `869ej5dc3`, Sabrina Navarro `869ej5dfb`.
  - Campos pendientes de crear (nivel 3 del diseño, todavía no son columnas reales): fecha "Última
    conversación significativa", fecha "Próximo seguimiento", texto "Motivos de oración activos",
    texto "Alertas activas", texto "Áreas de crecimiento", y un campo por evento de asistencia
    (Cumbre, Discipulado de 72, discipulado mensual, Intercesión, Noches de Vida, Domingo) — hoy
    viven como texto libre en la descripción de cada subtarea.
- **Lista "Grupos de Amistad (FM4.1-4.6)"** — ID `901220315596`
  - Una tarea por grupo, con la pareja a cargo, asistencia semanal, personas nuevas, consolidación,
    personas en New Life, última visita: FM4.1 `869ehn2rd`, FM4.2 `869ehn2u1`, FM4.3 `869ehn2ya`,
    FM4.4 `869ehn30n`, FM4.5 `869ehn330`.
  - Campo pendiente/en construcción: "Tendencia del grupo" (Creciendo/Estancado/Decreciendo) — mide
    el grupo como unidad (como pareja ministerial), es DISTINTO del estado pastoral individual.

### Folder: New Life (ID `901212988018`)
- Lista "Ciclos y Alumnos" — ID `901220315606` (vacía, pendiente de cargar ciclo actual y alumnos).
- Lista "Tareas Operativas Recurrentes" — ID `901220315608`.
- Equipo de apoyo operativo de Mariano en New Life: Adrián Caro e Ingrid Guaño.
- Cada ciclo de New Life arranca con **Encuentro**: un retiro de un día, ~2 veces al año (uno hacia
  marzo).
- New Life dura ~4 meses, 2 ciclos al año, 4 módulos: módulo 2 = activación en servicio
  (Servidores, Producción, Kids, con posibles excepciones como situación de unión libre); módulo 3
  = entrevistas de liderazgo (define intención de liderar de cada alumno); módulo 4 = cierre
  (aprobados, deserciones, candidatos a Lanzamiento).
- Excel oficial por ciclo (compartido con Costa Rica), Excel interno de asistencia (tutores), Excel
  de deserciones — todavía viven fuera de ClickUp.
- Después de New Life viene **Lanzamiento** (2/año, debe enviar la lista definitiva de candidatos)
  y Graduación (certificados con nombres revisados y enviados a Costa Rica, coordinación con
  Producción, Impact Worship, el pastor, decoración, un detalle por estudiante, togas y bandas
  "New Life" — descripción general del proceso recurrente; ver el detalle real del ciclo actual
  abajo).

#### Graduación New Life — 1 sept 2026 (registrado 17 agosto 2026)
Tarea madre creada en "Tareas Operativas Recurrentes": **"Graduación New Life — 1 sept 2026"** — ID
`869ejzpf3` (https://app.clickup.com/t/869ejzpf3). Mariano avisó que faltan varias cosas por
confirmar/hacer y hay que apurarse. Las 10 subtareas de abajo **quedaron bloqueadas por rate limit de
ClickUp (sigue bloqueado, ~21hs cada vez que se reintenta)** — crearlas como subtareas de
`869ejzpf3` apenas se libere:

1. **Certificados — verificar impresión (Juliana)**, urgente, vencimiento sugerido 25 ago. El PDF ya
   fue enviado a Mariano; **Juliana** (única persona del área administrativa de la iglesia) dijo que
   los iba a imprimir — falta confirmar si ya lo hizo.
2. **Bandas — links de proveedores (Adrián Caro)**, vencimiento sugerido 25 ago. Adrián tiene que
   entregar 2 links de proveedores de bandas **personalizadas** con el texto "New Life" y 2 links de
   bandas **genéricas sin personalizar** (opción más económica) — falta confirmar si ya los buscó.
3. **Chocolate decorado "completado" — comprar y decorar (Adrián Caro)**, vencimiento sugerido 28
   ago. Detalle por estudiante: un chocolate decorado con un papel que diga "completado". Adrián
   tiene que elegir y comprar el chocolate, reportarle a Mariano qué chocolate es/dónde lo compra/
   cuánto cuesta (para pasar presupuesto), y encargarse de la decoración de cada uno. Mariano fue
   explícito: no alcanza con que esté delegado, necesita que Adrián lo haga de verdad y reporte.
4. **Decoración — globos, sillas y Ferrero Rocher (Ingrid Guaño + Lurbin)**, vencimiento sugerido 28
   ago. Ingrid coordina con **Lurbin** (decoradora, apoyo externo) y tiene que reportar el estado de:
   decoración con globos, forrado de las sillas, y un detalle para los estudiantes con bombones
   Ferrero Rocher.
5. **Togas — descartadas para esta graduación, evaluar para la próxima** (sin vencimiento, es una
   nota). Se había indicado toga (sobretodo negro) por estudiante, pero sale 25€ c/u — muy caro y ya
   es muy tarde para avisarles a los estudiantes que deben pagarlo. Descartada para el 1 sept 2026;
   tenerla en cuenta para la próxima graduación, avisando con más anticipación si se quiere cobrar.
6. **Producción y roles de servicio (Carlos Prado)** — agregado 17 ago. Carlos encabeza producción;
   Mariano ya le pidió armar un rol/turnos para gente sirviendo en producción, redes sociales, etc.
   Falta seguimiento de que efectivamente lo esté armando.
7. **Rol de servidores (Margot)** — agregado 17 ago. Mariano ya le pidió a Margot armar el rol de
   servidores para que haya gente sirviendo durante la graduación. Falta seguimiento.
8. **Impact Worship — banda de música (David Valera)** — agregado 17 ago. Mariano ya le pidió a David
   Valera coordinar Impact Worship para que haya banda en vivo durante la graduación. Falta
   seguimiento. ⚠️ Mismo nombre y apellido que el David Valera de FM4.5 (discípulo que se activa el 5
   sept, ver sección 3/4) — no confirmado si es la misma persona, no asumirlo sin que Mariano lo
   confirme.
9. **Cronograma de Costa Rica (Pablo Carranza) → reenviar a Carlos Prado → avisar al pastor** —
   agregado 17 ago, tarea de Mariano mismo. Cadena de coordinación pendiente: (a) Mariano tiene que
   estar pendiente de que **Pablo Carranza** (equipo de Costa Rica) le envíe el cronograma de la
   graduación; (b) apenas lo tenga, reenviárselo a **Carlos Prado** para que coordine todos los temas
   de producción con el cronograma real; (c) una vez confirmado, hablar con **el pastor** para que
   prepare alguna enseñanza para el evento.
10. **🔴 Armar presupuesto general y cobro anticipado a estudiantes** — agregado 17 ago, la más
    urgente de todas: **quedan 15 días y los estudiantes todavía no saben que tienen que pagar para
    la graduación, ni cuánto**. Tarea de Mariano mismo, depende de que le confirmen antes:
    - Adrián (ítems 2 y 3: costo de bandas + costo del chocolate)
    - Ingrid (ítem 4: costo de decoración con Lurbin)

    Con esos 3 datos Mariano arma el presupuesto general, lo divide entre los estudiantes que van a
    la graduación, le avisa a los pastores que va a mandarle a cada estudiante un mensaje pidiendo el
    pago anticipado de un monto X — el objetivo explícito es que la graduación no le genere gastos a
    la iglesia. Sin esto resuelto pronto, se corre el riesgo de no llegar a tiempo a cobrar antes del
    1 sept.

### Folder: Vida Personal & Espiritual (ID `901212988023`)
Ojo: pese al nombre, este folder vive dentro del espacio de ministerio en ClickUp por razones
históricas — pero conceptualmente pertenece al área **personal** de este sistema, no a ministerio.
Ver `areas/personal/CLAUDE.md` para el contexto completo. Contiene las listas "Salud"
(`901220315615`) y "Desarrollo y Espiritual" (`901220315621`), ambas vacías.

### Folder: Ruge (1-4 Oct 2026) — ID `901212987972` — ✅ COMPLETO
- Lista "Equipo y Reuniones" — ID `901220315541`.
- Lista "Inventario" — ID `901220315543` — 214 ítems originales (Excel fuente:
  `INVENTARIO_2026_RUGE.xlsx`), 166 pendientes de acción, organizados en 15 tareas por comisión
  (Cocina, Logística, La Voz, Producción) y tipo de acción necesaria (comprar, confirmar
  préstamo/alquiler, decidir compra o préstamo, gestión con Costa Rica, encargar fabricación,
  verificar propiedad existente). El detalle línea por línea de qué falta de cada comisión está
  cargado en ClickUp, no hace falta duplicarlo acá — consultalo ahí.
- Lista "Preparación por Día" — ID `901220315548`.
- Equipo de logística: Marco Guanuchi, David Luzuriaga y **Julio César** (se sumó al equipo el 17
  agosto 2026 — antes eran solo Marco y David).
- Estructura del evento: jueves salida en bus desde la iglesia con senderistas y equipo, primera
  caminata al primer punto, logística de suministro (agua, altavoz, cuerdas) durante los 4 días.
  Ruge es un retiro de hombres en una montaña en Valencia, con logística de insumos, transporte
  (coches/camionetas/buses), radios, alimentación y seguridad además del inventario.
- Cada categoría del inventario tiene un encargado propio (ej. cocina, producción) con quien
  Mariano coordina tarea, fecha límite y reporte; luego él reporta al responsable general de Ruge.
- Mariano es el encargado de logística en esta edición — no está confirmado si lo será en futuras.

### Tareas de Ruge cargadas en ClickUp (14 agosto 2026)
El rate limit de la API se liberó antes de lo esperado. Ambas quedaron creadas en "Equipo y
Reuniones" (`901220315541`):

1. **"Retrospectiva logística Ruge — reto inicio de año (14 ago 2026)"** — ID `869ejwty5`
   (https://app.clickup.com/t/869ejwty5). Contiene el resumen completo de las notas de Mariano de la
   llamada con **Marco Guanuchi** y **David Luzuriaga** (equipo de logística), agrupado por tema
   (comunicaciones/radios, transporte, check-in y carga, vestimenta, comida, terreno/instalaciones,
   bienestar del equipo, rutas, compras/administrativo). El resumen de IA (Gemini) había salido muy
   pobre, así que se usó en cambio el Excel de notas propias de Mariano. ⚠️ Son notas de **parte** de
   la reunión, no necesariamente completas — si aparece más contenido, sumarlo a esta misma tarea.
2. **"Reunión de inventario Ruge con comisiones — miér 19 ago, 19:00hs"** — ID `869ejwtz6`
   (https://app.clickup.com/t/869ejwtz6), con fecha de vencimiento 19 ago 2026 19:00. Comisiones
   confirmadas por Mariano: Seguridad, Cocina, Producción (y otras sin nombrar todavía).

### Reparto de tareas por persona — llamada de logística 17 ago 2026, 21:00hs
Reunión con **Marco Guanuchi**, **David Luzuriaga** y **Julio César Navia** (recién sumado al
equipo ese mismo día). Fuente: transcripción completa de la llamada + el Excel
`Ruge_reparto_tareas_17ago2026.xlsx` que Mariano fue completando en vivo durante la reunión
(columnas Encargado y Fecha límite) y que después se terminó de ordenar con este sistema — versión
final entregada a Mariano como `Ruge_reparto_tareas_17ago2026_actualizado.xlsx`, con tres hojas:
"Resumen por bloque" (fecha límite y notas por grupo de tareas), "Detalle completo por ítem"
(214 ítems del inventario original, sin tocar — se repartió por bloque, no por ítem) y "Reparto
detallado por persona" (la misma información organizada por persona, distinguiendo quién es
**encargado general de un grupo de tareas** de quién se hace cargo de **una tarea específica
dentro de un grupo que lidera otra persona** — para no sobrecargar a una sola persona).

**Encargados generales por grupo de tareas:**
- **Marco Guanuchi**: Producción-confirmar préstamos (cámara/dron), Gestión con Costa Rica,
  Confirmar préstamos (altavoz/cuerdas/estuche insulina/mantel/mesas/radios iglesia), La Voz-comprar
  (corrobora, la compra la hace la familia de Marco Jurado), Buscar proveedores y comparar precios,
  Checklist de inventario del miércoles, Verificar TERMOS en bodega (discrepancia 9 vs 8,
  detectada en la retrospectiva).
- **Julio César Navia**: Encargar fabricación (rótulos/pegatinas), Decidir compra o préstamo
  (alargador/pala), Confirmar alquiler (⚠️ **el bloque más urgente, vence 19 ago** — bus, camión,
  furgoneta, radios VHF, teléfonos satelitales, troncos), Comprar no perecedero, Comprar/recibir/
  almacenar lo comprado (es el único del equipo que vive en Valencia, por eso coordina la
  recepción — se mueve en metro/bus, no tiene carnet de conducir todavía).
- **David Luzuriaga**: Completar cantidad faltante de logística, y los 5 bloques de Cocina
  completos (contacto real: **Adrián Rivera**, no solo Marco Chiriguaya como se pensaba antes) +
  Sueltos de la retrospectiva (cortafierro/cincel para la cruz). El tema puntual de las **carnes**
  (crítico — hubo un problema de tamaño en un reto anterior) lo ve David junto con Adrián Rivera
  específicamente, confirmado por Mariano el 17 agosto 2026.
- **Mariano**: es el **coordinador general** de todo el reparto, no ejecuta tareas de campo — su
  rol es armar la propuesta de presupuesto para administración de la iglesia, recibir los
  presupuestos/listas que arman Marco, Julio y David (ej. la lista de compras que David arme el
  miércoles) y pasarlos a Juliana (administración), ser el punto de contacto general con Marco
  Jurado, y controlar que los otros tres cumplan lo que se comprometieron a hacer. **Corrección 17
  agosto 2026**: en una primera versión de este registro se le había asignado a Mariano la tarea
  puntual de llamar a Richard (sobrino de Marco Jurado) por cinta reflectante y figuras de premios
  — Mariano aclaró que eso está mal, esa tarea es parte del bloque de Julio (vía Marco Jurado como
  contacto), y su propio rol es de coordinación/control, no de ejecución de tareas de compra
  individuales.

**Dentro del bloque más urgente (Confirmar alquiler, vence 19 ago, encargado general Julio) se
repartió por persona para no sobrecargar a nadie**: Marco Guanuchi habla con **Andrés Uquillas**
(quien alquiló el bus la vez pasada) y busca la empresa de radios VHF/teléfonos satelitales; Julio
habla con Mateo y Jefferson (camión cerrado/furgoneta) y con el vendedor de troncos (vía Marco
Jurado, para el 2-3 de octubre) y le hace seguimiento a Marco por el bus; David busca dónde alquilar
la pick-up/camión de caja abierta.

**Pendiente sin cerrar en esta llamada**: el bloque "Logística — Verificar propiedad existente"
(arena piscina, bolsas de provisiones, cajas de requisa, cuerdas elásticas piscina, estacas,
fideos) sigue sin encargado — depende de la reunión presencial del miércoles 19 ago, y además Marco
y Julio identificaron que parte de esos ítems (arena, cajas de requisa, cuerdas de piscina, y la
paja del bloque de compras) los gestionó el equipo de **Eventos** (Mauricio y Cristian) en el reto
anterior, no Logística — Julio le va a preguntar a Mauricio quién compró y dónde antes de asignar
un encargado final. No asumir un reparto ahí hasta que esa respuesta llegue.

### Lista "Eventos puntuales" — ID `901220372534` (dentro del folder Liderazgo)
Se creó el 14 de agosto de 2026 para eventos de un solo día con invitado especial. Diseño: una
tarea por evento, con una subtarea por cada uno de los 10 líderes con: entradas asignadas,
entradas vendidas, quién tiene el dinero, pago a administración (Pendiente/Pagado/Parcial), fecha
límite de pago.

**Tarea activa: "Tarde Profética — 15 ago — Pedro García"** — ID `869ej5fvj`
- Invitado: profeta Pedro García. Meta: mínimo 15 entradas.
- Subtareas y su estado al 14 de agosto (⚠️ varios datos son inciertos, ver más abajo):
  - Adrián Caro `869ej5fx0` — 3 entradas (la suya + Dries + Alejandro Arteaga), pagadas en
    efectivo. Parte de las 5 entradas asignadas al código FM4.1.
  - Ingrid Guaño `869ej5fyd` — 2 entradas (la suya + Nidia), **pago pendiente** (le falta hacer
    Bizum de ambas).
  - Diego Villavicencio `869ej5fzv` — cantidad de entradas incierta (ver pendientes). Mariano le
    prestó el dinero y ya pagó por él; Diego le debe la devolución.
  - Rebeca Lema `869ej5g0t` — mismo caso que Diego: cantidad incierta, Mariano ya pagó adelantando
    el dinero, ella le debe la devolución.
  - Rocío Jury `869ej5g26` — 1 entrada, pagada, comprobante ya enviado.
  - Jacobo Marulanda `869ej5g37` — 1 entrada, estado de pago sin confirmar.
  - Paulina Soto `869ej5g45` — 1 entrada, estado de pago sin confirmar.
  - Lisandro Tapia `869ej5g5r` — 1 entrada, no está confirmado si ya pagó.
  - David Valera `869ej5g89` — sin entradas asignadas mencionadas todavía.
  - Sabrina Navarro `869ej5gay` — sin entradas asignadas mencionadas todavía.
- **Pendientes de confirmar con Mariano (sin resolver al 14 ago):**
  1. Cantidad exacta de entradas de Diego y Rebeca (dijo primero 1 c/u, después "tres o un poco
     más" entre los dos — no cuadra).
  2. Si a David y Sabrina realmente no les tocó vender entradas o se le olvidó reportarlo.
  3. Si Jacobo y Paulina ya pagaron.
  4. Confirmación de Lisandro.
  5. Fecha límite real de pago a administración (se asumió el mismo 15 ago).
- Dos invitados en proceso de evangelización, todavía sin entrada confirmada, NO cuentan en la
  meta: Jesús Blanco y "Alejandro" (apellido pendiente). Mariano los sigue invitando activamente.

#### Retrospectiva del evento (registrada 17 agosto 2026, evento ya pasó)
Pendiente de cargar en ClickUp (agregar como actualización a la tarea `869ej5fvj` — **bloqueado por
el mismo rate limit de ClickUp que sigue activo**, cargar apenas se libere):

- **Problema detectado — pagos desorganizados hasta último momento**: Mariano no supo, hasta el
  mismo día del evento, si todos sus discípulos habían pagado sus entradas. Caso concreto: Lisandro
  Tapia no sabía si su madre había pagado o no, y no se lo pudo confirmar a tiempo — esto explica por
  qué el pendiente #4 de la lista de arriba (confirmación de Lisandro) nunca se resolvió realmente,
  no es un dato que haya quedado sin cargar, es que la confusión fue real y persistió durante todo el
  proceso.
- **Cambio de proceso decidido para la próxima vez (política, no solo para este evento)**: de ahora
  en más, Mariano va a **cobrarles primero a sus discípulos y recién después entregarles las
  entradas** — en vez del modelo de esta vez (repartir entradas primero y esperar que coordinen el
  pago después), que generó que ni los propios discípulos supieran si habían pagado o no.
- **Asistencia real confirmada**: fueron **todos** los discípulos de Mariano, incluyendo **Mateo
  Arteaga, David Valera y Sabrina Navarro** — pese a que estos tres todavía no son formalmente
  discípulos activos (se activan recién con el Lanzamiento del 5 sept, ver sección 3/4). También
  asistieron algunas ovejas de sus discípulos e invitados de primera vez.
- **Pendiente abierto**: Mariano ya pidió el listado completo de esas ovejas/invitados a sus
  discípulos — todavía no lo tiene. Apenas lo consiga, lo va a confirmar para completar el registro
  de asistencia real.
- **Para qué sirve este registro**: Mariano quiere usar este evento como **línea base** — la próxima
  vez que se haga un evento similar, comparar contra este para medir si de verdad se mejoró (mismo
  criterio que ya se usa con el baseline comercial de julio en `direcciones/comercial/CLAUDE.md`).

**Tarea "Lanzamiento — 5 sept 2026 — Activación de nuevos líderes"** — ID `869ejwu0q`
(https://app.clickup.com/t/869ejwu0q), en la misma lista `901220372534`, fecha 5 sept 2026. Creada
el 14 ago 2026 apenas se liberó el rate limit que la había bloqueado antes; contenido según la
sección 4 más abajo.

## 3. Composición REAL y actual de los grupos (corregido 14 agosto 2026)
Esto es importante: hay una diferencia entre "quién aparece nombrado en un grupo" y "quién es
formalmente discípulo activo de Mariano hoy". Mariano corrigió esto explícitamente porque antes el
sistema asumía que los 10 nombres ya eran discípulos activos, y no es así:

- **FM4.1** — Adrián Caro e Ingrid Guaño. **Activo y completo.** (Adrián deja el liderazgo a
  inicios de octubre 2026 tras casarse; entra Mateo Arteaga — ver sección 4).
- **FM4.2** — Diego Villavicencio y Rebeca Lema. **Activo y completo.**
- **FM4.3** — hoy solo **Rocío Jury** está activa. Jacobo Marulanda participa y ya tiene entrada
  para la Tarde Profética, pero formalmente se activa como discípulo el 5 de septiembre de 2026.
- **FM4.4** — el grupo **todavía no ha empezado formalmente**. Lisandro Tapia y Paulina Soto se
  activan el 5 de septiembre de 2026.
- **FM4.5** — el grupo **todavía no ha empezado formalmente**. David Valera y Sabrina Navarro se
  activan el 5 de septiembre de 2026.

Por esto es que, hasta el 14 de agosto, Mariano no había dado reporte pastoral de Jacobo, Paulina,
Lisandro, David ni Sabrina — no es un olvido, es que técnicamente todavía no son sus discípulos
directos en el sentido pastoral pleno.

## 4. El evento de Lanzamiento — 5 de septiembre de 2026
Evento puntual clave que activa en servicio a varios de los nombres de arriba y completa
formalmente los grupos FM4.3, FM4.4 y FM4.5:

- **Se activan como discípulos directos de Mariano ese día:** Jacobo Marulanda (completa FM4.3
  junto a Rocío), Paulina Soto y Lisandro Tapia (completan FM4.4), David Valera y Sabrina Navarro
  (completan FM4.5).
- **Mateo Arteaga NO se activa este día.** Mateo entra a FM4.1 recién cuando Adrián Caro se case y
  vuelva de su casamiento, a principios de octubre de 2026 (momento en el que Adrián deja el
  liderazgo). Es un evento separado y posterior al Lanzamiento — no confundir las dos fechas.
- Logística del evento de Lanzamiento en sí (dónde, cómo, quién más participa) todavía no está
  coordinada — es un pendiente abierto, no asumas detalles que Mariano no dio.

## 5. Discípulos actuales por grupo (lista rápida de referencia)
- FM4.1 — Adrián Caro e Ingrid Guaño
- FM4.2 — Diego Villavicencio y Rebeca Lema
- FM4.3 — Rocío Jury (activa) + Jacobo Marulanda (activa 5 sept)
- FM4.4 — Lisandro Tapia y Paulina Soto (ambos activan 5 sept)
- FM4.5 — David Valera y Sabrina Navarro (ambos activan 5 sept)

## 6. Ritmos ministeriales semanales/mensuales
- Miércoles: 1º y 2º del mes = Cumbre (asisten todos los líderes); 3º = Discipulado de 72 (lo
  imparte el pastor Fabio, sede Valencia); último = discipulado mensual de Mariano, 19:30, en un
  coworking alquilado en Torrent, Valencia.
- Otros espacios de asistencia a controlar en sus discípulos directos: intercesión (miércoles de
  madrugada), Noches de Vida (jueves), domingo.
- De las ovejas de sus discípulos (no de los discípulos mismos), Mariano solo supervisa: asistencia
  al grupo de amistad y asistencia a New Life — el resto es responsabilidad de cada líder.
- Además del estado pastoral individual de sus discípulos, Mariano quiere un scoring aparte de cómo
  va cada grupo como pareja ministerial (creciendo, estancado, decreciendo en gente) — ver campo
  "Tendencia del grupo" en la sección 2.
- Tras predicar en su grupo, cada líder debe: entregar el sobre de ofrendas, hacer el reporte
  correspondiente, y registrar la información en **Redil** (CRM de la iglesia, fuera de este
  sistema) — de ahí se puede extraer información oficial de asistencia a grupos y a New Life.

## 7. Pipeline ministerial general
Persona nueva → Grupo de amistad → Consolidación → Encuentro → New Life → Lanzamiento → Liderazgo
→ Nuevo grupo → Nuevos discípulos

Este pipeline es la lente con la que hay que leer todo lo demás: Jacobo, Paulina, Lisandro, David y
Sabrina están hoy en el tramo "New Life → Lanzamiento" del pipeline, todavía no llegaron a
"Liderazgo" pleno — de ahí que el 5 de septiembre sea la bisagra que los mueve al siguiente estado.

## 8. Cómo comportarte en esta área
- Cuando Mariano te cuente algo de un discípulo, grupo, New Life o Ruge, actualizá ClickUp
  directamente sin esperar a que te lo pida — es una instrucción explícita y permanente suya.
- Cuando la información que da es parcial o contradictoria (pasa seguido con las entradas y con
  las cantidades), no completes el hueco por tu cuenta: cargá lo que es claro y dejá anotado
  explícitamente qué falta confirmar, tanto en la descripción de la tarea como en tu respuesta a
  Mariano.
- Verificá siempre la composición real de los grupos contra la sección 3 antes de asumir que
  alguien es "discípulo activo" — el estado cambia con el Lanzamiento del 5 de septiembre y con la
  salida de Adrián en octubre.
- La API de ClickUp tiene rate limits que se activan con uso intensivo (pasó el 14 de agosto,
  bloqueó por ~24 horas) — si te pasa, avisale a Mariano en vez de reintentar en loop, y dejá
  anotado en este documento (o en un pendiente) qué quedó sin cargar para retomarlo apenas se
  libere.
