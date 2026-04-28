# Checklist de Lanzamiento

## 1. Repositorio GitHub

- [ ] Crear repositorio `rodrigocabezasz.github.io` en GitHub (público)
- [ ] Inicializar git local:
  ```bash
  git init
  git branch -M main
  git remote add origin https://github.com/rodrigocabezasz/rodrigocabezasz.github.io.git
  ```
- [ ] Crear `.gitignore`:
  ```
  output/
  __pycache__/
  *.pyc
  .pelican/
  ```
- [ ] Primer commit y push:
  ```bash
  git add .
  git commit -m "feat: sitio inicial con Pelican + Pico.css"
  git push -u origin main
  ```

## 2. GitHub Pages

- [ ] Ir a **Settings → Pages** en el repositorio
- [ ] En **Source**, seleccionar **GitHub Actions**
- [ ] Verificar que el workflow `deploy.yml` aparece en la pestaña **Actions** tras el push
- [ ] Confirmar que el deploy finaliza sin errores (✅ verde)
- [ ] Acceder a `https://rodrigocabezasz.github.io` y comprobar que carga correctamente

## 3. Plausible Analytics (opcional)

- [ ] Crear cuenta en [plausible.io](https://plausible.io)
- [ ] Añadir el dominio `rodrigocabezasz.github.io`
- [ ] Verificar que `publishconf.py` tiene `PLAUSIBLE_DOMAIN = 'rodrigocabezasz.github.io'`
- [ ] Confirmar en Plausible que recibe visitas tras el primer deploy

## 4. Contenido mínimo antes de publicar

- [ ] Completar `content/pages/about.md` con bio real
- [ ] Completar `content/pages/projects.md` con al menos un proyecto
- [ ] Revisar `content/pages/contact.md` (email correcto)
- [ ] Revisar el primer post de blog (`content/blog/primer-post.md`)
- [ ] Añadir favicon (`content/extra/favicon.ico`)

## 5. SEO básico

- [ ] Verificar que cada página tiene `<meta name="description">` no vacía
- [ ] Abrir DevTools → pestaña Elements y confirmar tags Open Graph en `<head>`
- [ ] Registrar el sitio en [Google Search Console](https://search.google.com/search-console)
- [ ] Enviar `https://rodrigocabezasz.github.io/sitemap.xml` a Search Console

## 6. Calidad

- [ ] Pasar el HTML de index por [validator.w3.org](https://validator.w3.org)
- [ ] Probar en móvil (DevTools → Toggle device toolbar)
- [ ] Verificar links del menú (Sobre mí, Proyectos, Contacto)
- [ ] Comprobar que el feed Atom carga: `/feeds/all.atom.xml`

## 7. Flujo de trabajo post-lanzamiento

```bash
# Nuevo post
python scripts/new_post.py "Mi nuevo post" --category Python --tags python,tutorial

# Build y preview local
"C:/Users/Rcabezas/AppData/Roaming/Python/Python314/Scripts/pelican.exe" content -s pelicanconf.py
# Abrir output/index.html en el navegador

# Publicar
git add content/blog/mi-nuevo-post.md
git commit -m "post: Mi nuevo post"
git push
# GitHub Actions despliega automáticamente
```
