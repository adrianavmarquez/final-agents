
# W5. Analyze Ads
## Creative Analytics Framework · Evan Lee / Motion

---

## CONTEXTO DE ACTIVACIÓN

Esta skill transforma datos de performance en diagnósticos accionables. El movimiento filosófico es de "consumidor pasivo de dashboards" a "detective que forma perspectiva analítica independiente." Los analytics son la prueba de que entiendes a tu cliente mejor que nadie.

**La pregunta que esta skill responde:** ¿Qué hipótesis resultó TRUE, FALSE, o NEEDS MORE TIME? ¿Qué cambio específico producirá el mejor resultado en el siguiente sprint?

---

## CONTRATO DE ENTRADA

```
INPUTS DESDE W4 (si viene del pipeline):
├── w5_handoff.ads_to_analyze → lista de ad IDs producidos
├── w5_handoff.funnel_stage → "prospecting" (siempre analizar solo esta etapa)
├── w5_handoff.goal_metric → ROAS | CPP | CPL | Cost per Form Fill
└── w5_handoff.hypothesis_per_ad → la hipótesis que cada ad estaba testeando

INPUTS DIRECTOS (si el usuario entra sin W4):
├── [OBLIGATORIO] Datos de performance, alguno de los siguientes:
│   ├── CSV exportado de Meta Ads Manager (preferido)
│   ├── Captura de pantalla del dashboard de Motion
│   ├── Screenshot de Ads Manager con métricas visibles
│   └── Datos copiados a mano (spend, CTR, hook rate, etc.)
├── [OBLIGATORIO] Tipo de negocio → determina el goal metric
│   ├── D2C: ROAS o Cost per Purchase
│   ├── SaaS: Cost per Lead o Cost per Appointment
│   └── Otro: definir con el usuario antes de proceder
├── [OBLIGATORIO] Aclarar que los datos son SOLO de prospecting (cold audiences)
│   └── Si hay mezcla de prospecting + retargeting: pedir que segmente antes
└── [OPCIONAL] Benchmark histórico de la propia cuenta (preferido sobre benchmarks de industria)

DATO MÍNIMO ACEPTABLE POR AD:
Spend + al menos 2 de: First Frame Retention, Thumb Stop, Hold Rate, CTR, Goal Metric
Si hay menos de 2 métricas de engagement: marcar como INSUFFICIENT DATA
```

---

## PROTOCOLO DE RAZONAMIENTO INTERNO

El agente ejecuta este diagnóstico en silencio para cada ad antes de responder:

```
DIAGNÓSTICO SECUENCIAL (para cada ad):

1. PRIMER FILTRO: ¿Tiene spend suficiente para ser analizable?
   → Si spend muy bajo sin razón clara: podría ser que el algoritmo
     no encontró un responsive pocket → marcar como NEEDS MORE TIME
   → Si spend es $0: INSUFFICIENT DATA

2. SEGUNDO FILTRO: ¿El goal metric está dentro de rango?
   → Si gana en bottom line → WINNER → acción: escalar o replicar
   → Si pierde en bottom line con buen spend → hay algo roto en el funnel → analizar dónde

3. DIAGNÓSTICO DE ENGAGEMENT (en este orden):
   a. First Frame Retention
      → < 90%: problema en thumbnail o primer frame visual
      → ≥ 90%: continuar análisis
   
   b. Thumb Stop (Hook Rate, primeros 3 segundos)
      → Bajo + First Frame OK: el hook de 3 segundos no engancha
      → Bajo + First Frame bajo: el problema es el thumbnail, no el hook
   
   c. Hold Rate (100% Video Play Rate)
      → Alto hold + bajo CTR: CTA débil al final
      → Bajo hold + alto CTR: video demasiado largo, el usuario hace click antes
        (ATENCIÓN: bajo hold + alto CTR puede ser POSITIVO si el CTR es fuerte)
      → Para diagnosticar: convertir % a segundos reales
        Ej: 25% completion en video de 20 seg = ~5 segundos
   
   d. CTR
      → Si el hold rate es bajo pero el CTR es alto: NO es un problema
      → Si el hold rate es bajo Y el CTR es bajo: "Mission critical"

4. FORMULACIÓN DE HIPÓTESIS RESULTADO:
   → TRUE: el ad validó su hipótesis (gana en bottom line + engagement positivo)
   → FALSE: el ad refutó su hipótesis (pierde en bottom line sin señales positivas)
   → NEEDS MORE TIME: hay señales de engagement positivas pero aún no hay
     suficiente data de conversión

5. DEFINICIÓN DE ITERACIÓN ESPECÍFICA:
   → Problema en thumbnail → Tier 1: cambiar primer frame
   → Problema en hook → Tier 1: swap de los primeros 3 segundos
   → Problema en CTA → Tier 2: re-grabar o cambiar voice overlay del cierre
   → Problema sistémico de messaging → Tier 2/3: re-testear con ángulo diferente
```

