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

### Personal — crisis de caja urgente (24 ago 2026, la más urgente de todas ahora mismo)

Mariano avisó que arrancó la semana con **menos de 700€ en total y hoy sin nada líquido** (pagó la
comida del día con tarjeta de crédito). Esta semana además se le cobran (o ya se cobraron, sin
precisar) la **tarjeta de crédito** y la cuota de **autónomos**. Detalle completo de deudas y
discrepancias en `areas/gotir/direcciones/finanzas/CLAUDE.md`, sección "Actualización 24 agosto
2026". Pagos pendientes a resolver esta semana, por orden en que los mencionó (no confirmado como
prioridad real todavía — Mariano pidió armar el orden cruzando contra lo que se cobre primero):
1. Micol Navarro — 406.000 ARS (ya marcada como la más urgente de todas, 17 ago).
2. Sabrina/su casero — 350€ o 305€ (monto sin confirmar, ver discrepancia en finanzas).
3. Exxo — saldo pendiente USD 237.
4. Matías Macho — 140.000 ARS.
5. Su propia casera — monto sin dar.
6. Reto Ruge (cuota de Mariano como servidor) — 250€.
7. Pasaje a Madrid (viaja el 29 ago) — monto sin dar.
- **Actualizado 24 ago 2026**: Mariano ya pagó una parte de la deuda a Micol Navarro — de los
  406.000 ARS originales quedan solo **80.000 ARS pendientes**.
- **Prioridad confirmada por Mariano (24 ago 2026)**: Federico/Sabrina (350€) es ahora la
  prioridad #1 a pagar, en cuanto entre el primer cobro cercano — Sara Sofía (825€) o Maryi
  Castañeda (2.475€), ambas todavía sin pagar a esta fecha. Desplaza a Micol de la posición #1.
- Estado: **abierto — urgente, prioridad de pago definida, esperando que entre el primer cobro**.
- Recordado: 2 veces (24 ago 2026; 25 ago, chequeo diario 18:00).

### GOTIR — seguimiento

**WhatsApp sin proveedor conectado tras la migración de reseller de GHL — RESUELTO (21 ago 2026), queda un seguimiento**
   - Detectado 19/20 ago 2026, investigando el caso de Regina Lucia Epifanio (ver
     `direcciones/comercial/CLAUDE.md` sección 10). Causa real: el reseller anterior de GHL
     (identificado por Mariano como "Trindia", ortografía sin confirmar — antes se había registrado
     acá como "God High Level", probablemente la misma transcripción oída distinto) dejó de darles
     servicio y los migró a una cuenta de Go High Level propia, sin proveedor de WhatsApp conectado.
   - **Resuelto por Mariano (21 ago 2026)**: reconectó el canal con un proveedor nuevo, **GoGHL.ai**
     (`app.goghl.ai`), y dio de alta los 4 números reales de GOTIR — los 4 muestran "Conectado".
     Detalle completo (números, a quién pertenece cada uno) en
     `direcciones/comercial/CLAUDE.md` sección 6.3.
   - **Seguimiento pendiente, a pedido explícito de Mariano**: revisar que todas las automatizaciones
     usen los números de WhatsApp correctos. Ya se confirmó lo que se puede confirmar por API — los
     números hardcodeados en este sistema (`{WA#1}` en los workflows de GHL, `fromNumber` de
     `ghl_send_message`) son válidos y están conectados. **Lo que queda sin poder auditar por API**
     (límite real de la API de GHL, no da acceso a la lógica interna de los workflows): revisar a
     mano en el builder de GHL si algún workflow apunta todavía a un canal de WhatsApp roto.
   - **Resuelto (21 ago 2026)**: Mariano confirmó que los 4 números son suyos (todos con sus
     propios móviles), los nombres viejos quedaron solo como etiqueta — los quiere mantener
     conectados a propósito, para futuros usos (JARVIS en otro número, un futuro comercial, otra
     persona ayudando en otra área) y porque algunos ya están en grupos de WhatsApp con clientes.
     No hay nada que cambiar acá.
   - Estado: **el bloqueo de fondo está resuelto — canal de WhatsApp funcionando de nuevo**.
   - Recordado: 3 veces (19/20 ago 2026; 20 ago, chequeo diario 20:00; 21 ago 2026, resolución).

