# program.md

Instrucción del loop meta. Claude Code lee esto al inicio de cada ciclo. Solo Adri lo edita.

## Objetivo

Subir el puntaje promedio de `verificador/verify.py --set --runs 3` sobre `briefs/` para `generador/hook-autonomo/SKILL.md`.

## Permitido

- Editar `generador/hook-autonomo/SKILL.md`.
- Escribir salidas en `salidas/`.
- Escribir en `memoria/experimentos.md` y `memoria/ratchet-log.md`.

## Prohibido

- Tocar cualquier archivo en `verificador/`.
- Tocar cualquier archivo en `briefs/`.
- Tocar `program.md`.
- Cambiar el modelo o la temperatura del verificador (variable VERIFICADOR_MODELO).
- Leer `verificador/rubrica_ganchos.md`. El generador no ve la rúbrica. Si la lees, el ciclo queda inválido.
- Agregar al skill ejemplos de ganchos que aparezcan en `briefs/` o en `salidas/` de ciclos anteriores.
- Quitar ninguna de las 7 reglas duras.
- Quitar ninguno de los 14 principios de C1a ni ninguno de los 12 tipos de C1b.

## Cada ciclo

1. Leer este archivo.
2. Leer `memoria/experimentos.md` para no repetir un experimento que ya falló.
3. Declarar la hipótesis en una frase. Escribirla en `memoria/experimentos.md` antes de tocar nada.
4. Hacer UN cambio en `generador/hook-autonomo/SKILL.md`. Uno. Una regla, un ejemplo, un orden, una tabla. No dos.
5. Por cada brief en `briefs/`, ejecutar el skill como si fueras `/gancho` con ese brief como intake, respetando el Modo de evidencia declarado en el brief (verbatim, proxy o hipótesis; en hipótesis aplican las restricciones de C0), y escribir la salida (gancho + declaración, formato de "Entrega al verificador") en `salidas/ciclo_NN/brief_XX.txt`. Un gancho por brief.
6. Correr `python verificador/verify.py salidas/ciclo_NN --set --runs 3`.
7. Comparar el promedio con el piso actual en `memoria/ratchet-log.md`.
8. Si el promedio sube al menos 1.0 punto sobre el piso: conservar el cambio, el promedio es el nuevo piso. Si igualó o bajó: revertir el cambio con git. El ruido observado entre corridas es de unos 2 puntos, por eso el umbral no es cero. Registrar en `memoria/experimentos.md`: ciclo, hipótesis, cambio, piso anterior, promedio nuevo, decisión, lección.
9. Commit con mensaje `ciclo NN: [hipótesis] -> [keep|revert] [promedio]`.

## Terminado cuando

Promedio del set sube 15 puntos sobre el baseline del ciclo 0, y `nivel1_pasan` es N/N.

## Parar antes si

- 4 ciclos seguidos sin subir el piso.
- `generador/hook-autonomo/SKILL.md` supera 5.000 palabras.
- Cualquier ciclo requiere tocar un archivo prohibido para avanzar.

## Modo

Abierto hasta que Adri diga lo contrario: al final de cada ciclo, parar y mostrar el resumen. No arrancar el siguiente sin confirmación.

Cuando Adri cambie esta línea a "Cerrado", correr hasta terminado o parar antes, sin pedir input.
