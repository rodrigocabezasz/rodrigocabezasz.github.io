# Sistema Cerebro Perdurable — Guía de Setup

## Qué tienes al terminar este setup

```
Tú escribes (viernes, 30 min)
        ↓
brain/02-Aprendizajes/  ← archivos locales
        ↓
sync_to_drive.py        ← sube a Drive automáticamente
        ↓
🧠 Cerebro Rodrigo (Drive) ← NotebookLM lo indexa
        ↓
gemini_ask.py           ← consulta Gemini + contexto del cerebro
        ↓
new_post.py             ← crea el post en Pelican
        ↓
git push                ← publica en tu sitio
```

---

## PASO 1 — Instalar dependencias (una sola vez, 2 min)

```bash
pip install google-genai python-dotenv google-api-python-client google-auth google-auth-oauthlib
```

---

## PASO 2 — Obtener API key de Gemini (2 min)

1. Ve a https://aistudio.google.com/app/apikey
2. Haz clic en **"Create API key"** → selecciona cualquier proyecto
3. Copia la clave (empieza con `AIza...`)
4. Crea el archivo `.env` en la raíz del proyecto:

```
GEMINI_API_KEY=AIzaSy_tu_clave_aqui
```

**Prueba inmediata:**
```bash
python scripts/gemini_ask.py
```
Si funciona, verás 2-3 ideas de posts. ¡La Gema ya está activa desde terminal!

---

## PASO 3 — Subir el Cerebro a Google Drive (5 min)

### Opción A: Manual (más rápido para empezar)
1. Abre `c:\MARCA PERSONAL\brain\` en el Explorador de Windows
2. Selecciona todas las carpetas (`01-Proyectos/`, `02-Aprendizajes/`, etc.)
3. Arrástralas a la carpeta **"🧠 Cerebro Rodrigo"** en drive.google.com
4. Espera a que suban (~1-2 min)

### Opción B: Automático con script (recomendado para uso continuo)

**Setup único de credenciales Drive API:**
1. Ve a https://console.cloud.google.com/
2. Crea un proyecto nuevo → nombre: `cerebro-rodrigo`
3. Menú izquierdo → "APIs y servicios" → "Biblioteca"
4. Busca "Google Drive API" → Habilitar
5. "Credenciales" → "+ Crear credenciales" → "ID de cliente de OAuth 2.0"
6. Tipo de aplicación: **Aplicación de escritorio** → nombre: `cerebro-sync` → Crear
7. Descarga el JSON → guárdalo como `credentials/client_secret.json`
8. En la URL de tu carpeta Drive, copia el ID:
   `drive.google.com/drive/folders/**ESTE_ES_EL_ID**`
9. Agrégalo al `.env`: `DRIVE_FOLDER_ID=ESTE_ES_EL_ID`

**Primera ejecución (abre el browser para autorizar):**
```bash
python scripts/sync_to_drive.py
```

**Ejecuciones posteriores (sin browser):**
```bash
python scripts/sync_to_drive.py          # sube todo
python scripts/sync_to_drive.py --dry-run  # preview sin subir
```

---

## PASO 4 — Agregar fuentes a NotebookLM (3 min)

1. Ve a https://notebooklm.google.com/
2. Abre **"🧠 Rodrigo - Cerebro Profesional"**
3. Panel izquierdo → **"+ Agregar fuente"**
4. Elige **"Google Drive"**
5. Navega a `🧠 Cerebro Rodrigo` → selecciona **todas las carpetas** → Insertar
6. NotebookLM empieza a indexar (~3-5 min)

> **Tip**: Después de cualquier `sync_to_drive.py`, NotebookLM actualiza las fuentes automáticamente.

---

## PASO 5 — Crear la Gema en Gemini (3 min)

1. Ve a https://gemini.google.com/gems
2. Clic en **"Nueva Gem"** (o "Create a gem")
3. Nombre: `🧠 Asistente Marca Personal`
4. En el campo **"Instrucciones"**, copia y pega el contenido de:
   `_prompts/gemini-cerebro.md`
5. Guarda la Gem

**Uso de la Gem en Gemini:**
- Abre la Gem
- Escribe: `Modo semanal: aquí están mis aprendizajes de esta semana: [pega tu semana]`
- O: `Modo serie: ¿cuál es la siguiente parte del Framework?`

---

## Flujo semanal (30 min cada viernes)

```bash
# 1. Crea/actualiza tu log de la semana (20 min escribiendo)
# Edita: brain/02-Aprendizajes/2025-WXX-aprendizajes.md

# 2. Sube al cerebro
python scripts/sync_to_drive.py

# 3. Consulta al asistente (10 min)
python scripts/gemini_ask.py --mode weekly

# 4. Crea el post (si hay idea lista)
python scripts/gemini_ask.py --create
# o directamente:
python scripts/new_post.py "Título del post" --tags python,fastapi

# 5. Publica
git add content/blog/tu-post.md
git commit -m "post: título del post"
git push

# 6. Cierra el ciclo: exporta el post al cerebro
python scripts/export_post_to_brain.py content/blog/tu-post.md
python scripts/sync_to_drive.py
```

---

## Comandos de referencia rápida

| Comando | Qué hace |
|---------|----------|
| `python scripts/gemini_ask.py` | Sugiere 2-3 ideas de post (modo semanal) |
| `python scripts/gemini_ask.py --mode series` | Próximo post de la serie activa |
| `python scripts/gemini_ask.py --mode evergreen` | Idea atemporal de alto impacto |
| `python scripts/gemini_ask.py --mode quarterly` | Reflexión trimestral |
| `python scripts/gemini_ask.py --create` | Sugiere Y crea el post |
| `python scripts/gemini_ask.py --brain-only` | Debug: ve qué contexto se envía |
| `python scripts/sync_to_drive.py` | Sube brain/ a Drive |
| `python scripts/sync_to_drive.py --dry-run` | Preview sin subir |
| `python scripts/export_post_to_brain.py <archivo>` | Post publicado → cerebro |
| `python scripts/new_post.py "Título" --tags t1,t2` | Crea esqueleto de post |
