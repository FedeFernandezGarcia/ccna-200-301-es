# CCNA sin vueltas

Sitio de estudio para el **CCNA 200-301**, en español, explicado desde cero.
Una sola página autocontenida: 29 módulos, sin dependencias externas, sin build.

**Leelo acá:** https://fernandezfederico1899-hue.github.io/ccna-200-301-es/

Lo escribí para estudiar yo, cansado y después de trabajar, porque el material que
encontraba daba por sabido justo lo que no sabía. Si te sirve, es tuyo.

## Qué incluye

- **29 módulos** en orden pedagógico, no el del temario oficial: cada cosa se apoya
  en la anterior. Arranca en "qué es una red" sin dar nada por sabido.
- **14 ejercicios de subnetting resueltos** paso a paso, más un generador de
  práctica infinita con corrección y explicación.
- **Simulacro de examen** con 60 preguntas repartidas según los pesos oficiales
  por dominio. Sin volver atrás, con reloj y desglose de resultados por dominio.
- **Calculadora de subredes** y conversor binario, interactivos.
- 7 diagramas SVG, 62 bloques de CLI real, 29 autoevaluaciones.
- Plan de estudio de 12 semanas pensado para estudiar después de trabajar.

## Estructura

```
src/ccna-sin-vueltas.html   El fuente. Es lo único que se edita.
index.html                  Generado por build.py. Standalone, para abrir local.
build.py                    Genera index.html desde el fuente.
tools/verificar_html.py     Chequea integridad estructural del sitio.
tools/verificar_vlsm.py     Verifica los cálculos del ejercicio de VLSM.
```

### Por qué hay dos HTML

El fuente de `src/` se publica tal cual como Artifact de Claude, y la plataforma
lo envuelve en su propio `<!doctype html><head>...</head><body>`. Por eso el
fuente **no lleva** esas etiquetas.

Sin doctype, un navegador que abre el archivo directo entra en **quirks mode**,
donde `document.documentElement.scrollTop` siempre devuelve 0. El JS del sitio
lee el scroll con `window.scrollY` justamente para funcionar en los dos modos,
pero conviene igual tener una versión con el wrapper correcto:

```bash
python build.py          # regenera index.html
```

## Verificar

```bash
python tools/verificar_html.py    # estructura, links del índice, balance de tags
python tools/verificar_vlsm.py    # recalcula el ejercicio de VLSM con ipaddress
```

Los cálculos de subnetting del material fueron verificados contra la librería
`ipaddress` de Python. El generador de ejercicios se validó dejándolo generar
250 ejercicios y contrastando cada respuesta contra la misma librería: 250 de 250.

## Sobre la versión del examen

El material está ordenado según el temario **v1.1**, que es el que se rendía al
momento de escribirlo (agosto 2026), y marca con una etiqueta los temas que pesan
más en la **v2.0**.

Los pesos por dominio y los objetivos salen de los dos PDF oficiales de Cisco:

- *CCNA Exam v1.1 (200-301)* — 6 dominios: 20 / 20 / 25 / 10 / 15 / 10 %
- *Implementing and Administering Cisco Solutions (200-301 CCNA) v2.0*
  (PDF fechado 14/05/2026) — 5 dominios: 25 / 25 / 20 / 20 / 10 %

**Ojo con las fechas de transición.** Las que circulan en blogs (último día de la
v1.1 el 02/02/2027) **no están verificadas contra Cisco**: `cisco.com` devuelve
403 a las herramientas automáticas. Antes de anotarte, confirmá en el sitio
oficial qué versión se toma en tu fecha, porque de eso depende qué estudiar el
último mes.

La nota de corte que usa el simulacro (82%) tampoco es oficial: Cisco no la
publica. Sirve como orientación, no como garantía.

## Licencia y alcance

Material de estudio de uso personal. No incluye ni redistribuye contenido con
copyright de Cisco: los temarios oficiales se citan como referencia y están
disponibles en el sitio de Cisco Learning Network.

## Quién lo escribió

Federico Fernández García — coordinador de sistemas y desarrollador. Trabajo con
redes, infraestructura y desarrollo en producción, y estoy preparando el CCNA.

[LinkedIn](https://www.linkedin.com/in/federico-fernandez-garcia-8297bb2b6)
