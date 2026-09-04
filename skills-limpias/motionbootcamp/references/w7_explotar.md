
# W7. Exploit Winning Ads
## Fase Exploit del Sprint Creativo · Sophia Beauvoir (Ready Set) + Viti Videtta (Happy Mammoth) + Janae LeVander (Caraway)

---

## CONTEXTO DE ACTIVACIÓN

Ya tienes un winner validado. El objetivo ahora es escalarlo sin asfixiarlo. En el mundo post-Andromeda, las reglas del scaling cambiaron: cambios menores (solo el hook, solo un overlay) no generan señal creativa nueva suficiente para el algoritmo. Se necesita variación significativa.

**El concepto central:** Ad Families. Un winner no se corre hasta la muerte, se convierte en el centro de una familia de ads que previene la fatiga y expande el reach.

**Referencia de escala real:** Happy Mammoth produce ~500 ads/semana. Caraway tiene ~360 ads UGC activos en 2026. El sistema que produce esto no es talento, es arquitectura.

---

## CONTRATO DE ENTRADA

```
INPUTS DESDE W6 (si viene del pipeline):
├── w7_handoff.validated_hypothesis → la hipótesis que el test validó
├── w7_handoff.winning_ad_from_explore → el ad con mejor señal para escalar
├── w7_handoff.messaging_angles_to_test → ángulos de messaging a multiplicar
├── w7_handoff.persona_to_expand → persona adicional detectada en el test
└── w7_handoff.scale_trigger → métrica que autorizó el escalado

INPUTS DIRECTOS (si el usuario entra sin W6):
├── [OBLIGATORIO] El winning ad a escalar (asset o descripción detallada)
│   └── El agente debe preguntar: ¿qué hace que este ad sea el winner?
│      (script, talent, hook, formato, persona, identificar el driver)
├── [OBLIGATORIO] Métricas del winner: CPA estable + CTR fuerte + spend acelerando
│   └── Sin estas 3 condiciones: verificar si realmente es un winner o NEEDS MORE TIME
├── [RECOMENDADO] Footage library disponible (para visual refreshes sin nuevo rodaje)
├── [RECOMENDADO] Pool de creators disponibles (para talent refreshes)
└── [OPCIONAL] Budget y timeline de producción

CRITERIO DE WINNER VÁLIDO (verificar antes de escalar):
□ CPA estable
□ CTR fuerte o engagement sano
□ Corriendo en múltiples audiencias (no solo una)
□ Spend acelerando
□ ROAS dentro de rango
Si no cumple los 5: marcar como "posible winner" y recomendar más data antes de escalar masivamente

COLOR TAG DEL WINNER (Happy Mammoth):
→ VERDE (Massive Winner): cumple los 5 criterios → hacer los swings más grandes
→ SCALE UP (doing great but not massive): cumple 3-4 → swings pequeños primero
```

---

## PROTOCOLO DE RAZONAMIENTO INTERNO

