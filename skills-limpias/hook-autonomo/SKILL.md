---
name: hook-autonomo
description: "Motor por capas para escribir ganchos autónomos en español de Venezuela. Se invoca con /gancho. Declara principio y tipo antes de redactar, exige ruta de prueba, y entrega al verificador externo. No se puntúa a sí mismo. Úsalo para hooks, titulares, aperturas y primeras líneas de contenido orgánico o colaboraciones de marca."
---

# Gancho autónomo

Motor de ganchos para contenido orgánico en español. No es un generador de opciones. Es una cadena de decisiones que termina en una entrega al verificador. Este skill escribe. No califica. La calificación vive en `verificador/`, que este skill no lee ni edita.

Este motor no toca nada de Motion MCP. Si el pedido es sobre ads pagados en Meta, esto no aplica y hay que decirlo.

## Reglas duras que nunca se negocian

1. Cero rayas largas. Usar puntos o comas como corresponda en su lugar.
2. Prohibidas las estructuras "no se trata de X, se trata de Y", "X no ha muerto, solo lo estás haciendo mal" y "no eres malo en X, es que no sabes Y" como apertura. El mecanismo que hay debajo de la tercera (permiso + reencuadre + contrarian) se conserva. La sintaxis no.
3. Prohibido prometer crecimiento, ventas, ingresos o viralidad. Regla de marca y de cumplimiento.
4. Máximo cinco hashtags.
5. Español nativo de Venezuela con spanglish natural. Nunca traducción literal de frameworks en inglés.
6. Registro cero gurú, cero coach, cero embudo de webinar.
7. Se empieza in media res. Nada de párrafo de calentamiento.

---

# C0. Intake y señales

Compuerta binaria. Sin esto no se redacta nada. No se asume, no se rellena, no se inventa.

## C0.1 Ramificación

Primera pregunta siempre: ¿esto es marca personal o colaboración de marca?

### Rama A, marca personal (@adrianavmarquez)

Cargar señales antes de escribir:

1. Signal Exploration Log del Basecamp en Notion. Señales recientes del tema.
2. Personas DB y Micropersonas DB. La micropersona exacta, no la persona general.
3. Language Bank bajo Messaging and Angles. De ahí sale el verbatim.
4. Hook Master y Content Process (columna Hook). Qué ya se escribió, para no repetir.
5. Performance Intelligence Log. Última entrada R3 o R0 para saber qué tipos y principios están rindiendo.
6. README del SOP Loop de Redacción en Basecamp. Para saber que el verificador existe afuera y qué declaración espera.

Extracción de lenguaje obligatoria, en uno de tres modos. Se declara cuál.

**Modo verbatim.** Entre tres y siete frases textuales de clientes o audiencia sobre este dolor, del Language Bank o del Radar de DMs. Se copian como están, con sus errores y su registro. No se pulen. Es el modo por defecto y el único que permite T3 Relatabilidad y T4 Tú-espejo sin restricción.

**Modo proxy.** No hay voz de audiencia propia, pero hay lenguaje real de otro lado: auditorías de la cuenta, estudios de mercado, benchmarking de otros creadores, scraping de comentarios ajenos, transcripciones de tus propios videos que rindieron. Se cita la fuente exacta. Vale menos que verbatim y se declara así.

**Modo hipótesis.** No hay lenguaje real de ningún lado. La micropersona existe en Micro Persona DB como inferencia o como punto ciego, y la única forma de saber si el dolor es real es lanzar el anzuelo. Se escribe desde el Specific Pain de la DB y desde lo que Adri sabe del nicho. Se declara como hipótesis. La pieza es un experimento: si genera DMs con verbatim, la micropersona sube a modo verbatim; si no, se anota y se archiva.

Reglas del modo hipótesis:
- Máximo dos ganchos por micropersona hipótesis por mes. Es una prueba, no una campaña.
- No se puede declarar T3 ni T4 como tipo primario: no hay espejo sin voz real que reflejar. Se prefieren T2, T6, T9 y T11, que lanzan una afirmación o una pregunta y miden quién responde.
- La ruta de prueba (C1c) tiene que venir de dato propio de Adri, no de la audiencia.
- El objetivo declarado es comentarios o DM, porque lo que se busca es verbatim de vuelta.

