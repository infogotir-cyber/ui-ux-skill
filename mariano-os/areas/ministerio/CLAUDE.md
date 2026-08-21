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

#### Graduación New Life — 1 sept 2026 (registrado 17 agosto 2026, actualizado 18 ago 2026)
Tarea madre creada en "Tareas Operativas Recurrentes": **"Graduación New Life — 1 sept 2026"** — ID
`869ejzpf3` (https://app.clickup.com/t/869ejzpf3). Las 10 subtareas de abajo **ya están creadas en
ClickUp** (se habían quedado solo documentadas acá por el rate limit viejo del conector oficial —
con el servidor MCP propio, 18 ago 2026, se crearon todas): `869ekhmgx`, `869ekhmh2`, `869ekhmhn`,
`869ekhmjn`, `869ekhmke`, `869ekhmkx`, `869ekhmmr`, `869ekhmnk`, `869ekhmp4`, `869ekhmq1` (en ese
orden, 1 a 10). Sumadas 3 más el mismo día (11 a 13): `869ekhpfh`, `869ekhpg2`, `869ekhpgn`.

**Cambio importante de responsables (18 agosto 2026)** — ver contexto sensible completo más abajo:
la pastora tomó de vuelta las tareas de bandas y chocolate del equipo de Mariano, y se las
reasignó directo a Juliana y Carlos Prado. La decoración (ítem 4) sigue siendo de Ingrid+Lurbin,
todavía sin resolver.

1. **Certificados — verificar impresión (Juliana)**, urgente, vencimiento sugerido 25 ago. El PDF ya
   fue enviado a Mariano; **Juliana** (única persona del área administrativa de la iglesia) dijo que
   los iba a imprimir — falta confirmar si ya lo hizo.
2. **Bandas — RESUELTO por Juliana (18 ago), ya NO es tarea de Adrián Caro/equipo de Mariano**. Se
   había pedido a Adrián buscar links de proveedores de bandas personalizadas y genéricas, pero
   llegó tarde. La pastora le pidió directo a Juliana ir a comprar bandas genéricas a un "chino".
3. **Chocolate decorado "completado" — RESUELTO por Juliana + Carlos Prado (18 ago), ya NO es tarea
   de Adrián Caro/equipo de Mariano**. Juliana compra los chocolates en Mercadona; Carlos Prado
   (producción) vela por que se haga el sticker de decoración de cada uno.
4. **Decoración — globos, sillas y Ferrero Rocher (Ingrid Guaño + Lurbin)** — SIGUE PENDIENTE (18
   ago), sin cambios de responsable. Ingrid coordina con **Lurbin** (decoradora, apoyo externo) pero
   todavía no compró nada — es el único costo que sigue faltando para el presupuesto (ítem 10).
   **Plan concreto pedido por Mariano (18 ago, tarde)**: máximo el **jueves 20 ago**, Lurbin ya tiene
   que haber comprado los globos y demás materiales — pedirle antes un **listado completo de todo lo
   que va a necesitar**, para asegurarse de que lo compre y lo lleve todo. Además, fijar con
   Ingrid/Lurbin **día y hora para armar toda la decoración** y dejarlo listo antes del 1 sept.
5. **Togas — descartadas para esta graduación, evaluar para la próxima** (sin vencimiento, es una
   nota). Se había indicado toga (sobretodo negro) por estudiante, pero sale 25€ c/u — muy caro y ya
   es muy tarde para avisarles a los estudiantes que deben pagarlo. Descartada para el 1 sept 2026;
   tenerla en cuenta para la próxima graduación, avisando con más anticipación si se quiere cobrar.
6. **Producción y roles de servicio (Carlos Prado)** — agregado 17 ago. Carlos encabeza producción;
   Mariano ya le pidió armar un rol/turnos para gente sirviendo en producción, redes sociales, etc.
   Falta seguimiento de que efectivamente lo esté armando. (Ahora Carlos también vela por el sticker
   del chocolate, ítem 3.)
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
10. **🔴 Armar presupuesto general y cobro anticipado a estudiantes** — la más urgente de todas:
    **los estudiantes todavía no saben que tienen que pagar para la graduación, ni cuánto**. Tarea de
    Mariano mismo. **Actualización 18 ago**: con bandas y chocolate resueltos directo por Juliana
    (fuera del presupuesto que arma el equipo de Mariano), el único dato que sigue faltando de
    verdad es el costo de decoración (ítem 4, Ingrid) — **pregunta abierta sin resolver**: no está
    confirmado si los costos de bandas/chocolate que ahora paga Juliana igual se prorratean entre
    los estudiantes o quedan a cargo de la iglesia directamente, no asumir.

    Con ese dato Mariano arma el presupuesto general, lo divide entre los estudiantes que van a
    la graduación, le avisa a los pastores que va a mandarle a cada estudiante un mensaje pidiendo el
    pago anticipado de un monto X — el objetivo explícito es que la graduación no le genere gastos a
    la iglesia. Sin esto resuelto pronto, se corre el riesgo de no llegar a tiempo a cobrar antes del
    1 sept.
11. **Confirmar con líderes: asistencia y pago de cada estudiante graduando** — agregado 18 ago,
    tarea de Mariano mismo. Con cada líder FM4 hay que confirmar que sus estudiantes que se gradúan
    van a asistir de verdad, y que van a pagar la cuota que les corresponde (depende de que el ítem
    10 ya tenga el monto definido).
12. **Cartelito con nombre por silla, para cada estudiante graduando** — RESUELTO 18 ago 2026, lo
    diseñó este sistema. Mariano mandó el PDF de referencia de la invitación de New Life (paleta
    azul-violeta y tipografía) y la lista de 10 graduandos, sin logo de la iglesia. Se armó un PDF
    imprimible de 10 cartelitos (~9x6.5cm c/u, 2 páginas con líneas de corte), reproduciendo el
    degradado y la tipografía de la referencia (Montserrat Bold para el nombre, Great Vibes para el
    acento "Graduación"), sin ningún logo. Mariano lo aprobó tal cual. **Detalle técnico**: se
    generó con `weasyprint` (instalado vía pip en la sesión) + fuentes de Google Fonts descargadas
    localmente (Montserrat, Great Vibes) — no había fuentes elegantes preinstaladas en el entorno.
    Falta: que Mariano imprima, corte y pegue cada cartelito en la silla correspondiente.
    Estudiantes: Sandra Elizabeth López Iza, Ivan Patricio Paredes, Angela Ainara Chávez López,
    Jacobo Marulanda Gómez, María Paulina Soto Rave, Noemí Fernández Urcuango, Lisandro David Tapia
    Salazar, Julio César Navia Camargo, Jessica Ivonne Mora Lovato, Luisa Jacqueline Lovato Macias.
    **Confirmado por Mariano (18 ago 2026): es la misma persona** — Julio César Navia, del equipo
    de logística de Ruge (ver folder Ruge más abajo), también se gradúa de New Life este ciclo.
13. **Invitación en Canva — una versión para estudiantes, otra para familiares** — agregado 18 ago.
    Dos piezas de diseño: invitación para cada estudiante graduando, e invitación distinta para los
    familiares de los estudiantes. **Sin responsable definido todavía** — no asumido. Este sistema no
    tiene conexión directa a Canva; si Mariano pide ayuda con esto, lo que se puede ofrecer es
    redactar el copy/contenido o armar un mockup de diseño para que alguien lo replique en Canva, no
    operar Canva directamente.

##### Contexto sensible — la pastora se enojó por la demora (18 agosto 2026)
Mismo criterio que el contexto sensible de la Tarde Profética más abajo: **no va a ClickUp**, queda
solo en el sistema privado, es para entender el contexto real, no un pendiente operativo.

Con la fecha ya cerca, la pastora se enojó mucho porque Mariano no había desarrollado bien ni a
tiempo las tareas que había delegado a su equipo de New Life: la compra de chocolates, el sticker
de decoración de cada chocolate (delegado a Adrián Caro), y la compra de bandas de graduación
(habían buscado links de proveedores en vez de resolver rápido comprando algo genérico). Como
consecuencia, la pastora le sacó esas tareas al equipo de Mariano y se las asignó directo a
**Juliana** (comprar bandas en un "chino" y chocolates en Mercadona) y a **Carlos Prado** (su
esposo, cabeza de producción de la iglesia — que vele por el sticker del chocolate). Es la
**tercera instancia** en pocos días de liderazgo pastoral mostrando insatisfacción real con la
ejecución/reporte a tiempo de Mariano y su equipo alrededor de un evento (después del Pastor Fabio
y la Pastora Mirna por la Tarde Profética, ver más abajo) — patrón que vale la pena que Mariano
tenga presente, no un hecho aislado.

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

### Reparto final de Ruge verificado contra el inventario real (17 ago 2026) — fuente de verdad
El excel que se fue armando en la reunión (166 ítems "pendiente gestionar") se cruzó item por item
contra `INVENTARIO_2026_RUGE.xlsx`, el inventario real que Mariano subió (200 ítems: 166 "pendiente
gestionar" + 34 ya en "ALMACEN RUGE" que igual necesitan que alguien los revise/confirme). Se
detectó que faltaban esos 34 en el detalle original y se sumaron. Mariano después descargó el
archivo "por persona", lo completó a mano (asignó los que habían quedado sin encargado) y lo
resubió como **versión definitiva ("ahora sí tengo el final final", 17 ago 2026, noche)** — esa
subida ya está incorporada acá. **Los 202 ítems del inventario tienen encargado, cero sin
asignar.** Único cambio de nombre que hizo Mariano: "MANTEL NEGRO PARA MESA DE CAMISETAS" pasó a
ser "MANTEL VERDE PARA MESA DE CAMISETAS" (coincide con lo dicho en la llamada — hay que comprarlo
de color verde).

**Archivos fuente de verdad, guardados en `areas/ministerio/recursos/`:**
- `INVENTARIO_2026_RUGE_original.xlsx` — el inventario real de 200 ítems tal como lo subió Mariano.
- `Ruge_reparto_tareas_17ago2026_actualizado.xlsx` — maestro con 3 hojas: "Resumen por bloque",
  "Detalle completo por ítem" (202 filas, encargado/fecha/notas ya sincronizados con la versión
  definitiva de Mariano), "Reparto detallado por persona". Para los 4 bloques que terminaron
  repartidos entre más de una persona a nivel ítem (Confirmar préstamos, Confirmar alquiler,
  Verificar propiedad existente, Comprar no perecedero), la columna Encargado de "Resumen por
  bloque" dice "Ver detalle por ítem (repartido)" — el reparto real está en `ruge_reparto_lookup.md`
  o en la hoja de detalle, no asumir un solo encargado para esos 4 bloques.
- `Ruge_reparto_por_persona_17ago2026.xlsx` — **archivo definitivo tal cual lo subió Mariano el 17
  ago 2026 de noche, sin reformatear** (para no arriesgar perder algo de su edición): una hoja por
  persona (Marco 35 ítems, Julio 17, David 150, Mariano 0 ítems + 4 tareas de coordinación) con
  ítem, bloque, si es tarea de su grupo o una tarea específica dentro de otro grupo, detalle/con
  quién hablar (ya con los contactos finales, ej. "Administración (Juliana)" para varios), la otra
  comisión con la que revisarlo, estado y fecha límite. **Ya no existe hoja "Sin asignar
  responsable" — no hace falta, no quedó ningún ítem sin encargado.**
- `ruge_reparto_lookup.md` — tabla generada automáticamente (ítem → persona → bloque → fecha
  límite) para responder rápido "¿quién se encarga de X?" sin abrir el excel — **ya actualizada con
  la versión definitiva, 202/202 con encargado**. Regenerar con el script correspondiente si el
  reparto vuelve a cambiar (no editar a mano, se desincroniza).

**Meta explícita de Mariano (17 ago 2026): todos los ítems del reparto confirmados (comprado,
prestado, alquilado o verificado según corresponda) antes del 20 de septiembre de 2026.** Pidió
explícitamente poder preguntar en cualquier momento "¿quién se encarga de tal ítem?" (dio el
ejemplo del adaptador de grifo) y recibir la respuesta correcta al instante — para eso está
`ruge_reparto_lookup.md`, hay que usarlo como primera fuente antes de decir "no sé" o de adivinar.

### Política de recordatorios de Ruge (pedida por Mariano 17 ago 2026)
Mariano no quiere tener que revisar el excel él mismo para saber qué se vence — pidió que el
sistema le avise proactivamente a medida que se acercan las fechas límite, con un mensaje ya
redactado listo para copiar y pegar a la persona correspondiente. Ejemplo textual que dio: *"El 19
de agosto se vence lo de reservar el Bus, entonces me envías recordatorio con propuesta de mensaje
así copio y envío a Marco Guanuchi pidiendo confirmación a ver si ya lo gestionó, y así con cada
ítem."*

Cómo comportarse:
- Cuando se acerque (1-2 días antes) o llegue la fecha límite de un bloque/ítem sin confirmación de
  que ya se resolvió, avisarle a Mariano con: qué es, quién es el encargado, y un mensaje de
  WhatsApp ya redactado (tono directo, pidiendo confirmación de gestión) listo para que Mariano lo
  copie y mande él mismo — no mandarlo por GHL ni por ningún canal automático, esto es ministerio,
  no GOTIR, y además no hay integración de WhatsApp para estos contactos.
- Si Mariano confirma en la conversación que algo ya se resolvió, actualizar el estado en
  `ruge_reparto_lookup.md`/el excel correspondiente — no hay hoy un campo de "confirmado" separado,
  agregar una nota en la fila o llevar registro acá si hace falta.
- El 18 de agosto (rate limit de ClickUp liberado, ver abajo) hay que sincronizar todo este reparto
  a la lista "Inventario" de ClickUp (ID `901220315543`) — asignar cada tarea al usuario de ClickUp
  correspondiente a cada persona, para que las fechas límite y el estado vivan ahí también, no solo
  en el excel.

### Chequeo físico de inventario en la nave — 19 agosto 2026, excel final con stock

Mariano fue a la nave a corroborar en vivo el inventario real de Ruge (cuánto hay de cada cosa vs.
lo que dice el sistema) y subió una versión "final y mejor organizada" del excel por persona
(`Tareas_asignadas_por_persona__Log_stica_1.xlsx`) para tomar como referencia de ahora en más —
**reemplaza a `Ruge_reparto_por_persona_17ago2026.xlsx`** como el documento de trabajo, aunque el
viejo se deja en `recursos/` como histórico, sin borrar.

**Archivo final construido y entregado a Mariano**:
`areas/ministerio/recursos/Ruge_tareas_por_persona_19ago2026_FINAL_con_stock.xlsx` — mismas 4 hojas
(Marco Guanuchi, Julio Cesar Navia, David Luzuriaga, Mariano Barcelona), con 4 columnas nuevas
agregadas a las 3 hojas de ítems (no a la de Mariano, que son tareas de coordinación sin cantidad):
- **Stock inventario**: número real de `INVENTARIO_2026_RUGE_original.xlsx` (columna STOCK ACTUAL),
  cruzado ítem por ítem contra el nombre de cada fila. **202/202 ítems emparejados** (35 Marco + 17
  Julio + 150 David — coincide con el reparto ya conocido, el archivo nuevo solo lo reorganiza
  mejor, no cambia qué le toca a quién).
- **Reto 50 hombres**: la meta de cantidad del inventario (columna RETO 50 HOMBRES), mismo cruce.
- **Conteo real (hoy)**: en blanco a propósito — es la columna que se completa a mano (impreso) o
  dictándomelo en el chat mientras se camina la nave.
- **Falta p/ reto 50**: fórmula real (`=IFERROR(MAX(0,Reto50-IF(Real<>"",Real,Stock)),"revisar
  unidad")`) — usa el conteo real si ya se cargó, si no cae al stock del sistema. Se recalcula solo
  apenas se escribe un número en "Conteo real".
- **3 ítems fuera del inventario formal** (ya documentados como "sueltos de la retrospectiva", sin
  stock/reto porque nunca estuvieron en el excel de inventario): protocolo de numeración de radios,
  cortafierro para la cruz, elementos para las prédicas (copa de cristal) — marcados
  "(fuera de inventario)" en vez de forzar un número.
- **Algunos ítems tienen el stock/reto en texto** (ej. "PAQUETES 7", "SOBRES 20", "3 SACOS") porque
  así está cargado en el inventario original — se dejaron tal cual (es información real y más útil
  que un número pelado), y la fórmula de faltante muestra "revisar unidad" en esos casos en vez de
  romperse con un error.
- Mismo tamaño de columnas que Mariano ya había definido en el archivo subido — las 4 columnas
  nuevas usan columnas que él mismo había dejado pre-anchadas (14.0 y 8.71 puntos) al lado de "Fecha
  límite", más 2 columnas nuevas angostas para Reto 50 y Falta. Encabezados con el mismo estilo
  (Arial 10 negrita, fondo azul) que el resto de la hoja. `print_area` seteado por hoja para que
  imprima limpio, sin páginas en blanco de más.

**Nombres que no coincidían exactamente entre el excel por persona y el inventario** (mismo ítem,
redactado distinto — resuelto por cruce manual, no asumido a ciegas): abreviaturas ("5L" vs
"CAPACIDAD 5 LITROS"), un typo real en el inventario ("CAMARELOS CON PROPOLEO" en vez de
"CARAMELOS..."), y el cambio de color ya documentado (MANTEL VERDE en el reparto = MANTEL NEGRO en
el inventario original, es el mismo ítem, cambia el color a comprar). Sin ambigüedad real en
ninguno de los 202 — donde había dos candidatos parecidos (ej. las dos cajas organizadoras 1ª/2ª
requisa) se distinguió por el número de orden.

**Detalle técnico del entorno, para no repetir la sorpresa**: este entorno de Claude Code no tenía
instalado `libreoffice-calc` (solo `libreoffice-core`), así que cualquier recálculo de fórmulas de
Excel fallaba/colgaba sin explicar por qué. Se instaló con `apt-get install -y libreoffice-calc` —
si vuelve a faltar en una sesión nueva (el contenedor es efímero), hay que reinstalarlo antes de
tocar cualquier excel con fórmulas.

### Conteo real cargado — reunión de inventario del 18/19 agosto (`Inventario_confirmado_en_stock.pdf`)

Mariano subió el PDF con las notas de la reunión física de inventario (por comisión: Cocina,
Logística, Eventos, Seguridad, Guías). Se cruzó contra los 202 ítems del excel final y se cargaron
**81 conteos reales** en la columna "Conteo real (hoy)" del archivo de la sección anterior — cada
uno emparejado por nombre exacto de ítem, sin inventar cantidades donde el texto era ambiguo.

**Aclaración conceptual de Mariano Jurado (encargado general de Ruge), transmitida por Mariano el
19/20 ago — importa para leer bien la columna "Otra comisión con la que revisar" del excel**: los
ítems asignados a Marco/Julio/David (equipo de logística) **no significan que logística tenga que
ejecutar personalmente los 214 ítems**. Regla real:
- Si el bloque dice solo una comisión (ej. "COCINA"), esa comisión lo hace al 100%.
- Si dice dos comisiones juntas (ej. "LOGÍSTICA Y EVENTOS", "LOGÍSTICA Y GUIAS"), la **segunda
  nombrada gestiona/ejecuta**, y **logística corrobora que se haya hecho** (check-in: confirmar que
  ya está en inventario o ya se subió al camión) — no lo compra ni lo consigue ella misma.
- Mismo patrón para producción, la voz, etc.: si el ítem dice "producción", lo hace producción;
  logística solo verifica.

Esto no cambia el excel en sí (la columna "Otra comisión" ya tenía este dato) — cambia cómo
interpretarlo: la "Falta p/ reto 50" de un ítem de otra comisión es una alerta para preguntarle a
esa comisión, no una tarea de compra para Marco/Julio/David.

**Confirmado por Mariano: el excel por persona con stock + reto 50 + conteo real "ya es el final
final definitivo".**

**Resueltas (19/20 ago) las ambigüedades pendientes de la sección anterior:**
- **Mantel** — corrección importante: **no** hay que comprar uno verde. Hay que **pedirle a la
  iglesia el mantel negro**, vía administración (Juliana) — tarea real de **Eventos**, Marco solo
  corrobora. Esto **revierte** la decisión registrada el 17 ago ("MANTEL NEGRO... pasó a ser MANTEL
  VERDE... hay que comprarlo de color verde") — se deja la nota vieja tal cual más abajo, sin
  borrar, con esta corrección al lado. Confirmado también que "Mantel negro de la iglesia
  (Jefferson)" del PDF es el mismo ítem, no uno nuevo. Cargado en el excel como pendiente de pedir
  (no como stock propio).
- **Arena** — resuelto, 38 sacos, cargado en ARENA PARA MEZCLA DE LODO 25KG. La de borde de
  piscina queda sin número separado — no se aclaró si son el mismo stock o dos distintos.
- **Banderas** — de España confirmadas, 2, ok. De tribu **siguen sin confirmar** — hay que
  corroborar cuáles faltan, no se cargó como completo.
- **Maletines** — no son un ítem aparte: son los estuches donde van las garrafas de butano.
  Van junto con BUTANOS (David, ya cargado con 12) — 3 de esos maletines están rotos, nota aparte,
  no resta del conteo de butano en sí.
- **Chuches** — confirmado: son los caramelos que se compran para las bolsas de provisiones, hay
  que comprar más. Coincide con CARAMELOS SURTIDOS ya cargado en 0.
- **Pala** — confirmado que es la misma que PALA GRANDE (Eventos). Reto real: **2 palas grandes**,
  hay 1 (ya cargado) — falta 1.
- **Batería de la Cruz** — confirmado, es la misma BATERIA MARCA BOSH ya cargada como "sin cargar".

**Siguen genuinamente pendientes, Mariano los va a corroborar él mismo:**
- "1 paquete paños pequeños", "1 linterna para cabeza", "1 martillo", "3 maletines rotos [detalle
  de cuáles]" — dijo explícitamente "eso no lo sé, ponlo como que falta para corroborarlo".
- Banderas de tribu — sigue sin confirmar si están todas.

### Documento definitivo — corrección de Mariano (19 ago 2026, noche)

Mariano tomó el excel de la sección anterior, lo corrigió a mano y lo volvió a subir como **el
documento final**: `areas/ministerio/recursos/Ruge_tareas_por_persona_DEFINITIVO_19ago2026.xlsx`
— **este archivo reemplaza a `Ruge_tareas_por_persona_19ago2026_FINAL_con_stock.xlsx`** como
fuente de verdad (el anterior se deja en `recursos/` como histórico, sin borrar). Estructura
unificada: quitó la columna "¿Encargado general o tarea específica?" y dejó las mismas columnas en
las 3 hojas de ítems (Bloque, Ítem, Detalle, Otra comisión, Estado, Fecha límite, Inventario, Reto
50 hombres, `(19/08)`, Falta p/ reto 50).

Cambios reales hechos por Mariano (diff verificado ítem por ítem, no solo confianza):
- **Limpió los "OK"/texto** que se habían dejado como placeholder (batería, kit primeros auxilios,
  parrilla, cucharas, etc.) y los convirtió en números reales (mayormente `1`), y los stock/reto en
  texto ("100 UNIDADES", "3 SACOS") en números limpios.
- **BUTANOS corregido de 12 a 2** — la cifra de 12 (6 usados + 6 nuevos) que se había cargado desde
  el PDF no era la correcta para este ítem específico.
- **Mantel: renombrado directamente en el excel** de "MANTEL VERDE PARA MESA DE CAMISETAS" a
  "MANTEL NEGRO PARA MESA DE CAMISETAS" — coincide con la corrección de la sección anterior (pedir
  a la iglesia, no comprar verde).
- **Cajas organizadoras**: renombradas con la capacidad real — "CAJAS ORGANIZADORAS 1ª REQUISA 90
  L" y "CAJAS ORGANIZADORAS 2ª REQUISA 55 L" (antes sin el dato de litros).
- **Fechas "máxima urgencia" movidas del 19 al 20 de agosto** (el 19 ya había pasado): camión caja
  abierta, alquiler autobús 55 plazas, radios VHF, teléfono satelital, furgoneta grande, camión
  caja cerrada, troncos — los 7 ítems del bloque "Confirmar alquiler".
- **RADIOS DE COMUNICACIÓN DE IGLESIA** pasó de fecha 26 ago a urgente, 20 ago — queda dentro del
  bloque "Confirmar préstamos" (8 ítems), que en general sigue con fecha 26 ago para el resto.
- **Reto de PLATOS DE CARTON DE 6 UNIDADES confirmado en 70** (no 150) — resuelve la discrepancia
  que había quedado pendiente.

**ClickUp actualizado (19 ago 2026, lista Inventario `901220315543`)**, a pedido explícito de
Mariano — acción directa, sin pedir confirmación (regla de creación/escritura de `mariano-os/
CLAUDE.md`):
- Tarea "Logística — Confirmar alquiler (7 ítems)" (`869ehmaur`): fecha límite movida del 19 al 20
  de agosto, con comentario detallando los 7 ítems que cubre.
- Tarea "Logística — Verificar TERMOS en bodega (discrepancia detectada)" (`869ejx25z`): marcada
  **completado** — confirmado 8 termos, 1 roto, coincide con la sospecha de la retrospectiva.
- Tarea "Logística — Confirmar préstamos (8 ítems)" (`869ehmayj`): sin cambiar la fecha general del
  bloque (los otros 7 ítems siguen el 26 ago), pero se agregó un comentario marcando que RADIOS DE
  COMUNICACIÓN DE IGLESIA es urgente aparte, 20 ago.
- Tarea "Cocina — Pendientes varios (atizador, verificar cucharas)" (`869eh5gh0`): comentario
  marcando que "verificar cucharas" ya se resolvió (100/100 confirmado), pero el atizador para
  mover el carbón sigue sin confirmar — no se cerró la tarea completa porque queda ese ítem suelto.
- El resto de las 18 tareas de ClickUp son de bloque (no de ítem), así que no se tocaron una por
  una — el detalle ítem por ítem sigue viviendo en el excel definitivo, no en ClickUp (mismo
  criterio ya documentado: ClickUp tiene 18 tareas a nivel de bloque, no 202 a nivel de ítem).

### Cambio de fuente de verdad — Marco Jurado retoma el inventario maestro (21 agosto 2026)

Mariano avisó que **Marco Jurado** (dueño real del inventario de Ruge — el archivo original
`INVENTARIO_2026_RUGE_original.xlsx` de la sección "Reparto final..." arriba ya era suyo) decidió
que no se siga trabajando sobre los derivados "por persona" que se armaron entre el 17 y el 19 de
agosto — quiere que se trabaje directo sobre un excel propio, organizado por ítem/comisión, que él
mismo actualizó y volvió a subir.

**Archivo nuevo, fuente de verdad única de ahora en más**:
`areas/ministerio/recursos/INVENTARIO_2026_RUGE_actualizado_21ago2026.xlsx` — hoja única "Hoja1",
247 filas, organizado por comisión (Cocina, Eventos, Guías, La Voz, Logística, Producción,
Seguridad, Tiempos) con bloques de ítems bajo cada una. Columnas: Artículo, Stock actual/Cantidad,
Reto 50 hombres, Régimen de tenencia (a veces ya incluye notas informales de quién presta/gestiona,
ej. "PRESTADO (MARCO GUANUCHI)"), Comisión de revisión, Estado, Gestión y finanzas, **Estado
actual** y **Checking** (dos columnas nuevas respecto al original de 17 ago, con notas reales de
avance — ej. "3 CAJAS DE MALETIN ROTAS" en cocinas portátiles de gas, "12 TALLA L Y 12 TALLA M" en
camisetas). Es, en esencia, una versión evolucionada del inventario original, no un documento
nuevo desde cero — confirmado comparando estructura y nombres de ítem contra
`INVENTARIO_2026_RUGE_original.xlsx`.

**Quedan deprecados como documento de trabajo activo** (se dejan en `recursos/` como histórico,
sin borrar, pero no se editan ni se usan como fuente de ahora en más): `Ruge_reparto_por_persona_
17ago2026.xlsx`, `Ruge_reparto_tareas_17ago2026_actualizado.xlsx`,
`Ruge_tareas_por_persona_19ago2026_FINAL_con_stock.xlsx`,
`Ruge_tareas_por_persona_DEFINITIVO_19ago2026.xlsx`.

**Regla nueva y explícita de Mariano sobre cómo trackear lo que el excel de Marco Jurado no
cubre**: si algo no tiene columna en su excel (el caso que dio como ejemplo: fecha límite), **no se
le agrega una columna nueva al archivo de Marco Jurado** — se seguimiento en nuestros propios
documentos (`ruge_reparto_lookup.md` y `pendientes-activos.md`), cruzando por nombre de ítem. Mismo
criterio para "quién es el encargado puntual" cuando eso no queda claro en la columna "Régimen de
tenencia".

`ruge_reparto_lookup.md` sigue existiendo y sigue siendo el lugar para esa info (fecha límite,
encargado) — pero ojo: se generó a partir de la versión "definitiva" de 202 ítems (19 ago), y el
excel nuevo de Marco Jurado tiene ~230 ítems reales (247 filas menos headers) — **no está
garantizado que los dos coincidan ítem por ítem todavía**. No se hizo una reconciliación completa
de una sola vez — se va cruzando a medida que se recorra tarea por tarea con Mariano, que es
justamente el paso siguiente que pidió.

**Dos hallazgos ya cruzados al leer el excel nuevo, relevantes para `pendientes-activos.md`** (sin
marcarlos `hecho` todavía — esa regla es de Mariano, no por inferencia, así que quedan para que él
los confirme):
- **"Banderas de tribu"**: el excel nuevo las tiene en 5/5 (`PROPIEDAD`, `ALMACEN RUGE`) — parece
  resuelto, pendiente que Mariano lo confirme.
- **"3 maletines rotos"**: aparece como nota en la columna Checking del ítem "COCINAS PORTATILES DE
  GAS" ("3 CAJAS DE MALETIN ROTAS") — el ítem en sí ya está `GESTIONADO`/`OK`, pero el detalle del
  maletín roto queda anotado sin resolver todavía.
- Sin rastro en el excel nuevo de "paños pequeños", "linterna de cabeza" ni "martillo" — siguen
  sin corroborar, tal como estaban.

### Rate limit de ClickUp (confirmado varias veces, 17-18 ago 2026) — RESUELTO 18 ago 2026
17 ago: al traer la lista de Inventario, la API devolvió "Rate limit exceeded" dos veces seguidas
(859 y luego 794 minutos restantes) — confirma que es un límite real que se va descontando, no un
error puntual. Se liberó como estaba previsto y el 18 ago a la mañana se pudo sincronizar.

18 ago 2026 (13:51 UTC): al cargar el campo "Encargado" en las 20 tareas de la lista Inventario,
el rate limit volvió a activarse **después de 14 actualizaciones exitosas** — "espera 1343
minutos" (~22h). Investigado a fondo ese mismo día: el límite que se estaba pisando **no es el
límite general de la API de ClickUp** (100 req/min en Business), sino un límite propio y mucho más
chico del conector MCP oficial (`mcp.clickup.com`, vía OAuth) — 300 llamadas/**24hs** (ventana
móvil, no resetea rápido) sin el add-on de pago "Everything AI" ($28/usuario/mes, workspace-wide).

**Solución permanente implementada**: se construyó un servidor MCP propio,
`mariano-os/mcp-servers/clickup/server.py` (mismo patrón que el de GHL — Python de un solo
archivo, PEP 723, `uv run --script`), que llama **directo a `api.clickup.com`** con el Personal
API Token de Mariano (`CLICKUP_API_TOKEN` en `.env`, gitignored) en vez de pasar por el MCP
alojado por ClickUp. Al no pasar por `mcp.clickup.com`, queda sujeto al límite general de la API
(100 req/min), no al de 300/día — alcanza sobrado para el uso diario. Tiene pacing propio (~0.7s
entre requests) para no volver a rafaguear. Registrado en `.mcp.json` como `clickup-personal`,
junto al conector oficial `ClickUp` (OAuth) que sigue disponible para lo que no requiera volumen.
**Paso manual que hizo falta y puede volver a hacer falta si el token se revoca**: el dominio
`api.clickup.com` estaba bloqueado por la política de red del entorno de Claude Code (igual que
pasó con GHL en su momento) — Mariano lo habilitó a mano en los ajustes del entorno.

**Sincronización real de ClickUp — estado final al 18 ago 2026**: la lista de Inventario
(`901220315543`) tiene **solo 20 tareas a nivel de bloque** (no 202 a nivel de ítem — coincide con
"Resumen por bloque", no con "Detalle completo por ítem"; el detalle por ítem vive a propósito en
`ruge_reparto_lookup.md`, no en ClickUp). No hay usuarios de Marco Guanuchi, Julio Cesar Navia ni
David Luzuriaga en el workspace de ClickUp (`clickup_get_workspace_members` solo devuelve a
Mariano) — **no se los puede asignar como "assignee" nativo de ClickUp**. Solución acordada con
Mariano: él creó a mano un custom field de texto llamado **"Encargado"** (id
`57a175ab-0b87-4ddf-b3ce-345d7da132c8`) en la lista Inventario, y ahí se carga el nombre (o el
reparto, si el bloque está dividido entre varios). Estado final, con el servidor propio ya
funcionando:
- 18 tareas activas, las 18 con "Encargado" cargado (0 sin asignar).
- Se borraron 2 tareas genéricas por indicación de Mariano: "Comprar, recibir y almacenar en lugar
  seguro lo comprado" (`869eh5d47`) y "Buscar proveedores y comparar precios de faltantes"
  (`869eh5d1n`) — la segunda porque depende de cada tarea puntual, cada encargado la resuelve
  dentro de la suya, no amerita una tarea aparte.
- "Proponer compra a administración de la iglesia" (`869eh5d2k`) → Encargado: Mariano Barcelona.
- "Checklist de inventario por categoría con encargado" (`869eh5d13`) → Encargado: Marco Guanuchi.

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

#### Retrospectiva del evento (registrada 17 agosto 2026, evento ya pasó) — CARGADA 18 ago 2026
Cargada como comentario en la tarea `869ej5fvj` (comment_id `90120253912854`), vía el servidor MCP
propio de ClickUp — ya no depende del rate limit del conector oficial:

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
- **Listado de asistencia real, versión final (recibido y aclarado 18 agosto 2026)**, cargado como
  comentarios en la tarea `869ej5fvj` (comment_id `90120253914268` y aclaración
  `90120253914789`):
  - FM4.1: Dris, Alejandro (apellido pendiente — el mismo invitado en evangelización mencionado
    arriba, distinto del siguiente), Alejandro Arteaga / "Fito" (aclarado por Mariano: "Fito
    Arteaga" = Alejandro Arteaga, no Mateo Arteaga — son personas distintas), Nidia, Adrián, Ingri,
    Mauricio.
  - FM4.2: Miguel (pagó en la puerta), Diego, Rebeca.
  - FM4.3: Margorie (pagó en la puerta), Rocío, Jacobo, Paulina, Lisandro.
  - También confirmados por Mariano (18 ago): **Mateo Arteaga, David Valera y Sabrina Navarro** —
    coincide con lo que ya decía esta retrospectiva, solo habían quedado fuera del listado escrito
    a mano por grupo. Registro de asistencia real ya cerrado, sin preguntas abiertas.

#### Contexto sensible — mensaje del Pastor Fabio Calderón previo al evento (14 agosto 2026)
Mariano compartió esto el 18 de agosto para que quede registrado junto a la retrospectiva — es
contexto pastoral delicado, tratarlo con discreción (no es para exponer, es para que el sistema
entienda la presión real detrás del cambio de proceso). **No se subió a ClickUp** — queda solo
acá, en el sistema privado — salvo que Mariano pida explícitamente lo contrario.

El viernes 14 de agosto, al ver que solo se habían reportado ~10 entradas vendidas para la Tarde
Profética (el día siguiente), el Pastor Fabio Calderón le escribió a Mariano expresando
preocupación fuerte: que ni la propia gente de los líderes iba a asistir, que estos eventos son
para ganar almas y le dolía verlos "perder" en cambio, que revisando por código de líder no
llegaba ni la mitad de la gente que se reporta semanalmente en los grupos, que le preocupaba tanto
el reporte bajo como el silencio de los líderes al respecto, que representaba un golpe financiero
fuerte para la iglesia, y que sentía que la estrategia pensada para ganar jóvenes no se había
entendido ni trabajado como tal.

**Por qué importa dejarlo anotado**: esto es lo que estaba en juego detrás del cambio de proceso
que Mariano decidió en la retrospectiva (cobrar primero, entregar entradas después) — no fue solo
una mejora operativa, fue una respuesta directa a una reprimenda pastoral real por bajo reporte y
silencio de los líderes. Tenerlo en cuenta para futuros eventos: el reporte temprano y honesto de
entradas/asistencia no es un detalle administrativo menor, tiene peso pastoral y financiero real
para Mariano frente a su liderazgo.

**Segunda instancia (17 agosto 2026, "el lunes")**: Mariano mandó el listado de asistencia real a
su liderazgo. La Pastora Mirna Gómez le respondió también con dureza, por la demora en responder
algo que se le venía consultando y que hacía falta para logística del propio evento (buscar
sillas, organizar) — le dijo, en sus palabras, que "no tengo palabras" ante que respondiera días
después de un evento que se le estaba consultando activamente.

**Nota explícita de Mariano (18 agosto 2026) sobre para qué sirve tener esto registrado**: no es
para cargarlo en ninguna tarea de ClickUp ni convertirlo en una acción — es para que el sistema
entienda el contexto real: tanto el Pastor Fabio como la Pastora Mirna quedaron **nada conformes**
con el desempeño de Mariano y su equipo alrededor de este evento (reporte bajo, silencio, demora
en responder). Es contexto relacional/pastoral de fondo, no un pendiente operativo.
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
