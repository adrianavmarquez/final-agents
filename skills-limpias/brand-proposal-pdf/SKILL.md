---
name: brand-proposal-pdf
description: "Genera el PDF oficial de propuestas de brand partnership de @adrianavmarquez con el sistema de diseño completo de la marca. Usar SIEMPRE que Adri pida crear, armar, redactar o rediseñar una propuesta para una marca en PDF, incluyendo frases como arma la propuesta para X marca, hazme el proposal de X, necesito la propuesta en PDF, recrea el proposal, cotización formal para la marca, pricing document, o cualquier variación. También usar cuando exista un deal en negociación con precios definidos y llegue el momento de producir el documento que se envía a la marca. El output es un PDF vía HTML + WeasyPrint con hero negro full-bleed, tarjetas redondeadas con pills AS REQUESTED / RECOMMENDED, dual pricing, stat cards negras, tabla side by side, menú à la carte, estrellita en el footer de cada página y metadata interna limpia con la identidad de Adri. NO usar para scripts de collab (eso es script-skill, .docx) ni para dashboards financieros internos (eso es HTML interactivo)."
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

# Brand Proposal PDF, @adrianavmarquez

Genera el documento de propuesta comercial que se envía a marcas (Microsoft, Manychat, goodr, etc).
Output: PDF de 3 a 5 páginas, diseño completo de marca, listo para adjuntar en email.

Pipeline: HTML → WeasyPrint → PDF → scrub de metadata → QA. Nunca docx, nunca reportlab directo.

---

## Antes de generar, reúne esto (pregunta lo que falte)

| Campo | Descripción |
|---|---|
| `MARCA` | Nombre de la marca y producto (ej: Microsoft Learn, AI Skills Navigator) |
| `COMPONENTES` | Workstreams del deal, cada uno con versión "as requested" y versión "recommended" |
| `PRECIOS` | Precio por componente en ambas versiones. Nunca inventar precios: vienen de la negociación |
| `MÉTRICAS` | 3-4 stats de leverage con números reales verificados (DMs, view rate, followers) |
| `MENÚ` | Precios unitarios à la carte + add-ons modulares |
| `CONTEXTO` | Qué pidió la marca literalmente, para que "as requested" refleje su email, no una paráfrasis |

Regla de negociación que el documento implementa: el ancla es el total recomendado, el menú
à la carte es la válvula de escape para que la marca baje piezas sin que Adri baje precios unitarios.

---

## Estructura del documento (orden fijo)

1. **Hero negro full-bleed**, logo, eyebrow, título con × roja, 2 líneas de subtítulo, barra roja
2. **Intro**. 1-2 oraciones de contexto
3. **Caja de temas** (si aplica), lavanda, eyebrow handwritten, lista numerada bold, nota muted
4. **Componentes** (uno por workstream), eyebrow "component 0N" + H2 + card con dual pricing
5. **Justificación con métricas**, párrafo de leverage + banda de 4 stat cards negras
6. **Side by Side**, tabla comparativa con fila TOTAL
7. **À La Carte Menu**, precios unitarios + add-ons + nota de definición en itálica
8. **Where this can grow**. 2 párrafos de visión Q siguiente
9. **Firma**"un abrazo, Adriana" handwritten roja + footer con URL

La estrellita va en el footer de TODAS las páginas vía `@bottom-center`. El logo va SOLO en el hero.

---

## Sistema de diseño. NO negociar estos valores

### Colores
```
--black:   #000000   hero, card headers (#0e0c14 para headers de card), stat cards
--white:   #FFFFFF   fondo general
--red:     #D72323   × del título, eyebrows handwritten, precios recommended, barra del hero, firma
--lav:     #F2E9FF   caja de temas, fila TOTAL del side by side
--yellow:  #FFBA35   pill RECOMMENDED, números de stats, texto de headers de tabla, borde del bonus
--blue:    #3846C4   fondo de headers de tabla (side by side y menú)
--ink:     #15131c   texto de cuerpo
--muted:   #6b6677   notas why, subs, notas legales
--line:    #e3d9f3   bordes de cards, divisores
--cream:   #FFF6E2   banda de bonus
--darksub: #bdb6cc   subtítulos sobre fondo negro
pill gris: fondo #EDEDF2, texto #55506A
```