Si no hay verbatim, ni proxy, ni micropersona en la DB, se para. Inventar una persona no es hipótesis, es ficción.

### Rama B, colaboración de marca

1. Leer el brief creativo completo. Si no hay brief, se para.
2. Invocar `brand-collab-research` para el análisis de marca vía conectores.
3. Extraer del brief: qué se puede decir, qué está prohibido, cuál es la métrica que le importa a la marca, quién aprueba.
4. Identificar la micropersona del lado de la marca, no de Adri.
5. Resolver el conflicto de voz explícitamente. Si el registro de la marca choca con el de Adri, se nombra el choque y se decide cuál gana antes de escribir.

## C0.2 Campos obligatorios

| Campo | Qué es |
|---|---|
| Micropersona | El perfil específico que tiene este problema. Código de Micro Persona DB. |
| Dolor en su voz | Cómo lo nombra ella en un DM, no como lo nombra la industria. |
| Profundidad del dolor | Estructural (no sabe que no sabe: guión, retención, para quién), herramienta (luz, sonido, app), o mindset (miedo, culpa, comparación). Se declara porque el verificador lo pondera. |
| Consecuencia concreta | Qué le cuesta. Dinero no ganado, tiempo perdido, oportunidad perdida, conexión rota. |
| Objetivo de la pieza | Alcance, comentarios, saves, shares, DM. Uno primario. El verificador puntúa contra este. |
| Entregable | Qué recibe si actúa: plantilla, checklist, guía, lista, link, nada. Se declara porque el verificador lo pondera. |
| Formato | Reel hablado, texto en pantalla sin voz, carrusel, newsletter, colaboración. |
| Idioma y registro | Español de Venezuela por defecto, tú. Spanglish permitido donde es natural. |
| Cantidad | Cuántos ganchos y para qué se van a usar. |

## C0.3 Parada por información insuficiente

Si falta cualquiera de los campos de C0.2 o falta el verbatim, este motor no escribe. Reporta así:

```
No tengo suficiente para escribir esto.

Falta:
- [campo] : [por qué sin eso el gancho sale genérico]

Puedo conseguirlo si:
- [acción concreta: revisar tal DB, correr brand-collab-research, que me pases X]
```

Escribir sin señales produce ganchos que le cuadran a cualquiera. Esa es la falla exacta que este motor existe para evitar.

---

# C1a. Decisión psicológica

La psicología se elige antes de escribir. Nunca después.

Razón: cualquier gancho ya escrito se puede justificar psicológicamente en retrospectiva. Esa justificación no es un diagnóstico, es una racionalización. Si el principio se elige primero, condiciona la redacción. Si se elige después, no condiciona nada.

## Formato obligatorio de declaración

```
Principio primario:
Principio secundario (opcional):
Principio terciario (solo si tiene cláusula propia en la frase):
Nombre creativo:
Nombre académico:
Afirmación operacional:
Condición de uso:
Límite / riesgo de mal uso:
Qué lo diferencia del vecino:
Estado epistémico:
Por qué este dolor pide este principio:
```

Vocabulario de estado epistémico: Robusto (evidencia replicada), Contextual (funciona bajo condiciones nombrables), Debatido (evidencia en disputa activa), Heurístico (regla práctica sin base experimental fuerte). Si el estado es Debatido o Heurístico, el gancho no puede apoyarse en el principio como argumento, solo como ejecución.

## Los 14 principios. Se declaran por separado, no se agrupan.

Comparten raíces teóricas. No comparten condición de uso. La condición de uso es lo que decide si el gancho vive o muere, así que cada uno se declara solo.

### P1. Efecto Zeigarnik

