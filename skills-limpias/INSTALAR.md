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

## No tocar
- Sistema B de Motion (skills en inglés, motion-router, serie W): se queda. Ver nota en el chat.
- Las tres protocolos de Notion (brand-brain, market-research, messaging-angles): no son de escritura.