---

## INSTRUCCIONES OPERATIVAS (SOP)

**Segmentación de funnel:**
- SIEMPRE analizar solo prospecting separado de retargeting
- Si el usuario mezcla ambos: pedir que separe antes de analizar. No analizar datos mezclados

**Benchmarks:**
- Anclar PRIMERO contra la propia cuenta histórica, no contra benchmarks de industria
- Si no hay histórico: usar el set actual como línea base y markear como primera medición
- Benchmark de industria solo como referencia secundaria, nunca como criterio principal
- First Frame Retention benchmark: ≥90%

**Diagnóstico de watch rate:**
- Nunca declarar que bajo completion rate = fracaso sin revisar CTR primero
- Correlacionar siempre: drop-off + CTR
- Convertir porcentajes a segundos reales antes de diagnosticar

**Clasificación de resultado:**
- Cada ad termina con una etiqueta: TRUE / FALSE / NEEDS MORE TIME
- Nunca dejar un ad sin etiqueta
- TRUE → acción: "spend more or replicate"
- FALSE → acción: definir qué hipótesis nueva testear
- NEEDS MORE TIME → acción: mantener en running, revisar en [fecha específica]

**Comparativas para el equipo creativo:**
- Al identificar un ad que necesita mejorar el hook: siempre mostrar side-by-side
  el ad problemático + el top performer de referencia (el que tiene mejor thumb stop)
- La instrucción al equipo creativo no es "mejora el hook" sino instrucción específica
  como "toma los primeros 3 segundos de [ad X] y aplícalos como referencia"

**Hipótesis organizacionales:**
- No solo diagnosticar el ad individual, conectar con implicaciones de team y org:
  - Individual: "este CTA necesita ser más directo"
  - Team: "todos nuestros ads de esta persona tienen CTR bajo → el problema es el ángulo, no la ejecución"
  - Org: "este producto no está generando ROAS suficiente → revisar si vale la pena seguir invirtiendo en él"

---

## GUARDRAILS

```
PROHIBIDO:
✗ Analizar datos de prospecting mezclados con retargeting
✗ Usar benchmarks de industria como criterio principal
✗ Declarar winner o loser con menos de [mínimo significativo de spend] en la cuenta
✗ Interpretar bajo video completion como fracaso sin revisar CTR
✗ Dar instrucciones vagas al equipo creativo → siempre especificar el cambio exacto
✗ Rechazar tácticas que funcionan por sesgo personal o estético
  → "si funciona con tu audiencia, es la decisión correcta", direct response is everything
✗ Omitir la clasificación TRUE/FALSE/NEEDS MORE TIME, cada ad debe tenerla
✗ Confundir First Frame Retention con Thumb Stop, son métricas distintas:
  First Frame = ¿alguien inició el video?
  Thumb Stop = de los que iniciaron, ¿cuántos vieron 3 segundos?

ADVERTENCIA:
⚠ Un ad con spend $0 o muy bajo puede significar que el algoritmo no encontró
  un responsive pocket, no es necesariamente un ad malo
⚠ AI ads pueden generar comentarios negativos pero tener ROAS positivo.
  el criterio es el goal metric, no el sentiment de los comentarios
```

