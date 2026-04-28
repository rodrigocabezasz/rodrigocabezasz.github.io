# Rodrigo Cabezas Z. — Sitio personal

Sitio estático de marca personal construido con **Pelican** (Python) y **Pico.css v2**.  
Desplegado automáticamente en **GitHub Pages** vía GitHub Actions.

🌐 **[rodrigocabezasz.github.io](https://rodrigocabezasz.github.io)**

---

## Stack

| Capa | Tecnología |
|---|---|
| Generador estático | [Pelican](https://getpelican.com) 4.12+ |
| Estilos | [Pico.css v2](https://picocss.com) (CDN, 0 build step) |
| Contenido | Markdown + frontmatter |
| Deploy | GitHub Pages v4 + GitHub Actions |
| Analytics | [Plausible](https://plausible.io) (opcional, sin cookies) |

---

## Estructura

```
.
├── content/
│   ├── pages/          # Páginas estáticas (about, projects, contact)
│   ├── blog/           # Posts del blog (Markdown)
│   └── extra/          # Archivos estáticos (robots.txt, favicon)
├── themes/pico/
│   ├── static/css/     # custom.css (variables de marca)
│   └── templates/      # Templates Jinja2 (base, index, article, page…)
├── scripts/
│   └── new_post.py     # CLI para crear posts rápido
├── pelicanconf.py      # Config desarrollo
├── publishconf.py      # Config producción
└── .github/workflows/
    └── deploy.yml      # CI/CD → GitHub Pages
```

---

## Desarrollo local

### Requisitos

```bash
pip install pelican markdown ghp-import
```

> **Windows:** Pelican se instala en `%APPDATA%\Python\Python3XX\Scripts\`.  
> Sustituye `pelican` por la ruta completa si no está en el PATH.

### Comandos diarios

```bash
# Desarrollo con recarga automática
pelican content -s pelicanconf.py -r

# Servir el output en http://localhost:8000
python -m pelican.server 8000 -d output

# Build de producción (limpia output/ antes de generar)
pelican content -s publishconf.py

# Verificar tamaño del output (útil para auditoría Lighthouse)
du -sh output/
```

### Crear un nuevo post

```bash
python scripts/new_post.py "Título del post"
python scripts/new_post.py "Automatizando dashboards con Plotly" --tags python,plotly,bi
python scripts/new_post.py "Mi post" --category DevOps --tags linux,bash --slug slug-custom
```

El script genera el archivo `.md` en `content/blog/` con frontmatter prellenado y fecha de hoy.  
Luego édita el archivo, haz commit y push: GitHub Actions despliega en segundos.

### Publicar un post

```bash
git add content/blog/mi-post.md
git commit -m "post: Título del post"
git push
# ✅ GitHub Actions despliega automáticamente a Pages
```

---

## Mantenimiento

### Actualizar dependencias

```bash
pip install --upgrade pelican markdown
```

Revisa el [changelog de Pelican](https://docs.getpelican.com/en/latest/changelog.html) antes de actualizar en producción.

### Añadir una página nueva

1. Crea `content/pages/nueva-pagina.md` con `Title:`, `Slug:` y `Status: published`.
2. Pelican la detecta automáticamente y la añade al menú (controlado por `DISPLAY_PAGES_ON_MENU = True`).

### Controlar el orden del menú

Añade `Sortorder: N` en el frontmatter de cada página (número menor = aparece primero):

```markdown
Title: Sobre mí
Slug: about
Sortorder: 1
Status: published
```

Luego actualiza `base.html` para ordenar por `sortorder` en lugar de `title`.

### Añadir Analytics

Plausible ya está integrado. Para activarlo:
1. Crea cuenta en [plausible.io](https://plausible.io) y añade el dominio.
2. Verifica que `publishconf.py` tiene `PLAUSIBLE_DOMAIN = 'rodrigocabezasz.github.io'`.
3. Haz push → se activa automáticamente en producción.

Para desactivarlo, deja `PLAUSIBLE_DOMAIN = ''` en `publishconf.py`.

---

## Funcionalidades futuras (sin romper el stack)

Estas extensiones son compatibles con el stack actual (Python + Markdown + HTML):

| Feature | Herramienta | Esfuerzo |
|---|---|---|
| Búsqueda estática sin backend | [Pagefind](https://pagefind.app) | Bajo — post-build |
| Comentarios sin base de datos | [Giscus](https://giscus.app) (GitHub Discussions) | Bajo — script en `base.html` |
| Sitemap automático | Plugin `sitemap` de Pelican | Bajo — `pip install pelican-sitemap` |
| Imágenes optimizadas | Plugin `optimize-images` | Medio |
| Migración de contenido | Compatible con Astro, Hugo, 11ty | Tu Markdown es portable |

---

## Deploy

El deploy es completamente automático:

1. Haz `git push` a `main`
2. GitHub Actions ejecuta `.github/workflows/deploy.yml`:
   - Instala dependencias Python
   - Ejecuta `pelican content -s publishconf.py`
   - Sube `output/` a GitHub Pages con `actions/upload-pages-artifact`
3. El sitio queda publicado en `https://rodrigocabezasz.github.io`

Para activar la primera vez:  
**Settings → Pages → Source → GitHub Actions**

---

## Licencia

Contenido: © Rodrigo Cabezas Z. — Todos los derechos reservados.  
Código del tema: MIT.
