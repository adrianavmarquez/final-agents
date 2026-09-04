---
name: text-screen-scripting
description: >
  Guionización de videos de texto en pantalla para el creador. Activar SIEMPRE que el creador diga "hazme un text screen", "quiero hacer un video solo con texto", "oracle loop", "frase en pantalla", "texto sobre video", o cualquier variación. También activar cuando el Ecosystem Architect defina una backbone semanal con formato text-screen y el creador quiera ejecutarla.

  Este skill es ingeniería de atención pura. No es un video con texto: es una experiencia de lectura bajo presión estética. Usa la fórmula de timing del Efecto Zeigarnik para calcular la duración exacta del clip, elige la dirección de arte según el peso emocional de la frase, y produce un deep caption que cambia de registro del video: de poético a quirúrgico. La frase es el único elemento visual. Tiene que ser suficientemente buena para sostenerse sola.
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

# Text Screen Scripting. The Oracle Loop

## Qué hace este skill

Produce un video donde la frase es el único protagonista visual. No hay voiceover, no hay presentador, no hay contexto hablado. Solo texto sobre imagen. Eso significa que la frase tiene que poder sostenerse completamente sola, y que el deep caption tiene que cambiar de registro completamente: el video hace el trabajo estético, el caption hace el trabajo de autoridad.

La ingeniería de atención de este formato descansa en el Efecto Zeigarnik: el cerebro humano odia las tareas inacabadas. Si el video termina cuando el usuario va por la última palabra, el cerebro necesita volver a verlo para cerrar el ciclo. Cada repetición suma tiempo de visualización al algoritmo. El loop no es estético: es una trampa psicológica calculada.

---

## FASE 1. LA DECLARACIÓN

### La frase es el formato

Antes del timing, antes de la dirección de arte, antes del caption: la frase tiene que estar lista y tiene que ser suficientemente buena. Un texto mediocre con timing perfecto sigue siendo mediocre.

**Criterio de calidad de la frase:**

La frase tiene que pasar los tres filtros en orden. Si falla uno, reescribir antes de continuar.

**Filtro 1, ¿Es una verdad que incomoda?**
Una frase de texto en pantalla no puede ser inspiracional genérica. Tiene que decir algo que el espectador reconoce como verdad pero que nadie había dicho exactamente así. Si la frase podría aparecer en un poster motivacional de aeropuerto, no sirve.

Señal de frase débil: "El éxito requiere consistencia y dedicación."
Señal de frase fuerte: "Tu mayor ventaja competitiva no es tu talento. Es tu capacidad de ser insoportablemente consistente cuando nadie te está mirando."

**Filtro 2, ¿Termina en su palabra más densa?**
El Efecto Zeigarnik funciona mejor cuando la palabra más pesada de la frase es la última. El cerebro cierra el ciclo en la palabra con mayor carga semántica o emocional. Si esa palabra está en el medio, el loop es más débil.

Estructura débil: "La consistencia cuando nadie mira es tu mayor ventaja."
(La palabra más densa, "ventaja", está cerca del final pero el cierre es neutro.)

Estructura fuerte: "Tu mayor ventaja competitiva no es el talento. Es quién eres cuando nadie mira."
(El cierre es "nadie mira", deja al espectador con una imagen, no con una conclusión.)

Regla de construcción: escribir la frase hacia su final. La última palabra o las últimas tres palabras tienen que ser las que más pesan. Reordenar si hace falta.

**Filtro 3, ¿Conecta con el POV base de la marca?**
Una frase de texto en pantalla es la forma más concentrada de posicionamiento que existe. Si no deriva de alguna capa del POV, es contenido flotante sin raíz de identidad. Verificar antes de continuar.

---

### Cálculo de timing. La Fórmula del Hachazo Inconcluso

Con la frase aprobada, calcular la duración exacta del clip:

```
T_total = (W / 2.8) - 0.65 segundos

Donde:
W    = número de palabras de la frase
2.8  = palabras por segundo de lectura cómoda en móvil
0.65 = el "robo" de tiempo que fuerza el loop
```

**Ejemplo de cálculo:**
Frase de 20 palabras: (20 / 2.8) - 0.65 = 7.14 - 0.65 = **6.49 segundos**