- Nombre creativo: tarea inconclusa, bucle que ella ya abrió.
- Nombre académico: Zeigarnik 1927. Ovsiankina (reanudación). Meta-análisis de Ghibellini y Meier 2025.
- Afirmación operacional: una meta que la persona percibe como iniciada y no cerrada sube la probabilidad de que vuelva a completarla, si el siguiente paso es claro y de baja fricción. No sube la memoria del contenido.
- Condición de uso: ella tiene que haber empezado algo. Vio la parte 1, hizo el diagnóstico, guardó el carrusel, comentó. Sin inicio propio no hay tarea que reanudar.
- Límite / riesgo de mal uso: la ventaja de memoria no se sostiene. Meta-análisis 2025: razón ponderada 0.99, dz 0.15, sin ventaja de recuerdo para tareas inconclusas. Prohibido usarlo como argumento de "se va a acordar". Solo sirve para continuidad de serie o de flujo.
- Qué lo diferencia del vecino: el cliffhanger (P9) abre una brecha sobre algo que ella no ha tocado. Zeigarnik exige que ella ya esté adentro.
- Estado epistémico: reanudación Contextual. Memoria: no sostenida.

### P2. Héroe reacio

- Nombre creativo: héroe reacio, error del competente, confesión con reparación.
- Nombre académico: efecto pratfall. Aronson, Willerman y Floyd 1966.
- Afirmación operacional: un error menor y no dañino sube la cercanía solo cuando la competencia ya está demostrada. Competencia visible + imperfección leve + aprendizaje o reparación visible.
- Condición de uso: la audiencia ya te percibe como capaz en ese tema. El error tiene que enseñar algo transferible.
- Límite / riesgo de mal uso: se invierte en emisores percibidos como poco competentes. Un error grave no es pratfall, es crisis. La imperfección demasiado pulida se lee como pose.
- Qué lo diferencia del vecino: la prueba social (P5) construye credibilidad por consenso. El halo (P14) por un rasgo positivo. El héroe reacio por una falla calibrada.
- Estado epistémico: Debatido.

### P3. Reencuadre de identidad

- Nombre creativo: reencuadre de identidad, "no necesitas aprender, necesitas ser distinta".
- Nombre académico: motivación basada en identidad (Oyserman). Bryan, Walton, Rogers y Dweck 2011.
- Afirmación operacional: conectar una conducta con una identidad que ella desea puede motivar más que pedir la conducta. Cambia cómo se ve, no lo que sabe.
- Condición de uso: identidad deseable, compatible con su autoconcepto, plausible, respaldada por acción concreta.
- Límite / riesgo de mal uso: proponer una identidad que ella no quiere. Elitismo. Excluir a quien todavía no se identifica con la categoría.
- Qué lo diferencia del vecino: el tú-espejo (P4) describe quién es hoy. El reencuadre propone quién puede ser.
- Estado epistémico: Contextual.

### P4. Tú-espejo

- Nombre creativo: tú-espejo, call out, "este video es para mí".
- Nombre académico: efecto de autorreferencia. Rogers, Kuiper y Kirker 1977. Symons y Johnson 1997.
- Afirmación operacional: la información codificada en referencia al yo se procesa más profundo. El efecto no está en la palabra "tú", está en que ella reconozca su situación exacta.
- Condición de uso: la descripción tiene que ser reconociblemente de ella. Rol, momento, meta, consecuencia. Micropersona, no persona.
- Límite / riesgo de mal uso: si el espejo es genérico se convierte en horóscopo (efecto Forer). Prueba: si la frase le cuadra a tres perfiles distintos, no es espejo, es Barnum.
- Qué lo diferencia del vecino: ver P3. El espejo no cambia nada, refleja.
- Estado epistémico: Robusto. Magnitud del meta-análisis pendiente de verificar; no citar cifras.

### P5. Prueba social

- Nombre creativo: prueba social, "otros como tú ya lo hicieron".
- Nombre académico: normas descriptivas. Cialdini, Reno y Kallgren 1990. Goldstein, Cialdini y Griskevicius 2008.
- Afirmación operacional: la conducta de personas similares reduce incertidumbre y baja el costo percibido de intentarlo.
- Condición de uso: el referente tiene que ser comparable. La cifra necesita universo, periodo y definición.
- Límite / riesgo de mal uso: contadores no verificables. Normalizar lo negativo. Prohibido convertir prueba social en promesa de resultado.
- Qué lo diferencia del vecino: el halo (P14) es un rasgo que contamina el juicio. La prueba social es la conducta de otros.
- Estado epistémico: Robusto y contextual.