```
PASO 1. Deconstruir el winner en sus componentes
  ↳ Hook: ¿cuáles son los primeros 3 segundos? ¿visual hook o copy hook?
  ↳ Angle: ¿cuál es el ángulo estratégico del ad? (dolor, aspiración, mecanismo, etc.)
  ↳ Format: ¿UGC, voiceover testimony, static, GIF, carousel?
  ↳ Emotional driver: ¿qué emoción activa? (inseguridad + esperanza, urgencia, etc.)
  ↳ Determinar: ¿cuál de estos 4 elementos es el DRIVER del performance?

PASO 2. Clasificar el winner (Color Tag)
  ↳ ¿Cumple los 5 criterios de winner válido? → VERDE o SCALE UP
  ↳ VERDE: diseñar los swings más grandes
  ↳ SCALE UP: empezar con swings pequeños para verificar si puede llegar a verde

PASO 3. Diseñar Easy Scales (Low-Hanging Fruit)
  ↳ Visual refreshes con footage existente en la library
  ↳ Talent refreshes con nuevo creator + mismo script
  ↳ Format testing del mismo messaging (static → video → carousel → GIF)
  ↳ Testing de longitudes de video (30s → 60s → 90s)
  ↳ Testing de orden de mensajes (¿qué pasa si el CTA va primero?)
  ↳ ATENCIÓN: en post-Andromeda, solo cambiar el hook NO genera señal suficiente

PASO 4. Diseñar Expansion Phase (Higher-Lift)
  ↳ Nuevo talent + diferente background + nueva estructura narrativa
  ↳ Persona testing: mismo script → nueva persona demográfica
  ↳ Mashup de winners: combinar thumb stop fuerte de AD-A + CTA fuerte de AD-B
  ↳ Nuevo ángulo del mismo producto (sleep / anxiety / focus en el caso de Calm)

PASO 5. Construir la Ad Family
  ↳ Mapear todas las iteraciones alrededor del winner base
  ↳ Definir cuántos batches: 3-5 batches de 3-5 ads cada uno
  ↳ 80% del scaling está en: hooks diferentes, mismo script diferentes creators,
     diferentes scripts mismo creator, mismo concepto diferente formato

PASO 6. Para programa UGC (Caraway method):
  ↳ ¿Hay equipo cross-funcional? Definir roles: Performance Creative / Influencer / Growth
  ↳ ¿Hay pool de creators? Segmentar: Core Persona Retainers vs. Expansion Creators
  ↳ Organizar por Content Buckets: Evergreen / Product Launches / Seasonal
  ↳ Para cada concepto: completar Concept Formula antes del brief

PASO 7. Planificar el Refresh (Version 2.0)
  ↳ El refresh se activa cuando: el winner fatiga Y todas las iteraciones dejan de funcionar
  ↳ "Terminator 1 y 2": el alma del ad debe ser reconocible, el script/visuals son nuevos
  ↳ Definir de antemano: ¿qué métrica en qué umbral indica fatiga?
```

---

## INSTRUCCIONES OPERATIVAS (SOP)

**Reglas post-Andromeda:**
- Solo cambiar el hook o un text overlay NO es suficiente para generar nueva señal creativa
- Alternativas de iteración significativa: visual refresh + talent refresh + format pivot + persona pivot + length test + message order test
- El algoritmo también diferencia por cambios semánticos: persona diferente, pain point diferente, on-ramp diferente, body copy diferente
- Si un ad no gasta: NO es rechazo. El algoritmo no encontró un responsive pocket para esa señal. Cambiar targeting, persona, o estructura del ad

**Easy Scales (hacer primero):**
1. Visual refresh: reemplazar shots con footage existente, mismo script
2. Talent refresh: nuevo creator + mismo script exacto
3. Single vs. multi-talent: testear si un creator outperforma mashups
4. Format testing: animated GIF → UGC → green screen → toggle animado
5. Length testing: ¿funciona mejor a 15 segundos o a 60?

**Expansion Phase (después de agotar Easy Scales):**
1. Nuevo talent + diferente background + diferente estructura narrativa
2. Mismo script → nueva persona demográfica (ej: grad reciente → padre con hijo universitario)
3. Mashup: tomar thumb stop de AD-A + CTA de AD-B → crear "super ad"
4. Nuevo ángulo del mismo beneficio (weight loss → energy → metabolism)

**Footage Library:**
- Cada shoot debe producir shots reutilizables para futuras iteraciones
- Definir "shots canónicos" basados en learnings: "anytime we work with a couple, request a dancing shot"
- La library permite refreshear conceptos múltiples veces antes de la fatiga

**Programa UGC estructurado (Caraway method):**
- Core Persona Retainers = mayoría del pool: creators que matchan las personas con mejor conversión
- Expansion Creators = minoría: ligeramente fuera de la persona core, abren audiencias nuevas
- Post-Andromeda: niches específicos > categorías generales ("biohacker que enfoca en macros" > "gym person")
- Content Buckets: Evergreen/BAU (siempre activos), Product Launches, Seasonal
- Proceso de research pre-briefing: ¿qué funcionó el año pasado? ¿qué funciona en el wild ahora? ¿cuál es la hipótesis? ¿cuál es el nivel de convicción?

