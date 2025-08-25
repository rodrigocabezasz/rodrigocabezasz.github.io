
# Datos personales y configuración principal
AUTHOR = 'Rodrigo Cabezas Zúñiga'
SITENAME = 'Portafolio de Rodrigo Cabezas Zúñiga'
SITESUBTITLE = 'Ingeniero en Control de Gestión & Data Scientist'
SITEURL = ""
THEME = "themes/flex"
TIMEZONE = 'America/Santiago'
DEFAULT_LANG = 'es'
EMAIL = 'rorocabezas@gmail.com'

# Descripción y navegación
SUMMARY_MAX_LENGTH = 60
MENUITEMS = (
    ('🏠 Inicio', '/'),
    ('💼 Mi CV', '/pages/cv.html'),
    ('📝 Blog', '/category/blog.html'),
    ('📁 Proyectos', '/category/proyectos.html'),
    ('✉️ Contacto', '/pages/contacto.html'),
    ('🐙 GitHub', 'https://github.com/rodrigocabezasz'),
    ('🔗 LinkedIn', 'https://www.linkedin.com/in/rodrigo-cabezas-zu%C3%B1iga-698a8532/'),
)



# Imagen de perfil real en el sidebar
AVATAR = 'images/perfil.jpg'
FAVICON = 'images/perfil.jpg'
CUSTOM_CSS = 'static/custom.css'

# Nombre y título profesional
AUTHOR = 'Rodrigo Cabezas Zúñiga'
SITESUBTITLE = 'Ingeniero en Control de Gestión & Data Scientist'

# Enlaces profesionales con íconos
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/rodrigo-cabezas-zu%C3%B1iga-698a8532/'),
    ('github', 'https://github.com/rodrigocabezasz'),
    ('envelope', 'mailto:rorocabezas@gmail.com'),
)

# Configuración de contenido
PATH = "content"
STATIC_PATHS = ['images', 'static']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Paginación y feeds
DEFAULT_PAGINATION = 5
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Otros ajustes
DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = True
DEFAULT_DATE_FORMAT = '%d %b %Y'
DATE_FORMATS = {
    'es': '%d %b %Y',
    'en': '%b %d, %Y',
}

## ...existing code...

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
