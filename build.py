"""Genera index.html (standalone) a partir del fuente del artifact.

El fuente de src/ se publica tal cual como Artifact de Claude, que envuelve el
contenido en su propio <!doctype html><head>...</head><body>. Por eso el fuente
NO lleva esas etiquetas.

Para abrir el sitio fuera de Claude (doble clic, o GitHub Pages) hace falta ese
wrapper: sin doctype el navegador entra en quirks mode. Este script lo agrega.

Uso:  python build.py
"""

import pathlib

RAIZ = pathlib.Path(__file__).parent
FUENTE = RAIZ / "src" / "ccna-200-301-es.html"
SALIDA = RAIZ / "index.html"

WRAPPER = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="El temario completo del CCNA 200-301 explicado desde cero, en español.">
<style>*,*::before,*::after{box-sizing:border-box}body{margin:0}</style>
{contenido}
</body>
</html>
"""


def main():
    if not FUENTE.exists():
        raise SystemExit("No encuentro el fuente: " + str(FUENTE))

    html = FUENTE.read_text(encoding="utf-8")

    if "<!doctype" in html.lower():
        raise SystemExit(
            "El fuente ya tiene doctype. Tiene que ser el archivo que se publica "
            "como artifact, sin wrapper."
        )

    # el <title> del fuente va en el head; el resto queda en el body
    marca = "</title>"
    corte = html.find(marca)
    if corte == -1:
        raise SystemExit("El fuente no tiene <title>.")
    corte += len(marca)

    head_extra = html[:corte].strip()
    cuerpo = html[corte:].lstrip()

    salida = WRAPPER.replace("{contenido}", head_extra + "\n</head>\n<body>\n" + cuerpo)
    SALIDA.write_text(salida, encoding="utf-8")

    print("Generado:", SALIDA)
    print("Tamano:", round(len(salida) / 1024, 1), "KB")


if __name__ == "__main__":
    main()
