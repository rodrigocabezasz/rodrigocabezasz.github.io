#!/usr/bin/env python3
"""
Cierra el ciclo: post publicado → Cerebro actualizado.
Exporta un post Pelican a brain/06-Posts-Publicados/posts-publicados.md

Uso:
  python scripts/export_post_to_brain.py content/blog/mi-post.md
  python scripts/export_post_to_brain.py content/blog/mi-post.md --preview

Luego sube el archivo actualizado a Drive:
  python scripts/sync_to_drive.py
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).parent.parent
BRAIN_POSTS = ROOT / "brain" / "06-Posts-Publicados" / "posts-publicados.md"


def parse_pelican_frontmatter(filepath: Path) -> dict:
    """Parsea el frontmatter de Pelican (formato clave: valor, sin ---)."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()
    meta = {}
    body_start = 0

    for i, line in enumerate(lines):
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            meta[key.strip().lower()] = val.strip()
            body_start = i + 1
        elif i > 0 and line.strip() == "":
            body_start = i + 1
            break

    meta["_body"] = "\n".join(lines[body_start:]).strip()
    return meta


def build_brain_entry(filepath: Path) -> str:
    meta = parse_pelican_frontmatter(filepath)

    title = meta.get("title", "Sin título")
    date_raw = meta.get("date", datetime.now().strftime("%Y-%m-%d"))
    date = date_raw[:10]  # solo YYYY-MM-DD
    tags = meta.get("tags", "")
    category = meta.get("category", "")
    slug = meta.get("slug", filepath.stem)
    summary = meta.get("summary", "")

    # Construir URL desde fecha y slug
    try:
        year, month = date[:4], date[5:7]
        url = f"/blog/{year}/{month}/{slug}/"
    except Exception:
        url = f"/blog/{slug}/"

    # Preview del cuerpo (primeros 400 chars, sin markdown de imágenes)
    body = meta.get("_body", "")
    body_clean = "\n".join(
        line for line in body.splitlines()
        if not line.startswith("![") and line.strip()
    )
    preview = body_clean[:400] + ("..." if len(body_clean) > 400 else "")

    return f"""
---

## {title}
**Fecha**: {date}
**URL**: {url}
**Tags**: {tags}
**Categoría**: {category}
**Resumen**: {summary}

**Preview del contenido**:
{preview}

**Follow-ups posibles**:
- [ ]
- [ ]
"""


def main():
    parser = argparse.ArgumentParser(
        description="Exporta un post publicado al cerebro (brain/06-Posts-Publicados)"
    )
    parser.add_argument("post", help="Ruta al archivo .md del post")
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Muestra la entrada generada sin guardar",
    )
    args = parser.parse_args()

    filepath = Path(args.post)
    if not filepath.exists():
        print(f"ERROR: No se encontró el archivo: {filepath}")
        sys.exit(1)

    entry = build_brain_entry(filepath)

    if args.preview:
        print("=== ENTRADA GENERADA (preview) ===\n")
        print(entry)
        print("\n=== Usa sin --preview para guardar ===")
        return

    if not BRAIN_POSTS.exists():
        print(f"ERROR: No existe {BRAIN_POSTS}")
        print("Asegúrate de tener la carpeta brain/ configurada.")
        sys.exit(1)

    with open(BRAIN_POSTS, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"✅ Post exportado al cerebro: {BRAIN_POSTS}")
    print(f"📄 Post: {filepath.name}")
    print()
    print("Próximo paso — sube el cerebro a Drive:")
    print("  python scripts/sync_to_drive.py")


if __name__ == "__main__":
    main()
