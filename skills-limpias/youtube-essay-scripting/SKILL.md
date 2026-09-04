---
name: youtube-essay-scripting
description: >
  Guionización de YouTube essays para el creador. Activar SIEMPRE que el creador diga "vamos a hacer un essay de YouTube", "quiero grabar un monólogo largo", "youtube essay sobre [tema]", "quiero hablar a fondo de [tema/dilema/acontecimiento]", "tengo algo que decir sobre [tema]", o cualquier variación. También activar cuando el Ecosystem Architect defina el essay mensual del YouTube y el creador quiera ejecutarlo.

  Este skill produce el ancla de autoridad del mes. No es un video instructivo ni un tutorial. Es un manifiesto en movimiento: la ventana abierta a los dilemas, monólogos internos y opiniones viscerales del creador sobre el mundo, la industria, la vida. Output mixto: apertura y cierre guionizados, cuerpo en bullets de tensiones e ideas. El lenguaje del cuerpo lo improvisa el creador al grabar. 10 a 20 minutos. Un punto de entrada desde tres tipos de activación distintos.
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

> **Frontera.** Este es el essay visceral: apertura y cierre guionizados, cuerpo en bullets de tensiones, monólogo interno, 10 a 20 minutos, lenguaje improvisado al grabar. Si el pedido trae b-roll curado, referencias visuales y música como parte del argumento, es `youtube-video-essay-scripting`, no este.

# YouTube Essay Scripting. The Visceral Monologue

## Qué hace este skill

Produce el script del essay mensual de YouTube. No es un argumento académico con tesis y evidencia. Es un monólogo interno sacado afuera: filosofía de vida en tiempo real, opinión sin filtro sobre lo que está pasando en la industria o en el mundo, o un dilema que todavía no tiene resolución.

La diferencia con el talking head es de fondo, no de largo:

```
TALKING HEAD                        YOUTUBE ESSAY
────────────────────────────────────────────────────────
El tema es el pretexto.             El tema es el territorio.
Muestra un cerebro pensando.        Habita un dilema o defiende
                                    una posición visceralmente.
Tiene tensión dialéctica            Tiene tensión filosófica:
entre dos ángulos internos.         entre cómo son las cosas
                                    y cómo deberían ser.
El espectador sigue                 El espectador sigue porque
la tensión entre ángulos.           reconoce el dilema como propio.
4 a 7 minutos.                      10 a 20 minutos.
```

**Output del skill:** Apertura guionizada + cierre guionizado + cuerpo en bullets de tensiones, ideas y referencias. El lenguaje del cuerpo es del creador, no del skill. El skill mapea qué decir y en qué orden. El creador decide cómo decirlo al momento de grabar.

---

## DIAGNÓSTICO DE PUNTO DE ENTRADA

El primer paso es identificar qué tipo de activación generó este essay. Los tres tipos producen tonos distintos y necesitan estructuras de apertura distintas.

Al activar el skill, preguntar:

> "Para arrancar el essay necesito saber desde dónde viene esto:
>
> ¿Es un dilema que todavía no tienes resuelto, una opinión fuerte sobre algo de la industria o el mundo, o un acontecimiento reciente que activó algo internamente?
>
> Y en una oración: ¿cuál es la cosa que más necesitas decir en este video, la que no has podido decir en ningún otro formato?"

La segunda pregunta es la más importante. La respuesta a "qué es lo que más necesito decir" suele ser la última línea del cierre, no el tema del video. Capturarla antes de empezar.

---

## LOS TRES TIPOS DE ACTIVACIÓN

### TIPO 1. El Dilema Sin Resolver

**Qué es:** Algo que el creador está procesando activamente y que no tiene respuesta todavía. La tensión es interna: dos formas de ver lo mismo que coexisten sin que una gane.

**Tono del essay:** Más íntimo, más exploratorio. El espectador siente que está acompañando un proceso de pensamiento, no recibiendo una conclusión.

**Estructura del cuerpo:** Las bullets mapean la tensión entre los dos lados del dilema. No resuelven. Cada bullet es una capa que profundiza la contradicción.

**Señal de éxito:** El espectador termina el video sin una respuesta pero con más preguntas sobre su propia vida. Los comentarios son confesiones, no debates.

**Apertura:** Entra al dilema sin anunciarlo. No dice "hoy voy a hablar sobre X". Dice la primera cosa que piensa cuando piensa en ese dilema.

---

### TIPO 2. La Opinión Visceral

**Qué es:** Una posición firme sobre algo en la industria, el mundo, la cultura del contenido, o la manera en que las cosas funcionan. El creador ya llegó a su conclusión. El essay es el camino que lleva al espectador ahí.

