"""Chequeo de integridad estructural del sitio.

Verifica que las etiquetas esten balanceadas, que el indice no tenga links
rotos y que no queden restos raros en el HTML.

Uso:  python tools/verificar_html.py
"""

import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).parent.parent
FUENTE = RAIZ / "src" / "ccna-200-301-es.html"

c = FUENTE.read_text(encoding="utf-8")
fallos = 0

print("Archivo:", FUENTE.name, "|", round(len(c) / 1024, 1), "KB")
print()

navs = re.findall(r'href="#([a-z0-9]+)"', c)
secs = re.findall(r'<section id="([a-z0-9]+)"', c)
rotos = [n for n in navs if n not in secs]
huerfanas = [s for s in secs if s not in navs]
print("Links en el indice:", len(navs), "| Secciones:", len(secs))
if rotos:
    print("  FALLA - links rotos:", rotos); fallos += 1
if huerfanas:
    print("  FALLA - secciones sin link:", huerfanas); fallos += 1
if not rotos and not huerfanas:
    print("  OK - el indice y las secciones coinciden")
print()

print("Balance de etiquetas:")
for tag in ["section", "table", "details", "svg", "figure", "tr", "pre", "summary", "div"]:
    o = len(re.findall("<" + tag + "[ >]", c))
    cl = len(re.findall("</" + tag + ">", c))
    estado = "OK" if o == cl else "FALLA"
    if o != cl:
        fallos += 1
    print("  ", tag.ljust(9), str(o).rjust(4), str(cl).rjust(4), estado)
print()

nums = re.findall(r'<span class="n">(\d+)</span>', c)
if nums == [str(i).zfill(2) for i in range(len(nums))]:
    print("Numeracion del indice: OK, correlativa de 00 a", str(len(nums) - 1).zfill(2))
else:
    print("Numeracion del indice: FALLA -", nums); fallos += 1

print("Preguntas del simulacro:", len(re.findall(r"\{d:\d,m:", c)))
print("Ejercicios resueltos:", len(re.findall(r'class="ej"', c)))
print("Autoevaluaciones:", len(re.findall(r'class="chk"', c)))

# el em-dash se evita a proposito en todo el texto
em = c.count(chr(8212))
print("Em-dashes:", em, "OK" if em == 0 else "FALLA")
if em:
    fallos += 1

print()
print("RESULTADO:", "todo en orden" if fallos == 0 else str(fallos) + " problema(s)")
sys.exit(1 if fallos else 0)
