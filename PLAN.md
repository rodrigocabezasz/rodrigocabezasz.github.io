# 🌐 PLAN: Marca Personal + Blog (Pelican + Python)

## 🎯 Objetivo
Sitio estático JAMstack para mostrar: CV, proyectos GitHub, blog semanal. Desplegado en GitHub Pages. 0 IA, 0 backend innecesario.

## 🛠️ Stack
- **SSG**: Pelican (Python 3.10+)
- **Estilo**: Pico.css v2 (CDN, 0 build step)
- **Contenido**: Markdown + frontmatter
- **Deploy**: GitHub Pages vía `ghp-import` o GitHub Actions
- **IDE**: VS Code + Claude (executor)

## 📐 Estructura Esperada

content/
├── pages/
│ ├── about.md
│ ├── projects.md
│ └── contact.md
├── blog/
│ ├── primer-post.md
│ └── ...
pelicanconf.py ← Config principal
publishconf.py ← Config producción
Makefile / tasks.py ← Atajos de build/deploy


## 🚦 Fases
1. **Setup**: `pelican-quickstart`, estructura base, `pelicanconf.py` personalizado
2. **Tema/Estilo**: Integrar Pico.css, layout limpio, header/footer, navegación
3. **Contenido**: CV, proyectos (cards estáticas), blog con tags
4. **Deploy**: GitHub Actions o `ghp-import`, dominio opcional
5. **SEO/Analytics**: `sitemap.xml`, `robots.txt`, meta tags, Plausible/Umami (opcional)

## ⚠️ Reglas para Claude
- No instales Node.js ni dependencias JS
- Todo debe funcionar con `python -m pelican`
- Usa solo Markdown + HTML básico
- Mantén `pelicanconf.py` limpio y documentado
- Actualiza `PROGRESS.md` tras cada paso

