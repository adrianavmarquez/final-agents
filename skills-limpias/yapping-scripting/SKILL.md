---
name: yapping-scripting
description: >
  Workflow interactivo de guionización para @adrianavmarquez. Usar SIEMPRE que Adri pida trabajar en un guión, guionizar una idea, corregir un script, hacer el yapping on script, o diga frases como "vamos a guionizar", "corrige mi guión", "ayúdame con este draft", "quiero guionizar esta idea", "hazme las instrucciones de scripting", o cualquier variación.

  Esta skill NO solo genera un doc, ejecuta un proceso completo de 5 pasos: estudia perfiles reales, acumula aperturas en una base de datos, revisa el guión con criterio editorial, mapea el ritmo y respiración del script, y aplica un límite estricto de 5 rondas de revisión. Activar ante cualquier solicitud de scripting o guionización.
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

> **Frontera.** Este es el workflow de guionización para hablar a cámara con revisión editorial en 5 rondas y mapa de ritmo. Si la pieza es voz en off sobre b-roll con tabla de audio y visual en paralelo, es `voiceover-scripting`, no este.

# Yapping on Script. Workflow Interactivo de Guionización

## Qué hace esta skill

Ejecuta un proceso de guionización de 5 pasos basado en el método de Tom Boyd, adaptado al **proceso de escritura** (no de cámara). Cada sesión estudia perfiles reales, acumula aperturas en una base de datos creciente, revisa el guión con criterio editorial, mapea pausas y ritmo, y limita las rondas de revisión a un máximo de 5.

---

## EL WORKFLOW. 5 PASOS EN ORDEN

### PASO 1. Estudio de perfiles pequeños

**Antes de tocar el guión, pedir esto:**

> "Para empezar, necesito que me des los links de 5 perfiles de creadores pequeños (menos de 10K seguidores) que te parezcan buenos. Pueden ser de cualquier plataforma. Voy a analizar sus mejores videos para extraer patrones de apertura."

Esperar a que Adri entregue los 5 links. No continuar sin ellos.

Una vez recibidos:
- Usar `web_search` o `web_fetch` para acceder a cada perfil
- Identificar los 2-3 videos con más engagement de cada perfil (outliers)
- Para cada video best-performing, extraer:
  - Las primeras 2-3 líneas del guion / lo que dicen en los primeros 3 segundos
  - El tipo de hook usado (Confesión / Afirmación Bold / Pregunta / Contraste / Curiosidad)
  - La promesa implícita de esa apertura
  - Si el ritmo es rápido, pausado, o variable

Presentar el análisis en formato conversacional, no como lista técnica.

---

### PASO 2. Agregar aperturas a la base de datos acumulativa

**Despues de cada sesion de analisis, guardar las aperturas extraidas usando `memory_user_edits`.**

Formato a guardar por cada apertura:
```
[APERTURA DB] Perfil: @handle | Hook type: X | Apertura: "texto exacto o parafrasis" | Promesa: que prometio | Plataforma: IG/TT/YT | Fecha: YYYY-MM
```

Antes de guardar, hacer `memory_user_edits command=view` para revisar si ya existe ese perfil o apertura. No duplicar.

Al inicio de cada nueva sesion de guionizacion, hacer `memory_user_edits command=view` y recuperar todas las entradas `[APERTURA DB]` para tenerlas como contexto de referencia activo.

**La base de datos crece con cada sesion. Ese es el punto.**

---

### PASO 3. Revision del guion con criterio editorial

Adri entrega su guion o draft de idea. Aplicar las 3 preguntas en este orden:

**3A. tiene punto de vista?**
Preguntarse: si alguien leyera esto sin saber quien es Adri, sabria exactamente en que cree? Si no es claro, senalarlo antes de cualquier correccion:

> "Antes de corregir nada: no me queda claro cual es tu creencia central en este guion. Puedes decirla en una sola oracion?"

No continuar con la revision hasta tener el POV definido.

**3B. La apertura pasa el filtro de la base de datos?**
Comparar la apertura del guion de Adri contra las aperturas guardadas en `[APERTURA DB]`. Usa alguno de los patrones que han demostrado funcionar? Si no, sugerir una alternativa basada en los patrones coleccionados.

**3C. Correccion del guion**
Con el POV confirmado y la apertura revisada, hacer la correccion completa. Respetar la voz de Adri al 100%: no suavizar, no formalizar, no quitar Spanglish, no quitar expresiones propias. Su phrasing original es sagrado.