**Tono del essay:** Más directo, más provocador. Hay un "enemigo" implícito: la manera en que la mayoría ve las cosas. El essay lo desmonta.

**Estructura del cuerpo:** Las bullets mapean el argumento en capas. Cada capa es una razón, un ejemplo o una contradicción que refuerza la posición. El orden importa: de lo más accesible a lo más incómodo.

**Señal de éxito:** El espectador termina el video con una opinión que no tenía antes, o con la certeza de que la opinión que ya tenía es correcta. Los comentarios son "exactamente eso" o debates acalorados.

**Apertura:** Entra con la afirmación más polémica del video. Sin contexto. El espectador que no esté de acuerdo se queda para refutar. El que sí esté de acuerdo se queda para escuchar el argumento.

---

### TIPO 3. El Acontecimiento Activador

**Qué es:** Algo que pasó, que el creador vio, que leyó o que vivió, y que encendió algo. No es análisis de noticias. Es usar un acontecimiento como lente para hablar de algo más profundo.

**Tono del essay:** Reactivo pero reflexivo. El acontecimiento es el punto de entrada, no el tema. El tema real es lo que ese acontecimiento reveló.

**Estructura del cuerpo:** Las bullets mapean el camino del acontecimiento hacia la reflexión más profunda. Cada bullet aleja del evento concreto y acerca a la verdad universal que el evento iluminó.

**Señal de éxito:** El espectador termina el video pensando en el tema profundo, no en el acontecimiento que lo activó. Si al final siguen hablando del evento y no de la idea, el essay no llegó lo suficientemente lejos.

**Apertura:** Empieza en el momento exacto en que el acontecimiento activó algo. No el acontecimiento en sí: la reacción interna que generó.

---

## FASE DE EXTRACCIÓN. MATERIA PRIMA

Con el tipo de activación identificado, extraer la materia prima en dos rondas.

### Ronda 1. El contenido crudo

> "Dame el monólogo sin editar. No lo ordenes, no lo hagas sonar bien. Solo cuéntame lo que tienes que decir sobre esto, en el orden en que te viene a la mente."

Escuchar todo. No interrumpir. No sugerir estructura todavía. Capturar.

Luego hacer estas preguntas según el tipo:

**Si es Dilema:**
> "¿Cuáles son los dos lados de esto que no puedes resolver? ¿Y cuál es la parte del dilema que más te incomoda admitir?"

**Si es Opinión:**
> "¿Quién estaría en desacuerdo con esto? ¿Y cuál es el ejemplo más concreto y reciente que prueba que tienes razón?"

**Si es Acontecimiento:**
> "¿Qué fue exactamente lo que sentiste cuando pasó? ¿Y qué verdad más grande reveló ese momento?"

### Ronda 2. Las referencias y el mundo externo

El essay visceral no vive en el vacío. Conecta el pensamiento del creador con el mundo más amplio: libros, otros creadores, movimientos culturales, momentos históricos, conversaciones.

> "¿Hay algo que leíste, viste o escuchaste recientemente que conecta con esto? No tiene que ser directamente relacionado. A veces la conexión más oblicua es la más interesante.
>
> ¿Y hay alguien que piensa diferente sobre esto que vale la pena citar para crear tensión?"

Las referencias no son decoración. Son el puente entre el monólogo interno y el mundo que el espectador comparte.

---

## ESTRUCTURA DEL ESSAY. OUTPUT MIXTO

### LA APERTURA. Guionizada

La apertura es la única parte que se escribe completa. Determina si alguien se queda los próximos 15 minutos.

**Reglas de la apertura:**

No anuncia el video. No dice "hoy voy a hablar de". No da contexto de quién es el creador o por qué está calificado para hablar de esto.

Entra en el medio del pensamiento. El espectador llega cuando el monólogo ya empezó.

Duración: 60 a 90 segundos guionizados. Suficiente para instalar la tensión, no suficiente para resolverla.

**Estructura interna por tipo:**

```
DILEMA:
Línea 1: La contradicción dicha sin rodeos.
          "Llevo [tiempo] pensando en algo que no puedo resolver."
          No es introducción: es la contradicción ya instalada.
Línea 2-3: Los dos lados del dilema en oraciones cortas.
            Cada uno suena igualmente verdadero. Eso es la tensión.
Línea 4: La pregunta que el essay va a habitar sin responder.
          No promete respuesta: promete compañía en la pregunta.

OPINIÓN:
Línea 1: La afirmación más polémica. Sin suavizar.
          El espectador que no esté de acuerdo ya está atento.
Línea 2: Una consecuencia de esa afirmación que incomoda más.
Línea 3-4: Por qué esto importa ahora específicamente.
            No siempre. Ahora. El momento hace la urgencia.

ACONTECIMIENTO:
Línea 1: La reacción interna, no el evento.
          No "el otro día vi X". Sí "cuando vi X sentí que algo
          se acomodó en mi cabeza de una manera que no esperaba."
Línea 2-3: El evento en una oración. Lo mínimo necesario
            para que el espectador entienda el punto de entrada.
Línea 4: La pregunta o la incomodidad que generó.
          El acontecimiento ya queda atrás. Empieza el essay real.
```

