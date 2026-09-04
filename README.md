# final-agents

Loops y agentes finales de @adrianavmarquez. Cada carpeta es un sistema cerrado con cuatro piezas separadas:

1. Un generador que puede cambiar.
2. Un verificador que el generador nunca lee.
3. Un set de prueba congelado.
4. Una memoria donde el piso solo sube.

Lo que no tenga esas cuatro piezas no vive aquí.

## Sistemas

| Carpeta | Qué es | Estado |
|---|---|---|
| `redaccion-loop/` | Karpathy loop para ganchos en español. Generador `hook-autonomo`, verificador de dos niveles, 16 briefs, ratchet. | Ciclo 0 generado, baseline pendiente de re-puntuar con verify v1.4 |

Cada carpeta tiene su README con requisitos, arranque y cuándo volver a claude.ai.

## Documentación fuera del repo

- Basecamp > SOP Loop de Redacción (Notion): cómo funciona el loop, reportes R1 a R4, post mortem mensual.
- Basecamp > SOP Micropersona nueva (Notion): seis sistemas que se actualizan cuando nace una micropersona.