**Concept Formula (obligatoria antes de cada brief):**
```
CONCEPT FORMULA:
1. Concept Title: [nombre corto del concepto]
2. Angle (Why This Works): [social proof | problem solution | mechanism | etc.]
3. Creative Guardrails: [delivery, tono, lo que NO hacer]
   Ej: "deadpan delivery, sarcastic drawbacks framed as benefits"
4. Objection Handling: [anticipar la objeción más común y reframearla]
   Ej: "too expensive" → "it's not cheap because I wanted something that would last"
```

**Cuándo hacer el Refresh (Version 2.0):**
- Solo cuando: winner fatiga (métricas caen) + todas las iteraciones dejaron de funcionar
- El Refresh no es un ad nuevo, es el mismo ad con nueva producción
- "El alma del ad debe sentirse como el winner anterior, aunque todo lo visual y el script sean nuevos"
- Analogía operativa: Terminator 1 y Terminator 2, reconocible, evolucionado

---

## GUARDRAILS

```
PROHIBIDO:
✗ Escalar antes de verificar los 5 criterios de winner válido
✗ Considerar "solo cambiar el hook" como iteración suficiente post-Andromeda
✗ Pensar que solo cambios visuales diferencian al ad para Andromeda →
  cambios de copy, persona, pain point y on-ramp también funcionan
✗ Interpretar que un ad que no gasta es un ad rechazado →
  es una señal de que no encontró responsive pocket, no de que el ad sea malo
✗ Copiar ads de competidores directamente (W4 lo aclara: extraer DNA, no clonar)
✗ Parar con la primera idea en el proceso de ideación original (Viti) →
  generar mínimo 5-10 combinaciones antes de elegir
✗ Hacer el Refresh antes de agotar las iteraciones →
  el Refresh es el último recurso, no la respuesta automática a la fatiga
✗ Escalar a 500 ads/semana sin un sistema (Brand Cards, Agents, Templates de W4) →
  sin sistema, el volumen produce inconsistencia, no performance

REGLA DE ORO DE IDEACIÓN (Viti):
✗ Nunca producir la primera idea que llega
→ La creatividad es un proceso mecánico:
  Gather (inputs específicos + generales) → Mental Mashup (forzar combinaciones) →
  Eureka (idea específica, no genérica) → Validar con 3 criterios → Producir

CRITERIOS DE VALIDACIÓN DE IDEA ORIGINAL:
1. "Feels true" → el target diría "eso soy yo"
2. Específica, no genérica → no puede decirla cualquier marca
3. Ángulo fresco → no es solo un claim mejorado, es una perspectiva nueva
Si no cumple los 3: volver al Mental Mashup, no publicar
```

---

## ESCENARIOS DE ERROR Y RESOLUCIÓN

```
ERROR 1: El "winner" no cumple los 5 criterios de winner válido
→ No escalar todavía
→ Identificar qué criterio falta: ¿es el CPA inestable? ¿está corriendo en pocas audiencias?
→ Recomendar continuar la fase de validación con el criterio faltante como objetivo

ERROR 2: Cambios menores no generan performance post-Andromeda
→ Escalar al siguiente nivel de iteración: si hiciste visual refresh → pasar a talent refresh
→ Si hiciste talent refresh → pasar a persona testing o format testing
→ Si todo eso falló: es señal de que el winner se está fatigando → iniciar Refresh (V2.0)

ERROR 3: Todos los ads de la family están fatigando al mismo tiempo
→ El winner llegó a su límite de escala con ese concepto
→ Iniciar Refresh (V2.0): mismo alma, nueva producción completa
→ Si el Refresh tampoco funciona: volver a W6_Explore para nuevo USP

ERROR 4: El programa UGC no tiene creators suficientes
→ Distinguir: ¿falta de cantidad o falta de calidad?
→ Si falta cantidad: ampliar pool con Expansion Creators (fuera de la persona core)
→ Si falta calidad: revisar proceso de vetting, ajustar brief y guardrails creativos
→ Post-Andromeda: priorizar creators con niche específico sobre creators genéricos

ERROR 5: El equipo produce muchos ads pero sin sistema (sin Concept Formula)
→ Implementar Concept Formula como gate obligatorio antes de cada brief
→ Sin Concept Formula completada: no se aprueba el brief para producción

ERROR 6: La idea que el agente propone es genérica
→ Verificar contra los 3 criterios de validación de Viti
→ Si falla criterio 2 (específica): hacer el Mental Mashup de nuevo con más inputs generales
→ Ejemplo correcto: "Tu cerebro tiene 47 tabs abiertos. El magnesio los cierra todos."
→ Ejemplo incorrecto: "El magnesio reduce la ansiedad y te ayuda a dormir."

ERROR 7: El usuario quiere escalar a volumen alto sin tener el sistema de W4
→ No bloquear, pero documentar el riesgo:
  "Escalar a alto volumen sin Brand Cards, Format Templates y Agents produce
  inconsistencia de marca y CPMs más altos por menor relevancia."
→ Recomendar invertir en el setup del sistema de W4 antes de escalar a >20 ads/semana
```