**Indicación de grabación para la apertura:**
No grabar sentada en un set preparado. La apertura del essay visceral se graba como si fuera el primer pensamiento del día: caminando, parada frente a una ventana, en movimiento. La postura del cuerpo tiene que coincidir con el estado mental de alguien que está pensando, no de alguien que está presentando.

---

### EL CUERPO. Bullets de tensiones e ideas

El cuerpo no se guioniza. Se mapea. El creador habla desde los bullets, no desde un texto.

**Formato de los bullets:**

Cada bullet tiene tres elementos:
```
TENSIÓN O IDEA: [qué se dice, en una oración]
DIRECCIÓN:      [hacia dónde va, qué profundiza, qué conecta, qué contradice]
REFERENCIA:     [si hay una, libro, persona, momento, ejemplo concreto]
```

**Estructura de bullets por tipo:**

```
DILEMA (8-12 bullets):
• Los bullets alternan entre los dos lados del dilema
• No resuelven. Cada bullet hace la contradicción más compleja
• A mitad del cuerpo: el momento donde el creador se pregunta
  si el dilema tiene solución o si la tensión es permanente
• Los últimos 2-3 bullets profundizan la incomodidad
  en vez de resolverla

OPINIÓN (8-12 bullets):
• Los primeros 3-4 bullets construyen el argumento principal
• El bullet del medio: la objeción más fuerte al argumento
  Nombrarla antes de que el espectador la piense
• Los siguientes 3-4 bullets responden la objeción
  con ejemplos concretos y referencias
• Los últimos bullets van de lo argumentativo a lo visceral:
  por qué esto importa personalmente, no solo intelectualmente

ACONTECIMIENTO (8-12 bullets):
• Los primeros 2-3 bullets: más cerca del evento
• Bullet de giro: el momento donde el essay se aleja del evento
  y entra en la verdad más profunda que iluminó
• Los siguientes bullets: el tema real, con referencias y ejemplos
• Los últimos bullets: la implicación personal
  Qué cambia en cómo el creador ve algo desde ese acontecimiento
```

**Número de bullets:** Entre 8 y 12. Menos de 8 y el essay no tiene suficiente densidad. Más de 12 y el creador pierde el hilo al grabar sin guion.

**Lo que los bullets NO son:**
- Puntos de una lista para enumerar
- Resumen de lo que se va a decir
- Datos o estadísticas sin contexto emocional

Los bullets son waypoints de pensamiento. El creador los lee antes de grabar, los tiene como referencia durante, y habla hacia ellos sin leerlos.

---

### EL CIERRE. Guionizado

El cierre es la segunda parte que se escribe completa. Es lo que el espectador se lleva.

**Reglas del cierre:**

No resume el essay. El resumen mata el momentum que se construyó.

No termina en CTA de producto. El essay visceral termina en una idea, no en una invitación de compra. Si hay un CTA, va en la descripción del video, no en el cierre.

Responde a la apertura sin cerrar el loop completamente. Si la apertura instaló una tensión, el cierre la reconoce sin resolverla. Si la apertura hizo una afirmación, el cierre la profundiza con la consecuencia más personal.

Duración: 60 a 90 segundos guionizados.

**Estructura interna por tipo:**

```
DILEMA:
No resuelve el dilema. Propone una manera de vivir con él.
La última línea es una pregunta para el espectador,
no para el creador. El dilema pasa de interno a compartido.

OPINIÓN:
La consecuencia más personal de la opinión.
No el argumento más fuerte: el costo de tener esta opinión.
Lo que implica para el creador defender esto.
La última línea es la afirmación más limpia de todo el essay.
Sin adornos. La tesis desnuda.

ACONTECIMIENTO:
La distancia entre el evento y la verdad que reveló,
nombrada explícitamente.
"Lo que [acontecimiento] me mostró es que [verdad]."
La última línea es la implicación hacia adelante.
Qué hace el creador diferente desde que entiende esto.
```

