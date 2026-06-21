# Documentacion del proyecto IA Aplicada

Esta documentacion explica el proyecto de forma sencilla y completa para que pueda revisarse, ejecutarse y subirse sin confusion.

## 1. Descripcion general

`IA_Aplicada` es un proyecto educativo hecho con notebooks de Jupyter. El proyecto muestra como integrar inteligencia artificial generativa con tareas practicas de Python:

- hacer preguntas a un modelo;
- resumir correos;
- leer datos con pandas;
- guardar resultados en archivos;
- analizar sentimientos;
- manejar errores;
- trabajar con JSON;
- construir un flujo final con datos simulados.

El proyecto esta pensado para ejecutarse en orden, desde el notebook `01` hasta el `08`.

## 2. Componentes principales

### `Datos/`

Contiene los archivos base del proyecto:

- `tabla.csv`: tabla pequena para practicar lectura con pandas.
- `reviews.csv`: conjunto de resenas usado para analisis de sentimiento.

Estos archivos son datos de entrada y deben permanecer en el repositorio.

### `notebooks/`

Contiene los 8 notebooks principales y el archivo auxiliar `_setup.py`.

Los notebooks son el centro del proyecto. Cada uno representa una parte del aprendizaje.

### `notebooks/_setup.py`

Archivo auxiliar compartido por los notebooks.

Centraliza funciones importantes:

- cargar variables desde `.env`;
- verificar claves API;
- detectar si se usan APIs reales o modo local;
- generar respuestas locales cuando no se quiere llamar a internet;
- guardar preguntas y respuestas en CSV;
- crear clientes locales simulados para Gemini y Groq.

Este archivo evita repetir codigo en todos los notebooks y hace que la ejecucion sea mas rapida y estable.

### `output/`

Carpeta de resultados generados.

No contiene datos base, sino archivos creados al ejecutar notebooks. Por ejemplo:

- respuestas generadas;
- resumenes;
- preguntas guardadas;
- resenas clasificadas;
- archivos intermedios para notebooks posteriores.

Si se elimina `output/`, los notebooks pueden volver a crear sus archivos.

## 3. Modo local y modo API real

El proyecto puede ejecutarse de dos formas.

### Modo local rapido

Es el modo recomendado para revisar o presentar el proyecto sin depender de internet.

```powershell
$env:USE_REAL_APIS="0"
```

En este modo:

- no se llama a Gemini ni Groq;
- se usan respuestas locales bien estructuradas;
- los notebooks ejecutan mucho mas rapido;
- se puede verificar toda la logica sin gastar tokens ni esperar respuestas externas.

### Modo API real

Usa Gemini y Groq realmente.

```powershell
$env:USE_REAL_APIS="1"
```

En este modo se necesita tener el archivo `.env` con las claves:

```env
GEMINI_API_KEY=tu_clave_de_gemini
GROQ_API_KEY=tu_clave_de_groq
```

Este modo puede demorar mas porque depende de internet y de la disponibilidad de las APIs.

## 4. Explicacion notebook por notebook

### 01_chat_gemini.ipynb

Objetivo:

Practicar una conversacion basica con un modelo tipo Gemini.

Que hace:

- carga configuracion del proyecto;
- crea un cliente Gemini real o local;
- define preguntas claras;
- genera respuestas;
- guarda las respuestas en `output/01_respuestas_chat_gemini.csv`;
- muestra una tabla con pregunta y respuesta.

Archivo generado:

```text
output/01_respuestas_chat_gemini.csv
```

### 02_groq_resumen_emails.ipynb

Objetivo:

Resumir correos electronicos usando un modelo de lenguaje.

Que hace:

- define una lista de correos de ejemplo;
- resume cada correo;
- guarda los resumenes en un archivo de texto;
- vuelve a leer el archivo para practicar lectura y escritura.

Archivo generado:

```text
output/lista-de-resumenes.txt
```

### 03_pandas_tabla.ipynb

Objetivo:

Practicar lectura de archivos CSV con pandas.

Que hace:

- lee `Datos/tabla.csv`;
- muestra la tabla;
- usa operaciones basicas como `head()` y `tail()`.

Archivo usado:

```text
Datos/tabla.csv
```

### 04_desafio_preguntas_llm.ipynb

Objetivo:

Crear preguntas, obtener respuestas y guardar resultados estructurados.

Que hace:

- define una lista de preguntas;
- guarda las preguntas en `output/preguntas.txt`;
- lee las preguntas desde el archivo;
- genera respuestas;
- guarda una tabla limpia con columnas `numero`, `pregunta` y `respuesta`;
- lee nuevamente el CSV con pandas.

Archivos generados:

```text
output/preguntas.txt
output/respuestas_preguntas.csv
output/respuestas1.csv
output/respuestas2.csv
```