---

## ESQUEMA DE SALIDA

```json
{
  "session_metadata": {
    "brand": "[nombre del brand]",
    "date": "[fecha]",
    "winner_ad_id": "[ad ID del winner base]",
    "color_tag": "VERDE | SCALE_UP",
    "driver_identified": "script | talent | hook | format | emotional_driver"
  },
  "winner_deconstruction": {
    "hook": "[descripción de los primeros 3 segundos]",
    "angle": "[ángulo estratégico]",
    "format": "[tipo de ad]",
    "emotional_driver": "[emoción que activa]",
    "persona": "[persona target]"
  },
  "ad_family": {
    "easy_scales": [
      {
        "ad_id": "SCALE-001",
        "iteration_type": "visual_refresh | talent_refresh | format_test | length_test",
        "change_made": "[descripción del cambio específico]",
        "what_stays_same": "[elementos que no cambian]",
        "andromeda_signal": "[por qué este cambio genera señal nueva para el algoritmo]"
      }
    ],
    "expansion_phase": [
      {
        "ad_id": "EXPAND-001",
        "iteration_type": "persona_pivot | new_angle | mashup | net_new_concept",
        "change_made": "[descripción del cambio significativo]",
        "new_element": "[nuevo talent | nueva persona | nuevo ángulo]",
        "what_stays_same": "[elementos del winner que se preservan]"
      }
    ],
    "total_ads_planned": 0,
    "batches": [
      {
        "batch_number": 1,
        "ads": ["SCALE-001", "SCALE-002", "SCALE-003"],
        "batch_focus": "[qué se está testeando en este batch]"
      }
    ]
  },
  "ugc_program": {
    "activated": false,
    "team_structure": {
      "performance_creative": "[responsabilidades]",
      "influencer_team": "[responsabilidades]",
      "growth_media": "[responsabilidades]"
    },
    "creator_pool": {
      "core_persona_retainers": "[descripción del perfil]",
      "expansion_creators": "[descripción del perfil]",
      "niche_focus_post_andromeda": "[niche específico, no categoría general]"
    },
    "content_buckets": {
      "evergreen_bau": "[temas core]",
      "product_launches": "[launches próximos]",
      "seasonal": "[fechas relevantes]"
    }
  },
  "concept_formulas": [
    {
      "concept_title": "[nombre]",
      "angle": "[por qué funciona]",
      "creative_guardrails": "[tono, delivery, restricciones]",
      "objection_handling": "[objeción anticipada → reframe]"
    }
  ],
  "refresh_plan": {
    "fatigue_signal": "[métrica y umbral que indica fatiga]",
    "refresh_trigger": "winner fatigues AND all iterations stop working",
    "refresh_brief": "[descripción de V2.0: mismo alma, nueva producción]"
  },
  "footage_library_additions": [
    "[shot canónico a pedir en el próximo rodaje basado en learnings]"
  ],
  "pipeline_complete": true,
  "next_cycle": "W3_Prioritize_Ad_Ideas",
  "w3_rediagnosis_trigger": "[señal que indica que el diagnóstico de marca debe actualizarse]"
}
```
