# IA Aplicada

Proyecto practico de inteligencia artificial aplicada con Python, Jupyter Notebook, APIs de modelos de lenguaje y analisis de datos.

El repositorio esta organizado como una secuencia de 8 notebooks. Cada notebook trabaja una parte del flujo: conexion con modelos, resumen de textos, lectura de datos, generacion de respuestas, analisis de sentimiento, validacion de errores, uso de JSON y un desafio final integrador.

## Objetivo

El objetivo del proyecto es practicar como usar IA generativa dentro de notebooks de Python de una forma ordenada, reproducible y facil de revisar.

En este proyecto se aprende a:

- Conectar Python con modelos de lenguaje.
- Usar variables de entorno para proteger claves API.
- Leer y escribir archivos `.txt` y `.csv`.
- Trabajar con datos usando `pandas`.
- Generar respuestas a preguntas con un modelo.
- Clasificar sentimientos en resenas.
- Validar errores comunes en Python.
- Pedir respuestas en formato JSON.
- Guardar resultados estructurados en la carpeta `output/`.

## Estructura del proyecto

```text
IA_Aplicada/
+-- Datos/
|   +-- reviews.csv
|   +-- tabla.csv
+-- notebooks/
|   +-- 01_chat_gemini.ipynb
|   +-- 02_groq_resumen_emails.ipynb
|   +-- 03_pandas_tabla.ipynb
|   +-- 04_desafio_preguntas_llm.ipynb
|   +-- 05_desafio_sentimiento_reviews.ipynb
|   +-- 06_aula6_validacion.ipynb
|   +-- 07_json.ipynb
|   +-- 08_desafio_final.ipynb
|   +-- _setup.py
+-- output/
|   +-- archivos generados al ejecutar los notebooks
+-- .env
+-- .gitignore
+-- requirements.txt
+-- DOCUMENTACION.md
+-- README.md
```

La carpeta `output/` se genera durante la ejecucion. No es necesario subir sus archivos si se quiere mantener el repositorio limpio, porque los notebooks pueden volver a crearlos.

## Notebooks

| Notebook | Tema principal |
| --- | --- |
| `01_chat_gemini.ipynb` | Preguntas y respuestas con un chat tipo Gemini |
| `02_groq_resumen_emails.ipynb` | Resumen de correos con modelos de lenguaje |
| `03_pandas_tabla.ipynb` | Lectura y exploracion basica de una tabla con pandas |
| `04_desafio_preguntas_llm.ipynb` | Generacion y guardado de respuestas a preguntas |
| `05_desafio_sentimiento_reviews.ipynb` | Clasificacion de sentimiento en resenas |
| `06_aula6_validacion.ipynb` | Manejo de errores y filtrado de resenas negativas |
| `07_json.ipynb` | Trabajo con respuestas estructuradas en JSON |
| `08_desafio_final.ipynb` | Flujo final integrando datos, IA, JSON y resumen |

## Instalacion

Desde la raiz del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Si usas VS Code, selecciona como kernel del notebook:

```text
Python (.venv)
```

o directamente:

```text
.\.venv\Scripts\python.exe
```

## Variables de entorno

El proyecto usa un archivo `.env` para guardar claves privadas.

Ejemplo:

```env
GEMINI_API_KEY=tu_clave_de_gemini
GROQ_API_KEY=tu_clave_de_groq
```

El archivo `.env` esta ignorado por Git para no subir claves privadas.

## Modo rapido y modo API real

Por defecto, los notebooks usan respuestas locales de ejemplo. Esto permite ejecutar todo rapido y sin depender de internet.

Modo rapido local:

```powershell
$env:USE_REAL_APIS="0"
```

Modo con APIs reales:

```powershell
$env:USE_REAL_APIS="1"
```

Cuando `USE_REAL_APIS=1`, los notebooks intentan llamar a Gemini y Groq usando las claves del archivo `.env`.

## Ejecucion recomendada

Para revisar el proyecto, ejecuta los notebooks en orden:

```text
01 -> 02 -> 03 -> 04 -> 05 -> 06 -> 07 -> 08
```

Algunos notebooks dependen de archivos generados por notebooks anteriores. Por eso conviene mantener el orden.

## Archivos generados

Al ejecutar los notebooks se crean archivos en `output/`, por ejemplo:

- `01_respuestas_chat_gemini.csv`
- `lista-de-resumenes.txt`
- `preguntas.txt`
- `respuestas_preguntas.csv`
- `respuestas1.csv`
- `respuestas2.csv`
- `reviews_sentimiento.csv`
- `resenas.txt`

Estos archivos son resultados de ejecucion. Si se borran, los notebooks los vuelven a crear.

## Documentacion completa

Para una explicacion mas detallada del flujo, revisa:

```text
DOCUMENTACION.md
```

Alli se explica que hace cada notebook, que archivos usa, que archivos genera y como solucionar errores comunes.
