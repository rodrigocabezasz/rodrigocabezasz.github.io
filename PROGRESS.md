# Bitácora de Implementación

| Fecha | Tarea | Estado | Notas |
|-------|-------|--------|-------|
| 2026-04-28 | Instalación `pelican`, `markdown`, `ghp-import` | ✅ | Pelican 4.12.0 en Python 3.14; ejecutable en `%APPDATA%\Python\Python314\Scripts\` |
| 2026-04-28 | Crear `pelicanconf.py` | ✅ | SITEURL, TIMEZONE, DEFAULT_LANG, ARTICLE_URL, PAGE_SAVE_AS configurados |
| 2026-04-28 | Crear `publishconf.py` | ✅ | Config producción con feeds activados |
| 2026-04-28 | `content/pages/about.md` | ✅ | Slug: about |
| 2026-04-28 | `content/pages/projects.md` | ✅ | Slug: projects |
| 2026-04-28 | `content/pages/contact.md` | ✅ | Slug: contact |
| 2026-04-28 | `content/blog/primer-post.md` | ✅ | Primer artículo del blog |
| 2026-04-28 | Esqueleto de tema `themes/pico/` | ✅ | 6 templates mínimos con Pico.css CDN; build: 1 artículo + 3 páginas OK |
| 2026-04-28 | **Fase 2: Tema + Navegación + Estructura visual completada** | ✅ | `custom.css`, `base.html`, `index.html`, `article.html`, `page.html` reescritos; build limpio |
| 2026-04-28 | **Fase 3: SEO + GitHub Actions deploy listos** | ✅ | Open Graph, Twitter Card, canonical, RSS, `robots.txt`, feeds Atom, `deploy.yml` Pages v4 |
| 2026-04-28 | **Fase 4: Analytics + script de posts + checklist listos** | ✅ | Plausible condicional, `scripts/new_post.py`, `CHECKLIST.md` |
| 2026-04-28 | **Cierre: README.md + .gitignore + recomendaciones de mantenimiento** | ✅ | Proyecto completo y listo para `git push` |

## Notas de entorno

- Python en PATH: `C:\Program Files\Python312\` (3.12, sin Pelican)
- Pelican en Python 3.14: `C:/Users/Rcabezas/AppData/Roaming/Python/Python314/Scripts/pelican.exe`
- Fix Jinja2: `sort(default=99)` no soportado → `sort(attribute='title')`
- Fix Windows: `publishconf.py` requiere `sys.path.insert(0, dirname(__file__))` antes del import
- `robots.txt` en `content/extra/robots.txt`, mapeado a raíz vía `EXTRA_PATH_METADATA`

## Proyecto completado — Próximos pasos

1. `git init && git remote add origin https://github.com/rodrigocabezasz/rodrigocabezasz.github.io.git`
2. `git add . && git commit -m "feat: sitio inicial" && git push -u origin main`
3. GitHub → Settings → Pages → Source: **GitHub Actions**
4. Verificar deploy en verde → abrir `https://rodrigocabezasz.github.io`