El clip se corta exactamente en ese segundo. No antes (el usuario puede cerrar el loop sin repetir), no después (el ciclo cierra completamente y el loop pierde fuerza).

**Tabla de referencia rápida:**

```
PALABRAS    DURACIÓN DEL CLIP
────────────────────────────────
8 palabras  2.20 segundos
10 palabras 2.92 segundos
12 palabras 3.63 segundos
15 palabras 4.70 segundos
18 palabras 5.77 segundos
20 palabras 6.49 segundos
22 palabras 7.20 segundos
25 palabras 8.27 segundos
28 palabras 9.34 segundos
```

Frases de menos de 8 palabras: el loop es demasiado corto para que el cerebro registre la lectura. Ampliar la frase o cambiar de formato.

Frases de más de 28 palabras: el loop es demasiado largo. El usuario cierra el ciclo cómodamente y no necesita repetir. Dividir en dos frases o cambiar a voiceover.

---

## FASE 2. DIRECCIÓN DE ARTE

Tres dimensiones visuales según el peso emocional y el tipo de frase. No son intercambiables.

---

### DIMENSIÓN 1. Multi-Shot Montage

**Cuándo usar:** Frases cortas (8-15 palabras), rítmicas o irónicas. La ironía necesita movimiento visual para que el contraste entre texto e imagen funcione. Las frases rítmicas se potencian con cortes en el ritmo del texto.

**Estructura:** 4 a 5 clips de 1 a 1.5 segundos cada uno. Cortes secos, sin transición. La secuencia de clips tiene que contar una historia visual pequeña que existe independientemente del texto.

**Principio de selección de clips:** Los clips no ilustran la frase. Son una realidad paralela que convive con el texto. El espectador procesa el texto y los clips simultáneamente, creando una tercera lectura que ninguno de los dos produce solo.

**Formato de entrega:**
```
MULTI-SHOT MONTAGE, [N] clips de [X] segundos

Clip 1: [descripción específica, qué se ve, qué plano, qué mood]
Clip 2: [descripción]
Clip 3: [descripción]
Clip 4: [descripción]
Clip 5: [descripción, si aplica]

Orden narrativo visual: [por qué esta secuencia crea una historia]
Punto de corte del loop: [en qué clip y en qué segundo termina el clip final]
```

---

### DIMENSIÓN 2. Atmospheric Continuous

**Cuándo usar:** Frases densas (15-28 palabras), filosóficas o de "hachazo". El clip continuo crea un estado mental de trance que prepara al espectador para absorber una frase de mayor peso semántico.

**Estructura:** 1 solo clip de la duración calculada. Movimiento sutil o cámara lenta. El elemento que se mueve tiene que ser natural (humo, luz, agua, viento, vapor) o un movimiento humano pausado (manos, cabello, respiración visible).

**Principio de selección de clip:** El movimiento del clip tiene que tener el mismo ritmo emocional que la frase. Una frase sobre urgencia no va sobre agua quieta. Una frase sobre proceso lento no va sobre humo que sube rápido.

**Formato de entrega:**
```
ATMOSPHERIC CONTINUOUS, [X] segundos

Elemento en movimiento: [qué se mueve y cómo]
Velocidad del clip: [en tiempo real / 50% velocidad / cámara lenta extrema]
Punto de inicio: [dónde empieza el clip para que el movimiento sea continuo]
Punto de corte: [dónde termina para que el loop se sienta natural]
Mood buscado: [íntimo / expansivo / urgente / quieto / melancólico]
```

---

### DIMENSIÓN 3. Subversive Contrast

**Cuándo usar:** Frases que contradicen o desmontan algo. El clip muestra exactamente lo que la frase está desmontando. La contradicción entre lo que se ve y lo que se lee es el mensaje. Es la dimensión de ironía y crítica.

**Estructura:** Puede ser un clip continuo o un montaje corto. Lo que define esta dimensión no es el número de clips sino la relación de contradicción explícita entre imagen y texto.

**Principio:** El clip tiene que mostrar algo aspiracional, exitoso o "correcto" según el consenso de la industria. El texto lo desmonta. La tensión entre los dos es lo que hace que el espectador se detenga.