---

### PASO 4. Mapa de ritmo y respiracion

Despues de entregar el guion corregido, siempre incluir un **mapa de ritmo** en este formato:

```
MAPA DE RITMO, [titulo del video]

[APERTURA - rapido]
Linea 1: "..." -> velocidad alta, tono directo
Linea 2: "..." -> mantener ritmo

[PAUSA 1, aqui respira el video]
Linea 3: "..." -> bajar tono, dejar que aterrice

[DESARROLLO - variable]
Linea 4-6: ritmo medio, construyendo
-> pausa natural despues de "..."

[PAUSA 2, momento de conexion]
Linea 7: "..." -> tono intimo, mas lento

[CIERRE - sube]
Linea 8-9: acelera hacia el CTA
Linea 10: "..." -> punto final, tono firme
```

Explicar brevemente por que esas pausas van ahi y que logran emocionalmente.

---

### PASO 5. Limite de revisiones

**Llevar un contador de revisiones en cada sesion.** Cada vez que Adri pida un cambio al guion, incrementar el contador y mencionarlo:

> "Revision 2 de 5."

Al llegar a revision 5, entregar esa version y decir:

> "Esta es tu revision 5 de 5. El guion esta listo. Publicar es parte del proceso, los datos del video te dicen el resto. No hay revision 6."

**No hacer una sexta revision bajo ninguna circunstancia.** Si Adri insiste, recordarle la regla y redirigir:

> "El limite de 5 revisiones existe exactamente para este momento. El perfeccionismo es el enemigo del volumen. Publica este, y el siguiente guion lo hacemos mejor con los datos de este."

---

## Base de datos de aperturas, inicio de sesion

Al inicio de cada sesion, recuperar entradas `[APERTURA DB]` de memoria y presentar un resumen antes de empezar:

> "Tengo [N] aperturas en tu base de datos de [X] perfiles. Los tipos de hook mas repetidos son: [lista]. Voy a tenerlos en cuenta al revisar tu guion."

Si no hay entradas aun (primera sesion), decir que se empieza desde cero hoy.

---

## Las 5 instrucciones canonicas (referencia interna)

| # | Titulo | Pregunta de cierre |
|---|--------|--------------------|
| 01 | Estudia guiones de creadores pequenos | Cual es la estructura de su guion? Como abre, como desarrolla, como cierra? |
| 02 | Colecciona aperturas que funcionan | Que tipo de apertura usaron? Que promesa hicieron en esa primera linea? |
| 03 | Aplica la prueba "Yo creo" | Cual es la creencia central de este video? La puedo decir en una sola oracion? |
| 04 | Analiza el ritmo, no solo las palabras | Donde van las pausas? Donde el guion respira? Como varian las longitudes de oracion? |
| 05 | Volumen primero, perfeccion despues | Ya escribi el guion o todavia lo estoy perfeccionando mentalmente? |

---

## Generar el doc de referencia (.docx)

Si Adri pide el documento fisico de instrucciones (no el workflow, sino el doc de marca para compartir), generarlo con estas specs:

```
COLORES: RED='D72323' | BLUE='3846C4' | YELLOW='FFBA35' | BLACK='000000' | WHITE='FFFFFF'
FUENTE: Poppins
PAGINA: US Letter (12240 x 15840 DXA), margenes 1080 DXA
```

Estructura del doc:
- Bloque titulo rojo: YAPPING ON SCRIPT (blanco bold 48pt)
- Subtitulo negro: italic amarillo 20pt
- Intro: 2 parrafos
- Header azul: LAS 5 INSTRUCCIONES
- Tabla editorial: header negro/amarillo | col izq azul (numero + titulo + subtitulo) | col der blanco (cuerpo + Preguntate: en rojo)
- Header azul: PRINCIPIO GUIA
- Footer rojo alineado derecha: adrianavmarquez.com @adrianavmarquez

Reglas tecnicas: nunca bullets unicode, ShadingType.CLEAR siempre, DXA en todas las tablas, sin tildes en strings JS.

Guardar en `/mnt/user-data/outputs/yapping_on_script.docx` y usar `present_files`.

---

## Principio guia

El guion que funciona no es el mas bonito. Es el que mas se parece a como realmente hablas. Escribe con ritmo. Escribe con punto de vista. Escribe en volumen. Los datos te dicen el resto.
