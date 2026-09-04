# Paquete de instalación, 2026-09-03

Sale de la auditoría del sistema de redacción. Todo va a claude.ai (Settings > Capabilities > Skills), reemplazando el skill del mismo nombre donde ya exista.

## Nuevas
- `marca-reglas-duras/` Capa 0. Instalar primero.

## Reemplazos (mismo nombre, versión limpia)
- `hook-autonomo/` v1.1 con cláusula de hipótesis. Es la que corre en el loop.
- 21 skills en español con rayas largas eliminadas (0 en todas) y la línea de Capa 0 al inicio:
  talking-head, carousel, text-screen, youtube-vlog-intake, tweet-atomic-snippets, storytime, youtube-video-essay, ecosystem-architect, substack, linkedin, youtube-essay, pov-finder, fast-reel, tcf-vende, email-sales, yapping, voiceover, email-inner-circle, caption-hook-writer, script-skill, brand-proposal-pdf, prompt-builder.
- Cuatro de ellas traen además una línea "Frontera" que dice cuál es la skill vecina y cuándo NO usar esta: los dos youtube essay, yapping y voiceover.

Método de limpieza de rayas: raya al inicio de línea pasa a viñeta; raya antes de mayúscula o cifra pasa a punto; raya antes de cierre de paréntesis o comillas desaparece; el resto pasa a coma. Revisado a mano en talking-head; el resto sigue la misma regla. Si ves una coma rara, es de ahí.

## Injerto
- `voc-mining/ADDENDUM_hook_research_brief.md` se pega al final de la skill `voc-mining` actual. Después se archiva `hook-research-analyzer`.

## Archivar (mover fuera de skills, no borrar)
- `hook-research-analyzer` (después del injerto)
- `design-taste-frontend-v1`

## Desinstalar plugins (Settings > Plugins)
brand-voice, small-business, customer-support, sales, human-resources, legal, finance, bio-research, atlan si aparece.

## Motion: consolidación de la serie W
- `motionbootcamp/` reemplaza a SIETE entradas: `motionbootcamp`, `motion-pipeline-w-series`, `w3-prioritize-ad-ideas`, `w4-makeads`, `w5-analyze`, `w6-explore`, `w7-exploit`. El contenido de las cinco W vive en `references/` y solo se abre desde /motionbootcamp.
- Borrar las siete anteriores DONDE ESTÉN. Ojo: existen dos veces, como skills de usuario (con descripción "Actívala SIEMPRE", las peligrosas) y dentro del plugin (neutralizadas). Van las dos.
- `motion-router` se queda tal cual. Es la entrada real para ads.
- Las skills en inglés de Motion (creative-strategy, concept-engine, build-brief, analyze-ad, etc.) se quedan: son el sistema B para BULK HVAC, Celestina, Sparked Reactions y la cuenta propia.

## No tocar
- Las tres protocolos de Notion (brand-brain, market-research, messaging-angles): no son de escritura.
