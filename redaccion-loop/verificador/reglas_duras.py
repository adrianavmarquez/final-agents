#!/usr/bin/env python3
"""
Nivel 1 del verificador. Determinista. No se puede convencer.

Uso:
    python reglas_duras.py archivo.txt          -> imprime fallos, exit 0 si pasa, 1 si falla
    python reglas_duras.py archivo.txt --json   -> imprime JSON con fallos

Solo Adri edita este archivo. El generador no lo toca.
Versión 1.2, 2026-09-03. Cambio LENTO-2026-09: todas las verificaciones corren solo sobre la línea GANCHO cuando existe, para no descalificar verbatim del Language Bank que vive en la DECLARACIÓN.
"""

import json
import re
import sys
import unicodedata

EM_DASH = "\u2014"
EN_DASH = "\u2013"

# Estructuras vetadas como regex, insensibles a mayúsculas y acentos
ESTRUCTURAS_VETADAS = [
    (r"no se trata de .{1,60}?\bse trata de\b", "no se trata de X, se trata de Y"),
    (r"\bno ha muerto\b.{0,80}?\b(solo|solamente|simplemente)\b", "X no ha muerto, solo lo estas haciendo mal"),
    (r"^\s*no eres (mal[oa]|malísim[oa]|pésim[oa]).{0,60}?\b(solo|solamente|simplemente|es que)\b", "no eres malo en X, es que no sabes Y (como apertura)"),
    (r"\bel problema nunca fue\b", "el problema nunca fue X, fue Y"),
    (r"\bno es (falta de|que|por|cuestion de|cuestión de)\b.{0,80}?\b(es que|sino que|es porque)\b", "no es X, es que Y (variante de superficie)"),
    (r"^\s*\w+\.\s", "apertura de una sola palabra seguida de punto"),
]

FRASES_VETADAS = [
    "en el mundo de hoy", "en un mundo donde", "la realidad es que",
    "aqui esta la verdad", "aquí está la verdad", "dejame explicarte", "déjame explicarte",
    "spoiler", "desbloquea", "potencia tu", "eleva tu", "transforma tu", "nivel siguiente",
    "siguiente nivel", "next level",
]

PROMESAS = [
    r"\bvas a crecer\b", r"\bte va a hacer viral\b", r"\bviral\b", r"\bduplica(r|s)? tus\b",
    r"\bmás seguidores\b", r"\bmas seguidores\b", r"\bganar dinero\b", r"\bfacturar\b",
    r"\bmás ventas\b", r"\bmas ventas\b", r"\bcrecer en redes\b", r"\bexplotar tu cuenta\b",
]

CALCOS = [
    "hacer una decision", "hacer una decisión", "tomar accion", "tomar acción",
    "crear impacto", "hacer sentido", "aplicar para", "estar supuesto a", "al final del dia",
    "al final del día", "en base a",
]

JERGA = [
    "optimizar distribucion", "optimizar distribución", "propuesta de valor",
    "segmentar audiencia", "segmentar tu audiencia", "buyer persona",
    "funnel", "embudo de ventas", "lead magnet", "top of funnel",
]

MAX_HASHTAGS = 5


def normaliza(s: str) -> str:
    s = s.lower()
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def extrae_gancho(texto: str) -> str:
    """Si el archivo trae el bloque de entrega, aísla la línea GANCHO. Si no, usa todo."""
    m = re.search(r"^GANCHO:\s*(.+?)$", texto, re.MULTILINE)
    return m.group(1).strip() if m else texto.strip()


def verifica(texto: str) -> list[str]:
    """Todas las reglas corren sobre el gancho, no sobre la declaración.
    La declaración trae verbatim del Language Bank y ese verbatim puede contener
    promesas o calcos que la audiencia dijo. Eso es dato, no falta."""
    fallos = []
    gancho = extrae_gancho(texto)
    g = normaliza(gancho)

    if EM_DASH in gancho:
        fallos.append("raya larga (em dash)")
    if EN_DASH in gancho:
        fallos.append("raya media (en dash), usar punto o coma")

    for patron, nombre in ESTRUCTURAS_VETADAS:
        if re.search(patron, g, re.IGNORECASE | re.MULTILINE):
            fallos.append(f"estructura vetada: {nombre}")

    for frase in FRASES_VETADAS:
        if normaliza(frase) in g:
            fallos.append(f"frase vetada: '{frase}'")

    for patron in PROMESAS:
        if re.search(patron, g, re.IGNORECASE):
            fallos.append(f"promesa de resultado: /{patron}/")

    for calco in CALCOS:
        if normaliza(calco) in g:
            fallos.append(f"calco del ingles: '{calco}'")

    for j in JERGA:
        if normaliza(j) in g:
            fallos.append(f"jerga sin traducir: '{j}'")

    hashtags = re.findall(r"#\w+", gancho)
    if len(hashtags) > MAX_HASHTAGS:
        fallos.append(f"{len(hashtags)} hashtags, maximo {MAX_HASHTAGS}")

    return fallos


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    ruta = sys.argv[1]
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()
    fallos = verifica(texto)
    if "--json" in sys.argv:
        print(json.dumps({"archivo": ruta, "pasa": not fallos, "fallos": fallos}, ensure_ascii=False, indent=2))
    else:
        if fallos:
            print(f"FALLA nivel 1: {ruta}")
            for f_ in fallos:
                print(f"  - {f_}")
        else:
            print(f"PASA nivel 1: {ruta}")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
