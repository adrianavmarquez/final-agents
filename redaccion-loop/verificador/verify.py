#!/usr/bin/env python3
"""
Verificador completo. Corre nivel 1 (reglas_duras.py) y nivel 2 (rúbrica vía API).

Uso:
    python verify.py salidas/brief_01_v1.txt                 -> puntaje de un gancho
    python verify.py salidas/ --set                          -> promedio del set completo
    python verify.py salidas/ --set --runs 3                 -> 3 corridas por gancho, promedia

Requiere ANTHROPIC_API_KEY en el entorno y `pip install anthropic`.
Solo Adri edita este archivo. El generador no lo toca. Versión 1.4, 2026-09-03. max_tokens 8000 (Opus 5 agotaba 1500 pensando y devolvía texto vacío); respuesta vacía o JSON inválido se reportan en stderr con stop_reason y marcan error_tuberia. --set aborta si algún archivo trae error_tuberia.
"""

import argparse
import json
import os
import statistics
import sys
from pathlib import Path

import anthropic

from reglas_duras import verifica

AQUI = Path(__file__).parent
RUBRICA_GANCHOS = (AQUI / "rubrica_ganchos.md").read_text(encoding="utf-8")
# El verificador tiene que ser al menos tan fuerte como el generador. Default Opus 5.
# Los modelos de la generación 5 y Opus 4.7 en adelante rechazan temperature/top_p/top_k con 400,
# así que no se pasa ningún parámetro de sampling. El ruido se controla con --runs.
# Opciones: claude-opus-5 (default), claude-fable-5-1 (más fuerte, más caro), claude-sonnet-4-6 (barato, para smoke tests).
MODELO = os.environ.get("VERIFICADOR_MODELO", "claude-opus-5")


UMBRAL_TOTAL = 90
UMBRAL_COMPUERTA = 80
COMPUERTAS_NUMERICAS = ["C2_ejecucion_fiel", "C3_autonomia", "C4_triada", "C5_claridad_encadenada",
                        "C6_voz", "C7_formato_cta", "C9_profundidad_y_objetivo"]


def calcula_total(r: dict) -> dict:
    """El total y el pasa los calcula el código, no el modelo.
    Razón: el modelo tiende a colapsar total a 0 cuando no pasa, y un loop que optimiza
    contra un 0 plano no tiene gradiente. Las compuertas sí se mueven; el total tiene que reflejarlas."""
    if r.get("descalificante"):
        r["total"] = 0.0
        r["pasa"] = False
        return r
    c = r.get("compuertas") or {}
    valores = []
    for k in COMPUERTAS_NUMERICAS:
        v = c.get(k)
        if isinstance(v, dict):
            v = min(float(x) for x in v.values()) if v else 0.0
        valores.append(float(v or 0))
    total = sum(valores) / len(valores) if valores else 0.0
    ruta = bool(c.get("C4_5_ruta_de_prueba", False))
    r["total"] = round(total, 1)
    r["pasa"] = total >= UMBRAL_TOTAL and all(v >= UMBRAL_COMPUERTA for v in valores) and ruta
    r["compuerta_minima"] = round(min(valores), 1) if valores else 0.0
    return r


def nivel2(texto: str, cliente: anthropic.Anthropic) -> dict:
    resp = cliente.messages.create(
        model=MODELO,
        max_tokens=8000,
        system=RUBRICA_GANCHOS,
        messages=[{"role": "user", "content": f"Verifica este gancho con su declaración:\n\n{texto}"}],
    )
    bruto = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    limpio = bruto.replace("```json", "").replace("```", "").strip()
    stop = getattr(resp, "stop_reason", "")
    bloques = [getattr(b, "type", "?") for b in resp.content]
    if not limpio:
        msg = f"verificador devolvió texto vacío (stop_reason={stop}, bloques={bloques}). Si stop_reason es max_tokens, el modelo agotó el presupuesto pensando: subir max_tokens."
        print(f"ERROR nivel 2: {msg}", file=sys.stderr)
        return {"descalificante": msg, "total": 0.0, "pasa": False, "bruto": bruto, "error_tuberia": True}
    try:
        return calcula_total(json.loads(limpio))
    except json.JSONDecodeError:
        msg = f"verificador devolvió JSON inválido (stop_reason={stop})"
        print(f"ERROR nivel 2: {msg}", file=sys.stderr)
        return {"descalificante": msg, "total": 0.0, "pasa": False, "bruto": bruto, "error_tuberia": True}


