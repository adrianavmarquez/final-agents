
# W3. Prioritize Ad Ideas
## De Research a Estrategia Accionable · Framework Dara Denny

---

## CONTEXTO DE ACTIVACIÓN

Esta skill resuelve el problema de **parálisis por análisis**: equipos que tienen research pero no saben qué producir primero ni por qué. El output de esta skill es el contrato estratégico que autoriza producción en W4.

**No activar** si el usuario ya tiene un roadmap definido y solo quiere producir (ir directo a W4).

---

## CONTRATO DE ENTRADA

El agente debe verificar estos inputs ANTES de proceder. Si falta alguno, pedirlo explícitamente antes de avanzar.

```
INPUTS REQUERIDOS:
├── [OBLIGATORIO] CSV o lista de reviews del cliente (mínimo 50 reviews)
│   └── Si no existe: pedir URL del producto para extraer reviews con Claude Co-Work
├── [OBLIGATORIO] URL de la Meta Ads Library del brand o competidor
│   └── Alternativa: capturas de pantalla de los top ads actuales
├── [RECOMENDADO] Objetivo de negocio del trimestre (crecimiento, nuevo producto, etc.)
└── [OPCIONAL] Budget estimado de producción (afecta el tier de edits recomendado)

INPUTS QUE HACEN CAMBIAR EL ANÁLISIS:
- Budget bajo → priorizar Tier 1 edits (hooks, text overlays) sobre producciones nuevas
- Marca nueva (<6 meses de ads) → no hay data de winners, priorizar testing amplio
- Producto nuevo → activar protocolo Harry's (ver Guardrails)
```

---

## PROTOCOLO DE RAZONAMIENTO INTERNO

El agente ejecuta estos pasos en silencio antes de producir cualquier output:

```
PASO 1. Analizar ads actuales
  ↳ ¿Qué personas parecen estar siendo targetadas desde los ads?
  ↳ ¿Qué awareness level dominan? (TOF, MOF, BOF)
  ↳ ¿Hay concentración en una sola persona? ¿Hay partnership ads?

PASO 2. Extraer personas reales desde reviews
  ↳ Identificar 5 personas por trigger/problema, rankeadas por:
     (a) Volumen: ¿cuántas reviews mencionan este trigger?
     (b) Intensidad emocional: ¿cuán fuerte es el lenguaje?
  ↳ Verificar que cada persona tenga al menos 3 citas reales de reviews

PASO 3. Mapear el GAP
  ↳ ¿Quién compra (reviews) vs. quién aparece en los ads?
  ↳ El gap = la mayor oportunidad estratégica no explotada

PASO 4. Formular el Diagnóstico
  ↳ Un statement de 1-2 oraciones que explique el "why" detrás de qué producir
  ↳ Ejemplos válidos:
     - "Este brand necesita más TOF para refill del funnel paid"
     - "Toda la producción está en una sola persona → abrir nueva audiencia"
     - "Hay learnings ganadores que no se están duplicando suficiente"

PASO 5. Clasificar ideas por Evidence Ranking
  ↳ HIGH CONFIDENCE: formatos/messaging/creators ya pressure-tested con data
  ↳ LOW CONFIDENCE: "el competidor lo lleva corriendo X días" (puede estar en retargeting),
                    ideas sin conexión a persona, research o awareness level
  ↳ RECHAZAR si la única evidencia es running time del competidor sin contexto

PASO 6. Construir Roadmap
  ↳ Priorizar 1-2 personas, no las 5 simultáneamente
  ↳ Asignar tier de edit a cada idea (1/2/3)
  ↳ Separar what to start NOW (week 1-2) vs. what goes to icebox
```

---

## INSTRUCCIONES OPERATIVAS (SOP)

Reglas directas extraídas del transcript. El agente las aplica sin excepción.

**Personas:**
- Si persona de ads ≠ persona de reviews → marcar como GAP ESTRATÉGICO, es la primera recomendación
- Si persona tiene alta intensidad emocional pero bajo volumen → marcar como HIGH PRIORITY TEST
- Siempre pedir al modelo que pruebe cada persona con citas específicas de reviews. Si no puede citar, la persona es inválida
- Máximo 5 personas. Priorizar 1-2 para acción inmediata

**Diagnóstico:**
- El diagnóstico debe ser 1-2 oraciones máximo
- Debe responder: ¿qué necesita este brand HACER con sus ads ahora mismo?
- Se rediagnostica quarterly. Si el usuario tiene diagnóstico del trimestre anterior, comparar

**Evidence Ranking:**
- Si el usuario presenta una idea cuya única evidencia es "el competidor lo tiene corriendo mucho tiempo": RECHAZAR con explicación → ese ad puede estar buried en retargeting
- Si idea tiene data propia de performance: HIGH CONFIDENCE
- Si idea conecta persona + awareness level + research = HIGH CONFIDENCE
- Si idea es intuición sin respaldo: LOW CONFIDENCE → va al icebox, no al sprint

**Roadmap:**
- Estructura siempre en 4 partes: Creators / Icebox / Quarterly / Monthly
- Icebox: todas las ideas sin filtro. Nadie es juzgado por lo que pone ahí
- Quarterly: mapear holidays, launches, personas asignadas a momentos del año
- Monthly: idea + persona target + 3 variaciones de messaging
- Las ideas del sprint inmediato (low hanging fruit) deben poder producirse en ≤1 semana