### Tipografía y jerarquía
```
Familia principal: Poppins (400, 600, 700, 800)
Handwritten: Plunct bold si el .ttf está disponible; si no, Caveat bold (sustituto aprobado)

H1 hero:        26pt / 800 / caps / letter-spacing -0.3px / blanco, × en rojo
H2 sección:     15pt / 800 / caps / ink
Eyebrow:        13.5pt / handwritten bold / rojo / minúsculas ("component 01", "build your own")
Eyebrow hero:   7pt / 600 / caps / letter-spacing 3.5px / darksub
Body:           9.5pt / 400 / line-height 1.5-1.55
Why-notes:      8pt / muted, con "Why:" en bold
Precios card:   12pt / 800, rojo si es recommended, ink si es as-requested
Precio TOTAL:   11pt / 800 en la fila lavanda, recommended en rojo
Pills:          6.5pt / 700 / letter-spacing 0.8px / caps
Headers tabla:  7pt / 700 / letter-spacing 1.5px / amarillo sobre azul
Stats grandes:  16pt / 800 / amarillo
Stats labels:   6pt / 700 / letter-spacing 1.2px / blanco / caps
Firma:          19pt / handwritten bold / rojo
URL footer:     7pt / 600 / letter-spacing 3px / muted / caps
```

### Componentes

**Card de componente:** border 1px line, radius 14px, overflow hidden, `page-break-inside: avoid`.
Header fondo #0e0c14 con título blanco 800 y subtítulo darksub 7.5pt separado por " · ".
Filas divididas con `border-bottom: 1px dashed var(--line)`. Cada fila es una tabla de 3 celdas:
pill (98px) | descripción | precio (70px, right). Banda bonus opcional al final: fondo cream,
border-left 4px amarillo, 8pt.

**Pills:** radius 20px, padding 3px 9px. AS REQUESTED = gris. RECOMMENDED = amarilla.
La fila recommended lleva la descripción principal en bold + nota "Why:" en 8pt muted.

**Stat cards:** tabla con `border-spacing: 8px 0`, celdas negras radius 12px, 25% cada una,
número amarillo arriba, label blanca caps abajo con `<br>` para dos líneas.

**Side by Side:** header azul con texto amarillo espaciado, filas con border line,
primera columna con nombre bold + sub muted, columnas de datos centradas,
fila TOTAL con fondo lavanda, recommended en rojo.

**Menú:** misma tabla, headers de sección azul/amarillo intercalados entre grupos de filas,
precios right bold. Después del menú siempre va la nota en itálica 8pt definiendo términos
técnicos del pricing (ej: qué significa "format execution").

### Reglas de copy dentro del documento
- Cero em dashes. Separadores con " · " (punto medio) o comas.
- Dual pricing siempre: "as requested" refleja literalmente lo que la marca pidió,
  "recommended" es el upsell con su "Why:" justificado en beneficio de la marca, no de Adri.
- Los totales viven en el documento, nunca en el email de envío.
- La pieza de métricas justifica el único componente donde se propone MÁS de lo pedido.
- Cierre siempre deja puerta a Q siguiente + "ready to move straight into production".

---

## Cómo generar

1. Lee `assets/template_reference.html`: es la propuesta Microsoft Q3 completa y funcional.
   Clónala y reemplaza contenido manteniendo clases y estructura CSS intactas.
2. Copia `assets/star_footer.png` y `assets/logo_header.png` al directorio de trabajo.
   Si Adri sube un logo nuevo, redimensiona: logo máx 420px ancho, estrella 26px.
3. Ejecuta el build:

```bash
python3 skills/brand-proposal-pdf/scripts/build_pdf.py mi_propuesta.html "Titulo Del Documento" /mnt/user-data/outputs/Nombre_Propuesta.pdf
```

El script instala Poppins y Caveat si faltan, renderiza con WeasyPrint, limpia la metadata
(Author y Creator: Adriana V. Marquez, Producer: adrianavmarquez.com) y corre el QA.

## QA obligatorio antes de entregar (el script lo automatiza, verifica su output)

1. **Espaciado de palabras:** extraer texto y confirmar que no hay palabras fusionadas
   ("isthe", "buildsanticipation"). Si aparecen, el render de fuentes falló.
2. **Paginación:** revisar qué arranca cada página con pdftotext por página. La página 1
   lleva margen 0 (hero bleed), las demás margen superior 42px. PROHIBIDO footer huérfano:
   la firma + footer van envueltos en un div con `page-break-inside: avoid` junto a la
   sección de cierre.
3. **Imágenes:** pdfimages -list debe mostrar el logo solo en página 1 y la estrella en
   todas las páginas. Peso total del PDF menor a 300KB (comprimir imágenes si no).
4. **Metadata:** pdfinfo debe mostrar la identidad de Adri, nunca el nombre del motor.
5. **Cálculos:** verificar con bash que cada subtotal y el total suman exacto antes de
   escribir el HTML. Un precio mal sumado mata la credibilidad de toda la propuesta.