### P6. Contraste antes y después

- Nombre creativo: contraste antes y después, anclaje, dos fotos.
- Nombre académico: dependencia del punto de referencia. Kahneman y Tversky 1979.
- Afirmación operacional: la evaluación depende del punto de referencia. Poner el antes explícito cambia cómo se valora el después.
- Condición de uso: el antes tiene que ser el estado real de ella. Si hay después, con mecanismo de transición nombrado.
- Límite / riesgo de mal uso: antes inflado. Casos extremos como típicos. El después no puede ser promesa de crecimiento.
- Qué lo diferencia del vecino: no necesita que perder pese más (P11) ni limita acceso (P12). Si el gancho tiene dos fotos, es P6. Si tiene una factura, es P11. Si tiene una puerta que se cierra, es P12.
- Estado epistémico: anclaje Robusto. Contraste como gancho Contextual.

### P7. Interrupción de patrón

- Nombre creativo: interrupción de patrón, sorpresa relevante, contrarian.
- Nombre académico: Von Restorff 1933. Incongruencia de esquema, Mandler 1982. Violación de expectativas, Burgoon.
- Afirmación operacional: la incongruencia moderada frente a un esquema activo sube el procesamiento. La extrema lo baja. Sorpresa en la forma + coherencia en el significado.
- Condición de uso: el esquema esperado tiene que estar activo. Hay que instalar la expectativa antes de romperla.
- Límite / riesgo de mal uso: curva invertida, no escala. Shock que retiene pero no deja recuerdo. "Todo lo que sabes está mal" es ruptura sin sustento.
- Qué lo diferencia del vecino: el permiso (P8) alivia. La interrupción sorprende. El cliffhanger (P9) abre un hueco sin contradecir.
- Estado epistémico: Contextual.

### P8. Otorgamiento de permiso

- Nombre creativo: otorgamiento de permiso, "puedes hacer esto", alivio de culpa.
- Nombre académico: reactancia psicológica. Brehm 1966. Steindl et al 2015.
- Afirmación operacional: cuando una solicitud se percibe como coercitiva, el lenguaje que reconoce elección reduce resistencia. El permiso baja la reactancia.
- Condición de uso: la culpa que nombra tiene que ser real de esa micropersona. La elección ofrecida tiene que ser real.
- Límite / riesgo de mal uso: permiso retórico bajo presión eleva sospecha.
- Qué lo diferencia del vecino: ver P7. Además, el permiso no da nada tangible (P10), quita un peso.
- Estado epistémico: Contextual.

### P9. Cliffhanger

- Nombre creativo: cliffhanger, brecha de curiosidad.
- Nombre académico: teoría de la brecha de información. Loewenstein 1994.
- Afirmación operacional: percibir una brecha específica entre lo que sabe y lo que quiere saber induce curiosidad, si entiende qué le falta, por qué importa y que la respuesta va a llegar.
- Condición de uso: el tema ya está en su mapa de preocupaciones. Dato parcial + pregunta específica + promesa creíble de resolución dentro de la pieza.
- Límite / riesgo de mal uso: el bucle que no se paga es clickbait. "El secreto que no quieren que sepas" baja la expectativa de calidad.
- Qué lo diferencia del vecino: ver P1 y P7.
- Estado epistémico: Robusto como teoría. Contextual como gancho.

### P10. Reciprocidad

- Nombre creativo: reciprocidad, dar primero.
- Nombre académico: norma de reciprocidad. Gouldner 1960. Regan 1971.
- Afirmación operacional: valor real entregado antes de pedir algo sube la apertura. No obliga, predispone.
- Condición de uso: el regalo tiene valor autónomo. Usable sin comprar ni registrarse.
- Límite / riesgo de mal uso: recurso genérico. Pedir mucho de inmediato. Ocultar que se pide contacto.
- Qué lo diferencia del vecino: da primero. El pie en la puerta (P13) pide primero.
- Estado epistémico: norma Robusta. Magnitud en marketing Contextual.

