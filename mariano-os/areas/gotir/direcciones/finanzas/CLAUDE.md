# GOTIR — Finanzas (CLAUDE.md)

> Primer documento real de esta dirección, creado el 17 de agosto de 2026 a partir de la situación
> financiera real que Mariano compartió ese día (deudas pendientes y necesidad de caja operativa).
> Antes de esto la dirección no tenía `CLAUDE.md` propio — el contexto de la app "GOTIR Finanzas"
> vivía disperso en `areas/gotir/CLAUDE.md`, sección "Contexto operativo adicional"; se traslada acá.

---

## 0. Quién es quién

- **Mariano**: único responsable de finanzas de GOTIR, igual que del resto de las áreas — lleva todo
  él solo.

## 1. Situación financiera actual — deudas pendientes (registrado 17 agosto 2026)

Mariano fue explícito en que GOTIR está pasando un momento financiero ajustado (es también la razón
del descuento que le hizo Exxo ese mes — ver `direcciones/marketing/CLAUDE.md`). Deudas reales
pendientes al 17 de agosto, tal como las dio, **sin convertir monedas ni sumarlas por mi cuenta**
(son monedas distintas — EUR, USD, ARS — no comparables directamente sin un tipo de cambio real):

- **Sabrina Navarro** — **350 EUR**, sueldo de julio 2026. Instrucción específica de Mariano: este
  pago **no se le hace a ella directamente** — hay que pagarlo **al dueño del departamento donde
  ella alquila** (pago dirigido, no un depósito a su cuenta). ⚠️ Nota de contexto: el `CLAUDE.md`
  raíz registra que "Sabrina ya no trabaja en GOTIR", pero acá se le debe sueldo de julio — no se
  resuelve la aparente tensión por mi cuenta, puede ser un pago retroactivo de cuando todavía
  colaboraba parcialmente; no asumir. Ver también `direcciones/comercial/CLAUDE.md` sección 5.2
  para el contexto personal (se trata con discreción).
- **Exxo Studio** — **USD 237**, saldo pendiente del plan de agosto (de un total de USD 517, se
  pagaron USD 280 — ver `direcciones/marketing/CLAUDE.md` sección 1 para el detalle completo).
- **Matías Macho** (cliente) — **140.000 ARS**. Mariano lo mencionó como "un cliente" al que le debe
  este monto — **no se especificó el motivo** (¿reembolso, comisión, pago de más?). No asumir, solo
  dejar registrado que es una deuda de GOTIR hacia un cliente, no al revés.
- **Micol Navarro** — **406.000 ARS**. Es una cuota de una deuda que **Sabrina** está pagando (a
  Micol, que es su hermana), y esa cuota **cuenta como parte del sueldo de julio que Mariano le debe
  a Sabrina** — es decir, en vez de pagarle esa porción del sueldo directamente a Sabrina, se le paga
  a Micol para cubrir la cuota de la deuda de Sabrina con ella. Estructura de pago dirigido, igual
  que con lo del departamento arriba.

### Necesidad de caja operativa (no es una deuda, es un requerimiento activo)
- Mariano necesita tener **dinero en pesos argentinos disponible en su cuenta de MercadoPago** para
  pagar las **Ads de la campaña activa de estancias por estudios** (la campaña de agosto que armó
  Exxo — ver `direcciones/marketing/CLAUDE.md` secciones 2 y 3). Sin monto específico dado todavía —
  es una necesidad recurrente mientras la campaña esté activa, no un pago puntual.

## 2. Cómo comportarte en esta área

- No convertir ni sumar montos en distintas monedas por cuenta propia — presentarlos tal como
  Mariano los dio, con su moneda original, salvo que él pida explícitamente una conversión.
- No asumir motivos, fechas de pago ni prioridad entre las deudas que Mariano no haya dado — son
  datos reales parciales, no una lista completa y cerrada de la situación financiera de GOTIR.
- Cualquier pago real (a Sabrina/su casero, a Exxo, a Matías Macho, a Micol) requiere confirmación
  explícita antes de ejecutarse por cualquier canal — ver "Regla de creación/escritura" en
  `CLAUDE.md` raíz. Hoy este sistema no tiene ninguna herramienta conectada para ejecutar pagos
  (Holded sigue sin conectar — ver `CLAUDE.md` raíz), así que por ahora esto es solo registro, no
  ejecución.
- Temas de sueldo y deuda personal de Sabrina son sensibles — tratarlos con la misma discreción que
  Mariano les daría él mismo, sin exponerlos innecesariamente fuera de este documento.

## 3. Contexto operativo (trasladado desde `areas/gotir/CLAUDE.md` el 17 agosto 2026)

### GOTIR Finanzas (app interna)
- App web de gestión financiera a medida que cubre finanzas de la empresa y personales.
- Desplegada en un VPS de Contabo.
- Construida en React puro + Node.js + SQLite.
- Usa un sistema de 5 fases/buckets, tracking de ventas, fondos de emergencia, control de
  presupuesto personal, y seguimiento de diezmo.
- Una segunda app ("Panel de KPIs") también está desplegada en el mismo servidor — hecha por
  Sabrina con Claude Code; para mantenerla actualizada hay que subir el código y la aplicación al
  VPS.
- **Pendiente real**: no está conectada a `mariano-os` todavía — las deudas de la sección 1 se
  registraron acá manualmente porque Mariano las contó por chat, no porque este sistema haya leído
  la app en vivo. Candidata a ser la fuente operativa real de esta dirección si se conecta en algún
  momento.
