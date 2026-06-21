"""Utilidades compartidas para los notebooks de IA Aplicada."""

import csv
import os
from pathlib import Path
from types import SimpleNamespace


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATOS_DIR = PROJECT_ROOT / "Datos"
OUTPUT_DIR = PROJECT_ROOT / "output"


def load_env(path: Path | None = None) -> None:
    """Carga variables desde .env en la raiz del proyecto."""
    env_path = path or (PROJECT_ROOT / ".env")
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def require_key(name: str) -> str:
    """Valida una clave solo cuando se usan APIs reales."""
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Falta {name} en el archivo .env")
    return value


def use_real_apis() -> bool:
    """Activa llamadas reales solo si USE_REAL_APIS=1."""
    return os.getenv("USE_REAL_APIS", "0") == "1"


def answer_question(question: str) -> str:
    """Respuestas locales claras para las preguntas usadas en clase."""
    lower = " ".join(str(question).lower().split())

    if "que es la ia" in lower or "que es inteligencia artificial" in lower or "inteligencia artificial" in lower:
        return (
            "La inteligencia artificial (IA) es un area de la informatica que crea sistemas "
            "capaces de realizar tareas asociadas a la inteligencia humana. Por ejemplo, puede "
            "entender lenguaje, reconocer imagenes, analizar datos, aprender patrones y apoyar "
            "la toma de decisiones."
        )
    if "que puedes hacer" in lower:
        return (
            "Puedo responder preguntas, resumir textos, clasificar informacion, analizar datos "
            "con Python y guardar resultados en tablas o archivos."
        )
    if "ejemplos de uso de la ia" in lower or "usos de la ia" in lower:
        return (
            "Tres ejemplos de uso de la IA en la vida diaria son: asistentes virtuales "
            "que responden preguntas, recomendaciones de peliculas o musica en plataformas "
            "digitales, y filtros que detectan correo no deseado o contenido riesgoso."
        )
    if "de que esta hecho el sol" in lower:
        return (
            "El Sol esta compuesto principalmente por hidrogeno y helio. En su nucleo, el "
            "hidrogeno se fusiona y produce helio, liberando energia en forma de luz y calor."
        )
    if "saturno" in lower:
        return (
            "Saturno esta compuesto principalmente por hidrogeno y helio. Sus anillos estan "
            "formados sobre todo por hielo, polvo y fragmentos rocosos."
        )
    if "galaxia mas antigua" in lower:
        return (
            "Las galaxias mas antiguas observadas pertenecen al universo temprano, pocos "
            "cientos de millones de anos despues del Big Bang. Estos datos pueden cambiar "
            "con nuevas observaciones astronomicas."
        )
    if "estrella mas grande" in lower:
        return (
            "Una de las estrellas mas grandes conocidas es UY Scuti, aunque su tamano exacto "
            "tiene incertidumbre y puede actualizarse con nuevas mediciones."
        )
    if "estrella mas cercana al sol" in lower:
        return (
            "La estrella mas cercana al Sol es Proxima Centauri. Esta a unos 4.24 anos luz "
            "y forma parte del sistema Alfa Centauri."
        )
    return ""


def summarize_email(prompt: str) -> str:
    """Resumen local para los correos de ejemplo."""
    lower = " ".join(str(prompt).lower().split())
    if "reporte de ventas" in lower:
        return "Resumen: se envia un reporte de ventas y se solicitan comentarios."
    if "suscripcion" in lower or "suscripción" in lower:
        return "Resumen: se confirma la renovacion de una suscripcion y el cargo aplicado."
    if "quedar" in lower or "tomar un cafe" in lower:
        return "Resumen: se propone retomar el contacto y coordinar un encuentro."
    if "plazo" in lower or "entrega" in lower:
        return "Resumen: se recuerda una fecha limite de entrega academica."
    return "Resumen: el correo contiene informacion relevante que requiere revision o seguimiento."


def fallback_text(prompt: str, task: str = "general") -> str:
    """Respuesta local util para ejecutar notebooks sin depender de internet."""
    lower = " ".join(str(prompt).lower().split())

    if task == "sentimiento":
        if any(word in lower for word in ["mala", "defecto", "defectuoso", "lenta", "no cumple", "terrible", "broken"]):
            return "Negativa"
        if any(word in lower for word in ["excelente", "buena", "perfecto", "recomiendo", "rapida", "love", "great"]):
            return "Positiva"
        return "Neutra"
    if task == "categorias":
        return "calidad del producto, entrega, precio, atencion al cliente"
    if task == "json_reviews":
        return (
            '[{"categoria": "calidad del producto", "resenas": ["Producto con fallas o baja durabilidad"]}, '
            '{"categoria": "entrega", "resenas": ["Demoras o problemas con el envio"]}, '
            '{"categoria": "atencion al cliente", "resenas": ["Dificultad para resolver reclamos"]}]'
        )
    if task == "evaluaciones_json":
        return (
            '[{"usuario": "demo", "resena_original": "Producto correcto", '
            '"evaluacion": "Neutra", "explicacion": "Ejemplo local sin conexion"}]'
        )
    if "resume" in lower and "correo" in lower:
        return summarize_email(prompt)

    answer = answer_question(prompt)
    if answer:
        return answer

    return (
        "No se llamo a la API real. El notebook funciona en modo local; activa "
        "USE_REAL_APIS=1 para consultar el modelo."
    )


def safe_generate(callable_obj, prompt: str, task: str = "general") -> str:
    """Ejecuta un modelo real o devuelve una respuesta local estructurada."""
    if not use_real_apis():
        return fallback_text(prompt, task)
    try:
        result = callable_obj(prompt)
        return getattr(result, "text", result)
    except Exception as exc:
        print(f"Usando respuesta local porque la API no estuvo disponible: {type(exc).__name__}")
        return fallback_text(prompt, task)


def save_question_answers(path: Path, items: list[dict]) -> None:
    """Guarda preguntas y respuestas en CSV sin romper comas ni saltos."""
    path.parent.mkdir(exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["numero", "pregunta", "respuesta"])
        writer.writeheader()
        writer.writerows(items)


class _LocalChat:
    def send_message(self, prompt: str) -> str:
        return fallback_text(prompt)


class _LocalGeminiModels:
    def generate_content(self, model: str, contents: str):
        return SimpleNamespace(text=fallback_text(contents))


class _LocalGeminiChats:
    def create(self, model: str):
        return _LocalChat()


class LocalGeminiClient:
    def __init__(self):
        self.models = _LocalGeminiModels()
        self.chats = _LocalGeminiChats()


class _LocalGroqCompletions:
    def create(self, model: str, messages: list[dict]):
        prompt = messages[-1].get("content", "") if messages else ""
        message = SimpleNamespace(content=fallback_text(prompt))
        return SimpleNamespace(choices=[SimpleNamespace(message=message)])


class _LocalGroqChat:
    def __init__(self):
        self.completions = _LocalGroqCompletions()


class LocalGroqClient:
    def __init__(self):
        self.chat = _LocalGroqChat()
