# experimentos.md

Memoria del loop. El agente escribe aquí cada ciclo. Adri escribe aquí cada decisión del loop lento con prefijo LENTO-AAAA-MM.

Formato por ciclo:

```
## Ciclo NN, AAAA-MM-DD
Hipótesis:
Cambio:
Piso anterior:
Promedio nuevo:
Desviación entre runs:
Decisión: keep | revert
Lección:
```

## Hipótesis pendientes desde R0 Baseline (2026-09-03)

Vienen del cruce histórico de Sandcastles. Son el orden sugerido de los primeros ciclos. Cada una es un ciclo, no se combinan.

1. Profundidad del dolor obligatoria en C0 con ejemplos por nivel. Ya está en la versión 1.0 del skill. El ciclo 0 la mide.
2. Reordenar C1b para que T12 y T3 aparezcan con su dato propio antes que T4, para sesgar hacia tipos con conversión probada cuando el objetivo es comentarios o DM.
3. Agregar en "AQUÍ SE REDACTA" tres ejemplos de apertura que hagan P8 + P3 + P7 sin la sintaxis vetada. Ninguno puede venir de briefs/.
4. Exigir que el generador señale con corchetes qué palabras hacen cada principio declarado, como parte de la declaración.
5. Instrucción explícita en T6 de usar cifras propias de Adri (Radar, Metricool, quiz) cuando el objetivo es alcance.

## LENTO-2026-09

Sin cambio de rúbrica. Baseline histórico registrado en Performance Intelligence Log como R0. Primer cruce real: 2026-10-03.

## LENTO-2026-09, cambio 1 de 1 del mes

Fecha: 2026-09-03. Origen: hallazgo de Claude Code en Fase 0.
Cambio: reglas_duras.py v1.1. Todas las verificaciones de nivel 1 corren solo sobre la línea GANCHO cuando existe. Antes, promesas y calcos corrían sobre el archivo completo y descalificaban verbatim del Language Bank que vive en la DECLARACIÓN.
Evidencia: caso reproducible, gancho limpio con "mas seguidores" en Dolor en su voz fallaba nivel 1.
Nota: este es el único cambio de verificador permitido en septiembre. Cualquier otro ajuste a la rúbrica espera al cruce de octubre.

LENTO-2026-09, nota al cambio 1: verify.py v1.1. Se quitó temperature=0 porque Sonnet 5, Opus 4.7+, Opus 5 y Fable 5 rechazan parámetros de sampling con 400. Default del verificador pasa a claude-opus-5 para que el juez sea al menos tan fuerte como el generador. Sonnet 4.6 queda como opción barata para smoke tests vía VERIFICADOR_MODELO. El ruido entre corridas se controla con --runs, no con temperature.

LENTO-2026-09, nota al cambio 1, parte 3 (pre ciclo 0): verify.py v1.2 calcula total y pasa en código desde las compuertas; el modelo tendía a colapsar total a 0 cuando no pasaba, lo que dejaba al ratchet sin gradiente. reglas_duras.py v1.2 agrega la variante "no es falta de X, es que Y" que el smoke test dejó pasar por nivel 1 y cazó nivel 2. rubrica_ganchos.md aclara que el modelo solo puntúa compuertas. Regla aclarada: arreglos de tubería en verify.py y reglas_duras.py antes del ciclo 0 no cuentan como cambio de rúbrica; después del ciclo 0, todo verificador/ queda congelado hasta el cruce de octubre.

LENTO-2026-09, nota al cambio 1, parte 4 (última tubería pre ciclo 0): verify.py v1.3 emite en --set desviacion y compuerta_minima por archivo, más desviacion_promedio y compuerta_minima_set agregados. Antes se calculaban y se perdían al serializar. Ventana de tubería cerrada: a partir del ciclo 0, verificador/ congelado.

LENTO-2026-09, nota al cambio 1, parte 5 (pre ciclo 0): cláusula de hipótesis. C0 del skill pasa de "sin verbatim no se escribe" a tres modos de evidencia: verbatim, proxy, hipótesis. rubrica_ganchos.md v1.1 agrega las restricciones del modo hipótesis (sin T3/T4 primario, objetivo comentarios o DM, prueba desde dato propio). Motivo: un sistema que solo escribe con verbatim no puede testear personas nuevas, y seis de once micropersonas no tienen voz real guardada. briefs 11 a 16 agregados en modo proxy e hipótesis. Set congelado en 16.
