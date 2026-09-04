
# W4. Make Ads
## Producción de Creativos con AI · Framework Will Sartorius

---

## CONTEXTO DE ACTIVACIÓN

Esta skill convierte ideas priorizadas en ads reales usando un stack de AI. Hay 3 métodos con diferentes hit rates y tiempos de producción. El agente selecciona el método correcto según el contexto del usuario.

**Método Quick Win (60-70% hit rate):** clonar + repurpose en <2 horas  
**Método Escalable (90-95% hit rate):** sistema con Brand Cards + Agents, setup inicial de 4-6 horas  
**Método Animación:** convertir static ganador a GIF, reduce CPMs  

---

## CONTRATO DE ENTRADA

```
INPUTS DESDE W3 (si viene del pipeline):
├── w4_handoff.priority_ideas → ideas a producir con evidencia validada
├── w4_handoff.priority_personas → persona(s) a targetar
├── w4_handoff.reference_ads → ads propios ganadores para brand reference
├── w4_handoff.format_recommendation → tipo de ad recomendado
└── w4_handoff.tier_recommendation → tier de edit (1/2/3)

INPUTS DIRECTOS (si el usuario entra sin W3):
├── [OBLIGATORIO] Ad de competidor a clonar O idea propia a producir
├── [OBLIGATORIO] URL del brand + nombre del producto + descripción del producto
├── [OBLIGATORIO] 2-3 ads propios con fonts y colores visibles (para brand reference)
│   └── Si no existen: pedir brand guidelines en PDF o URL del sitio web
├── [OBLIGATORIO para animación] Static ad que se quiere animar
└── [OPCIONAL] Budget y plataforma destino (Meta 9:16, 1:1, 4:5)

VERIFICACIÓN PREVIA:
→ ¿El usuario tiene acceso a Fal.ai? Si no: explicar que es la plataforma de ejecución
→ ¿El usuario tiene Claude Desktop o Claude Code? Para el sistema escalable es necesario
→ ¿El ad existente es un static o video? Determina el método de animación
```

---

## PROTOCOLO DE RAZONAMIENTO INTERNO

```
PASO 1. Seleccionar método según contexto
  ↳ ¿El usuario quiere un resultado RÁPIDO y tiene ad de referencia?
     → Quick Win Method (pasos 1-6)
  ↳ ¿El usuario quiere producir VOLUMEN (10+ ads) con consistencia de marca?
     → Sistema Escalable (pasos 12-21)
  ↳ ¿El usuario tiene un static GANADOR y quiere más reach a menor CPM?
     → Método Animación (pasos 7-11)
  ↳ ¿El usuario quiere el mismo winning ad en DIFERENTES FORMATOS?
     → Multiplicación de formatos (paso 21)

PASO 2. Verificar brand assets disponibles
  ↳ ¿Hay Brand Spec Card (imagen con fonts/colores)? Si no → generarla primero
  ↳ ¿Hay 2-3 ads propios de referencia visual? Si no → pedir antes de generar prompt
  ↳ ¿Hay brand guidelines en PDF? → convertir a markdown antes de subir a Claude

PASO 3. Determinar la longitud del prompt de NanoBanana 2
  ↳ Target: 1,000-1,500 palabras. Nunca menos de 800, nunca más de 2,000
  ↳ Si el prompt es corto → NanoBanana 2 llenará los huecos de forma impredecible

PASO 4. Para animación: definir frame structure
  ↳ ¿El static existente es start frame o end frame?
  ↳ Generar el frame faltante con NanoBanana 2 antes de ir a Veo
  ↳ Preparar JSON prompt para Veo 3.1 (NO text-based prompt)
```

---

## INSTRUCCIONES OPERATIVAS (SOP)

### QUICK WIN METHOD

**Paso 1. Encontrar ad a clonar:**
- Usar Motion o Meta Ads Library
- Criterio de selección: top impressions en categoría relevante o misma industria

**Paso 2. Deconstruir con Claude:**
```
PROMPT DE DECONSTRUCCIÓN:
"Analiza este ad y extrae su DNA visual:
- Ad format (static/video/carousel/GIF)
- Copy structure y hierarchy
- Layout y composición
- Background y ambiente
- Typography (jerarquía visual, tamaños relativos)
- Visual devices (íconos, arrows, overlays, badges)
- Color palette (roles de cada color)
- Spacing y balance
NO interpretes el messaging. Describe solo los elementos visuales."
```

**Paso 3. Adaptar al brand:**
- En el mismo chat: "Reworkea este DNA visual para [brand name]. URL: [url]. Producto: [descripción]. El copy debe cambiar completamente para nuestro producto. La estructura visual se mantiene."

**Paso 4. Recolectar assets:**
- Descargar 2-3 ads propios con fonts y colores visibles
- Descargar imagen del producto desde el sitio web
- Descargar el ad clonado como referencia de layout

**Paso 5. Generar prompt NanoBanana 2:**
- Instrucción de match: "match exact colors, fonts, type, and visual tone de mis brand references"
- Instrucción de layout: "usa el ad de referencia solo para estructura y composición, NO para copy ni producto"
- Target: 1,000-1,500 palabras