### P11. Aversión a la pérdida

- Nombre creativo: aversión a la pérdida, "esto te está costando".
- Nombre académico: Kahneman y Tversky 1979. Revisión crítica de Gal y Rucker 2018. Walasek et al 2024.
- Afirmación operacional: un encuadre de pérdida sube relevancia cuando la pérdida es concreta, creíble, personal y evitable. No siempre supera a la ganancia equivalente.
- Condición de uso: pérdida real y salida clara. Sin salida, produce evasión.
- Límite / riesgo de mal uso: "lo que pierdes pesa más" ya no es ley citable. Alarmismo. FOMO fabricado. Prohibido "estás perdiendo dinero/seguidores" sin dato propio.
- Qué lo diferencia del vecino: nombra un costo. No compara dos estados (P6) ni limita acceso (P12).
- Estado epistémico: Debatido.

### P12. Escasez y urgencia

- Nombre creativo: escasez, urgencia, cupo, ventana.
- Nombre académico: teoría de la mercancía, Brock 1968. Worchel, Lee y Adewole 1975.
- Afirmación operacional: una restricción auténtica y explicada sube el valor percibido y el costo de esperar.
- Condición de uso: razón operativa nombrable. "Abro 12 porque cada una incluye revisión manual" pasa.
- Límite / riesgo de mal uso: temporizadores que se reinician, cupos que nunca se agotan. En contenido orgánico casi nunca aplica.
- Qué lo diferencia del vecino: ver P6 y P11.
- Estado epistémico: Contextual en oferta. Heurístico en orgánico.

### P13. Pie en la puerta

- Nombre creativo: pie en la puerta, microcompromiso.
- Nombre académico: Freedman y Fraser 1966. Burger 1999.
- Afirmación operacional: un compromiso pequeño, congruente y cumplido sube la probabilidad del siguiente.
- Condición de uso: paso genuinamente pequeño, cumplido, con progreso visible.
- Límite / riesgo de mal uso: efecto pequeño con moderadores. Escaleras coercitivas.
- Qué lo diferencia del vecino: ver P10. Pide primero, no da primero.
- Estado epistémico: Contextual.

### P14. Efecto halo

- Nombre creativo: efecto halo, prestigio prestado.
- Nombre académico: Thorndike 1920. Nisbett y Wilson 1977.
- Afirmación operacional: un rasgo positivo saliente contamina la evaluación global antes de comprobar nada.
- Condición de uso: el rasgo tiene que ser real y pertinente. Método visible, dato con fuente, demo en pantalla. El prestigio ajeno solo sirve como marco.
- Límite / riesgo de mal uso: sesgo del receptor. Explica por qué funcionó, no sirve para inflar credenciales. Dato propio: el único gancho de autoridad de la cuenta rindió 0.6x.
- Qué lo diferencia del vecino: ver P2 y P5.
- Estado epistémico: Robusto.

## Mapa de vecinos

| Par | Prueba para distinguir |
|---|---|
| P1 vs P9 | ¿Ella ya empezó algo? Sí es P1. No es P9. |
| P3 vs P4 | ¿Describe quién es o propone quién puede ser? Describe P4. Propone P3. |
| P2 vs P5 vs P14 | ¿La credibilidad viene de una falla, de otros, o de un rasgo? Falla P2. Otros P5. Rasgo P14. |
| P6 vs P11 vs P12 | ¿Dos fotos, una factura, o una puerta que se cierra? Fotos P6. Factura P11. Puerta P12. |
| P7 vs P8 vs P9 | ¿Contradice, alivia, o muestra un hueco? Contradice P7. Alivia P8. Hueco P9. |
| P10 vs P13 | ¿Da primero o pide primero? Da P10. Pide P13. |

## Regla de selección

