# Secuencia post-pago — GOTIR Comercial

> Creado 25 septiembre 2026, a pedido explícito de Mariano. **Reescrito a fondo el 26 septiembre
> 2026** tras descubrir, al inspeccionar el workflow real de GHL, que gran parte de esto ya existía
> (aunque desactualizado/con bugs) — este documento ya no es un diseño desde cero, es el estado real
> verificado en vivo más lo que se corrigió/agregó el 26 sept. Motivo textual de Mariano (25 sept):
> quiere que "apenas pagan ya tengan todo claro y no sientan que desaparecemos apenas pagan".

## 0. Dónde vive esto realmente en GHL — corregido 26 sept 2026

**Corrección importante sobre la versión anterior de este documento**: se había asumido que el
acceso a la plataforma se mandaba por email con "olvidé mi contraseña". Falso — el mecanismo real
es la acción nativa de GHL **"Course Grant offer"**, que le da al contacto acceso directo a un
producto de curso/membresía (probablemente lo que sostiene `app.clientclub.net` por debajo).

El workflow que hace todo esto **no es** "Pago realizado- contrato" (ese solo crea/actualiza la
oportunidad y manda el contrato por `Send Documents & Contracts`) — es **"nuevo cliente start"**
(Publicado, en Seguimiento), que se dispara con el trigger "La Oportunidad Ha Cambiado / Trámite has
changed" y se ramifica por un Condition según el campo **"Tipo de trámite"**. De las 8 ramas
posibles, solo 4 tienen contenido real armado hoy: **VISADO ARG, ESTANCIA, VISADO LATAM,
RENOVACIÓN POR ESTUDIOS** (antes mal titulada "CUENTA PROPIA", ver sección 3). Las otras 4
(**CUENTA PROPIA** real, CUENTA AJENA, RENOVACIÓN DE ESTUDIOS-vacía-duplicada, None) van directo a
FINAL sin hacer nada — esos clientes hoy no reciben ningún onboarding.

## 1. Qué hace cada rama construida, en su versión ORIGINAL (antes de las correcciones de hoy)

