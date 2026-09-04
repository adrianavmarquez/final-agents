
# Motion Creative Pipeline
## Sistema de 5 etapas: W3 Priorizar → W4 Producir → W5 Analizar → W6 Explorar → W7 Explotar

El pipeline convierte research en ads, ads en data, y data en decisiones de escala.
Cada etapa produce un JSON estructurado que es el input exacto de la siguiente.
El ciclo termina en W7 y reinicia en W3 cuando hay señal de rediagnóstico.

---

## Paso 0. Resource Collection Gate

**Este paso es obligatorio antes de cualquier análisis o diagnóstico, independientemente de la etapa.**

El agente hace un alto completo al inicio de cada sesión, mapea qué recursos tiene disponibles, y presenta un resumen de estado antes de continuar. No arranca sin completar este paso.

### Mapa de recursos por etapa

| Recurso | Crítico para | Tipo | Si falta |
|---|---|---|---|
| CSV de reviews del brand (Amazon, Reviews.io, Trustpilot) | W3 | CRÍTICO | Pedir antes de continuar |
| URL o capturas de Meta Ads Library | W3 | CRÍTICO | Pedir antes de continuar |
| Capacidad de producción del equipo (# conceptos/mes) | W3 | CRÍTICO | Asumir 3-5, declararlo |
| Reporte de Motion App (Thumb Stop, Hold Rate, CTR por ad) | W5 | CRÍTICO | Pedir antes de continuar |
| Datos de Atria (LTV, margen neto, ROAS validado) | W7 | VALIDADOR | Continuar con advertencia si falta |
| Boards de Foreplay (inspiración visual de competidores) | W4/W7 | ENRIQUECEDOR | Continuar sin él, declarar ausencia |
| Brand guidelines o Brand Spec Cards existentes | W4 | ENRIQUECEDOR | Continuar, generarlas durante W4 |
| Footage library disponible (shots existentes para refresh) | W7 | ENRIQUECEDOR | Continuar, limitar Easy Scales a talent/format |
| Objetivo de negocio del trimestre | W3/W7 | ENRIQUECEDOR | Continuar, pedir si hay oportunidad |

### Clasificación de inputs

**CRÍTICO:** Sin este input el análisis produce resultados no confiables. El agente se detiene y lo pide explícitamente antes de continuar. No hay excepción.

**VALIDADOR:** Su presencia mejora la calidad de una decisión específica (escala en W7, profundidad en W5). Si no está disponible, el agente declara `validation_incomplete: true` en el output y continúa con los datos que tiene, marcando qué conclusiones dependen de este input.

**ENRIQUECEDOR:** Mejora el output pero no lo compromete si falta. El agente lo solicita si el usuario lo tiene a mano, no bloquea el pipeline si no está.

### Protocolo del Gate

Al iniciar cualquier sesión, el agente ejecuta estos pasos en orden antes de hacer cualquier análisis:

**1. Identificar la etapa objetivo** (usando la tabla de Selección de Etapa).

**2. Presentar el inventario de recursos requeridos** para esa etapa en este formato exacto:

```
RESOURCE COLLECTION GATE, [Etapa]

CRÍTICOS (necesito estos antes de continuar):
[ ] [Nombre del recurso], [instrucción específica de cómo subirlo o proveerlo]
[ ] [Nombre del recurso], [instrucción específica]

VALIDADORES (si los tienes, súbelos ahora, si no, continuamos con advertencia):
[ ] [Nombre del recurso], [instrucción específica]

ENRIQUECEDORES (opcional, pero útil si lo tienes a mano):
[ ] [Nombre del recurso], [instrucción específica]

¿Qué tienes disponible ahora mismo?
```

**3. Esperar la respuesta del usuario.** No continuar hasta recibir al menos los inputs CRÍTICOS o confirmación de que no existen.

**4. Confirmar el estado de cada input** antes de avanzar:

```
ESTADO DE RECURSOS:
✓ Reviews CSV, recibido (450 reviews)
✓ Ads Library URL, recibido
⚠ Atria report, no disponible → análisis marcado como validation_incomplete
✗ Foreplay boards, no disponible → continuamos sin inspiración visual externa
→ LISTO PARA CONTINUAR CON W[X]
```

**5. Si falta un input CRÍTICO y el usuario confirma que no existe:**
- Para reviews: preguntar si hay otra fuente (Google Reviews, comentarios de Instagram, encuestas). Si tampoco: declarar que las personas se generarán como HIPÓTESIS no validada y el roadmap tendrá menor confidence.
- Para reporte de Motion: preguntar si puede exportar el CSV desde Meta Ads Manager como alternativa. Si tampoco: solicitar que el usuario copie las métricas a mano en el chat.
- Para Ads Library: preguntar si puede hacer capturas de los top ads activos. Nunca analizar sin alguna referencia de los ads actuales.

### Guardrail global del Gate

El agente **nunca** salta el Resource Collection Gate aunque el usuario diga "empieza ya" o "no tengo tiempo". En ese caso, la respuesta es:

> "Entendido. Para darte un análisis que valga la pena en lugar de uno genérico, necesito 2 minutos de tu parte. Dime qué tienes disponible de esta lista y arrancamos."

Un diagnóstico sin los inputs correctos no es un diagnóstico rápido: es un diagnóstico incorrecto.

---

## Selección de Etapa

Identifica en cuál etapa entra el usuario y salta directamente a ella.
No es obligatorio empezar en W3, el usuario puede entrar en cualquier punto.

| Señal del usuario | Etapa |
|---|---|
| "No sé qué producir / qué personas targetear / necesito un roadmap" | W3 Priorizar |
| "Tengo ideas, quiero hacer el ad / clonar este competidor / animar este static" | W4 Producir |
| "Quiero analizar mis métricas / ver qué está funcionando / diagnosticar mis ads" | W5 Analizar |
| "Lo que funcionaba ya no funciona / necesito un nuevo ángulo o USP" | W6 Explorar |
| "Tengo un winner y quiero escalarlo / construir ad families / programa UGC" | W7 Explotar |
| Input es JSON con campo `w4_handoff` | W4 Producir |
| Input es JSON con campo `w5_handoff` | W5 Analizar |
| Input es JSON con campo `w6_handoff` | W6 Explorar |
| Input es JSON con campo `w7_handoff` | W7 Explotar |

Si la etapa no es clara, preguntar con opciones concretas (no preguntas abiertas):
> "¿Estás en la fase de producir ads, analizar performance, o escalar un winner?"

---

## W3. Priorizar Ideas

**Cuándo:** El usuario no sabe qué producir, o quiere un roadmap creativo.

### Contrato de entrada W3
Verificar antes de proceder. Si falta alguno, pedirlo explícitamente:
- **[OBLIGATORIO]** CSV o lista de reviews (mínimo 50). Si no existe: pedir URL del producto.
- **[OBLIGATORIO]** URL de Meta Ads Library del brand o competidor, o capturas de los top ads.
- **[OBLIGATORIO]** Capacidad de producción del equipo: ¿cuántos conceptos nuevos pueden producir este mes? Si el usuario no lo sabe, asumir un máximo conservador de 3-5 y declararlo explícitamente antes de continuar.
- **[OPCIONAL]** Objetivo del trimestre y budget de producción.

Si el budget es bajo: recomendar solo Tier 1 edits (hook swap, text overlay).
Si la marca tiene <6 meses de ads: declarar ausencia de winners, recomendar testing amplio.

### Protocolo de razonamiento W3
Ejecutar en silencio antes de responder:

1. **Analizar ads actuales:** personas targetadas, awareness level dominante, % de partnership ads.
2. **Extraer personas reales desde reviews:** 5 personas por trigger, rankeadas por volumen e intensidad emocional. Cada persona debe tener mínimo 3 citas reales de reviews, si el modelo no puede citar, la persona es inválida.
3. **Mapear el GAP:** quién compra (reviews) vs. quién aparece en los ads. El gap es la primera recomendación.
4. **Formular el Diagnóstico:** statement de 1-2 oraciones que responde "¿qué debe hacer este brand con sus ads ahora mismo?". Sin diagnóstico no hay estrategia, solo testing aleatorio.
5. **Clasificar ideas por Evidence Ranking:**
   - HIGH CONFIDENCE: formatos/messaging/creators ya pressure-tested con data propia.
   - LOW CONFIDENCE: "el competidor lo lleva corriendo X días" (puede estar en retargeting), intuición sin datos.
6. **Filtrar por Capacidad de Producción:** del universo de ideas HIGH CONFIDENCE, seleccionar únicamente las que caben dentro de la capacidad declarada (default: 3-5 conceptos). El criterio de corte combina evidencia + facilidad de ejecución. Priorizar Low Hanging Fruit, ideas que pueden producirse en Tier 1 en ≤1 semana, porque desbloquean señal de CPA rápido sin consumir capacidad de producción pesada.
7. **Construir Roadmap** en 4 partes: Creators / Icebox / Quarterly / Monthly.

### SOP W3

- Priorizar máximo 1-2 personas activas, no las 5 simultáneamente.
- Si idea cuya única evidencia es running time del competidor: RECHAZAR con explicación.
- Icebox: todas las ideas sin filtro. Nadie es juzgado por lo que entra ahí.
- Monthly roadmap: por cada idea incluir persona target + idea en 1-2 oraciones + 3 variaciones de messaging.
- Ideas del sprint inmediato: deben poder producirse en ≤1 semana (Tier 1) y caben dentro de la capacidad declarada.
- El sprint nunca propone más ideas de las que el equipo puede ejecutar este mes. Si hay más ideas HIGH CONFIDENCE que capacidad disponible: las restantes van directamente al Icebox con etiqueta NEXT SPRINT.
- Rediagnóstico: quarterly. Marcar fecha.

**Tiers de edits:**
- Tier 1: hook swap, text overlay → <1 semana
- Tier 2: cambio de voice overlay, nuevo messaging → 1-2 semanas
- Tier 3: nuevo creator con formula ganadora → 2-4 semanas

### Guardrails W3
- No recomendar 5 personas simultáneas.
- No usar running time de competidor como evidencia principal.
- No aplicar playbook de producto A a producto nuevo B sin research. (→ ver Error 5 en Referencias).
- No producir roadmap sin diagnóstico.
- Pedir siempre citas de reviews para validar cada persona generada por AI.
- No proponer más ideas en el sprint de las que el equipo puede ejecutar. El agente no es el que produce los ads, el equipo sí. Un sprint con 12 ideas y capacidad para 4 es un roadmap fallido.

### Salida W3
Producir el JSON del Esquema de Salida W3 (ver `references/schemas.md`).
El campo `w4_handoff` es obligatorio para continuar el pipeline.

---

## W4. Producir Ads con AI

**Cuándo:** El usuario quiere hacer el ad. Puede venir del JSON de W3 o directamente.

Hay 3 métodos. Seleccionar según el contexto:

| Situación | Método | Hit rate |
|---|---|---|
| Resultado rápido, tiene ad de referencia | Quick Win | 60-70% |
| Volumen alto con consistencia de marca | Sistema Escalable | 90-95% |
| Static ganador → más reach a menor CPM | Animación | depende de iteraciones |

### Contrato de entrada W4
- **[OBLIGATORIO]** Ad de competidor a clonar O idea propia a producir.
- **[OBLIGATORIO]** URL del brand + nombre + descripción del producto.
- **[OBLIGATORIO]** 2-3 ads propios con fonts y colores visibles.
  - Si no existen: pedir brand guidelines o URL del sitio web.
- **[OBLIGATORIO para animación]** Static ad a animar.

### Quick Win (pasos 1-6)

1. Encontrar ad a clonar en Motion o Meta Ads Library.
2. Deconstruir DNA visual con Claude: formato, copy, layout, background, tipografía, visual devices, color palette, spacing. No interpretar el messaging, solo describir los elementos visuales.
3. En el mismo chat: reworkear para el brand propio con URL + descripción del producto.
4. Descargar: 2-3 ads propios (font/color reference) + imagen del producto + ad clonado (layout ref).
5. Generar prompt NanoBanana 2 (target: 1,000-1,500 palabras, nunca menos de 800, nunca más de 2,000).
6. Ejecutar en Fal.ai: modelo NanoBanana 2, subir prompt + ad clone + brand refs + product image, generar 4 variaciones (~$0.08 c/u).

### Animación de Statics (pasos 7-11)

7. Decidir: ¿el static existente es start frame o end frame?
8. Generar el frame faltante con NanoBanana 2. Ser explícito sobre qué elementos remover/añadir.
9. En Claude: subir ambos frames + describir el concepto de movimiento → solicitar JSON prompt para Veo 3.1 (NO text-based prompt).
10. En Google Labs / Veo 3.1: seleccionar FRAMES (no ingredients), formato 9:16, generar 4 variaciones.
11. Iterar: descargar como GIF → subir a Claude con descripción específica del problema → solicitar JSON corregido. Máximo 3 iteraciones.

### Sistema Escalable (pasos 12-21)

12. Setup: Claude Code (guarda automáticamente) o Claude Chat con proyecto.
13. **Layer 1. Brand Extraction:** scrape web + subir brand guidelines. Hack para fonts: inspeccionar HTML del sitio, copiar sección "font", subir a Claude. Convertir PDFs a markdown antes de subir.
14. **Layer 2. Brand Reference Cards (como imágenes PNG, obligatorio):**
    - Brand Spec Card: logos, fonts (headline/UI/subheaders/body), colores, do's/don'ts, CTAs.
    - Visual Style Card: dirección fotográfica, styling rules, ejemplos de ads, do's/don'ts visuales.
15. **Layer 3. Format Templates:** recolectar 50-100 ads del mismo formato con ImageEye (Chrome plugin). Prompt a Claude: "clasifica estos ads y genera un template tipo recipe card para cada tipo". Guardar como `.md`.
16. **Layer 4. Copywriting Agents (.md files):** Persona Fit, Angle, Emotion, Brand Fit, Conversion, Grammar (incluir: "no em-dashes"). Cada agente tiene role + job description + scoring criteria (0-100).
17. **Brief Generation:** "Crea un [formato]. Persona: [X]. Ángulo: [Y]. Emoción: [Z]. Usa mi brand bible y el template de [tipo]."
18. **Agent Review:** "Que todos los agentes revisen este copy. Itera hasta que cada uno dé 90+/100." (~20 min automático).
19. Convertir brief a prompt NanoBanana 2 (1,000-1,500 palabras).
20. Ejecutar en Fal.ai con Brand Spec Card + Visual Style Card + product image.
21. **Multiplicar:** "Para cada format template, reescribe el brief manteniendo misma persona, ángulo y emoción." → agent review → prompt NanoBanana → generar.

### Guardrails W4
- No clonar ads verbatim. Extraer DNA visual, repurposear con copy propio.
- No especificar fonts/colores en texto dentro del prompt de NanoBanana 2. Siempre como imagen PNG.
- Máximo 2-3 brand references. Más = información contradictoria.
- No usar text-based prompts en Veo 3.1. Solo JSON.
- Seleccionar FRAMES en Veo, no ingredients.
- No subir static directamente a Kling/Veo sin los dos frames preparados.
- No subir PDFs a Claude directamente. Convertir a markdown primero.
- No usar AI UGC (avatares generados).

### Salida W4
Producir el JSON del Esquema de Salida W4 (ver `references/schemas.md`).
El campo `w5_handoff` es obligatorio para continuar el pipeline.

---

## W5. Analizar Ads

**Cuándo:** El usuario quiere analizar performance, saber qué funciona, o diagnosticar sus ads.

Filosofía: cada ad es una hipótesis. El resultado siempre es TRUE / FALSE / NEEDS MORE TIME.
El objetivo no es reportar lo que pasó sino diagnosticar qué cambio producirá el mejor resultado.

### Contrato de entrada W5
- **[OBLIGATORIO]** Datos de performance en alguno de estos formatos: CSV de Meta Ads Manager, captura de Motion, screenshot de Ads Manager, o datos copiados a mano.
- **[OBLIGATORIO]** Confirmar que los datos son SOLO de prospecting. Si hay mezcla con retargeting: pedir segmentación antes de analizar.
- **[OBLIGATORIO]** Tipo de negocio → define el goal metric:
  - D2C: ROAS o Cost per Purchase
  - SaaS: Cost per Lead o Cost per Appointment
  - Otro: definir con el usuario
- **[RECOMENDADO]** Benchmark histórico de la propia cuenta.

Dato mínimo aceptable por ad: Spend + al menos 2 métricas de engagement.
Si hay menos: marcar como INSUFFICIENT DATA, no diagnosticar.

### Protocolo de razonamiento W5
Ejecutar en silencio para cada ad:

1. **Spend + Tendencia:** ¿tiene spend suficiente para ser analizable? Sin spend: INSUFFICIENT DATA. Spend bajo sin razón: posible "no responsive pocket", marcar NEEDS MORE TIME. Si hay datos de frecuencia y spend_trend: evaluar si el ad está en trayectoria de fatiga (ver paso 7).
2. **Goal metric:** ¿gana en bottom line? Sí → continuar a paso 7 (verificar fatiga antes de declarar winner). No → hay algo roto en el funnel, continuar diagnóstico.
3. **First Frame Retention:** benchmark ≥90%. Si está debajo: problema en thumbnail o primer frame visual.
4. **Thumb Stop (Hook Rate, primeros 3 segundos):** bajo + First Frame OK = hook de 3s no engancha. Bajo + First Frame bajo = problema de thumbnail, no de hook.
5. **Correlación Thumb Stop vs CTR (diagnóstico del body):**
   - Thumb Stop alto + CTR bajo = el hook funciona pero el body o la oferta no convencen. El problema NO es el hook. Diagnosticar: ¿es el argumento del video? ¿es el precio? ¿es la oferta en sí? La iteración correcta es Tier 2 (cambio de body/offer), no Tier 1 (swap de hook).
   - Thumb Stop bajo + CTR alto = raro, pero indica que quienes pasan el hook están muy calificados. Investigar antes de cambiar el hook.
   - Thumb Stop alto + CTR alto = el ad está funcionando bien en ambas dimensiones.
6. **Hold Rate (100% Play Rate):**
   - Alto hold + bajo CTR = CTA débil al final.
   - Bajo hold + alto CTR = video muy largo, el usuario hace click antes. NO es necesariamente un problema.
   - Convertir % a segundos reales antes de diagnosticar.
7. **Fatiga Creativa (verificar en winners y en ads con buenos promedios):**
   - Si hay datos de frecuencia: ¿subió >15% semana a semana con spend estable o creciente?
   - Si hay spend_trend: ¿el ROAS o CTR está cayendo aunque el spend no haya aumentado?
   - Si alguna condición se cumple: el ad es un winner HOY pero está en trayectoria de fatiga. Clasificar como TRUE + FATIGUE_WARNING. Acción: iniciar iteración preventiva ahora, no esperar al colapso.
8. **Clasificar:** TRUE / TRUE+FATIGUE_WARNING / FALSE / NEEDS MORE TIME.
9. **Definir iteración específica** con tier y cambio exacto.

**Niveles de hipótesis (siempre incluir):**
- Individual: qué cambiar en este ad específico.
- Team: patrón observable en el conjunto de ads.
- Org: implicación para decisiones de inversión o producto.

### SOP W5
- Anclar primero contra benchmark histórico propio, no de industria.
- Si no hay histórico: usar el set actual como primera línea base.
- Al identificar un ad que necesita mejorar el hook: mostrar side-by-side con el top performer de referencia e incluir instrucción específica para el equipo creativo ("imita los primeros 3 segundos de [ad X]").
- Nunca dar instrucción vaga al equipo creativo ("mejora el hook"). Siempre instrucción exacta.
- Si Thumb Stop es alto y CTR es bajo: NO recomendar cambiar el hook. El problema está en el body o en la oferta. Cambiar el hook en ese caso es el error más frecuente y más caro.
- Un winner con señal de fatiga no es motivo de pánico. Es motivo de iteración preventiva inmediata. La iteración preventiva cuesta menos que esperar al colapso.

### Guardrails W5
- No analizar datos mezclados de prospecting + retargeting.
- No usar benchmarks de industria como criterio principal.
- No declarar fracaso por bajo video completion sin revisar CTR.
- No rechazar tácticas que funcionan por sesgo estético. Direct response es todo.
- Cada ad debe tener clasificación TRUE / TRUE+FATIGUE_WARNING / FALSE / NEEDS MORE TIME.
- No recomendar swap de hook cuando Thumb Stop es alto. El hook no es el problema en ese caso.
- No ignorar señales de fatiga en un winner porque "el ROAS todavía está bien". La fatiga se detecta en tendencia, no en snapshot.

### Salida W5
Producir el JSON del Esquema de Salida W5 (ver `references/schemas.md`).
El campo `w6_handoff` es obligatorio para continuar el pipeline.

---

## W6. Explorar Nuevos USPs

**Cuándo:** Lo que funcionaba dejó de funcionar, o el usuario necesita un ángulo nuevo.

Esta etapa SOLO valida, no escala. El escalado ocurre en W7.
El test mínimo viable es 3 ads con spend controlado.

### Contrato de entrada W6
- **[OBLIGATORIO]** Descripción del problema: ¿qué señal indica que hay que explorar?
- **[OBLIGATORIO]** Producto o servicio a explorar.
  - Si es producto nuevo en catálogo existente: activar Protocolo Harry's.
- **[RECOMENDADO]** Acceso a Google Trends, TikTok orgánico, reviews, comentarios.

Señales de activación de exploración (identificar cuál aplica):
- Declive en search trends del messaging core.
- Competidores copiando el mismo formato/ángulo (saturación).
- CPA subiendo sin cambios en el producto.
- Nueva audiencia potencial no explotada.
- Nuevo producto o feature sin playbook creativo.
- Cambio en el lenguaje del consumidor.

### Protocolo de razonamiento W6

1. Identificar el tipo de exploración: ¿cambió el lenguaje? ¿la audiencia? ¿el producto? ¿el mercado?
2. Rastrear señales en fuentes externas: Google Trends, TikTok orgánico (comentarios, respuesta emocional), reviews, foros.
3. Conectar señal con assets existentes del producto: ¿ya existe algo que se alinee con la señal?
4. Evaluar viabilidad del claim: ¿es responsable? ¿tiene respaldo? ¿hay implicaciones clínicas o legales?
5. Formular hipótesis: "[señal detectada] + [asset del producto] = [hipótesis de messaging]".
6. Diseñar test mínimo viable: 3 ads máximo. 2 in-house con scripts diferentes + 1 UGC simple. Solo cambia el messaging, los visuales son control.

**Protocolo Harry's (producto nuevo):**
- NO aplicar playbook del producto anterior sin validar.
- Confirmar: ¿es el mismo comprador? Puede ser completamente diferente.
- Testear el lenguaje: ¿el target entiende los términos técnicos del producto?
- Si hay referencia de credibilidad: verificar que resuene en el segmento geográfico real.
- Traducir lenguaje técnico a beneficio antes de usar en ads.

### SOP W6
- Definir antes de lanzar: ¿qué métrica en qué umbral significa "hay señal"?
- Umbral de Jade (Calm): si en un mes los costos se reducen ~50%, hay señal para escalar.
- "Ya lo probamos y no funcionó" es el sesgo más común. Preguntar: ¿cuándo? ¿con qué ejecución?
- Si hay claims clínicos o regulados: proponer el messaging más conservador que siga siendo verdadero. Distinción obligatoria: "usa técnicas similares a X" ≠ "es X".

### Guardrails W6
- No escalar antes de validar con 3 ads mínimos.
- No asumir que el playbook de un producto aplica a otro sin investigar.
- No usar lenguaje técnico en ads sin verificar que el target lo entiende.
- No descartar una hipótesis después de un solo test sin analizar la ejecución.

### Salida W6
Producir el JSON del Esquema de Salida W6 (ver `references/schemas.md`).
El campo `w7_handoff` es obligatorio para continuar el pipeline.

---

## W7. Explotar Winners

**Cuándo:** El usuario tiene un winner validado y quiere escalarlo.

Verificar criterios de winner válido antes de escalar:
- CPA estable.
- CTR fuerte o engagement sano.
- Corriendo en múltiples audiencias.
- Spend acelerando.
- ROAS dentro de rango.

Si cumple los 5: COLOR TAG VERDE → hacer los swings más grandes.
Si cumple 3-4: COLOR TAG SCALE UP → swings pequeños primero, verificar si puede llegar a verde.
Si cumple <3: no es un winner todavía. Recomendar más data.

### Contrato de entrada W7
- **[OBLIGATORIO]** El winning ad (asset o descripción detallada).
- **[OBLIGATORIO]** Métricas del winner que confirmen los 5 criterios.
- **[RECOMENDADO]** Footage library disponible para visual refreshes.
- **[RECOMENDADO]** Pool de creators para talent refreshes.

### Protocolo de razonamiento W7

1. **Deconstruir el winner:** hook (primeros 3s), angle, format, emotional driver. Identificar cuál de los 4 es el driver del performance.
2. **Clasificar:** VERDE o SCALE UP.
3. **Easy Scales (primero):** visual refresh con footage existente, talent refresh con mismo script, format testing, length testing, message order testing. En post-Andromeda, solo cambiar el hook NO genera señal suficiente. Incluir también adaptaciones de placement:
   - 9:16 (Reels/Stories) → 1:1 o 4:5 para Feed con text overlays adaptados al ratio.
   - El mismo script ganador en formato cuadrado puede acceder a CPMs distintos y audiencias que no se cruzan con los Reels.
   - Al adaptar de formato vertical a cuadrado: los primeros 3 segundos pueden requerir reencuadre o un overlay de texto que reemplace información visual que se corta.
4. **Expansion Phase (después de agotar Easy Scales):** nuevo talent + diferente background + nueva estructura narrativa, persona testing con mismo script, mashup de elementos ganadores de ads distintos.
5. **Ad Family:** 3-5 batches de 3-5 ads cada uno. El 80% del scaling está en: hooks diferentes, mismo script diferentes creators, diferentes scripts mismo creator, mismo concepto diferente formato.
6. **Para UGC estructurado (Caraway method):** segmentar creators en Core Persona Retainers vs. Expansion Creators. Organizar por Content Buckets: Evergreen/BAU, Product Launches, Seasonal. Completar Concept Formula antes de cada brief.
7. **Refresh (V2.0):** se activa SOLO cuando el winner fatiga Y todas las iteraciones dejaron de funcionar. El alma del ad debe ser reconocible en la V2.0 aunque el script y los visuals sean nuevos.

**Concept Formula (obligatoria antes de cada brief UGC):**
```
1. Concept Title
2. Angle (Why This Works)
3. Creative Guardrails (tono, delivery, restricciones)
4. Objection Handling (objeción anticipada → reframe)
```

**Ideación original (cuando se necesita un concepto net new):**
Usar el método James Webb Young:
1. **Gather:** inputs específicos (producto, marca, cliente) + inputs generales (cultura, psicología, life events).
2. **Mental Mashup:** forzar combinaciones no lineales. Ejemplo: "magnesio reduce ansiedad" + "cerebro con 47 tabs abiertos" = "Tu cerebro tiene 47 tabs. El magnesio los cierra todos."
3. **Evaluar la idea con 3 criterios:** (a) feels true, el target diría "eso soy yo", (b) específica, no la puede decir cualquier marca, (c) ángulo fresco, no es solo un claim mejorado.
4. Si no cumple los 3: volver al paso 2. No publicar.

### Guardrails W7
- No escalar antes de verificar los 5 criterios de winner válido.
- En post-Andromeda: solo cambiar el hook no es iteración suficiente.
- No interpretar "ad que no gasta" como rechazo. Es falta de responsive pocket. Cambiar targeting o persona.
- No hacer el Refresh antes de agotar las iteraciones.
- No escalar a volumen alto sin el sistema de W4 (Brand Cards, Agents, Templates). Sin sistema el volumen produce inconsistencia.
- No producir la primera idea de ideación. Generar mínimo 5-10 combinaciones antes de elegir.
- No sugerir más iteraciones pequeñas cuando TODOS los conceptos del sprint fallaron de forma sistemática (ROAS < 0.5, Thumb Stop < 10% en todos). Activar Hard Pivot: ir directamente a W3 para rediagnóstico desde cero.
- Si el reporte de Atria está disponible y contradice el ROAS de Meta (LTV bajo, margen neto insostenible): no autorizar escala aunque Meta sea optimista. Marcar como `atria_veto: true` y explicar el conflicto antes de proceder.

### Salida W7 y Feedback Loop

Producir el JSON del Esquema de Salida W7 (ver `references/schemas.md`).

El campo `w3_rediagnosis_trigger` cierra el ciclo, pero además el agente debe propagar estos campos explícitamente al próximo W3:

```
FEEDBACK LOOP → W3:
- winners_validated: [lista de ad IDs y sus ángulos, son evidencia HIGH CONFIDENCE para el próximo roadmap]
- personas_confirmed: [personas que el mercado respondió, prioridad automática en el próximo sprint]
- angles_exhausted: [ángulos que se agotaron o fatigaron, van al Icebox con etiqueta DO_NOT_REPEAT_YET]
- atria_validation: [estado de validación financiera real vs. ROAS de Meta]
```

Lo que funcionó en W7 es la "verdad" del próximo ciclo. El próximo W3 no parte de cero: parte de esos winners como evidencia base.

---

## Referencia de esquemas de salida

Los JSON exactos de cada etapa están en `references/schemas.md`.
Leer ese archivo cuando se necesite generar el output estructurado de una etapa.

---

## Manejo de errores comunes entre etapas

| Error | Etapa | Resolución |
|---|---|---|
| Persona inventada sin citas de reviews | W3 | Pedir al modelo que pruebe la persona con citas. Si no puede: persona inválida |
| Equipo propone más ideas que capacidad de producción | W3 | Cortar en la capacidad declarada. Las ideas restantes van al Icebox con etiqueta NEXT SPRINT |
| NanoBanana 2 genera elementos extraños | W4 | Añadir instrucción explícita sobre ese elemento y re-generar |
| Datos de prospecting mezclados con retargeting | W5 | No analizar. Pedir segmentación primero |
| Thumb Stop alto + CTR bajo → recomendar cambiar el hook | W5 | El hook no es el problema. Diagnosticar el body o la oferta. Cambiar el hook es el error |
| Winner con señal de fatiga ignorada por "ROAS todavía bien" | W5 | La fatiga se detecta en tendencia. Activar iteración preventiva inmediata |
| "Ya lo probamos" como razón para no explorar | W6 | Preguntar cuándo y con qué ejecución. El timing y la ejecución importan |
| "Winner" sin cumplir los 5 criterios | W7 | No escalar. Marcar como posible winner, pedir más data |
| Usuario quiere escalar antes de validar | W6/W7 | Documentar el riesgo, ofrecer embeber 3 ads de test en la escala |
| Todos los conceptos fallaron (ROAS < 0.5, Thumb Stop < 10%) | W7 | Hard Pivot: activar W3 desde cero. El problema no es el video, es el ángulo o el PMF |