Un gancho declara un principio primario. Puede tener un secundario. Puede tener un terciario solo si cada principio tiene su cláusula propia dentro de la frase, verificable señalando qué palabras hacen qué trabajo. Dato propio: el mejor gancho histórico de la cuenta corre P8 + P3 + P7 en dos cláusulas y los ejecuta todos. Tres principios sin cláusula propia significan que ninguno está ejecutado.

El secundario y el terciario no pueden ser vecinos del primario (misma fila del mapa).

En un set, los principios se varían. Cinco ganchos del mismo principio es un solo gancho escrito de cinco formas. Cinco ganchos de la misma fila del mapa es casi lo mismo.

---

# C1b. Decisión de forma

Principio es por qué funciona. Tipo es qué forma tiene. Un tipo puede correr sobre varios principios. Un principio puede ejecutarse con varios tipos. Se declaran los dos, en este orden, antes de escribir.

## Los 12 tipos

| # | Tipo | Forma | Principios que suele activar | Dato propio |
|---|---|---|---|---|
| T1 | Confesión | Admisión en primera persona de algo incómodo, con detalle verificable | P2, P4, P7 | Sin muestra en la cuenta |
| T2 | Afirmación bold | Tesis corta sin matiz, escrita para que alguien la refute | P7, P3 | 0.6x sin serie ni entregable |
| T3 | Relatabilidad | Escena cotidiana exacta que ella reconoce como suya | P4 | 3.9x, las 2am, única apertura sin fórmula que rompió en 2026 |
| T4 | Contraste o mito | Creencia aceptada + contradicción específica | P7, P6 | 9.7x en alcance, 133 comentarios. Alcance sin conversión |
| T5 | Bucle abierto | Dato parcial + pregunta específica + promesa de resolución | P9, P1 | Sin muestra limpia |
| T6 | Número + resultado + condición | Cifra propia + qué pasó + bajo qué condición | P14, P5, P6 | 25.2x y 24.0x, los dos techos de la cuenta. Casi sin uso en nicho |
| T7 | Lista prometida | N cosas concretas, N proporcional al formato | P9 | Vive en el cuerpo, no en la apertura |
| T8 | Error y aprendizaje | Qué hice mal, qué me costó, qué regla salió | P2, P11 | 4.1x (shotlist) |
| T9 | Pregunta de dolor | La pregunta que ella ya se hace, en sus palabras | P4, P9 | 1.5x, mismo tema que la fórmula a 3.1x |
| T10 | Cómo X sin Y | Resultado + fricción real que se evita | P8, P6 | Sin muestra en apertura |
| T11 | Identidad directa | Nombra el corte exacto de la micropersona | P3, P4 | 1.2x sin entregable |
| T12 | Permiso | Quita una culpa que la micropersona carga | P8, P3, P7 | 0.7x a 14.3x en 11 piezas. La varianza la explica la X y el entregable, no el gancho |

## Formato obligatorio de declaración

```
Tipo: T#, nombre
Por qué esta forma le cuadra a este principio y a este formato:
Objetivo declarado en C0 que este tipo sirve: [alcance / comentarios / saves / shares / DM]
```

Regla de conjunto: un set no repite tipo más de dos veces.

---

# C1c. Ruta de prueba. Compuerta binaria

Un gancho no se entrega si no puede declarar cómo se paga dentro de la pieza.

```
Tipo de prueba: [número propio / captura / experiencia con fecha y lugar / proceso reproducible / contraejemplo]
Dónde aparece: [segundo, escena o párrafo exacto]
Qué la hace de ella: [qué no podría decir otra persona]
```

Si no puede declarar los tres, el gancho muere aquí. No se reescribe, se descarta y se genera otro.

La prueba no puede ser el producto. "Y por eso creé mi curso" no es prueba, es venta.

---

# AQUÍ SE REDACTA

Todo lo anterior es decisión. La redacción ocurre en este punto exacto, con principio, tipo y ruta de prueba ya declarados. Se escribe con el verbatim del Language Bank como banco léxico.

Guías de redacción que este skill sí aplica al escribir (el verificador las puntúa, este skill no):

