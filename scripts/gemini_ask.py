#!/usr/bin/env python3
"""
Asistente de contenido con Cerebro Personal.
Equivalente a una Gemini Gem, pero lee tus archivos locales directamente.

Uso:
  python scripts/gemini_ask.py                # Modo semanal: sugiere 2-3 ideas
  python scripts/gemini_ask.py --mode weekly  # Igual que el anterior
  python scripts/gemini_ask.py --mode series  # Siguiente post de la serie activa
  python scripts/gemini_ask.py --mode evergreen  # Idea evergreen de alto impacto
  python scripts/gemini_ask.py --mode quarterly  # Reflexión trimestral
  python scripts/gemini_ask.py --create       # Sugiere Y crea el post directamente

Requisitos:
  pip install google-genai python-dotenv
  Crear .env con: GEMINI_API_KEY=tu_clave_aqui
  Obtener clave en: https://aistudio.google.com/app/apikey
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

# Windows: forzar UTF-8 en stdout para soportar emojis
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

try:
    from google import genai
    from dotenv import load_dotenv
except ImportError:
    print("Instala dependencias: pip install google-genai python-dotenv")
    sys.exit(1)


ROOT = Path(__file__).parent.parent
BRAIN_DIR = ROOT / "brain"
PROMPTS_DIR = ROOT / "_prompts"
SCRIPTS_DIR = ROOT / "scripts"


def load_api_key() -> str:
    load_dotenv(ROOT / ".env")
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key:
        print("ERROR: GEMINI_API_KEY no encontrada.")
        print("  1. Ve a https://aistudio.google.com/app/apikey")
        print("  2. Crea una clave API (gratis con tu cuenta Google)")
        print("  3. Crea el archivo .env en la raíz del proyecto:")
        print("     GEMINI_API_KEY=tu_clave_aqui")
        sys.exit(1)
    return key


def read_brain() -> str:
    """Lee todos los archivos del cerebro y los compila en un contexto."""
    if not BRAIN_DIR.exists():
        return "(Sin archivos de cerebro cargados aún)"

    sections = []
    folder_order = [
        "01-Proyectos",
        "02-Aprendizajes",
        "03-Tecnologias",
        "04-Ideas",
        "05-Metas",
        "06-Posts-Publicados",
    ]

    for folder_name in folder_order:
        folder = BRAIN_DIR / folder_name
        if not folder.exists():
            continue
        files = sorted(folder.glob("*.md"))
        if not files:
            continue
        sections.append(f"\n## 📁 {folder_name}\n")
        for f in files:
            content = f.read_text(encoding="utf-8").strip()
            sections.append(f"### {f.name}\n{content}\n")

    return "\n".join(sections) if sections else "(Sin archivos de cerebro cargados aún)"


def read_master_prompt() -> str:
    prompt_file = PROMPTS_DIR / "gemini-cerebro.md"
    if prompt_file.exists():
        return prompt_file.read_text(encoding="utf-8")
    return ""


def build_prompt(mode: str, brain_context: str, master_prompt: str) -> str:
    mode_instructions = {
        "weekly": (
            "Modo SEMANAL: Revisa los aprendizajes recientes y los proyectos activos. "
            "Sugiere 2-3 ideas de post concretas con su outline completo."
        ),
        "series": (
            "Modo SERIE: Identifica la serie de posts más activa (probablemente Framework de Gestión). "
            "Sugiere el siguiente post lógico que continúe la narrativa, con outline detallado."
        ),
        "evergreen": (
            "Modo EVERGREEN: Identifica un tema de alta búsqueda en el ecosistema Python/BI/automatización "
            "que Rodrigo pueda cubrir desde su experiencia real. Debe ser un tema que aguante meses. "
            "Sugiere 1 idea muy desarrollada."
        ),
        "quarterly": (
            "Modo REFLEXIÓN TRIMESTRAL: Analiza el cerebro completo. "
            "Sigue el formato del prompt de reflexión trimestral: resumen del trimestre, "
            "logros, gaps, y plan para el próximo trimestre."
        ),
    }

    instruction = mode_instructions.get(mode, mode_instructions["weekly"])

    return f"""
{master_prompt}

---

## CONTEXTO ACTUAL DEL CEREBRO

{brain_context}

---

## INSTRUCCIÓN PARA ESTA SESIÓN

{instruction}

Responde en español. Usa el formato Markdown definido en el prompt maestro.
Sé específico con los títulos (incluye palabra clave SEO) y los outlines (3-4 H2 mínimo con descripción breve).
"""


MODELS = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
]


def call_gemini(prompt: str, api_key: str) -> str:
    client = genai.Client(api_key=api_key)
    print("⏳ Consultando Gemini...\n")

    last_error = None
    for model in MODELS:
        try:
            response = client.models.generate_content(model=model, contents=prompt)
            print(f"[modelo: {model}]\n")
            return response.text
        except Exception as e:
            err_str = str(e)
            if "429" in err_str or "RESOURCE_EXHAUSTED" in err_str:
                print(f"  [{model}] cuota agotada, probando siguiente modelo...")
                last_error = e
                continue
            raise  # otro error → propagar

    # Todos los modelos agotados
    print("\nERROR: Cuota agotada en todos los modelos.")
    print("Probablemente el proyecto de tu API key tiene billing habilitado sin créditos.")
    print("Solución: ve a https://aistudio.google.com/app/apikey y crea una key nueva")
    print("  → elige 'Create API key in new project' para usar el free tier gratuito.")
    raise last_error


def ask_to_create_post(response_text: str) -> None:
    """Parsea la primera idea del response y ofrece crear el post."""
    print("\n" + "─" * 60)
    print("¿Quieres crear el esqueleto del primer post sugerido?")
    print("Escribe el título exacto o presiona Enter para saltar: ", end="")
    title = input().strip()

    if not title:
        print("Ok. Usa: python scripts/new_post.py \"Título\" --tags tag1,tag2")
        return

    print("Tags (separados por coma, ej: python,fastapi): ", end="")
    tags = input().strip() or "python"

    print("Categoría (Python / Automatización / BI): ", end="")
    category = input().strip() or "Python"

    cmd = [
        sys.executable,
        str(SCRIPTS_DIR / "new_post.py"),
        title,
        "--tags", tags,
        "--category", category,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error:", result.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Asistente de contenido con Cerebro Personal"
    )
    parser.add_argument(
        "--mode",
        choices=["weekly", "series", "evergreen", "quarterly"],
        default="weekly",
        help="Modo de operación (default: weekly)",
    )
    parser.add_argument(
        "--create",
        action="store_true",
        help="Después de sugerir, ofrece crear el post directamente",
    )
    parser.add_argument(
        "--brain-only",
        action="store_true",
        help="Solo muestra el contexto del cerebro que se enviará a Gemini (debug)",
    )
    args = parser.parse_args()

    brain_context = read_brain()

    if args.brain_only:
        print("=== CONTEXTO DEL CEREBRO ===\n")
        print(brain_context)
        print(f"\n[{len(brain_context)} caracteres]")
        return

    api_key = load_api_key()
    master_prompt = read_master_prompt()
    full_prompt = build_prompt(args.mode, brain_context, master_prompt)

    response = call_gemini(full_prompt, api_key)

    print("=" * 60)
    print(f"🧠 CEREBRO PROFESIONAL — Modo: {args.mode.upper()}")
    print("=" * 60)
    print(response)

    if args.create:
        ask_to_create_post(response)


if __name__ == "__main__":
    main()