**Tiers de edits:**
- Tier 1 (Iteration): hook swap, text overlay → <1 semana
- Tier 2 (Post-production): cambio de voice overlay, nuevo messaging → 1-2 semanas
- Tier 3 (Producción nueva): nuevo creator con formula ganadora → 2-4 semanas

---

## GUARDRAILS

```
PROHIBIDO:
✗ Recomendar 5 personas para testing simultáneo, máximo 1-2 activas
✗ Usar running time de competidor como evidencia principal de una idea
✗ Asumir que el mismo playbook funciona para un producto nuevo sin research
  (Protocolo Harry's: producto nuevo = customer research desde cero)
✗ Priorizar creatividad sobre evidencia, si hay duda entre idea original vs.
  duplicar lo que ya funciona, duplicar primero
✗ Incluir ads promocionales no-evergreen (Mother's Day, Black Friday statics)
  en el roadmap core, esos van a un proceso MVP separado
✗ Saltarse el paso de citar reviews para validar personas, el AI puede inventar
  personas que no existen en los datos reales
✗ Producir roadmap sin diagnóstico, sin diagnóstico no hay estrategia, hay testing aleatorio

ADVERTENCIA ACTIVA:
⚠ Si el usuario tiene poco presupuesto → priorizar Tier 1 y Tier 2 únicamente
⚠ Si la marca tiene <6 meses de data → declarar ausencia de winners, recomendar
  testing amplio antes de duplicar
⚠ Si hay conflicto entre lo que el cliente quiere hacer y lo que la data sugiere:
  presentar ambas opciones con razonamiento, no suprimir la recomendación data-driven
```

---

## ESCENARIOS DE ERROR Y RESOLUCIÓN

```
ERROR 1: Reviews insuficientes (<50)
→ Solicitar acceso a reviews adicionales (Google, Trustpilot, Amazon, comentarios de social)
→ Si imposible: marcar personas como HIPÓTESIS no validada, proceder con advertencia

ERROR 2: No hay data de performance propia (cuenta nueva)
→ Cambiar modo: no hay winners a duplicar
→ Recomendar testing amplio de 3-5 ángulos distintos en Tier 1
→ Usar ad library de competidores SOLO como inspiración de formato, no como evidencia

ERROR 3: El cliente insiste en una idea de LOW CONFIDENCE
→ No bloquear. Colocar en roadmap con etiqueta HYPOTHESIS/LOW EVIDENCE
→ Recomendar testearla con el menor costo de producción posible (Tier 1)
→ Definir métrica de validación antes de producir

ERROR 4: Gap persona muy grande (ads targeting A, compra B completamente diferente)
→ No recomendar cambio total inmediato
→ Proponer split: 70% continuar con persona actual (no romper lo que funciona),
  30% abrir persona real de reviews (exploración controlada)

ERROR 5: Producto nuevo en catálogo existente
→ Activar Protocolo Harry's explícitamente:
  - No asumir que el playbook del producto anterior aplica
  - Investigar si el comprador es el mismo
  - Validar que el lenguaje del cliente resuene (no usar términos técnicos que el target no conoce)
  - Testear con 3 ads de bajo costo antes de escalar
```

---

## ESQUEMA DE SALIDA

El output de esta skill es un JSON estructurado que sirve como input directo para W4_MakeAds.

```json
{
  "session_metadata": {
    "brand": "[nombre del brand]",
    "date": "[fecha]",
    "diagnosis": "[1-2 oraciones del diagnóstico de marca]",
    "diagnosis_confidence": "HIGH | MEDIUM | LOW",
    "next_diagnosis_review": "[fecha trimestral]"
  },
  "persona_analysis": {
    "ad_personas": [
      {
        "name": "[nombre descriptivo]",
        "description": "[1 oración]",
        "evidence": "ads_library"
      }
    ],
    "real_personas": [
      {
        "name": "[nombre basado en trigger]",
        "trigger": "[problema específico que causó la compra]",
        "volume_rank": 1,
        "emotional_intensity": "HIGH | MEDIUM | LOW",
        "supporting_quotes": ["[cita 1 de review]", "[cita 2 de review]"],
        "in_current_ads": true
      }
    ],
    "gap_detected": true,
    "gap_description": "[descripción del gap entre persona de ads vs. persona real]",
    "priority_personas": ["[persona_1]", "[persona_2]"]
  },
  "roadmap": {
    "icebox": [
      {
        "idea": "[descripción de la idea]",
        "persona": "[persona target]",
        "evidence_level": "HIGH | LOW",
        "tier": 1
      }
    ],
    "sprint_now": [
      {
        "idea": "[descripción]",
        "persona": "[persona target]",
        "messaging_variations": ["[hook 1]", "[hook 2]", "[hook 3]"],
        "tier": 1,
        "evidence": "[por qué esta idea tiene evidencia sólida]",
        "production_time": "< 1 semana"
      }
    ],
    "quarterly_calendar": {
      "Q1": "[personas y temas asignados]",
      "Q2": "[personas y temas asignados]"
    }
  },
  "next_skill": "W4_MakeAds",
  "w4_handoff": {
    "priority_ideas": ["[idea 1 con mayor evidencia]", "[idea 2]"],
    "priority_personas": ["[persona 1]", "[persona 2]"],
    "reference_ads": "[URLs o descripciones de ads ganadores existentes a usar como referencia]",
    "format_recommendation": "UGC | Static | Video | Mix",
    "tier_recommendation": 1
  }
}
```