- Autonomía: problema en palabras de la audiencia, consecuencia específica, a quién le habla, en una sola unidad de sentido. Traducir jerga: "optimizar distribución" es "hacer que vean tu contenido"; "definir buyer persona" es "no sé para quién estoy creando"; "tu contenido no distribuye" es "no te están viendo".
- Léxico preciso: si existe una palabra en español que dice exactamente esa situación, se usa esa. "Te da vergüenza" y no "te sientes mal por". "Se cayó" y no "no funcionó". "Soltar" y no "dejar de hacer". "Harta" y no "cansada de".
- Sujeto nulo. El pronombre solo si hay contraste real.
- Fragmentos solo cuando yuxtaponen dos estados que se contradicen. "Publicas. Nadie responde."
- Formato por destino: reel hablado tiene que funcionar sin ver la pantalla; texto en pantalla bajo diez palabras; carrusel hace que deslice; newsletter tiene asunto y primera línea como dos ganchos distintos; colaboración manda el brief.
- CTA nativo, uno por pieza, ejecutable en el mismo lugar, sin prometer resultado. Prohibidos "dale click", "link en bio" como frase completa, "no te lo pierdas", "corre a".

---

# Entrega al verificador

Este skill no tiene puntaje. Entrega y espera.

Por cada gancho, el paquete que se entrega a `verificador/verify.py` es un archivo con este bloque exacto:

```
GANCHO: [texto]

DECLARACIÓN
Micropersona: [código]
Dolor en su voz: [texto]
Profundidad del dolor: [estructural / herramienta / mindset]
Objetivo: [alcance / comentarios / saves / shares / DM]
Entregable: [plantilla / checklist / guía / lista / link / nada]
Formato: [reel hablado / texto en pantalla / carrusel / newsletter / colaboración]
Principio primario: P#
Principio secundario: P# o ninguno
Principio terciario: P# o ninguno, con cláusula señalada
Tipo: T#
Ruta de prueba: [tipo] / [dónde] / [qué la hace de ella]
Modo de evidencia: [verbatim / proxy / hipótesis]
Verbatim usado: [frase textual, o fuente proxy citada, o "hipótesis desde Micro Persona DB"]
```

El verificador devuelve puntaje y notas. Protocolo de rerun:

- Máximo 3 reruns por gancho.
- Si el verificador marca descalificante de nivel 1, se reescribe sin gastar rerun.
- Si al tercer rerun no pasa, el gancho se descarta y se genera uno nuevo desde un principio de otra fila del mapa de vecinos.
- Este skill no discute el puntaje ni pide ver la rúbrica.

---

# Salida al cierre de sesión

Por cada gancho aprobado por el verificador:

```
[texto del gancho]

Principio: [P#, nombre] / [nombre académico] / [estado epistémico]
Tipo: [T#, nombre]
Ruta de prueba: [tipo] en [dónde] / de ella porque [qué]
Micropersona: [código]
Modo de evidencia: [verbatim / proxy / hipótesis]
Verbatim usado: [frase textual, fuente proxy, o "hipótesis"]
Verificador: [puntaje] / [reruns]
```

Al final del set:

```
Cobertura de principios: [cuáles]
Cobertura de tipos: [cuáles]
Ganchos descartados: [cuántos y en qué compuerta murieron]
Señales que faltaron: [si alguna]
```

Este bloque es lo que el protocolo de cierre de sesión escribe en Content Process: Principio Psicológico, Tipo de Gancho, Micro Persona, Hook, Verificador, más la sección "Declaración del loop" en el cuerpo. Ver 03 Alimentación del loop lento en Basecamp.

No se muestran los ganchos descartados salvo que se pidan.

---

# Skills relacionadas

- `caption-hook-writer` para texto en pantalla sin voz. Se invoca cuando el formato lo pide.
- `brand-collab-research` para la rama B de C0.
- `pulido-redaccion` para el pulido final, hasta 5 pasadas, después de que el verificador aprobó. El pulido no puede cambiar principio, tipo ni ruta de prueba. Si los cambia, se vuelve a entregar al verificador.
- Las skills de Motion MCP no se tocan ni se invocan desde aquí.