**Ejemplo:** Clip de un feed de Instagram perfectamente curado y estético. Frase: "El contenido más bonito de tu nicho probablemente no está vendiendo nada." El contraste es el hook.

**Formato de entrega:**
```
SUBVERSIVE CONTRAST

Clip: [qué se ve, el elemento "aspiracional" o "correcto"]
Por qué este clip específico: [qué representa que la frase va a desmontar]
Relación texto-imagen: [cómo exactamente se contradicen]
Intensidad del contraste: [sutil / medio / explícito]
```

---

### Posición del texto en pantalla

La tipografía va en el tercio superior o inferior. Nunca en el centro. El centro compite con el visual. El tercio superior o inferior respira.

```
REGLA DE POSICIÓN

Frase de 1 línea:    Tercio inferior, deja el visual como protagonista
Frase de 2 líneas:   Tercio superior, el texto lidera, el visual suporta
Frase de 3+ líneas:  Dividir en dos frases o cambiar de formato

Tipografía: Minimalista. Sin serif en pantalla de móvil.
            Sin hashtags dentro del video.
            Sin emojis dentro del video.
            Color: blanco sobre oscuro o negro sobre claro.
            Nunca color sobre color.
```

---

## FASE 3. THE DEEP CAPTION

### El cambio de registro es obligatorio

El video hace el trabajo estético. El caption hace el trabajo de autoridad. Son registros completamente distintos y no pueden sonar igual.

El error más común: escribir un caption que imita el tono poético de la frase. Eso produce redundancia. El espectador que leyó la frase ya tiene el vibe. El caption tiene que darle algo que el video no puede dar: contexto, argumento, evidencia, consecuencia.

El caption empieza con "Lo que no te dicen de esto es que..." y no mira atrás.

---

### Los tres bloques del deep caption

**BLOQUE 1. Expansión (no repetición)**

Arranca con: "Lo que no te dicen de esto es que..."

No parafrasea la frase. Profundiza la idea que la frase solo insinúa. El espectador que terminó el video tiene una pregunta implícita: ¿y entonces? Este bloque responde esa pregunta con profundidad, no con más poesía.

Longitud: 3 a 5 líneas. Lo suficiente para que el usuario haga click en "ver más" pero no tan largo que parezca que puede leerse sin hacerlo.

**BLOQUE 2. El Insight del 20%**

Desarrolla la idea con la profundidad que el video no permite. Habla directamente al 20% que está construyendo algo real: los que están en el proceso, no los que están mirando desde afuera.

Este bloque puede tener estructura de lista si el insight tiene partes. Máximo 5 puntos si es lista. Si es prosa, máximo 150 palabras.

La señal de que este bloque está bien: si alguien lo lee sin haber visto el video, tiene valor completo. No depende del video para entenderse.

**BLOQUE 3. CTA de Culto**

No pide follow. No pide like. No lleva a una venta directa.

El CTA de culto hace que el usuario guarde el post para un momento específico de su vida. Crea un contrato emocional con el contenido.

Fórmulas disponibles:

```
CTA DE PRESERVACIÓN:
"Guárdalo para cuando el ruido exterior sea demasiado fuerte."
"Guárdalo para el día que quieras abandonar esto."
"Guárdalo para cuando dudes de que vale la pena."

CTA DE COMPARTIR ESPECÍFICO:
"Mándaselo a quien necesita escuchar esto hoy."
"Mándaselo a quien está construyendo algo solo."

CTA DE REFLEXIÓN ACTIVA:
"¿En qué parte de tu proceso estás ahora mismo?"
"¿Cuándo fue la última vez que hiciste esto cuando nadie miraba?"

CTA DE ACCESO PROFUNDO:
"Si quieres el framework completo detrás de esto, está en [plataforma]."
```

Elegir uno solo. El CTA que intenta hacer todo no hace nada.

---

### Formato completo del deep caption

```
DEEP CAPTION, [Título del text screen]

━━━ PRIMERA LÍNEA (visible antes del "ver más") ━━━
"Lo que no te dicen de esto es que..."
[completar, máx 125 caracteres para IG / 100 para TikTok]

━━━ BLOQUE 1. EXPANSIÓN ━━━
[3 a 5 líneas que profundizan sin repetir]
[Termina creando urgencia de hacer click en "ver más"]

━━━ BLOQUE 2. INSIGHT DEL 20% ━━━
[El argumento real. Específico, para quien está en el proceso.]
[Lista de máx 5 puntos o prosa de máx 150 palabras]

━━━ BLOQUE 3. CTA DE CULTO ━━━
[Una sola línea del menú de CTAs según objetivo del mes]
```

