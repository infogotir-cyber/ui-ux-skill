# Secuencia post-pago — GOTIR Comercial

> Creado 25 septiembre 2026, a pedido explícito de Mariano. Mismo espíritu que
> `secuencia-post-agendamiento.md` (que resuelve el tramo entre agendar y la llamada), pero para el
> tramo siguiente: **entre que el cliente paga y que arranca de verdad su trámite**. Motivo textual
> de Mariano: quiere que "apenas pagan ya tengan todo claro y no sientan que desaparecemos apenas
> pagan".

## 0. Qué ya existe (no tocar)

Dos piezas ya automatizadas, disparadas cuando una oportunidad pasa a la etapa **Pagado** (workflow
"Pago realizado- contrato", ver `CLAUDE.md` sección 10.2):
1. **Envío del contrato** — documento de firma vía sendlink.co.
2. **Envío del acceso a la plataforma** — email con el link de la plataforma y la indicación de usar
   "olvidé mi contraseña" para crear la propia (mismo patrón usado con Pamela Luján, 23-24 sept 2026).

Todo lo de abajo es **nuevo**, a sumar al mismo disparador de "Pagado" — ninguna de las piezas de
abajo reemplaza lo que ya existe, se agregan.

## 1. Principio de diseño: fragmentar, no descargar todo junto

Mismo criterio que ya rige la Fase 3 de la llamada de ventas (`CLAUDE.md` sección 2): si se manda
todo de una sola vez (contrato + plataforma + video + comunidad + seguro + médico + elegir curso +
facturación), el cliente recibe un bloque abrumador y es fácil que ignore la mitad. Se reparte en
**3 momentos**, con el mismo mecanismo de `Wait` que ya usa `secuencia-post-agendamiento.md`:

- **Momento 1 — inmediato** (junto con el contrato y el acceso a la plataforma).
- **Momento 2 — 3 horas después** (tiempo para que ya haya entrado a la plataforma una vez).
- **Momento 3 — 1 día después** (lo que no es urgente el mismo día: elegir curso, facturación).

## 2. Momento 1 — Inmediato (junto con contrato + acceso a plataforma)

Bienvenida cálida + mapa corto de lo que sigue, para que sepa que esto recién empieza, no que ya
terminó con el pago.

> ¡Bienvenido/a a GOTIR, [Nombre]! 🎉
>
> Ya tenés tu contrato y tu acceso a la plataforma en camino — en los próximos días te voy a ir
> mandando todo lo que necesitás para arrancar bien: un video corto de cómo usar la plataforma, el
> acceso a nuestra comunidad de viajeros, y los últimos datos que nos faltan de tu parte.
>
> Cualquier duda, esta es tu vía directa. ¡Vamos con todo! 🙌

## 3. Momento 2 — +3 horas: plataforma en video + Comunidad GOTIR

**Video de la plataforma — pendiente de grabar** (ver guion en la sección 5 más abajo, es lo único
de este documento que todavía no está listo para automatizar). Una vez grabado, va acá con el link.

> Para que le saques el jugo a la plataforma, grabé este video corto explicando qué vas a encontrar
> ahí, cómo entrar y cómo ir subiendo tu documentación: [LINK DEL VIDEO — pendiente]
>
> Y para que te sumes a otras personas que ya pasaron o están pasando por lo mismo que vos —
> consejos, experiencias reales, acompañamiento — te dejo el link de nuestra Comunidad GOTIR:
> https://chat.whatsapp.com/BSxDC6caz9nHFc7t4RK8LW?mode=gi_t

## 4. Momento 3 — +1 día: elegir curso, seguro, médico y facturación

Fragmentado en 4 bloques cortos dentro del mismo mensaje (o 2 mensajes separados si se prefiere
menos denso) — ninguno es urgente el mismo día del pago, por eso va al día siguiente.