def verifica_archivo(ruta: Path, cliente: anthropic.Anthropic, runs: int) -> dict:
    texto = ruta.read_text(encoding="utf-8")
    fallos1 = verifica(texto)
    if fallos1:
        return {"archivo": str(ruta), "nivel1": fallos1, "total": 0, "pasa": False, "nivel2": None}
    totales, resultados = [], []
    for _ in range(runs):
        r = nivel2(texto, cliente)
        resultados.append(r)
        totales.append(float(r.get("total", 0)))
    promedio = statistics.mean(totales) if totales else 0
    errores = sum(1 for r in resultados if r.get("error_tuberia"))
    return {
        "archivo": str(ruta),
        "error_tuberia": errores,
        "nivel1": [],
        "total": round(promedio, 1),
        "desviacion": round(statistics.pstdev(totales), 1) if len(totales) > 1 else 0,
        "pasa": all(r.get("pasa") for r in resultados),
        "compuerta_minima": round(statistics.mean(float(r.get("compuerta_minima", 0)) for r in resultados), 1),
        "nivel2": resultados[-1],
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("ruta")
    p.add_argument("--set", action="store_true", help="ruta es una carpeta, promediar todo")
    p.add_argument("--runs", type=int, default=1)
    args = p.parse_args()

    cliente = anthropic.Anthropic()
    ruta = Path(args.ruta)

    if args.set:
        archivos = sorted(ruta.glob("*.txt"))
        if not archivos:
            print("sin archivos .txt en la carpeta")
            sys.exit(2)
        resultados = [verifica_archivo(a, cliente, args.runs) for a in archivos]
        errores = sum(r.get("error_tuberia", 0) for r in resultados)
        if errores:
            print(f"ABORTADO: {errores} llamada(s) al nivel 2 fallaron por tubería (texto vacío o JSON inválido). El promedio no es válido y no se fija piso. Ver stderr.", file=sys.stderr)
            print(json.dumps({"set": str(ruta), "abortado": True, "errores_tuberia": errores, "por_archivo": [{"archivo": r["archivo"], "error_tuberia": r.get("error_tuberia", 0), "nivel1": r["nivel1"]} for r in resultados]}, ensure_ascii=False, indent=2))
            sys.exit(3)
        promedio = statistics.mean(r["total"] for r in resultados)
        n1 = sum(1 for r in resultados if not r["nivel1"])
        salida = {
            "set": str(ruta),
            "n": len(resultados),
            "promedio": round(promedio, 1),
            "nivel1_pasan": f"{n1}/{len(resultados)}",
            "pasan": sum(1 for r in resultados if r["pasa"]),
            "desviacion_promedio": round(statistics.mean(r.get("desviacion", 0) for r in resultados), 1),
            "compuerta_minima_set": min((r.get("compuerta_minima", 0) for r in resultados), default=0),
            "por_archivo": [{"archivo": r["archivo"], "total": r["total"], "desviacion": r.get("desviacion", 0), "compuerta_minima": r.get("compuerta_minima", 0), "pasa": r["pasa"], "nivel1": r["nivel1"]} for r in resultados],
        }
        print(json.dumps(salida, ensure_ascii=False, indent=2))
        sys.exit(0 if salida["pasan"] == len(resultados) else 1)
    else:
        r = verifica_archivo(ruta, cliente, args.runs)
        print(json.dumps(r, ensure_ascii=False, indent=2))
        sys.exit(0 if r["pasa"] else 1)


if __name__ == "__main__":
    main()
