AUTHOR = 'Rodrigo Cabezas Zúñiga'
SITENAME = 'Rodrigo Cabezas Z.'
SITEURL = 'https://rodrigocabezasz.github.io'
SITESUBTITLE = 'Ingeniero en Control de Gestión &amp; Data Scientist'

PATH = 'content'
TIMEZONE = 'America/Santiago'
DEFAULT_LANG = 'es'

THEME = 'themes/pico'

# ── URLs ──
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'

# ── Navegación ──
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = []  # Añadir tuplas (label, url) para links manuales si se necesita

# ── Feeds (desactivados en desarrollo) ──
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ── Archivos estáticos ──
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt':  {'path': 'robots.txt'},
}

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True

# ── Analytics (vacío en desarrollo, activo en producción vía publishconf.py) ──
PLAUSIBLE_DOMAIN = ''