---

## ENTREGA FINAL

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TEXT SCREEN, [Título interno]
Dimensión visual: [MULTI-SHOT / ATMOSPHERIC / SUBVERSIVE]
Plataforma: [destino]
POV activado: [qué capa del posicionamiento mueve]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FRASE ON-SCREEN
"[frase aprobada]"

Filtro 1 (¿incomoda?):      [PASA / FALLA, razón]
Filtro 2 (¿termina densa?): [PASA / FALLA, razón]
Filtro 3 (¿conecta POV?):   [PASA / FALLA, capa que activa]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CÁLCULO DE TIMING
Palabras: [W]
T_total = ([W] / 2.8) - 0.65 = [resultado] segundos
Duración del clip: [resultado redondeado a .1s]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIRECCIÓN DE ARTE
[Formato según dimensión elegida]

Posición del texto: [tercio superior / tercio inferior]
Tipografía: [indicaciones mínimas de estilo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEEP CAPTION
[Tres bloques completos]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NOTA DE PRODUCCIÓN
Plataformas secundarias: [ajustes si va a más de una]
Música sugerida: [tipo de música que refuerza el mood, sin nombrar canciones específicas con copyright]
```

---

## CRITERIO DE REVISIÓN

**¿La frase pasa los tres filtros?** Si falla cualquiera, reescribir antes de calcular timing o diseñar el visual. Un texto mediocre con buena dirección de arte sigue siendo mediocre.

**¿El clip termina en el segundo calculado?** Si el timing es de 6.49 segundos y el clip dura 7, el loop se cierra y pierde fuerza. El cálculo es instrucción de edición, no sugerencia.

**¿La dimensión visual corresponde al peso emocional de la frase?** Una frase filosófica sobre Multi-Shot produce disonancia. Una frase irónica sobre Atmospheric produce pesadez. La dimensión no es preferencia estética: es decisión estratégica.

**¿El caption cambia de registro respecto al video?** Si el caption suena poético, reescribir. Tiene que sonar analítico, argumentado, como alguien que habla directamente al que está construyendo algo.

**¿El CTA pide una sola cosa?** Si hay más de un CTA, eliminar hasta quedar con uno.

**¿La primera línea del caption funciona sin el video?** Si depende de haber visto el video para tener sentido, reescribir.

---

## LÍMITE DE REVISIONES

Máximo 5 rondas. Contador explícito:

> "Revisión [N] de 5."

En revisión 5:
> "Esta es tu revisión 5 de 5. El text screen está listo para producción. El timing calculado es la única instrucción de edición que no puede ignorarse: si el clip dura más o menos de [X] segundos, el loop no funciona como fue diseñado."

---

## HANDOFF

Recibe de:
- **ecosystem-architect:** La backbone semanal con formato text-screen es el brief. El objetivo de conversión del mes determina qué CTA de culto se usa.
- **pov-finder:** La frase tiene que derivar de alguna capa del POV. El Filtro 3 lo verifica. Si no conecta, no es posicionamiento: es contenido flotante.
- **storytime-scripting / voiceover-scripting:** El cierre de un storytime o el Shift de un voiceover suelen producir la frase más densa del ciclo. Si alguna de esas piezas tiene una línea que funciona sola, es candidata directa para un text screen.

Alimenta a:
- **fast-reel-scripting:** Una frase de text screen que generó tracción puede convertirse en la frase on-screen de un fast reel de la semana siguiente, con el deep caption como base del caption extendido.
- **carousel-scripting:** La frase puede ser la Slide 09 (cheat-sheet) de un carrusel Inspirador o el A-ha Moment de un carrusel Analista.
- **ecosystem-architect (siguiente mes):** Si el text screen generó loops (tiempo de visualización alto con pocas views), ese dato entra al Paso 0 como señal de qué tipo de frase y dimensión visual retiene más.
