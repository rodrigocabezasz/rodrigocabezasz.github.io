"""
Crea un nuevo post de blog con frontmatter prellenado.

Uso:
    python scripts/new_post.py "Título del post"
    python scripts/new_post.py "Título del post" --category DevOps --tags python,linux
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[áàäâ]', 'a', text)
    text = re.sub(r'[éèëê]', 'e', text)
    text = re.sub(r'[íìïî]', 'i', text)
    text = re.sub(r'[óòöô]', 'o', text)
    text = re.sub(r'[úùüû]', 'u', text)
    text = re.sub(r'ñ', 'n', text)
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def build_frontmatter(title: str, slug: str, category: str, tags: list[str]) -> str:
    today = date.today().isoformat()
    tags_str = ', '.join(tags) if tags else 'general'
    return f"""Title: {title}
Date: {today}
Category: {category}
Tags: {tags_str}
Slug: {slug}
Summary: Escribe aquí un resumen de una o dos frases para el listado del blog.

<!-- Escribe el contenido del post debajo de esta línea -->

## Introducción

...
"""


def main() -> None:
    parser = argparse.ArgumentParser(description='Crea un nuevo post de blog.')
    parser.add_argument('title', help='Título del post')
    parser.add_argument('--category', default='General', help='Categoría (default: General)')
    parser.add_argument('--tags', default='', help='Tags separados por coma (default: general)')
    parser.add_argument('--slug', default='', help='Slug personalizado (se genera desde el título si se omite)')
    args = parser.parse_args()

    slug = args.slug if args.slug else slugify(args.title)
    tags = [t.strip() for t in args.tags.split(',') if t.strip()]

    blog_dir = Path(__file__).parent.parent / 'content' / 'blog'
    blog_dir.mkdir(parents=True, exist_ok=True)

    output_path = blog_dir / f'{slug}.md'
    if output_path.exists():
        print(f'Error: ya existe {output_path}', file=sys.stderr)
        sys.exit(1)

    output_path.write_text(build_frontmatter(args.title, slug, args.category, tags), encoding='utf-8')
    print(f'Post creado: {output_path}')


if __name__ == '__main__':
    main()
