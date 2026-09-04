# Injerto para voc-mining: salida "Hook Research Brief"

Rescatado de `hook-research-analyzer` antes de archivarla. Es lo único de esa skill que `voc-mining` y `review-audit` no hacían: convertir el lenguaje extraído en un brief listo para `hook-autonomo`.

Pegar al final de `voc-mining/SKILL.md`, como sección nueva. Todo lo demás de la skill archivada (persona de Jake, referencias a Motion, categorías de hooks en inglés) se descarta.

---

## Salida final: Hook Research Brief

Cuando la extracción termina, además de los buckets de lenguaje, se entrega este bloque. Es el puente a `hook-autonomo`: lo que aquí se escribe entra directo en C0 como verbatim o como proxy.

### Lenguaje listo para gancho
- **Números y cifras:** cantidades, plazos, precios, porcentajes que la audiencia dijo. Textuales.
- **Frases exactas:** entre 5 y 10 frases verbatim, con su fuente (plataforma, fecha, handle si es público). Sin pulir.
- **Palabras cargadas:** las 10 palabras de mayor carga emocional que se repiten. Solo las que usa la audiencia, no las que usaría un copywriter.

### Micropersona probable
Código de Micro Persona DB al que apunta este lenguaje, con la frase que lo delata. Si el lenguaje no cuadra con ninguna, se declara "micropersona nueva candidata" y se sigue el SOP de Basecamp.

### Nivel de awareness dominante
Unaware, Problem-aware, Solution-aware, Product-aware o Most-aware, con dos frases de evidencia. Esto decide si el gancho puede ser T3/T4 (espejo) o tiene que ser T2/T6/T9 (afirmación o pregunta).

### Tres ángulos para escribir primero
Cada uno en una frase: quién, qué verdad emocional toca, qué entregable lo paga. Nombrar el principio psicológico sugerido (P1 a P14) y el tipo (T1 a T12) sin redactar el gancho. El gancho lo escribe `hook-autonomo`, no esta skill.

### Qué evitar
Ángulos, palabras o encuadres que este lenguaje indica que no van a aterrizar: porque están quemados, porque contradicen el POV de Adri, o porque tocan una promesa de resultado.

### Modo de evidencia
Declarar si lo extraído es verbatim (voz propia de la audiencia de Adri), proxy (comentarios ajenos, reviews de terceros, benchmarking) o insuficiente. `hook-autonomo` lo hereda tal cual.
