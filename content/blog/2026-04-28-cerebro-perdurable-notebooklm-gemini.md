Title: Cerebro Perdurable: cómo construí un sistema de creación de contenido con NotebookLM y Gemini
Date: 2026-04-28 18:00
Category: Python
Tags: python, automatizacion, gemini, notebooklm, productividad, marca-personal
Slug: cerebro-perdurable-notebooklm-gemini
Summary: Construí un sistema que conecta mis proyectos reales, aprendizajes semanales y Gemini para generar ideas de posts con contexto real. Así funciona y cómo lo puedes replicar.

Uno de los problemas más comunes de mantener un blog técnico no es la falta de conocimiento: es la fricción para convertir ese conocimiento en contenido publicado. Terminas un proyecto, aprendes algo valioso, resuelves un error complicado… y ese aprendizaje se evaporiza antes de llegar al blog.

Este post documenta cómo construí un sistema para resolver exactamente ese problema, usando herramientas que probablemente ya tienes: Google Drive, NotebookLM y la API de Gemini.

## El problema: conocimiento que se evapora

Trabajo con Python, FastAPI, Streamlit y MySQL en proyectos reales. Cada semana hay aprendizajes: un patrón que funciona bien, un error que me costó horas, una decisión de arquitectura que resultó ser correcta. El problema es que ese conocimiento vive disperso en mi cabeza, en comentarios de código, en tarjetas de Trello.

Cuando intento escribir un post, empiezo desde cero: ¿de qué escribo? ¿esto ya lo cubrí? ¿tengo suficiente material?

La solución que necesitaba tenía que cumplir tres criterios:
- **Baja fricción**: no más de 20-30 minutos semanales para mantenerla
- **Contextual**: las sugerencias de contenido tienen que conocer mis proyectos reales, no inventar
- **Acumulativa**: cada semana que pasa, el sistema tiene que ser más inteligente, no más pesado

## La arquitectura: Captura → Organiza → Consulta → Publica

```
brain/ (local + Drive)          NotebookLM
├── 01-Proyectos/    ─────────→  🧠 Rodrigo - Cerebro Profesional
├── 02-Aprendizajes/ ─────────→     (indexa automáticamente)
├── 03-Tecnologias/  ─────────→           ↓
├── 04-Ideas/        ─────────→    gemini_ask.py
├── 05-Metas/        ─────────→    (lee brain/ local + llama Gemini API)
└── 06-Posts-Publicados/               ↓
                                  Ideas de posts con outline
                                           ↓
                                    new_post.py → contenido/blog/
                                           ↓
                                      git push → sitio publicado
```

Hay tres componentes principales:

### 1. El Cerebro: archivos Markdown en carpetas temáticas

Creé una carpeta `brain/` con seis subcarpetas:

- **01-Proyectos**: un archivo por proyecto, con stack, logros, aprendizajes y posts potenciales
- **02-Aprendizajes**: un archivo por semana con capturas rápidas en bullet points
- **03-Tecnologías**: guías personales de cada herramienta (mis patrones reales, no tutoriales genéricos)
- **04-Ideas**: backlog de ideas de posts con estado (pendiente / en progreso / publicado)
- **05-Metas**: objetivos trimestrales
- **06-Posts Publicados**: resumen de lo ya escrito, para no repetir y construir sobre ello

El formato es simple Markdown, sin estructura rígida. El objetivo es capturar, no perfeccionar.

### 2. La Sincronización: Drive → NotebookLM

`brain/` está sincronizada con Google Drive. NotebookLM indexa esa carpeta automáticamente como fuente, lo que significa que cada vez que actualizo un archivo y lo subo a Drive, el Cerebro se actualiza sin intervención manual.

Para automatizar la subida, construí `sync_to_drive.py`:

```python
# scripts/sync_to_drive.py
# Sube todos los archivos de brain/ a Google Drive con un comando

def sync_brain(service, root_folder_id: str) -> None:
    for folder_name in FOLDER_ORDER:
        local_folder = BRAIN_DIR / folder_name
        drive_folder_id = get_or_create_subfolder(service, root_folder_id, folder_name)
        for md_file in sorted(local_folder.glob("*.md")):
            upload_file(service, md_file, drive_folder_id)

# Uso:
# python scripts/sync_to_drive.py
# python scripts/sync_to_drive.py --dry-run
```

Internamente usa la Google Drive API con OAuth2. La primera vez abre el browser para autorizar; después funciona sin intervención.

### 3. El Asistente: gemini_ask.py

Este es el componente central. Un script Python que:

1. Lee todos los archivos de `brain/` y los compila en un contexto
2. Carga el prompt maestro desde `_prompts/gemini-cerebro.md`
3. Llama a la API de Gemini con ese contexto + instrucción de modo
4. Devuelve ideas de posts con título SEO, descripción, tags, outline completo y el comando listo para ejecutar

```python
# scripts/gemini_ask.py (fragmento)

def read_brain() -> str:
    """Lee todos los archivos del cerebro y los compila en un contexto."""
    sections = []
    for folder_name in FOLDER_ORDER:
        folder = BRAIN_DIR / folder_name
        for f in sorted(folder.glob("*.md")):
            content = f.read_text(encoding="utf-8").strip()
            sections.append(f"### {f.name}\n{content}\n")
    return "\n".join(sections)

def call_gemini(prompt: str, api_key: str) -> str:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text
```