**Paso 6. Ejecutar en Fal.ai:**
- Modelo: NanoBanana 2
- Subir: prompt + ad clone (layout ref) + 2-3 brand refs + product image
- Generar 4 variaciones (~$0.08 c/u)

---

### MÉTODO ANIMACIÓN

**Paso 7. Decisión de frames:**
- Determinar: ¿el static existente es START frame o END frame?
- Si hay bloqueo creativo: usar prompt de brainstorming con Claude para generar 3-5 ideas de concepto de animación

**Paso 8. Generar frame complementario:**
```
PROMPT PARA FRAME FALTANTE:
"Tengo este ad estático que será el [start/end] frame de una animación.
Concepto de animación: [descripción del movimiento].
Genera el [end/start] frame donde:
- Los elementos [lista] deben estar en posición [descripción]
- Remover: [elementos a quitar]
- Agregar: [elementos a añadir]
Mantén exactamente los mismos colores, fonts y estilo visual."
```

**Paso 9. Preparar JSON prompt para Veo 3.1:**
```
PROMPT EN CLAUDE:
"Tengo dos frames para animar:
[SUBIR IMAGEN 1] → Este es mi START FRAME
[SUBIR IMAGEN 2] → Este es mi END FRAME
Concepto: [descripción del movimiento]
Duración: 8 segundos
Genera un JSON prompt para Veo 3.1 que cree una animación suave de start a end frame."
```

**Paso 10. Ejecutar en Google Labs / Veo 3.1:**
- Seleccionar: FRAMES (no ingredients)
- Formato: 9:16
- Generar 4 variaciones
- NUNCA usar text-based prompts en Veo → usar JSON exclusivamente

**Paso 11. Iterar:**
- Descargar output como GIF
- Subir GIF a Claude + describir problemas específicos
- Prompt: "Dame un JSON prompt corregido para Veo 3.1 que fix [problema específico] y mantenga todo lo que sí funcionó"
- Repetir máximo 3 veces

---

### SISTEMA ESCALABLE (Claude Code)

**Paso 12. Setup del workspace:**
- Claude Code (recomendado, guarda automáticamente) o Claude Chat con proyecto
- Crear folder local para el brand

**Paso 13. Layer 1: Brand Extraction:**
- Ejecutar brand extraction prompt (scrape web: productos, valores, posicionamiento)
- Si hay brand guidelines en PDF: convertir a markdown PRIMERO
- Hack para fonts/colors: Inspeccionar página web → buscar "font" en HTML → copiar código → subir a Claude

**Paso 14. Layer 2: Brand Reference Cards (OBLIGATORIO como imágenes PNG):**
- Brand Spec Card: logos, fonts (headline/UI/subheaders/body), colores, do's/don'ts, CTAs
- Visual Style Card: dirección fotográfica, styling rules, quote del founder, ejemplos de ads, do's/don'ts visuales
- Convertir output HTML a PNG y GUARDAR en el proyecto

**Paso 15. Layer 3: Format Templates:**
- Recolectar 50-100 ads del mismo formato con ImageEye/Image Downloader (Chrome plugin)
- Prompt: "Clasifica estos ads en tipos distintos y genera un template para cada tipo que defina: estructura de copy, layout, visual devices"
- Cada template = "recipe card" = archivo .md
- GUARDAR cada template

**Paso 16. Layer 4: Copywriting Agents (.md files):**
```
AGENTES A CREAR:
- Persona Fit Agent: ¿habla directamente a la persona target?
- Angle Agent: ¿el ángulo es claro y específico?
- Emotion Agent: ¿activa la emoción correcta del buyer?
- Brand Fit Agent: ¿es coherente con la voz de la marca?
- Conversion Agent: ¿tiene CTA claro y motivador?
- Grammar Agent: incluir explícitamente "no m-dashes, no em-dashes"
Cada agente: role + job description + scoring criteria (0-100)
```

**Paso 17. Brief Generation:**
```
PROMPT:
"Quiero crear un [formato de ad].
Persona: [persona del W3 handoff]
Ángulo: [idea del W3 handoff]
Emoción: [driver emocional]
Usa mi brand bible y el format template de [tipo] para escribir el brief completo."
```

**Paso 18. Agent Review:**
```
PROMPT:
"Haz que todos los agentes revisen este copy.
Itera hasta que cada agente le dé un 90+/100.
Muéstrame el score final de cada agente."
(Proceso automático ~20 minutos)
```

**Paso 19. Convertir a NanoBanana 2 prompt:**
- "Convierte el brief que acabamos de crear en un prompt para NanoBanana 2 de 1,000-1,500 palabras"

**Paso 20. Ejecutar en Fal.ai con spec cards:**
- Subir: prompt + Brand Spec Card (PNG) + Visual Style Card (PNG) + product image
- Resize según plataforma: 9:16 (Stories), 1:1 (Feed), 4:5 (Feed móvil)

