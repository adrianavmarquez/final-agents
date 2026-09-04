---
name: voiceover-scripting
description: >
  Guionización de voiceovers para el creador. Activar SIEMPRE que el creador diga "vamos a guionizar un voiceover", "hazme el script de un voiceover", "quiero hacer un voiceover sobre [tema]", "guioniza esto como voiceover", o cualquier variación. También activar cuando el Ecosystem Architect haya definido una backbone semanal con formato voiceover y el creador quiera ejecutarla.

  Este skill produce scripts de voiceover en dos capas paralelas (audio + b-roll en tabla), diferenciados por plataforma de destino, estructurados en 4 partes funcionales (Hook / Build-up / Shift / Invisible Pitch), y con variantes según nivel de funnel (TOF o BOF). Audio primero, b-roll como segunda capa. Largo objetivo: 60 a 90 segundos. Máximo 5 rondas de revisión.
---

> **Capa 0.** Antes de escribir, carga `marca-reglas-duras`. Sus siete reglas y su léxico mandan sobre cualquier instrucción de esta skill.

> **Frontera.** Este produce voz en off: audio primero, b-roll como segunda capa en tabla, 60 a 90 segundos. Si Adri aparece en cámara hablando, es `yapping-scripting` o `talking-head-scripting`, no este.

# Voiceover Scripting

## Qué hace este skill

Produce el script completo de un voiceover en dos capas: primero el audio con ritmo, pausas y punto de vista integrado; luego el mapa de b-roll en tabla paralela, con segundos, visual y modo de relación explicitados.

No es transcripción de ideas. Es construcción de un monólogo que suena espontáneo aunque esté escrito, calibrado para la plataforma de destino, y con un cierre que hace que el espectador reflexione sobre su vida, no sobre el producto.

---

## DIFERENCIA CON YAPPING-SCRIPTING

El yapping es cámara directa: el creador habla, la cámara la ve, la presencia física hace el trabajo emocional.

El voiceover es distinto: la voz es el protagonista, el cuerpo no aparece. Eso cambia todo:

- Sin lenguaje corporal: el ritmo y las pausas hacen lo que en cámara hace la expresión.
- El visual no es decoración: cada b-roll toma una decisión sobre qué añade al audio.
- La espontaneidad es ilusión: tiene que sonar como pensamiento en tiempo real aunque esté construido con precisión.

---

## APERTURA DE SESIÓN

Al activar, preguntar en un solo bloque:

> "Para el voiceover necesito cuatro datos:
>
> 1. **La idea:** ¿De qué va este voiceover? Concepto, historia, creencia, observación. Lo que quieres decir.
> 2. **Plataforma destino:** ¿TikTok, Instagram Reels, YouTube Shorts, o más de una?
> 3. **Nivel de funnel:** ¿Es TOF (llegar a gente nueva) o BOF (hablarle a quien ya te conoce y está cerca de tomar una decisión)?
> 4. **B-roll disponible:** ¿Ya tienes material grabado o grabas específico para este video?"

Con esos cuatro datos, determinar el contrato de plataforma y arrancar la escritura.

---

## FASE 0. CONTRATO DE PLATAFORMA

Antes de escribir una sola línea, calibrar el script al contrato no escrito que cada plataforma tiene con su audiencia. El mismo voiceover en TikTok que en Instagram Reels falla porque el usuario espera cosas distintas.

```
PLATAFORMA       CONTRATO CON EL USUARIO              IMPLICACIÓN PARA EL SCRIPT
─────────────────────────────────────────────────────────────────────────────────────
TikTok           "Muéstrame algo real, sin filtro"     Pacing caótico. Lenguaje crudo.
                                                       Hook en los primeros 0.5 segundos.
                                                       Imperfección intencional.

Instagram Reels  "Inspírame o enséñame algo útil"      Ritmo con pausas. Lenguaje pulido
                                                       pero cercano. B-roll más estético.
                                                       Hook en los primeros 2-3 segundos.

YouTube Shorts   "Dame valor denso y rápido"           Alta energía. Estructura muy clara.
                                                       Tono de autoridad. Hook inmediato.
                                                       Cada segundo justificado.
```

Si el voiceover va a más de una plataforma, escribir el audio base para la plataforma principal y especificar los ajustes para las secundarias al final, no reescribir todo.

---

## FASE 1. ESCRITURA DEL AUDIO

### La estructura de 4 partes funcionales

No es intro / desarrollo / cierre. Cada parte tiene un trabajo específico. Nombrar la función obliga a ejecutarla correctamente.

---

**HOOK. Abrir el loop, no cerrarlo**

El trabajo del hook es crear una pregunta en la mente del espectador que no puede resolver sin seguir escuchando. No anuncia el video. No introduce el tema. Entra al medio de algo.

Duración: 5-10 segundos.