Estructura común a las 4 ramas activas: Assign to user → Internal Notification (interno, "avisanos
si podrás tomar el cliente", **iba directo al abogado externo**) → Create Or Update Opportunity
(con "Proveedor" cargado) → Update contact field (OPP ID) → Course Grant offer → 3 SMS al cliente:

1. **Bienvenida** (inmediato) — presentación de GOTIR y acompañamiento.
2. **Comunidad GOTIR** — con el link real: `https://chat.whatsapp.com/BSxDC6caz9nHFc7t4RK8LW?s=cl&p=i&ilr=0`
3. **Próximos pasos** — avisa que un abogado va a contactar pronto, y da el link de la plataforma
   (`https://uttdf7grgmbznkerppnm.app.clientclub.net/`) con instrucción de entrar con el mismo mail.

Cierra con Wait 1 día (ventana Lun-Vie 9-18hs) → Internal Notification interna ("¿pudiste
contactar al cliente?", con links a "Primer contacto SI/NO", dos workflows aparte que están en
Borrador/sin publicar — gap real, no arreglado hoy) → FINAL.

**Bug de timing encontrado y corregido en ESTANCIA (ver sección 4)**: los `Wait` entre estos 3 SMS
estaban en **1 minuto** en vez de horas/días — los 3 mensajes le llegaban al cliente casi juntos,
no espaciados como se pretendía.

## 2. El problema de fondo que disparó todo lo de hoy: derivación "en crudo"

Mariano notó que el Proveedor (abogado externo) se carga y se le avisa **casi al toque de pagar**
— antes de que el cliente reciba ni siquiera el mensaje de Momento 3 (curso/seguro/médico/
facturación). Esto contradice lo que él quiere: que el abogado reciba al cliente ya con curso
elegido, seguro/médico gestionados, y sabiendo usar la plataforma — para que el abogado no sienta
que se le pasan casos "en crudo" mientras GOTIR dice que ya hizo "la primera parte".

**Confirmado por Mariano**: el "Internal Notification" temprano de ESTANCIA le llega directo al
abogado (no al equipo interno de GOTIR) — esto no era un detalle menor, era literalmente el
problema a resolver.

### 2.1 Diseño ideal (Mariano, 26 sept) — pospuesto para otra sesión

Mariano propuso algo más robusto que un simple `Wait` de tiempo: preguntarle al cliente
explícitamente si ya completó cada requisito (seguro contratado o propio, médico contactado con el
formulario a mano, curso elegido/inscrito, plataforma entendida) y **recién derivar cuando todo esté
confirmado**, no solo cuando pasó tiempo.

**Por qué se pospuso (decisión conjunta, 26 sept)**: construir esto bien requiere 4 campos
personalizados nuevos de contacto (`seguro_confirmado`, `medico_confirmado`, `curso_confirmado`,
`plataforma_confirmada` — tipo "Botón de opción" Sí/No, ya creados en GHL, carpeta cualquiera,
objeto Contacto), preguntas con **opciones numeradas** (no texto libre — una automatización basada
en reglas no puede interpretar lenguaje natural variado), y un Condition final que chequee los 4
juntos antes de derivar, con un colchón de seguridad (notificar a Mariano para confirmar en vez de
derivar en silencio). Con el tiempo real que Mariano tenía disponible hoy, se decidió construir
primero la **versión simple** (sección 4) y dejar esto documentado para retomar con calma.

**Spec para cuando se retome** (no construido, solo diseñado):
- Después de "Próximos pasos", agregar preguntas con opciones numeradas tipo: *"1️⃣ Ya until until lo
  hice / 2️⃣ Ya tengo [seguro/médico] propio, no necesito el vuestro / 3️⃣ Todavía no, ¿me ayudás?"*
  — el Condition chequea si la respuesta **incluye "1" o "2"** (resuelto) vs. cualquier otra cosa
  (pendiente, se recuerda). Para seguro y médico, el disparador principal debería ser la
  **submission real del formulario** (más confiable que texto libre — mismo patrón que ya usa el
  workflow "Facturación", sección 5), con esta pregunta numerada como respaldo para el caso "ya
  tengo el mío propio, nunca voy a completar el formulario".
- Condition final: si los 4 campos = Sí → Update Opportunity (Proveedor) + Internal Notification al
  abogado. Si no, recordatorio + espera más, y como colchón, avisarle a Mariano en vez de derivar en
  silencio ante cualquier duda.
- El video de la plataforma (guion en sección 6) se engancha acá también, como parte de "plataforma
  confirmada".

## 3. Bug de nombres encontrado en el Condition — corregido 26 sept 2026

La rama con todo el contenido armado estaba titulada **"CUENTA PROPIA"**, pero su condición real
filtraba por **"Renovación" + "Reagrupación"** — nada que ver con Cuenta Propia. Mientras tanto,
había otra rama, correctamente titulada "CUENTA PROPIA" (condición real = "Cuenta propia"), que iba
directo a FINAL sin nada armado — los clientes de Cuenta Propia real nunca recibieron onboarding.

**Corregido**: la rama con contenido se renombró a **"Renovación por estudios"** (sin tocar su
condición ni su contenido, ya funcionaba bien puertas adentro) y se borró la rama vacía duplicada
"RENOVACIÓN DE ESTUDIOS" que nunca se ejecutaba (quedaba interceptada antes por la mal titulada).

**Pendiente de fondo, no resuelto, anotado en `pendientes-activos.md`**: "Reagrupación" no es un
tipo de trámite en sí — es un atributo que puede sumarse a cualquier trámite (Visado, Estancia,
Residencia). Hoy vive mezclado dentro de la condición de "Renovación". Mismo caso con "Renovación"
en general (se puede renovar una Estancia, no solo Estudios) — Mariano decidió no complicarse con
esto ahora, arrancar solo con "Renovación por estudios" como caso principal.

## 4. Lo corregido/agregado HOY (26 sept 2026) — en el CLON, todavía sin publicar

**Todo esto se hizo en un clon** del workflow ("Copy - nuevo cliente start"), no en el original
publicado (51 inscritos activos) — por seguridad, no se sabe con certeza qué le pasa a contactos ya
en curso cuando se edita en vivo. El clon queda en **Borrador**, sin promover a producción, hasta
probarlo con "Probar flujo de trabajo" en una próxima sesión.

**Rama ESTANCIA, terminada hoy:**
1. Wait entre Bienvenida y Comunidad corregido de 1 minuto a **3 horas** (falta confirmar si
   también se corrigió el segundo Wait, entre Comunidad y Próximos pasos — quedó en un valor corto,
   no crítico).
2. Se sacó el campo "Proveedor" (tenía **Carolina Chapo**, colaboradora con la que GOTIR ya no
   trabaja — ver sección 7) del "Create Or Update Opportunity" temprano — la oportunidad se sigue
   creando, pero sin asignar proveedor ahí.
3. Se borró el "Internal Notification" temprano (el que avisaba al abogado en crudo) — su texto se
   guardó para reutilizar al final.
4. Se agregó, después de "Próximos pasos": Wait 1 día → SMS nueva (Momento 3, ver sección 6.1,
   texto y link de facturación ya confirmados reales) → Wait 2-3 días → **Actualizar oportunidad**
   (la acción nueva, no la vieja "Create Or Update" que GHL avisó que se va a discontinuar) con
   Proveedor = **María García Serrano** → el Internal Notification recreado (mismo texto de antes)
   → de ahí sigue el chequeo interno que ya existía ("¿contactaste?") sin tocar.

**Falta (próxima sesión), en orden sugerido:**
1. Probar la rama ESTANCIA del clon con "Probar flujo de trabajo".
2. Replicar la misma corrección (mover Proveedor + notificación al final, agregar SMS Momento 3) en
   **VISADO ARG** y **VISADO LATAM** — ninguna de las dos tenía Proveedor cargado (a propósito,
   Mariano le había pedido a Sabrina que no derive automático) — ahora que se sabe el criterio
   real (sección 7), corresponde agregarlo recién al final también, no antes.
3. Corregir Momento 3 en VISADO ARG/LATAM: **sin el punto de certificado médico** (los visados no
   lo requieren, sección 8) — solo curso + seguro + facturación.
4. Agregar el campo "Valor del cliente potencial" (`{Contact.Custom Fields.Monto}`) en VISADO LATAM
   y Cuenta Propia/Ajena — ahí **sí se puede usar el valor real** (Wilmen y Sebastián Sánchez
   Lorente no tienen cuenta de GHL, no hay riesgo de exposición). En VISADO ARG, seguir con el
   criterio de placeholder (Gisela sí tiene cuenta de GHL).
5. Construir de cero la rama **CUENTA PROPIA** (real, la que va a FINAL hoy) — ver sección 4.1.
6. Cuando todo esté probado: renombrar el original a "nuevo cliente start — OLD", pasarlo a
   Borrador (sin tocar su estructura, para que los 51 en curso terminen tranquilos con la versión
   vieja), y publicar el clon con el nombre real.

### 4.1 Rama CUENTA PROPIA — a construir desde cero

No lleva seguro ni certificado médico (sección 8), ni "elegir curso" (no es trámite de estudios).
Estructura sugerida, más simple que ESTANCIA: Assign to user → Internal Notification (interno) →
Create/Actualizar Oportunidad (Trámite=Cuenta Propia, sin Proveedor todavía) → Update contact field
→ Bienvenida (sin mencionar curso) → Wait → quizás Comunidad GOTIR → Wait días → SMS final (solo
facturación, ver sección 6.2) → Wait → Actualizar oportunidad (Proveedor = **Sebastián Sánchez
Lorente**, directo, sin dejarlo en blanco — confirmado por Mariano) → Internal Notification al
abogado → FINAL.

## 5. Formulario de facturación — confirmado, existe y está conectado

`YrHyk4NpBIqxf59EoH0S` ("Datos de facturación") es el correcto — confirmado por Mariano. Existe
además un workflow **"Facturación"** (Publicado, 5 inscritos) que escucha cuando se envía este
formulario y crea el contacto en **Holded** automáticamente — Mariano avisó que probablemente no
esté funcionando todavía porque **la cuenta de Holded no está activa**. No bloquea agregar el
mensaje que pide el formulario, solo significa que hasta que Holded esté conectado, las respuestas
no se van a sincronizar solas.

**Formulario "Información post venta"** (`SWmA6ppCjrTKnDE8yXuT`) — revisado, no es lo mismo:
campos de "packs elegidos, moneda/cotización, tipo de trámite, monto" — parece pensado como
**registro interno** de lo que se vendió (para Mariano/equipo, no para el cliente), con 0
submissions, nunca usado. No se pisa con nada de acá — queda anotado por si en algún momento se
quiere retomar como registro del precio real por caso (ver `comercial/CLAUDE.md` sección 14).

## 6. Textos confirmados hoy (26 sept, español neutro — "tú", no "vos", a pedido de Mariano)

### 6.1 Momento 3 — ESTANCIA (ya cargado en el clon)

> {WA#1} Para ir avanzando con tu expediente, necesito 4 cositas de tu parte:
>
> 1️⃣ Elige tu curso — ya vimos las opciones en la llamada. Cuéntame cuál eliges (Opción 1, 2 o 3) y
> te paso el contacto directo de la escuela, o te ayudo yo mismo con la inscripción.
>
> 2️⃣ Seguro de salud — completa este formulario para que te contactemos con las opciones:
> https://link.apisystem.tech/widget/form/AsJhK7rdZoR9u4mLa42L
>
> 3️⃣ Certificado médico — completa este otro para coordinar tu videollamada con el médico:
> https://link.apisystem.tech/widget/form/cEDEfPmUek1rjyO4dGEM
>
> 4️⃣ Datos de facturación — para emitirte la factura, completa aquí: [link real del formulario
> "Datos de facturación", ya pegado en el clon]
>
> Cualquier duda con cualquiera de los 4 puntos, escríbeme 💙

### 6.2 Momento 3 — VISADO ARG / VISADO LATAM (sin médico — a cargar)

> {WA#1} Para ir avanzando con tu visado, necesito 3 cositas de tu parte:
>
> 1️⃣ Elige tu curso — ya vimos las opciones en la llamada. Cuéntame cuál eliges (Opción 1, 2 o 3) y
> te paso el contacto directo de la escuela, o te ayudo yo mismo con la inscripción.
>
> 2️⃣ Seguro de salud — completa este formulario para que te contactemos con las opciones:
> https://link.apisystem.tech/widget/form/AsJhK7rdZoR9u4mLa42L
>
> 3️⃣ Datos de facturación — para emitirte la factura, completa aquí: [link del formulario "Datos de
> facturación"]
>
> Cualquier duda con cualquiera de los 3 puntos, escríbeme 💙

### 6.3 Momento único — CUENTA PROPIA/AJENA (sin seguro, médico ni curso — a cargar)

> {WA#1} Para seguir avanzando con tu trámite, solo me falta un dato de tu parte: tus datos de
> facturación, para poder emitirte la factura correspondiente. Completa aquí: [link del formulario
> "Datos de facturación"]
>
> Cualquier duda, escríbeme 💙

## 7. Colaboradores/proveedores por trámite — confirmado 26 sept 2026

**Carolina Chapo ya no colabora con GOTIR** — hay que sacarla de todas partes (workflows, este
documento, `comercial/CLAUDE.md`). Quedaba hardcodeada como Proveedor default en la rama ESTANCIA
(ver sección 4) — ya corregida ahí. Falta revisar si aparece en otro lado (formulario "Trámites
derivados a Carolina Chapo", workflow "Carolina Chapo - tramites" — ver `comercial/CLAUDE.md`
secciones 5.3/5.5/5.7, no tocado hoy).

Mapa de reemplazo, confirmado por Mariano:
- **Estancia** → **María García Serrano**.
- **Cuenta Propia / Cuenta Ajena** → arranca Mariano, lo continúa y cierra **Sebastián Sánchez
  Lorente**. Campo Proveedor = Sebastián directo (no se deja en blanco).
- **Visado Argentina** → **Gisela Justribó** (salvo excepciones que Mariano deriva a Wilmen).
- **Visado LATAM** → **Wilmen Mendoza**.

**Sobre la regla de ocultar el valor real** (`comercial/CLAUDE.md` sección 14): aplica solo a
colaboradores con cuenta de usuario en GHL. **Wilmen y Sebastián Sánchez Lorente NO tienen cuenta**
(confirmado por Mariano — "no son muy amigos de la tecnología") — para Visado LATAM y Cuenta
Propia/Ajena se puede cargar el valor real sin riesgo. Gisela y María García Serrano sí tienen
cuenta — sigue aplicando el placeholder ahí.

## 8. Requisitos reales por tipo de trámite — confirmado 26 sept 2026

Regla dada por Mariano, aplicada a los textos de la sección 6:
- **Visados, Renovaciones y Modificaciones a residencia (Cuenta propia o Cuenta ajena) — NO
  requieren certificado médico.**
- **Visados, Estancias y Renovaciones — SÍ requieren seguro de salud.** Las modificaciones a
  residencia (Cuenta propia/ajena) **NO requieren seguro**.
- Estancia es la única que lleva ambos (seguro y médico) — no está en ninguna lista de excepción.

## 9. Guion para el video de la plataforma (a grabar) — sigue pendiente

Sin cambios respecto a la versión anterior — Mariano no llegó a grabarlo hoy. Estructura sugerida,
~3-5 minutos:

1. **Qué es**: la plataforma (`https://uttdf7grgmbznkerppnm.app.clientclub.net/`) es donde va a
   vivir todo tu expediente — requisitos, instructivos paso a paso, y el lugar donde subís tu
   documentación para que el abogado la revise.
2. **Cómo entrar**: mostrar en pantalla el link, aclarar que llega por email, y que si nunca puso
   contraseña usa "olvidé mi contraseña" para crear la propia.
3. **Qué va a encontrar adentro**: portal del cliente, sección de cursos/instructivos, certificado.
4. **Cómo subir documentación**: mostrar en pantalla dónde y cómo se sube cada requisito.
5. **Qué pasa después de subir un documento**: el abogado lo revisa, aprueba o pide corrección —
   aclarar que no es instantáneo.
6. **Cierre**: a quién contactar si algo no funciona o tiene dudas.

## 10. Qué falta, resumen honesto (26 sept 2026)

1. **Grabar el video** (sección 9) — sin esto, el mensaje de plataforma queda solo en texto (que ya
   funciona razonablemente bien, no es un bloqueante duro).
2. **Probar y publicar el clon** — rama ESTANCIA lista, falta testear con "Probar flujo de trabajo"
   y decidir el corte (rename del viejo a OLD + Borrador, publicar el clon).
3. **Replicar la corrección en VISADO ARG y VISADO LATAM** (sección 4, punto 2).
4. **Construir CUENTA PROPIA desde cero** (sección 4.1).
5. **Diseño condicional completo** (sección 2.1) — pospuesto a propósito, spec ya documentada.
6. **Sacar a Carolina Chapo de todos lados** — solo se corrigió el default de ESTANCIA hoy, falta
   revisar el resto de lo que la menciona (sección 7).
7. Confirmar si "Primer contacto SI/NO" (Borrador, sin publicar) debe terminar de construirse — los
   links del Internal Notification final ya apuntan ahí (`landing.gotir.es/PrimercontactoSI/NO`).
