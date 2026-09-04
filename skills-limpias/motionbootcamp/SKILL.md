---
name: motionbootcamp
description: "Referencia del bootcamp de creative strategy de Motion (serie W: W3 priorizar, W4 producir, W5 analizar, W6 explorar, W7 explotar). Se invoca SOLO de forma explícita con /motionbootcamp o cuando el usuario dice 'consulta el curso', 'qué dice la W5', 'material del bootcamp', 'el pipeline W'. Nunca se activa sola en trabajo real de ads; para eso está motion-router y las skills de Motion. Es material de consulta: cómo lo harían los instructores."
---

# Motion Bootcamp, serie W

Material de consulta. No es un flujo de trabajo que corre solo. Cuando Adri quiere saber cómo lo haría un instructor del bootcamp, o quiere el JSON de handoff de una etapa, se abre aquí.

Para trabajo real de ads (analizar una cuenta, escribir hooks de paid, priorizar creativos para BULK HVAC, Celestina o Sparked Reactions) la entrada es `motion-router`, que carga el config de la marca y elige entre las skills de Motion. Este skill no reemplaza eso.

## Cómo se usa

1. Adri dice qué etapa quiere consultar, o describe el problema y este skill elige la etapa.
2. Se lee `references/pipeline_w.md` para el mapa completo y los gates entre etapas.
3. Se abre solo la referencia de la etapa que aplica. No se cargan las cinco.
4. La respuesta cita la etapa y el framework del instructor, y termina señalando qué skill de Motion ejecutaría eso en producción.

## Etapas

| Etapa | Instructor | Referencia | Produce |
|---|---|---|---|
| W3 Priorizar | Dara Denney | `references/w3_priorizar.md` | Personas reales vs targetadas, diagnóstico de marca, evidence ranking, roadmap |
| W4 Producir | Will Sartorius | `references/w4_producir.md` | Ads con AI: NanoBanana, Veo, UGC sintético |
| W5 Analizar | Evan Lee | `references/w5_analizar.md` | Cada ad como hipótesis TRUE / FALSE / NEEDS MORE TIME |
| W6 Explorar | Jade Heritage (Calm), Daniel Rivera (Harry's) | `references/w6_explorar.md` | Nuevos USPs y ángulos desde la data |
| W7 Explotar | Sophia Beauvoir, Viti Videtta, Janae LeVander | `references/w7_explotar.md` | Ad families, programa UGC, refresh plan |

Los esquemas JSON de handoff entre etapas están en `references/schemas.md`. Los evals en `references/evals.json`.

## Reglas

- Capa 0: `marca-reglas-duras` manda sobre cualquier copy que salga de aquí, aunque el bootcamp esté en inglés.
- Este skill no llama a Motion MCP. Si hace falta data real, se sale a `motion-router`.
- Si Adri pide "hazlo", no "explícame cómo lo harían", este skill no es el lugar. Se redirige.