### 05_desafio_sentimiento_reviews.ipynb

Objetivo:

Clasificar resenas segun sentimiento.

Que hace:

- lee `Datos/reviews.csv`;
- toma la columna de texto de las resenas;
- clasifica cada resena como `Positiva`, `Negativa` o `Neutra`;
- agrega una columna nueva llamada `Sentimiento`;
- guarda el resultado para usarlo en notebooks posteriores.

Archivos usados:

```text
Datos/reviews.csv
```

Archivo generado:

```text
output/reviews_sentimiento.csv
```

### 06_aula6_validacion.ipynb

Objetivo:

Practicar manejo de errores y filtrar datos.

Que hace:

- muestra ejemplos de `try/except`;
- evita errores comunes como sumar numeros con texto;
- lee las resenas clasificadas;
- filtra resenas negativas;
- une las resenas negativas para analizarlas.

Archivo usado:

```text
output/reviews_sentimiento.csv
```

Si ese archivo no existe, el notebook puede crear una version local para seguir funcionando.

### 07_json.ipynb

Objetivo:

Trabajar con respuestas estructuradas en JSON.

Que hace:

- lee resenas negativas;
- pide una clasificacion por categorias;
- obtiene una respuesta en formato JSON;
- convierte el texto JSON a una estructura de Python usando `json.loads()`;
- muestra el resultado como lista de diccionarios.

Archivo usado:

```text
output/reviews_sentimiento.csv
```

### 08_desafio_final.ipynb

Objetivo:

Integrar todo lo aprendido en un flujo final.

Que hace:

- usa categorias de resenas negativas;
- genera un conjunto de resenas simuladas;
- guarda las resenas en `output/resenas.txt`;
- analiza una muestra;
- genera resultados en JSON;
- procesa conteos por sentimiento;
- une resultados para mostrar un resumen final.

Archivo generado:

```text
output/resenas.txt
```

## 5. Orden recomendado de ejecucion

Ejecutar en este orden:

```text
01_chat_gemini.ipynb
02_groq_resumen_emails.ipynb
03_pandas_tabla.ipynb
04_desafio_preguntas_llm.ipynb
05_desafio_sentimiento_reviews.ipynb
06_aula6_validacion.ipynb
07_json.ipynb
08_desafio_final.ipynb
```

Motivo:

- algunos notebooks generan archivos que otros notebooks usan despues;
- ejecutar en orden evita errores por archivos faltantes;
- el flujo queda mas facil de entender.

## 6. Instalacion paso a paso

Desde la raiz del proyecto:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Luego abrir VS Code y seleccionar el kernel:

```text
.\.venv\Scripts\python.exe
```

Si aparece un error como `kernel is dead`, cambiar el kernel del notebook a `.venv`.

## 7. Errores comunes

### Error: `Cannot run cells, as the kernel is dead`

Causa probable:

VS Code esta usando otro Python, por ejemplo `Python 3.12`, en lugar del entorno `.venv`.

Solucion:

Seleccionar el kernel:

```text
Python (.venv)
```

o:

```text
.\.venv\Scripts\python.exe
```

### Error: falta `GEMINI_API_KEY` o `GROQ_API_KEY`

Causa:

Se activo el modo API real y no existen las claves en `.env`.

Solucion:

Crear un archivo `.env` con:

```env
GEMINI_API_KEY=tu_clave_de_gemini
GROQ_API_KEY=tu_clave_de_groq
```

O usar modo local:

```powershell
$env:USE_REAL_APIS="0"
```

### La ejecucion demora mucho

Causa:

Cada notebook puede iniciar un kernel nuevo si se ejecuta con `nbconvert`. En VS Code tambien puede demorar si usa APIs reales.

Solucion:

- usar modo local con `USE_REAL_APIS=0`;
- ejecutar los notebooks en orden desde el mismo kernel;
- evitar reiniciar el kernel entre notebooks si no es necesario.

## 8. Que se debe subir al repositorio

Recomendado subir:

```text
README.md
DOCUMENTACION.md
requirements.txt
.gitignore
Datos/
notebooks/
```

No subir:

```text
.env
.venv/
__pycache__/
output/
```

Motivo:

- `.env` contiene claves privadas;
- `.venv/` pesa mucho y se puede recrear;
- `__pycache__/` es generado por Python;
- `output/` contiene resultados que se pueden regenerar.

## 9. Resumen final

El proyecto esta organizado para demostrar un flujo completo de IA aplicada:

1. conectar o simular modelos de lenguaje;
2. generar respuestas;
3. resumir texto;
4. leer datos;
5. clasificar sentimientos;
6. validar errores;
7. trabajar con JSON;
8. guardar resultados reutilizables.

La estructura actual permite revisar el proyecto rapidamente en modo local y tambien usar APIs reales cuando se quiera probar con modelos externos.