> Para ir avanzando con tu expediente, necesito 4 cositas de tu parte:
>
> **1. Elegí tu curso** — ya vimos las opciones en la llamada. Contame cuál de las 3 elegís
> (Opción 1, 2 o 3) y te paso el contacto directo de la escuela para que te matricules, o te ayudo
> yo mismo con la inscripción.
>
> **2. Seguro de salud** — completá este formulario para que te contactemos con las opciones:
> https://link.apisystem.tech/widget/form/AsJhK7rdZoR9u4mLa42L
>
> **3. Certificado médico** — completá este otro para coordinar tu videollamada con el médico:
> https://link.apisystem.tech/widget/form/cEDEfPmUek1rjyO4dGEM
>
> **4. Datos de facturación** — para poder emitirte la factura correspondiente, completá acá:
> [formulario "Datos de facturación" ya existente en GHL, `YrHyk4NpBIqxf59EoH0S` — confirmar con
> Mariano si sigue siendo el que quiere usar, ver `CLAUDE.md` sección 5.3]
>
> Cualquier duda con cualquiera de los 4 puntos, escribime.

**Nota importante sobre el punto 1 (elegir curso)**: `CLAUDE.md` sección 11.2 establece que de cara
al cliente **nunca se nombra la institución específica** ("se dice Opción 1/2/3") — esta regla es
para proteger la comisión de GOTIR (evitar que el cliente vaya directo a la escuela). Esa regla
sigue vigente acá: el mensaje pide elegir por número, y Mariano revela el nombre real de la escuela
recién cuando responde en privado, no en este mensaje automático.

## 5. Guion para el video de la plataforma (a grabar)

Estructura sugerida, ~3-5 minutos, para que Mariano lo grabe cuando pueda — no es un guion palabra
por palabra, son los puntos que tiene que cubrir:

1. **Qué es**: la plataforma (`https://uttdf7grgmbznkerppnm.app.clientclub.net/`) es donde va a vivir
   todo tu expediente — requisitos, instructivos paso a paso, y el lugar donde subís tu
   documentación para que el abogado la revise.
2. **Cómo entrar**: mostrar en pantalla el link, aclarar que llega por email, y que si nunca puso
   contraseña usa "olvidé mi contraseña" para crear la propia (mismo mecanismo ya usado).
3. **Qué va a encontrar adentro**: portal del cliente, sección de cursos/instructivos, sección de
   comunidad (si aplica dentro de la plataforma, distinta de la Comunidad de WhatsApp), certificado.
4. **Cómo subir documentación**: mostrar en pantalla dónde y cómo se sube cada requisito.
5. **Qué pasa después de subir un documento**: el abogado (Sebastián/María/Gisella) lo revisa, lo
   aprueba o pide corrección — aclarar que no es instantáneo, para manejar expectativas.
6. **Cierre**: a quién contactar si algo no funciona o tiene dudas.

## 6. Qué falta para que esto quede realmente funcionando

Honesto sobre el estado real, mismo criterio que el resto del sistema — nada de esto se puede armar
por API (mismo límite ya documentado: GHL no tiene endpoint para crear/editar workflows):

1. **Grabar el video** (sección 5) — sin esto, el Momento 2 queda incompleto.
2. **Construir esto en el builder de GHL** (o en n8n, si se conecta a la Fase B de la Propuesta 4,
   `CLAUDE.md` sección 13.6) — agregar los pasos de los Momentos 1-3 al workflow "Pago realizado-
   contrato" existente, con los `Wait` correspondientes (3 horas, 1 día). Mismo tipo de trabajo
   manual que ya hizo Mariano para `secuencia-post-agendamiento.md` guiado paso a paso por captura
   de pantalla.
3. **Confirmar el formulario de facturación** — se asumió que es el ya existente
   (`YrHyk4NpBIqxf59EoH0S`, "Datos de facturación"), pero no se confirmó explícitamente con Mariano.

Hasta que el punto 2 esté armado en el builder, este procedimiento se puede seguir **manualmente**
igual que se hizo con Pamela Luján — mandando cada pieza a mano después de cada pago, en el orden y
el timing de este documento.