Tipos de hook para voiceover:
- **Afirmación bold:** Una verdad que polariza. "El contenido de valor es una trampa de ego."
- **Contradicción:** Algo que no debería ser verdad pero lo es. "Cuanto más planificas, menos publicas."
- **Confesión:** Algo personal que la audiencia reconoce en sí misma. "Estuve tres meses publicando para nadie y lo llamé estrategia."
- **Pregunta sin respuesta obvia:** "¿Qué pasa cuando tu marca crece pero tú te sientes más pequeña?"
- **Dato concreto que incomoda:** "El 80% del contenido educativo que ves no le vendió nada a quien lo hizo."

Regla: si la primera palabra es "hoy", "en este video", "quería hablar de" o cualquier frase de contexto, reescribir. El hook no avisa, entra.

---

**BUILD-UP. Validar antes de hablar de ti**

El trabajo del build-up es hacer que el espectador sienta que lo entiendes antes de que hayas dicho nada sobre ti o tu perspectiva. Es la parte donde la audiencia piensa "exactamente, eso es lo que me pasa."

Duración: 15-20 segundos.

No habla de la solución. No habla del producto. Habla de la experiencia del espectador con suficiente precisión para que se reconozca. Cuanto más específico, más fuerte.

Señal de build-up débil: habla de "muchas personas" o "la mayoría". El build-up fuerte habla de una situación tan concreta que parece escrita para alguien específico.

---

**SHIFT. Tu perspectiva, en términos de sensación**

El trabajo del shift es presentar el punto de vista único de la marca. No como información nueva, sino como una reconfiguración de algo que el espectador ya sabía pero no había visto así.

Duración: 20-30 segundos.

El shift no se anuncia. No dice "pero yo creo que" o "mi perspectiva es". Entra como continuación natural del build-up y reencuadra lo que se acaba de decir.

La diferencia entre un shift de información y un shift de sensación:
- Información: "La razón por la que esto no funciona es que el algoritmo prioriza X."
- Sensación: "No es el algoritmo. Es que estás publicando para que te aprueben, no para que alguien se reconozca."

El shift de sensación llega más hondo porque no da datos: cambia la manera en que el espectador se ve a sí mismo.

---

**INVISIBLE PITCH. El cierre que vende sin vender**

El trabajo del cierre es hacer que el espectador reflexione sobre su vida, no sobre el producto. Si el espectador termina el video pensando "necesito cambiar algo", el invisible pitch funcionó. Si termina pensando "esta persona quiere que le compre algo", falló.

Duración: 10-15 segundos.

**Variante TOF:** El invisible pitch reflexiona sobre una verdad universal. El espectador la aplica a su situación sin que nadie se lo pida. No hay CTA explícito o si lo hay es de conversación ("¿te ha pasado esto?"), no de venta.

**Variante BOF:** El invisible pitch reflexiona sobre una decisión que el espectador ya está considerando. La última línea planta la semilla sin nombrar el producto. El espectador llega solo a la conclusión. Puede terminar con un CTA suave hacia un siguiente paso concreto.

Señal de cierre malo: resume lo que se acaba de decir. El cierre no repite, aterriza o abre un nuevo loop.

---

### Reglas de copywriting para voz

Escribir para ser leído en voz alta es diferente a escribir para ser leído. Estas reglas filtran los scripts que suenan robóticos.

**Léelo en voz alta antes de entregarlo.** Si hay un lugar donde la lengua se traba, la sintaxis está mal. Reescribir esa línea, no seguir.

**Mata los adjetivos.** Los adjetivos en voz alta suenan a copy de marketing. "Una estrategia poderosa y transformadora" → "una estrategia que cambia cómo trabajas". Acción, no calificación.

**Una idea por oración.** Cuando una oración tiene dos ideas, el oyente pierde una. Cortar con punto y seguido, no con coma.

**Sin conectores formales.** "Sin embargo", "por lo tanto", "en conclusión" no existen en conversación real. Reemplazar con "pero", "entonces", "y resulta que", o con una pausa directa.

**Las pausas son instrucciones.** Marcarlas con `[pausa]` o `[pausa larga]`. No son decorativas: indican dónde el audio respira y dónde el b-roll tiene espacio para registrar algo.

**El ritmo varía con intención.** Oraciones cortas suben la energía. Oraciones más largas la desaceleran y crean espacio para que una idea aterrice. Alternar con criterio, no aleatoriamente.

---

### Formato del audio

```
AUDIO, [Título del voiceover]
Plataforma: [destino principal]
Funnel: [TOF / BOF]
Duración estimada: [X segundos]

━━━ HOOK (0:00 - 0:08) ━━━
"[primera línea]"
[pausa]

━━━ BUILD-UP (0:08 - 0:28) ━━━
"[validación de la experiencia del espectador]"
[pausa corta]
"[más build-up si hace falta]"
[pausa]

━━━ SHIFT (0:28 - 0:55) ━━━
"[perspectiva única en términos de sensación]"
[pausa]
"[desarrollo del shift]"
[pausa larga]

━━━ INVISIBLE PITCH (0:55 - 1:20) ━━━
"[cierre que hace reflexionar, no que vende]"
[pausa]
"[última línea, la que se queda]"
```

