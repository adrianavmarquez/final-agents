# redaccion-loop

Karpathy loop para el sistema de redacción de @adrianavmarquez. Generador y verificador separados. Este README es el paso a paso para Claude Code y dice cuándo volver a claude.ai.

Documentación del sistema completo: Basecamp > SOP Loop de Redacción, en Notion.

---

## Qué hay en este repo

```
redaccion-loop/
  program.md                        instrucción del loop meta. Solo Adri la edita
  generador/hook-autonomo/SKILL.md  el skill reescrito. Lo único que el loop puede tocar
  verificador/
    reglas_duras.py                 nivel 1, determinista, exit 0 o 1
    rubrica_ganchos.md              nivel 2, system prompt del verificador. El generador no la lee
    verify.py                       corre ambos niveles, promedia el set. v1.4
  briefs/                           set de prueba congelado el 2026-09-03: 16 briefs
    README_briefs.md                tabla de cobertura y modos de evidencia
    brief_01 a brief_16             10 verbatim, 2 proxy, 4 hipótesis
    brief_template.md
  memoria/
    experimentos.md                 hipótesis pendientes ya cargadas desde R0
    ratchet-log.md                  el piso solo sube
  salidas/                          lo que el generador produce cada ciclo. Ignorado por git
```

---

## Estado al 2026-09-03 y arranque rápido

**Dónde va.** Repo instalado y con commit limpio. 16 briefs congelados. Ciclo 0 generado (salidas/ciclo_00, 16 salidas, nivel 1 pasa 16/16) pero SIN baseline válido: verify v1.3 devolvía 0.0 por tubería (Opus 5 agotaba max_tokens pensando). verify v1.4 lo corrige. Falta: instalar v1.4, humo con un archivo, re-puntuar ciclo_00 sin regenerar, fijar piso.

**Requisitos.** Python 3.11+, `pip install -r requirements.txt`, variable `ANTHROPIC_API_KEY` en el entorno. Si la clave vive en ~/.zshrc, Claude Code la ve solo con `zsh -ic 'comando'`. Opcional: `VERIFICADOR_MODELO=claude-fable-5-1` para un juez más duro; default `claude-opus-5`.

**Dos tipos de sesión de Claude Code, nunca se mezclan.**
- Mantenimiento: puede leer todo, incluida la rúbrica. Sirve para instalar archivos, commits, humo del verificador. NUNCA genera ganchos.
- Ciclo: sesión nueva, sin adjuntos, abre la carpeta y lee program.md. NUNCA abre verificador/rubrica_ganchos.md. Genera, verifica, compara con el piso, conserva o revierte, commit.

**Cuándo volver a claude.ai (loop lento).** Después del ciclo 0 (calibrar juez contra el ojo). Después del ciclo 5. Cuando un ciclo requiera tocar program.md, briefs/ o verificador/. Cuatro ciclos seguidos sin subir 1.0 punto. Día 3 de cada mes para el post mortem R1 a R4.

**Micropersona nueva.** Seguir el SOP en Basecamp (Notion): Micro Persona DB, prompt del Radar de DMs en n8n, GHL, Content Process, Language Bank, select de Airtable Social Listening. Después, un brief nuevo en modo hipótesis aquí y el ciclo 0 se repite como baseline nuevo.

**Sistemas que alimentan briefs/.** Language Bank (Notion, lo escribe el Radar de DMs n8n 7HHfrBSRvWpRh0FU), Airtable Social Listening - Adrianavmarquez / Instagram Raw (lo escribe Make 6145359 vía n8n 8Y1xkramD4wJWtTC), Micro Persona DB (Notion).

---

## Fase 0. Setup, 15 minutos, tú

1. Crea un repo privado en GitHub llamado `redaccion-loop`. Sube esta carpeta tal cual.
2. En tu terminal:

```bash
git clone [tu repo]
cd redaccion-loop
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=[tu key]
python verificador/reglas_duras.py generador/hook-autonomo/SKILL.md
```

Tiene que decir `PASA nivel 1`. Si no, algo se corrompió al subir.

3. Abre Claude Code en la carpeta:

```bash
claude
```

---

## Fase 1. Instalar el skill nuevo, 5 minutos, tú en claude.ai

El skill instalado no vive en `~/.claude/skills`. Vive en claude.ai y se sincroniza al desktop en una ruta de sesión que se pisa sola. Sobrescribirla en disco no dura.

Instalación real: en claude.ai, en el proyecto donde está el SOP, sube `generador/hook-autonomo/SKILL.md` como reemplazo del skill `hook-autonomo`. Guarda la versión anterior en `memoria/backup_hook_autonomo_v_anterior.md` del repo antes.

Para el loop esto no importa: program.md hace que Claude Code lea el skill directo del repo. Instalarlo en claude.ai es solo para tus sesiones de redacción con `/gancho`.

---

## Fase 2. Briefs, 30 a 45 minutos, tú con Claude Code

Necesitas 10 a 15 briefs reales y congelados. Vienen de tus bases en Notion. Claude Code no tiene el MCP de Notion salvo que lo configures, así que la forma más rápida es exportar a mano.

Para cada brief:

1. Abre Micro Persona DB en Notion y elige una micropersona. Cubre al menos: RETI, COLE, 1839, CULP, NADA, ENVI, COBR, LIST, PORT. Repite las que tengan más DMs.
2. Abre Language Bank y copia 3 a 7 frases textuales de ese dolor. Como están, con errores.
3. Llena `briefs/brief_template.md` y guárdalo como `briefs/brief_01.md`, `brief_02.md`, etc.

Regla: los briefs no se editan después del ciclo 0. Si te das cuenta de que uno está mal, lo dejas y anotas en experimentos.md que ese brief es ruido.