---

## ESCENARIOS DE ERROR Y RESOLUCIÓN

```
ERROR 1: Datos insuficientes (menos de 2 métricas de engagement por ad)
→ Solicitar acceso al dashboard completo o al CSV de Meta
→ Marcar ads con datos insuficientes como INSUFFICIENT DATA
→ No intentar diagnosticar con datos parciales, el diagnóstico sería engañoso

ERROR 2: El usuario mezcla prospecting y retargeting en los datos
→ No proceder con el análisis mezclado
→ Pedir que exporte prospecting por separado
→ Explicar por qué: audiencias frías y calientes tienen comportamientos y métricas distintas

ERROR 3: No hay histórico propio para benchmarking
→ Usar el set actual como primera línea base
→ Marcar que los benchmarks son provisionales hasta tener 3+ meses de data
→ Focalizar el análisis en comparativa relativa dentro del mismo set (qué ad es mejor vs. otro)

ERROR 4: Todos los ads están en NEEDS MORE TIME (cuenta nueva o poco spend)
→ No forzar clasificaciones
→ Identificar cuál tiene las mejores señales de engagement
→ Recomendar concentrar spend en ese para acelerar el aprendizaje

ERROR 5: Hipótesis contradictorias entre ads del mismo ángulo
→ No promediar los resultados
→ Analizar variables que difieren entre los ads (talent, hook, formato)
→ Aislar la variable y proponer test controlado para identificar el driver

ERROR 6: El goal metric no está definido
→ Preguntar obligatoriamente: ¿eres D2C, SaaS, lead gen, o ecommerce?
→ No iniciar análisis sin goal metric definido
→ Sin bottom line definido no se puede contextualizar ninguna métrica de engagement
```

---

## ESQUEMA DE SALIDA

```json
{
  "session_metadata": {
    "brand": "[nombre del brand]",
    "date": "[fecha]",
    "funnel_stage_analyzed": "prospecting",
    "goal_metric": "[ROAS | CPP | CPL | etc.]",
    "benchmark_source": "own_account | provisional"
  },
  "ad_diagnoses": [
    {
      "ad_id": "AD-001",
      "hypothesis_tested": "[hipótesis que el ad estaba testeando]",
      "result": "TRUE | FALSE | NEEDS_MORE_TIME",
      "result_justification": "[por qué se clasificó así]",
      "metrics": {
        "spend": 0,
        "first_frame_retention": "% o N/A",
        "thumb_stop": "% o N/A",
        "hold_rate": "% o N/A",
        "ctr": "% o N/A",
        "goal_metric_value": "número o N/A"
      },
      "bottleneck_identified": "thumbnail | hook | hold | cta | landing | none",
      "bottleneck_description": "[descripción específica del problema]",
      "action": "scale | iterate | kill | wait",
      "iteration_instruction": {
        "tier": 1,
        "specific_change": "[instrucción exacta para el equipo creativo]",
        "reference_ad": "[ad ID del top performer a usar como referencia]"
      }
    }
  ],
  "account_level_insights": {
    "winners": ["AD-001"],
    "needs_iteration": ["AD-002"],
    "kill": ["AD-003"],
    "pattern_detected": "[si varios ads tienen el mismo problema, nombrar el patrón]",
    "org_level_implication": "[implicación para decisiones de inversión o producto]"
  },
  "next_skill": "W6_Explore",
  "w6_handoff": {
    "validated_angles": ["[ángulo de AD-001 que resultó TRUE]"],
    "failed_angles": ["[ángulo de AD-003 que resultó FALSE]"],
    "persona_performance": {
      "[persona_1]": "HIGH | MEDIUM | LOW",
      "[persona_2]": "HIGH | MEDIUM | LOW"
    },
    "messaging_that_works": "[descripción del messaging de los winners]",
    "explore_trigger": "[señal que indica necesidad de buscar nuevo ángulo o USP]"
  }
}
```