~~**Revisión de automatizaciones (builder de GHL) — RESUELTA por completo (21 ago 2026)**~~
   - El login automatizado por navegador no fue viable (protección anti-bot de GHL/Cloudflare —
     detalle completo en `direcciones/comercial/CLAUDE.md` sección 6.3, decisión deliberada de no
     intentar evadirla). Mariano mandó capturas de pantalla de los nodos relevantes en su lugar.
   - Se encontraron 2 nodos sin el código `{WA#1}` (VISADOS → "WhatsApp Bienvenida" y "Lead capture
     landing" → "SMS") — detalle en `direcciones/comercial/CLAUDE.md` sección 5.9. Los dos son en
     realidad **Fragmentos de GHL** (Conversaciones → Fragmentos: "Mensaje bienvenida visados" y el
     de "Lead capture landing"), no texto suelto dentro del nodo — dato nuevo para el futuro: los
     nodos "WhatsApp Bienvenida"/"SMS" que usan una plantilla real editan el Fragmento por separado,
     no el cuadro de texto del workflow (que queda de solo lectura).
   - **Confirmado por Mariano (21 ago 2026): los dos Fragmentos ya están corregidos.**
   - Estado: **hecho**.

### GOTIR — urgente

0. **Promo en USDT/Binance ofrecida a Javier Maddia — venció el viernes 21 ago, pero no se cayó la venta**
   - Detectado 19 ago revisando la llamada del 18 ago (73 min, familia de 3, ~2.475€ potenciales).
     Mariano ya envió por correo una promoción agresiva por pagar en USDT vía Binance, con fecha
     límite el viernes 21 — el cliente además prefiere pagar así.
   - **Contradice directamente** la política de centralización de pagos que Mariano fijó el 14 ago
     (todo en euros, sin cripto, sin dólares — ver `areas/gotir/CLAUDE.md`, "Política de
     centralización de pagos").
   - **Aclarado 24 ago 2026, leyendo el chat real**: Javier escribió el 22 ago *"Aún estamos en la
     espera del pago de la jubilación... Dios mediante tenga esa disponibilidad, iniciaremos el
     proceso"* — no rechazó nada, está esperando que le liquiden su jubilación en Venezuela para
     poder pagar. La oportunidad en GHL (`id=gYhBhziKOBoqeSrFDeqs`, 825€) sigue en "Información y
     contrato enviado", sin moverse desde el 18 ago.
   - **Pendiente real que queda**: (a) decisión de Mariano sobre si la promo USDT sigue en pie pese
     a que venció la fecha, dado que la demora es por algo fuera del control del cliente; (b) mensaje
     de seguimiento cálido (sin mencionar el vencimiento) avisándole que el cupo de la Opción 2 se
     llena rápido y **se reserva recién cuando se paga la inscripción** (corregido 24 ago — Mariano
     aclaró que GOTIR no puede reservarlo sin ese pago, la primera versión del mensaje lo daba a
     entender mal) — a confirmar antes de enviarlo.
   - Estado: **abierto — esperando que Javier cobre su jubilación, no una venta caída**.
   - Recordado: 7 veces (19 ago 2026; 20 ago, chequeo diario 20:00; 22 ago, chequeo de la mañana;
     22 ago, chequeo diario 20:00; 23 ago, chequeo diario 20:00; 24 ago 2026, aclarado; 25 ago,
     chequeo diario 18:00).

1. **Nazareth Rengel — no-show del 18 ago sin reconexión todavía**
   - Referida por Jesús Mosquera. La nota en GHL dice "pendiente contactar para reagendar" pero no
     hay evidencia de que se le haya escrito, a diferencia de Yeraldin (mismo día, misma situación,
     ya recontactada). Ya pasaron 2 días.
   - Estado: **abierto**, ya van 5 días sin reconexión.
   - Recordado: 6 veces (19 ago 2026; 20 ago, chequeo diario 20:00; 22 ago, chequeo de la mañana;
     22 ago, chequeo diario 20:00; 23 ago, chequeo diario 20:00; 25 ago, chequeo diario 18:00).

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
     eran relevantes solo si se elegía la Propuesta 2, que no fue la elegida. **Revisado a fondo el
     25 ago 2026** (a raíz del pedido de automatizar el mini-funnel pre-llamada, ítem 2 más abajo):
     "Bot setter" resultó ser solo un router (trigger "el cliente respondió" → webhook a n8n), y ese
     webhook está muerto — no existe ningún workflow en n8n con ese path. Detalle completo en
     `direcciones/comercial/propuestas-sistema-comercial.md`, sección Propuesta 2.
   - **Pendiente separado, todavía sin ejecutar a propósito**: Mariano preguntó si se puede aplicar
     esto en retroactivo a todos los clientes que escribieron y no se les respondió en los últimos
     meses. Es técnicamente posible, pero no se ejecutó — motivo completo en
     `direcciones/comercial/CLAUDE.md` sección 13.5 (choca con la decisión ya tomada de priorizar
     leads activos sobre nurturing histórico de +2.000 contactos, generaría demasiados borradores
     de golpe para que Mariano revise, y en rigor es una capacidad de la Fase C, que todavía no
     existe). Recomendación dada: acotarlo a los últimos 30 días cuando llegue el momento, no a
     "todos, meses".
   - Estado: **Fase A completa (25 ago 2026, los 2 workflows de GHL probados con datos reales),
     Fase B y C sin empezar**.
   - Recordado: 4 veces (20 ago 2026, tras la elección; 22 ago, chequeo diario 20:00; 23 ago,
     chequeo diario 20:00; 25 ago, chequeo diario 18:00).

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
   - Recordado: 4 veces (20 ago 2026, madrugada — 2 mensajes seguidos; 20 ago, chequeo diario 20:00;
     25 ago, en curso ahora mismo con Mariano en el builder).

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
   - Recordado: 6 veces (19 ago 2026, chequeo diario 20:00; 20 ago, chequeo diario 20:00; 22 ago,
     chequeo diario 20:00; 23 ago, chequeo diario 20:00; 25 ago, chequeo diario 18:00).
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
   - **Actualizado 25 ago 2026**: Fragmento 9 (el CTA de agendar) ajustado con lenguaje asuntivo
     (checklist de venta, sección 12.4). Mariano pidió que esto corra automático apenas llega un
     mensaje nuevo, no que él tenga que mandar cada Fragmento a mano — se evaluó manual vs. bot
     (recomendación dada: bot, porque son preguntas de filtro predecibles y de bajo riesgo, pero
     probarlo primero en vivo antes de automatizar del todo). **Decisión de Mariano**: probar los 9
     Fragmentos manual con los próximos 3-5 leads reales primero, y recién ahí automatizar. Se
     revisó si algún workflow "Bot" ya existente en GHL servía de base — no, ver ítem de la
     Propuesta 4 más arriba. **Decisión (25 ago 2026): el bot para este mini-funnel se construye
     nuevo, desde cero, en n8n** — construcción todavía sin empezar, se retoma en una próxima
     sesión.
   - Estado: **bloqueado (esperando a Mariano) — texto terminado y cargado en el sistema, falta que
     Mariano pegue los 9 Fragmentos en GHL y los pruebe manual con leads reales antes de que se
     construya la versión bot en n8n**.
   - Recordado: 6 veces (19 ago 2026, chequeo diario 20:00; 20 ago 2026; 20 ago, chequeo diario
     20:00; 25 ago 2026; 25 ago, en curso ahora mismo — 9 Fragmentos ya cargados en GHL por
     Mariano, falta probarlos con leads reales).

3. **Migrar la cuenta de ads a facturación en euros (hoy en pesos, vía Mercado Pago Argentina)**
   - Detalle completo en `direcciones/marketing/CLAUDE.md`, sección 6. Mariano ya decidió hacerlo
     (más caro pero deducible, y no le parece correcto operar en ARS para un negocio español), pero
     sin fecha todavía — acaba de cargar 70.000 ARS para no cortar la campaña mientras tanto.
   - Estado: **abierto**, sin fecha.
   - Recordado: 5 veces (21 ago 2026, dos veces el mismo día; 22 ago, chequeo diario 20:00; 23 ago,
     chequeo diario 20:00; 25 ago, chequeo diario 18:00).

4. **Conectar el sistema a la cuenta de administrador de anuncios de Mariano (Meta Ads Manager)**
   - Detalle completo en `direcciones/marketing/CLAUDE.md`, sección 7. Pedido explícito de Mariano
     para tener visibilidad en tiempo real de la inversión y el desempeño de las campañas de Exxo.
   - **Plataforma confirmada (21 ago 2026): Meta Ads Manager.**
   - **Falta antes de poder construirlo**: (a) un access token de la API de Marketing de Meta con
     permiso `ads_read` (idealmente de un usuario del sistema, no caduca a los 60 días), y (b) el ID
     de la cuenta de anuncios (`act_XXXXXXXXXXXXX`) — ver instrucciones de dónde conseguir cada uno
     en `direcciones/marketing/CLAUDE.md` sección 7.
   - Estado: **abierto — bloqueado esperando que Mariano consiga el token y el ID de cuenta**.
   - Recordado: 5 veces (21 ago 2026, dos veces el mismo día; 22 ago, chequeo diario 20:00; 23 ago,
     chequeo diario 20:00; 25 ago, chequeo diario 18:00).

5. **Repositorio de marketing de Exxo — conseguirlo y dárselo a este sistema para tener contexto real**
   - Detalle en `direcciones/marketing/CLAUDE.md`, sección 11.1 punto 8. Agustín se comprometió en
     la reunión del 25 ago a transferir el repo completo de marketing (GitHub) a la cuenta de
     GOTIR. **El objetivo explícito de Mariano es pasárselo a este sistema** para tener contexto
     completo del trabajo de marketing, no solo tener la custodia — falta: (1) que Agustín lo
     transfiera, (2) que Mariano avise cuando lo tenga, (3) cargarlo/conectarlo acá.
   - Estado: **en curso**, esperando a Agustín.

6. **Confirmar monto real de fondos demostrables — cambio de criterio a "100% IPRE mensual"**
   - Surgió en la reunión del 25 ago con Agustín (`direcciones/marketing/CLAUDE.md` sección 11.2):
     se acordó reemplazar la cifra fija de fondos demostrables ya documentada en
     `direcciones/comercial/CLAUDE.md` (~7.200€) por un mínimo del 100% del IPRE mensual por
     titular. No está confirmado si el monto en euros que resulta de esto es igual, mayor o menor
     al que se viene usando en llamadas reales. **No usar la cifra de IPRE con clientes hasta que
     Mariano confirme el monto exacto.**
   - Estado: **abierto, bloqueante para el nuevo PDF de venta**.

7. **Confirmar si Mariano acepta el script de alertas de Ads en vez del informe periódico pedido**
   - Agustín ofreció, en lugar de un informe de rendimiento periódico (lo que Mariano había
     pedido), un script para la computadora de Mariano que avise cuando una campaña se bloquee o
     interrumpa — ver `direcciones/marketing/CLAUDE.md` sección 11.1, punto 5.
   - Estado: **abierto**, a confirmar si esto es suficiente o si Mariano insiste en el informe.

8. **Avisarle a Agustín que NO migre el WhatsApp de la centralita al número personal de Mariano**
   - Se había acordado en la reunión del 25 ago (ver `direcciones/marketing/CLAUDE.md` sección
     11.4), pero Mariano lo canceló acá el 26 ago al ver la implicancia real (riesgo sobre los
     workflows con `{WA#1}`, contradice el pedido anterior de separar su número personal del
     comercial). **Falta que Mariano se lo comunique a Agustín** — solo quedó frenado en este
     sistema, Agustín todavía puede estar por avanzar con eso.
   - Estado: **abierto — urgente, avisar a Agustín antes de que lo ejecute**.

10. **3 tareas de Mariano pendientes de la reunión del 25 ago con Agustín (Exxo)**
    - Detalle completo en `direcciones/marketing/CLAUDE.md` sección 11.2.1: (a) mandarle a Agustín
      una captura del flujo de automatización actual de GHL y explicarle cómo funciona; (b) subir
      las fotos profesionales (versión impresión y web) a la carpeta que va a compartir Agustín;
      (c) exportar los prospectos del CRM (~2.000 generales + ~500 calificados) para remarketing.
    - Estado: **abierto**, ninguna de las 3 hecha todavía.

11. **Dar el texto estandarizado de las 3 opciones de curso para la página nueva del PDF de venta**
    - Ver `direcciones/marketing/CLAUDE.md` sección 11.2. Tarea de Mariano, destraba la página 3
      nueva del PDF junto con la definición de los 3 números de pricing (ítem relacionado, sigue
      abierto también).
    - Estado: **abierto**.

9. **Permisos de API en GHL otorgados a Agustín (Exxo) — confirmado por Mariano (26 ago), sin objeciones**
   - Ver `direcciones/marketing/CLAUDE.md` sección 11.4. No requiere ninguna acción de este sistema,
     solo queda registrado: de ahora en más hay dos actores con acceso de escritura a la misma
     cuenta de GHL.
   - Estado: **cerrado** — informativo, tenerlo presente si aparece algo raro en GHL que este
     sistema no hizo.

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
   - Recordado: 5 veces (20 ago, chequeo diario 20:00; 21 ago, cambio de fuente; 22 ago, chequeo
     diario 20:00; 23 ago, chequeo diario 20:00; 25 ago, chequeo diario 18:00).
   - **Actualizado 25 ago 2026 (mañana)**: Mariano ya les mandó a Marco y Julio la minuta de la
     reunión del 24 ago con todos los pendientes y la fecha límite (jueves 27 ago) — cubre lo mismo
     que este sistema iba a recordarles por separado del bloque "26 ago" (cámara/dron, Costa Rica,
     préstamos, estructura de rótulos, pegatina de provisiones). Mariano les hace seguimiento él
     mismo por la tarde o mañana — no volver a mandarle recordatorios de este bloque hasta que él
     cuente cómo les fue.

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
   - Recordado: 5 veces (21 ago 2026, dos actualizaciones el mismo día; 22 ago, chequeo diario
     20:00; 23 ago, chequeo diario 20:00; 25 ago, chequeo diario 18:00).

5. **Grupo de Madrid — Marianne y Yorlenny en riesgo de no ir al Lanzamiento (5 sept 2026)**
   - Detalle completo en `areas/ministerio/CLAUDE.md`, sección "Grupo de Madrid". Mariano tiene
     llamada **hoy (21 ago 2026)** con Yorlenny, Marianne y Jenny (su pareja ministerial en Madrid)
     para visionarlas — las dos manifestaron querer renunciar por el costo de viajar a Valencia.
   - Estado: **abierto, esperando el resultado de la llamada del 21 ago** — decisión pastoral, este
     sistema no participa, solo espera que Mariano cuente cómo quedó. Ya pasaron 2 días sin novedad
     registrada.
   - **Agregado 24 ago 2026**: Mariano va a viajar a Madrid el **29 de agosto** para despedirse y
     hacer el último grupo de amistad ahí — falta comprar el pasaje (ver también el ítem de caja
     urgente arriba). Sin monto ni fecha de compra confirmada.
   - Recordado: 5 veces (21 ago 2026; 22 ago, chequeo diario 20:00; 23 ago, chequeo diario 20:00;
     24 ago 2026; 25 ago, chequeo diario 18:00).

8. **Reto Ruge — dos reuniones hoy (24 ago) y listado de servidores a visionar sin armar**
   - Área: ministerio (Ruge). Hoy Mariano tiene reunión a las **21:00** con el equipo de logística y
     a las **22:00** con el equipo de servidores. Detalle completo del estado de logística (cruzado
     contra el excel de Marco Jurado) en `areas/ministerio/CLAUDE.md`, sección "Reuniones de hoy".
   - Pidió armar un **listado de los hombres que está visionando** para servir en el reto — todavía
     no dio nombres, falta que los aporte antes de poder armar la lista.
   - Estado: **abierto — reuniones hoy a la noche**.
   - Recordado: 2 veces (24 ago 2026; 25 ago, chequeo diario 18:00).

6. **Asignar a Emiliano Ortiz y Litzy a un grupo FM4 (4.1, 4.2 o 4.3)**
   - Detalle completo en `areas/ministerio/CLAUDE.md`, sección "Campaña de evangelización rumbo al
     Encuentro". Los dos fueron por primera vez a Noches de Vida el 20 ago 2026; Mariano dijo que
     los va a repartir más adelante, sin fecha concreta todavía.
   - Estado: **abierto**, sin urgencia declarada.
   - Recordado: 4 veces (21 ago 2026; 22 ago, chequeo diario 20:00; 23 ago, chequeo diario 20:00;
     25 ago, chequeo diario 18:00).

7. **Sistema de seguimiento 1:1 con discípulos FM4 — registro de fechas en marcha**
   - Detalle completo y tabla de registro en `areas/ministerio/CLAUDE.md`, sección 8.3. Mariano
     pidió que no pasen más de 3 semanas sin que se reúna individualmente con cada uno de sus
     discípulos (Adrián, Ingrid, Diego, Rebeca, Rocío, Jacobo, y probablemente
     Lisandro/Paulina/David/Sabrina una vez activos) — quiere ir agendando llamadas para sostener
     ese ritmo.
   - **Primeros datos reales (21 ago 2026)**: Mariano confirmó que se reunió "la semana pasada" con
     **Diego Villavicencio, Rocío Jury e Ingrid Guaño**. Fecha imprecisa (no se dio el día exacto),
     queda registrada así, sin inventar precisión. Faltan Adrián Caro, Rebeca Lema y Jacobo
     Marulanda — todavía sin ninguna reunión registrada.
   - **Falta antes de poder avisar proactivamente con precisión**: como la fecha es "la semana
     pasada" y no un día puntual, el aviso de las ~3 semanas va a ser aproximado, no exacto al día.
   - Estado: **abierto — tracking en marcha, con 3 de ~10 discípulos ya con una fecha registrada**.
   - Recordado: 5 veces (21 ago 2026, dos veces; 22 ago, chequeo diario 20:00; 23 ago, chequeo
     diario 20:00; 25 ago, chequeo diario 18:00).

---

## Hechos (quedan un tiempo como registro antes de limpiarse)

- ~~Post-mortem obligatorio de venta perdida en el checklist "después de colgar"~~ — agregado a
  `areas/gotir/direcciones/comercial/CLAUDE.md`, sección 2, paso 6, el 19 agosto 2026.
