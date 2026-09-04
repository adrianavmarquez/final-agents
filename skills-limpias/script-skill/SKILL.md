---
name: script-skill
description: "Genera el documento oficial de script de collab de @adrianavmarquez para compartir con marcas. Usar SIEMPRE que Adri pida crear, redactar o preparar un script de collab, partnership, sponsorship o brand deal, incluyendo frases como hazme el script para X marca, prepara el doc de collab, necesito el script de X marca, arma el documento para la marca, o cualquier variación. El output es un .docx HÍBRIDO con el branding unificado de Adri: hero negro con logo, acentos handwritten horneados como imagen, tabla beat-by-beat con headers azules y letra amarilla, estrellita en el footer de cada página y texto nativo comentable. Listo para abrir en Google Docs y dejar comentarios de la marca. Hace juego visual con el skill brand-proposal-pdf: proposal en PDF para pitch, script en docx para colaboración, misma casa."
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

# Brand Script Generator, @adrianavmarquez

Genera el documento de script de collab oficial de Adri para compartir con marcas.
Output: `.docx` que se abre en Google Docs para comentarios colaborativos.

**Arquitectura híbrida (la regla de oro):** todo lo que la marca necesita comentar o editar
es TEXTO NATIVO (beats, overlays, notas). Todo lo puramente visual va HORNEADO COMO IMAGEN
PNG (logo, acentos handwritten, firma, estrellita), porque Google Docs no tiene Plunct ni
esquinas redondeadas pero renderiza imágenes pixel-perfect. Así el doc se ve como el proposal
PDF de la marca y sigue siendo 100% comentable donde importa.

**División de sistema documental:** propuestas y pricing → `brand-proposal-pdf` (PDF, pitch,
nadie tacha encima). Scripts de collab → este skill (.docx, la marca comenta beat por beat).
Ambos comparten el mismo lenguaje visual.

---

## Lo que necesitas antes de generar

| Campo | Descripción |
|---|---|
| `NOMBRE_COLLAB` | Nombre de la marca o campaña. Ej: "EMERGENT AI COLLAB" |
| `HANDLE` | Handle de Adri. Siempre: `@adrianavmarquez` (vive dentro del logo horneado) |
| `BEATS` | Lista de beats: visual + script/texto en pantalla + nota de dirección |
| `OVERLAYS` | Textos, claims, CTAs, handles y disclaimers que necesitan aprobación de la marca |
| `NOTAS_PRODUCCION` | Instrucciones técnicas y de producción para el equipo |
| `REFERENCIAS_VISUALES` | Descripciones de referencias para que la marca entienda el tono |

Siempre pregunta antes de inventar claims o nombres de producto.

---

## Estructura del documento (orden fijo, siempre igual)

1. **Hero negro full-width**: logo horneado (120px) + título del collab en blanco bold caps
   (texto nativo) + subtítulo `Script + Overlays + Producción + Ref Visuales` en gris +
   barra roja delgada debajo
2. **Script Beat by Beat**: eyebrow handwritten horneado + H2 caps + tabla 3 columnas
   (Visual / Script+Texto en pantalla / Notas de dirección), filas alternadas blanco/gris
3. **Textos para aprobación de marca**: eyebrow horneado + H2 + tabla 2 columnas
   (Tipo en bold / Contenido/Copy exacto)
4. **Notas de producción**: eyebrow horneado + H2 + bullets con "·" rojo
5. **Referencias visuales**: eyebrow horneado + H2 + bullets con "·" rojo
6. **Firma**: "un abrazo, Adriana" horneada (imagen) + ADRIANAVMARQUEZ.COM en caps espaciadas
7. **Footer de página**: estrellita 18px centrada, en TODAS las páginas (footer del docx)

---

## Estética de marca. NO negociar estos valores

```
Fuente nativa: Poppins (existe en Google Docs, siempre segura)
Handwritten:   horneada como PNG desde Caveat bold (o Plunct bold si el .ttf está instalado)

Rojo:     #D72323  → barra del hero, bullets ·, color de los acentos handwritten
Azul:     #3846C4  → fondo de headers de AMBAS tablas
Amarillo: #FFBA35  → texto de headers de AMBAS tablas, handle en el logo
Negro:    #000000  → hero band, cuerpo de texto, bordes de tabla
Blanco:   #FFFFFF  → fondo general, filas de datos
Gris:     #F5F5F5  → filas alternadas de la tabla de beats
Gris sub: #BDB6CC  → subtítulo sobre el hero negro
Muted:    #6B6677  → URL del cierre

Título hero:     24pt / bold / caps / blanco sobre negro (nativo, NO imagen: es editable)
H2 sección:      16pt / bold / caps / negro
Headers tabla:   9pt / bold / amarillo sobre azul / letter-spacing
Cuerpo y celdas: 10pt / Poppins regular
Eyebrows:        imágenes assets/eye_*.png a ~160-270px de ancho según largo del texto
Firma:           assets/firma.png a 170px
Bordes de tabla: SINGLE negro (GDocs los respeta; NO usar dashed, los convierte feo)
Bullets:         "·" en rojo bold + dos espacios
Márgenes:        0.75" lados, footer con espacio para la estrellita
Tamaño:          US Letter
```

**Prohibido en este formato:** esquinas redondeadas, bordes punteados, fondos de página,
fotos de fondo detrás de texto editable. Nada de eso sobrevive Google Docs. Si el elemento
es decorativo e imprescindible, se hornea como imagen; si no sobrevive como imagen inline,
no va.

---

## Cómo generar el documento

1. Los assets viven en `assets/`: logo_header.png, star_footer.png, firma.png,
   handle_yellow.png y los cuatro eyebrows pre-horneados (eye_beats, eye_overlays,
   eye_produccion, eye_referencias).
2. Si necesitas un acento handwritten NUEVO (una sección custom), hornéalo con PIL:
   Caveat bold desde ~/.fonts/Caveat.ttf, color #D72323, fondo transparente, render a
   ~96px de altura de fuente y muéstralo a un tercio del tamaño para que quede nítido.
3. Lee `scripts/generate_reference.js`: es la implementación completa y funcional.
   Clónalo, edita el objeto DATA del inicio con los datos del collab, y ejecuta:

```bash
cd /home/claude && node generate_mi_collab.js
```

4. Valida SIEMPRE y verifica que las imágenes entraron:

```bash
python3 /mnt/skills/public/docx/scripts/office/validate.py /mnt/user-data/outputs/[collab]_script.docx
# QA de imágenes: convertir a pdf con soffice y correr pdfimages -list
# Debe haber: logo en pág 1, eyebrows en sus secciones, firma al final, estrella en cada página
```

El output va a `/mnt/user-data/outputs/[nombre_collab]_script.docx`.

---

## Notas editoriales de voz

- El subtítulo del hero es siempre: `Script + Overlays + Producción + Ref Visuales`
- Los beats de script van en primera persona de Adri, tono conversacional, sin formalidades
- Los overlays son copy exacto listo para aprobación, nada de placeholders vagos
- Las notas de dirección son instrucciones cinematográficas concretas: ángulo, ritmo, duración
- Las referencias visuales explican el tono visual, no el contenido
- Nunca incluir fechas de entrega, honorarios ni términos contractuales, eso vive en el
  proposal (brand-proposal-pdf) o en el contrato, jamás en el script
- Cero em dashes en el contenido del documento; separadores con "·"