**Paso 21. Multiplicar en formatos:**
```
PROMPT:
"Tengo este winning ad. Aquí están mis format templates: [lista].
Para cada formato, reescribe el brief manteniendo:
- Misma persona: [X]
- Mismo ángulo: [Y]
- Misma emoción: [Z]
Adapta el copy a la estructura de cada template."
→ Ejecutar agent review para cada variación
→ Generar prompt NanoBanana para cada una
```

---

## GUARDRAILS

```
PROHIBIDO:
✗ Clonar ads verbatim, extraer DNA visual y repurposear con copy propio
✗ Usar texto para especificar fonts/colores en el prompt de NanoBanana 2
  → NanoBanana 2 no entiende hex codes ni nombres de font (excepto Times New Roman/Garamond)
  → SIEMPRE usar Brand Spec Card como imagen
✗ Subir más de 3 brand references a NanoBanana 2 → información contradictoria
✗ Usar text-based prompts en Veo 3.1 → usar JSON exclusivamente
✗ Seleccionar "ingredients" en Veo 3.1 → seleccionar FRAMES
✗ Animar subiendo el static directamente a Kling/Veo sin los dos frames → no funciona
✗ Subir PDFs a Claude directamente → convertir a markdown primero
✗ Usar AI UGC (avatares generados por AI para UGC) → desaconsejado explícitamente
✗ Declarar el primer output de Veo como final → siempre iterar mínimo 1 vez

EXPECTATIVAS DE MANEJO:
⚠ Primera generación de video/GIF probablemente imperfecta → es normal, iterar
⚠ Hit rate del Quick Win: 60-70% → no todas las generaciones serán usables
⚠ Sistema Escalable: hit rate 90-95% pero requiere setup de 4-6 horas
⚠ Veo 4 (si está disponible al momento de uso) puede cambiar el workflow de JSON
```

---

## ESCENARIOS DE ERROR Y RESOLUCIÓN

```
ERROR 1: Output de NanoBanana con elementos extraños (outlines raros, colores incorrectos)
→ Identificar el elemento específico que falló
→ Agregar instrucción explícita al prompt: "[elemento] debe ser [descripción exacta]"
→ Re-generar. Si persiste, aumentar la especificidad de esa sección del prompt

ERROR 2: Animación de Veo con movimiento incorrecto
→ Descargar como GIF
→ Describir a Claude los problemas específicos (no "está mal", sino "el oso no levanta el producto")
→ Solicitar JSON corregido que fix esos issues y mantenga lo que sí funcionó

ERROR 3: Fonts y colores no se reproducen correctamente
→ Verificar que se subió la Brand Spec Card como imagen (PNG), no como texto
→ Si el problema persiste: ir al código HTML del sitio, copiar la sección de fonts,
  subir a Claude para actualizar las spec cards

ERROR 4: Agentes no llegan al 90+/100 después de varias iteraciones
→ Revisar si hay conflicto entre agentes (ej: Persona Fit dice A, Brand Fit dice B)
→ Priorizar el agente más relevante para el objetivo del ad
→ Ajustar la descripción del agente con menor coherencia

ERROR 5: No hay ads de referencia de la marca
→ Usar solo el ad a clonar como referencia de estructura
→ Generar Brand Spec Card desde el sitio web y la descripción del producto
→ Marcar los primeros outputs como DRAFT, validar con el cliente antes de producir más

ERROR 6: Usuario quiere producir para TikTok además de Meta
→ Los prompts de formato cambian (9:16 es el mismo pero el pacing del copy es diferente)
→ El sistema escalable permite formatos separados por plataforma
→ Crear un format template específico para TikTok con sus propias reglas de copy
```

---

## ESQUEMA DE SALIDA

Output estructurado que sirve como input para W5_Analyze_Ads.

```json
{
  "session_metadata": {
    "brand": "[nombre del brand]",
    "date": "[fecha]",
    "method_used": "quick_win | animation | scalable_system",
    "persona_targeted": "[persona del W3 handoff]",
    "angle_used": "[ángulo de la idea]"
  },
  "ads_produced": [
    {
      "ad_id": "AD-001",
      "format": "static | gif | video",
      "persona": "[persona target]",
      "angle": "[ángulo estratégico]",
      "awareness_level": "TOF | MOF | BOF",
      "hook": "[primeros 3 segundos o headline principal]",
      "asset_location": "[ruta o URL del asset]",
      "production_method": "quick_win | scalable",
      "agent_scores": {
        "persona_fit": 92,
        "angle": 88,
        "emotion": 95,
        "brand_fit": 90,
        "conversion": 87,
        "grammar": 100
      }
    }
  ],
  "system_assets": {
    "brand_spec_card": "[ruta PNG]",
    "visual_style_card": "[ruta PNG]",
    "format_templates": ["[template_1.md]", "[template_2.md]"],
    "agents_configured": true
  },
  "next_skill": "W5_Analyze_Ads",
  "w5_handoff": {
    "ads_to_analyze": ["AD-001", "AD-002"],
    "funnel_stage": "prospecting",
    "goal_metric": "[ROAS | CPP | CPL según tipo de negocio]",
    "hypothesis_per_ad": {
      "AD-001": "[hipótesis que este ad está testeando]"
    }
  }
}
```