Tiene cuatro modos de operación:

```bash
# Modo semanal: sugiere 2-3 ideas basadas en aprendizajes recientes
python scripts/gemini_ask.py --mode weekly

# Modo serie: identifica el siguiente post lógico de una serie activa
python scripts/gemini_ask.py --mode series

# Modo evergreen: idea atemporal de alto impacto SEO
python scripts/gemini_ask.py --mode evergreen

# Modo trimestral: reflexión sobre el trimestre y plan para el siguiente
python scripts/gemini_ask.py --mode quarterly

# Sugerir + crear el post directamente
python scripts/gemini_ask.py --create
```

Un ejemplo de output real (modo weekly):

```
### Idea 1: Framework de Gestión (Parte 6) — Dashboards con Plotly y Streamlit
**Descripción**: Implementa visualizaciones dinámicas de KPIs usando Plotly y Streamlit.
**Tags**: fastapi, streamlit, plotly, dashboards
**Comando**: python scripts/new_post.py "Framework de Gestión (Parte 6)..." --tags fastapi,streamlit,plotly
**Outline**:
- ## Del dato maestro al dashboard: el problema de la visibilidad
- ## Conectando FastAPI y Streamlit con Plotly
- ## KPIs clave para Control de Gestión: ejemplos con código
- ## Escalar hacia datos transaccionales
**Fuente del cerebro**: framework-gestion-empresarial.md, 05-Metas
```

Gemini conoce mis proyectos, sabe qué publiqué, y sugiere posts que **construyen sobre lo existente** en lugar de empezar de cero.

### 4. El Cierre del Ciclo: export_post_to_brain.py

Después de publicar un post, ejecuto:

```bash
python scripts/export_post_to_brain.py content/blog/mi-post.md
python scripts/sync_to_drive.py
```

El primer script extrae el frontmatter del post (título, fecha, tags, resumen) y lo agrega al archivo `brain/06-Posts-Publicados/posts-publicados.md`. Así el sistema "recuerda" lo que ya escribiste y nunca sugiere repetir un tema.

## El flujo semanal (30 minutos el viernes)

```
Viernes 17:00 — Alimentar el cerebro (20 min)
  └── Crear/editar brain/02-Aprendizajes/2026-WXX-aprendizajes.md
  └── Bullet points: ✅ logros, 🐛 errores resueltos, 💡 ideas, 📚 lecturas
  └── python scripts/sync_to_drive.py

Viernes 17:20 — Consultar al asistente (10 min)
  └── python scripts/gemini_ask.py --mode weekly
  └── Elegir 1 idea del output
  └── python scripts/new_post.py "Título" --tags tag1,tag2 --category Python
  └── Escribir el borrador (puede ser la semana siguiente)
```

## Por qué funciona mejor que una Gem de Gemini web

Una Gem de Gemini es un prompt persistente en la interfaz web. Es útil, pero tiene una limitación: no puede leer tus archivos locales. Cada vez que quieres contexto, tienes que copiarlo manualmente.

`gemini_ask.py` es funcionalmente una Gem, pero con acceso automático al contenido de `brain/`. No hay copy-paste: el script construye el contexto, llama a la API y entrega el resultado directamente en la terminal.

La Gem en Gemini web sigue siendo útil para consultas rápidas desde el móvil o el navegador, donde pegas tus aprendizajes de la semana directamente en la conversación. Los dos usos se complementan.

## Setup en 15 minutos

**1. Instalar dependencias:**
```bash
pip install google-genai python-dotenv google-api-python-client google-auth google-auth-oauthlib
```

**2. Crear `.env`:**
```
GEMINI_API_KEY=tu_clave_de_aistudio.google.com
DRIVE_FOLDER_ID=id_de_tu_carpeta_en_drive
```

**3. Poblar el cerebro:**
Los archivos de `brain/` ya vienen pre-poblados con estructura base. El primer viernes, los personalizas con tus proyectos reales.

**4. NotebookLM:**
- Crear notebook en notebooklm.google.com
- Agregar fuente → Google Drive → seleccionar carpeta `brain/`

**5. Probar:**
```bash
python scripts/gemini_ask.py --mode weekly
```

El código completo está en el [repositorio del sitio](https://github.com/rodrigocabezasz/rodrigocabezasz.github.io) en la carpeta `scripts/` y `_prompts/`.

## Qué aprendí construyendo esto

El sistema más útil no es el más sofisticado, es el que tiene menos fricción para usar. 30 minutos a la semana es sostenible. Un sistema que requiere 2 horas de setup cada vez no lo es.

El efecto compuesto es real: cada semana que alimentas el cerebro, las sugerencias de Gemini son más específicas y relevantes. En mes 1 sugiere ideas genéricas basadas en tus proyectos; en mes 3 identifica patrones en tus aprendizajes y conecta temas que tú no habrías conectado.

El próximo paso natural es automatizar la subida semanal a Drive con una GitHub Action programada. Pero eso merece su propio post.