Cuando estén, pega en Claude Code:

```
Lee todos los briefs en briefs/. Verifica que cada uno tiene todos los campos del template y al menos 3 frases de verbatim. Reporta los que estén incompletos. No los edites.
```

---

## Fase 3. Ciclo 0, baseline, 20 minutos, Claude Code

Pega en Claude Code:

```
Lee program.md. Es tu instrucción para un loop de mejora. Estamos en modo abierto.

Corre el ciclo 0, que es el baseline: no cambies nada en el skill. Por cada brief en briefs/, ejecuta generador/hook-autonomo/SKILL.md como si fueras /gancho con ese brief como intake C0, y escribe la salida en salidas/ciclo_00/brief_XX.txt usando el formato exacto de "Entrega al verificador".

Un gancho por brief. No leas verificador/rubrica_ganchos.md bajo ninguna circunstancia.

Cuando terminen los 15, corre:
python verificador/verify.py salidas/ciclo_00 --set --runs 3

Registra el promedio y nivel1_pasan como piso inicial en memoria/ratchet-log.md, fila del ciclo 0. Muéstrame el JSON completo y para.
```

Lo que revisas tú en ese JSON, antes de seguir:

- `nivel1_pasan`: si es menor que N/N, el skill todavía produce descalificantes. Mira cuáles. Si son rayas largas o la fórmula, el skill tiene un problema de instrucción que hay que arreglar a mano antes de arrancar el loop.
- `desviacion` por archivo: si es mayor que 8 en varios, el verificador es ruidoso y hay que subir `--runs` a 5.
- Lee tres salidas al azar. Pregúntate si el puntaje del verificador coincide con tu ojo. Si el verificador puntúa 92 algo que tú no publicarías, la rúbrica está mal calibrada. Eso se arregla en claude.ai, no aquí. Ver "Cuándo volver".

---

## Fase 4. Loop abierto, 5 ciclos, Claude Code con tu confirmación entre cada uno

```
Corre el ciclo 1 según program.md. Toma la primera hipótesis pendiente de memoria/experimentos.md. Un cambio. Muéstrame el diff del skill antes de correr las salidas. Cuando apruebe, corre las salidas y el verificador, compara con el piso, decide keep o revert, registra, y para.
```

Repite para los ciclos 2 a 5 cambiando el número. En cada uno revisas el diff antes y el resultado después.

Qué buscar en estos cinco:

- Que el piso suba al menos una vez. Si en 5 ciclos no sube nada, o el skill ya está en su techo con esta rúbrica, o la rúbrica no discrimina. Las dos son información.
- Que los reverts tengan lección escrita. "Bajó" no es una lección. "Bajó porque el ejemplo nuevo empujó al generador hacia T4 cuando el objetivo era DM" sí lo es.
- Que el agente no haya tocado nada prohibido. `git log --stat` te lo dice.

---

## Fase 5. Loop cerrado, cuando confíes en el verificador

Cambia la última sección de program.md de "Abierto" a "Cerrado". Entonces:

```
Lee program.md. Modo cerrado. Corre desde el ciclo actual hasta la condición de terminado o de parar antes. No me pidas input entre ciclos. Al final dame el resumen de todos los experimentos con lo que funcionó y lo que no.
```

Y te vas. Cuando vuelvas, lees experimentos.md y ratchet-log.md.

---

## Cuándo volver a claude.ai

Claude Code es para correr el loop. claude.ai, dentro del proyecto con el SOP, es para todo lo demás. Vuelves a claude.ai en estos momentos:

**1. Después del ciclo 0, siempre.** Traes el JSON del baseline y tres salidas de ejemplo. En claude.ai se revisa si el verificador está midiendo lo que crees. Si hay que ajustar pesos en `rubrica_ganchos.md`, se decide ahí, se anota en experimentos.md con prefijo LENTO, y tú editas el archivo. El loop nunca toca la rúbrica.

**2. Después del loop abierto (ciclo 5).** Traes experimentos.md. En claude.ai se lee qué hipótesis funcionaron y se registra en Performance Intelligence Log. Si el skill mejoró, se sube la versión nueva al proyecto de claude.ai y se marca en la auditoría de Notion.

**3. Cada sesión de redacción.** Escribes con `/gancho` en claude.ai, no en Claude Code. Al cerrar, "cierra la sesión" popula Content Process. Claude Code no tiene acceso a Notion.

**4. Día 3 de cada mes.** Post mortem: R1 Metricool, R2 Sandcastles, R3 Cruce, R4 Señales. Todo en claude.ai porque necesita Metricool, Sandcastles, n8n, GHL y Notion. Si R3 marca Worth Iterating, esa hipótesis va a experimentos.md y se corre un ciclo en Claude Code.

**5. Cuando el loop pare antes por 4 ciclos sin mejora.** Eso significa que el skill llegó al techo de esta rúbrica. La siguiente mejora no está en el skill, está en la rúbrica o en los briefs, y esa es una decisión de loop lento.

Lo que nunca se hace en Claude Code: cambiar la rúbrica, cambiar los briefs, escribir en Notion, correr el post mortem, decidir sobre reglas de marca.

---

## Cuando el skill de ganchos corra limpio

Se replica la estructura para el siguiente skill. Orden sugerido por unidad de trabajo y por lo que dijo R0: `fast-reel-scripting` (porque el caption es el entregable y R0 mostró que el entregable manda), después `talking-head-scripting`, después los demás. Cada uno necesita su `rubrica_scripts.md` en verificador/, sus briefs propios, y limpieza previa de rayas largas con:

```bash
grep -c $'\u2014' ~/.claude/skills/*/SKILL.md | grep -v ':0'
```

Eso te dice cuáles skills todavía le enseñan al modelo a escribir con raya larga.
