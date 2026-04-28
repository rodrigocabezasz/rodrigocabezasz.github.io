import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pelicanconf import *

# ── Producción ──
SITEURL = 'https://rodrigocabezasz.github.io'
RELATIVE_URLS = False

# ── Feeds activados en producción ──
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# ── Limpia el output antes de cada build ──
DELETE_OUTPUT_DIRECTORY = True

# ── Analytics ──
PLAUSIBLE_DOMAIN = 'rodrigocabezasz.github.io'