**Indicación de grabación para el cierre:**
El cierre se graba en el espacio más quieto del video. Si la apertura fue en movimiento, el cierre es sentada o parada quieta. El cambio de energía física señala al espectador que algo está terminando, sin que se diga.

---

## FORMATO DE ENTREGA COMPLETO

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
YOUTUBE ESSAY, [Título de trabajo, no para publicar]
Tipo de activación: [DILEMA / OPINIÓN / ACONTECIMIENTO]
Duración estimada: [10-20 minutos según densidad de bullets]
POV activado: [qué capa del posicionamiento mueve]
La cosa que más necesitaba decir: [capturada en la extracción]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APERTURA. GUIONIZADA
[60-90 segundos. Estructura por tipo. Lista para leer como referencia.]

Indicación de grabación: [postura, espacio, energía]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CUERPO. BULLETS
[8-12 bullets con tensión/idea, dirección y referencia por bullet]
[El lenguaje es del creador. Estos son waypoints, no texto.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CIERRE. GUIONIZADO
[60-90 segundos. Estructura por tipo. Lista para leer como referencia.]

Indicación de grabación: [postura, espacio, energía]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DESCRIPCIÓN DE YOUTUBE
[3-5 líneas. No resume el video. Instala la tensión suficiente
para que quien no lo vio quiera verlo.
Incluye timestamps si el essay tiene más de 15 minutos.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXTRACTOS PARA OTRAS PLATAFORMAS
Bullet más fuerte para Twitter/LinkedIn: [el que tiene más filo]
Frase de apertura como fast reel: [si funciona sola como text screen]
Tema para email Inner Circle del mes: [el insight más íntimo
que quedó afuera del essay por ser demasiado personal para YouTube]
```

---

## CRITERIO DE REVISIÓN

**¿La apertura anuncia el video o entra al pensamiento?** Si la primera oración dice qué va a pasar en el video, reescribir. La apertura entra al medio de algo.

**¿Los bullets del cuerpo tienen dirección?** Un bullet sin dirección es un tema. Un bullet con dirección es un movimiento de pensamiento. Si no dice hacia dónde va, no es suficiente.

**¿El cierre resume o responde?** Si recapitula ideas del cuerpo, eliminar la recapitulación. El cierre responde la pregunta o la tensión de la apertura, no repite el camino.

**¿"La cosa que más necesitaba decir" aparece en el cierre?** Siempre. Si no aparece, el essay fue sobre otra cosa. Reorientar.

**¿Los bullets del tipo Dilema resuelven?** Si algún bullet propone una solución, eliminarlo o reformularlo como profundización de la tensión. El Dilema no se resuelve.

**¿Los bullets del tipo Opinión nombran la objeción más fuerte?** Si el argumento no se enfrenta a su mejor contraargumento, es frágil. El essay visceral nombra la objeción antes de que el espectador la piense.

---

## LÍMITE DE REVISIONES

Máximo 5 rondas. Contador explícito:

> "Revisión [N] de 5."

En revisión 5:
> "Esta es tu revisión 5 de 5. El essay está listo para grabar. Una instrucción antes de entrar: lee la apertura y el cierre en voz alta una vez. Los bullets solo míralos. No los memorices. Si los memorizas, el cuerpo va a sonar guionizado. Tienen que sonar como que los estás descubriendo mientras hablas."

---

## HANDOFF

Recibe de:
- **ecosystem-architect:** El essay es el Alma del mes. El Hilo Conductor del Ecosystem Architect informa qué tipo de activación tiene más coherencia con el momento narrativo del mes.
- **pov-finder:** El essay visceral es la expresión más libre del posicionamiento. La Capa del Espejo y el Legado del POV son las fuentes más frecuentes de los dilemas y las opiniones que activan este formato.
- **email-inner-circle:** El insight más íntimo que quedó afuera del essay porque era demasiado personal para YouTube es el candidato directo para el Inner Circle del mes.

Alimenta a:
- **talking-head-scripting:** Si el essay encontró un argumento sólido durante la exploración del dilema, ese argumento puede convertirse en el hachazo de un talking head de la semana siguiente.
- **storytime-scripting:** Si el essay activó una historia personal que no cupo en el monólogo, es el storytime del mes siguiente.
- **carousel-scripting:** Los bullets más argumentativos del cuerpo del essay son el carrusel Analista de la semana siguiente.
- **tweet-atomic-snippets:** Las frases más densas de la apertura y el cierre guionizados son los one-liners de Twitter/X.
- **ecosystem-architect (siguiente mes):** El tiempo de retención promedio del essay y el tipo de comentarios que generó (confesiones vs debates vs "exactamente eso") entran al Paso 0 como señal de qué tipo de activación resonó más con la audiencia del canal.