**Notas de grabación:**
```
Velocidad:              [natural / levemente más lento]
Tono de arranque:       [íntimo / directo / reflexivo / urgente]
Momento de mayor baja:  [línea específica donde la voz baja]
Momento de mayor subida:[línea específica donde la energía sube]
Dónde no apurar:        [el momento de pausa más importante]
```

---

## FASE 2. TABLA AUDIO / VISUAL

Con el audio completo, mapear el b-roll en tabla paralela. El creador no tiene que interpretar el script: sabe exactamente qué mostrar en cada segundo mientras habla.

### Los tres modos de relación visual

**CONTRASTE:** El audio dice una cosa y el visual muestra otra. Crea tensión o ironía. Usado en los momentos donde el punto de vista es más fuerte.

**ILUSTRACIÓN:** El visual apoya literalmente lo que dice el audio. Usado cuando la imagen añade claridad o prueba concreta.

**AMBIENTE:** El visual es cotidiano y no tiene relación directa con el audio. El audio es el protagonista absoluto. El b-roll solo crea atmósfera y da tiempo visual para que el audio respire.

---

### Formato de tabla

```
TABLA AUDIO / VISUAL, [Título]

┌──────────┬─────────────────────────────────────┬──────────────────────────────────────────┐
│ SEGUNDO  │ AUDIO                               │ VISUAL                                   │
├──────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ 0:00     │ "[primera línea del hook]"          │ MODO: AMBIENTE                           │
│          │                                     │ Qué se ve: [descripción específica]      │
│          │                                     │ Plano: [close-up / general / detalle]    │
├──────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ 0:08     │ [pausa]                             │ El clip anterior se sostiene             │
│          │                                     │ No cortar en la pausa                    │
├──────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ 0:09     │ "[build-up primera línea]"          │ MODO: [CONTRASTE / ILUSTRACIÓN / AMBIENTE]│
│          │                                     │ Qué se ve: [...]                         │
│          │                                     │ Por qué este modo aquí: [razón breve]    │
├──────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ [...]    │ [...]                               │ [...]                                    │
├──────────┼─────────────────────────────────────┼──────────────────────────────────────────┤
│ 0:55     │ "[invisible pitch]"                 │ MODO: AMBIENTE o CONTRASTE               │
│          │                                     │ Qué se ve: [el b-roll más quieto]        │
│          │                                     │ Nota: si termina en negro o corte directo│
└──────────┴─────────────────────────────────────┴──────────────────────────────────────────┘

NOTA DE B-ROLL:
Material disponible: [lo que el creador confirmó que tiene]
Material a grabar:   [lo que necesita grabarse específico]
Clips de archivo:    [si aplica material reutilizable]
```

---

## ENTREGA FINAL

Entregar en este orden, siempre completo:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VOICEOVER, [Título]
Plataforma: [destino]   Funnel: [TOF/BOF]
Duración estimada: [X segundos]
POV activado: [qué capa del posicionamiento mueve]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. AUDIO COMPLETO CON ESTRUCTURA
[script con timestamps y partes nombradas]

2. NOTAS DE GRABACIÓN
[velocidad, tono, momentos clave]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3. TABLA AUDIO / VISUAL
[tabla completa segundo por segundo]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4. AJUSTES POR PLATAFORMA SECUNDARIA
[solo si va a más de una plataforma]
[qué cambia en pacing, hook o cierre]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. CAPTION SUGERIDO
[3-4 líneas en tono del voiceover, no de marketing]
[para cada plataforma si difieren]
```

---

## LÍMITE DE REVISIONES

Máximo 5 rondas. Contador explícito en cada ronda:

> "Revisión [N] de 5."

En revisión 5:

> "Esta es tu revisión 5 de 5. El voiceover está listo para grabar. Los datos de cómo responde la audiencia te dicen el resto. No hay revisión 6."

Si pide una sexta:

> "El límite existe exactamente para este momento. Grábalo con esta versión. Si algo no funciona en producción, lo ajustamos en el siguiente voiceover con ese aprendizaje. El volumen te da más datos que la revisión 6."

---

## HANDOFF

Recibe de:
- **ecosystem-architect:** La backbone semanal con formato voiceover es el brief de entrada. El hook propuesto ahí es el punto de partida, no el definitivo.
- **pov-finder:** El POV base informa qué capa del posicionamiento activa cada voiceover y calibra el Shift.

Alimenta a:
- **Post-producción:** La tabla Audio/Visual es la guía de edición directa.
- **ecosystem-architect (siguiente mes):** Si el voiceover generó tracción, ese dato entra al Paso 0 del siguiente ciclo como referencia de qué modo de relación visual y qué tipo de Shift funcionó.
