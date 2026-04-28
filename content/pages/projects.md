Title: Mi Trabajo
Slug: projects
Sortorder: 3
Status: published

<style>
/* ── Filtros ── */
.category-filters {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin: 1.5rem 0 2rem;
}
.filter-btn {
  padding: .35rem 1.1rem;
  border: 1px solid var(--pico-muted-border-color);
  border-radius: 999px;
  background: transparent;
  color: var(--pico-color);
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
  transition: background .15s, border-color .15s, color .15s;
}
.filter-btn:hover,
.filter-btn.active {
  background: #0077cc;
  border-color: #0077cc;
  color: #fff;
}

/* ── Grid de proyectos ── */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  gap: 1.25rem;
}

/* ── Tarjeta de proyecto ── */
.project-card-new {
  border: 1px solid var(--pico-muted-border-color);
  border-radius: .75rem;
  background: var(--pico-card-background-color);
  transition: border-color .15s, transform .15s, box-shadow .15s;
  overflow: hidden;
}
.project-card-new:hover {
  border-color: #0077cc;
  transform: translateY(-3px);
  box-shadow: 0 6px 24px rgba(0, 119, 204, .12);
}
.project-card-new[data-hidden="true"] { display: none; }

.project-card-new__body {
  padding: 1.25rem 1.4rem;
  display: flex;
  flex-direction: column;
  height: 100%;
}

/* Badges */
.project-card-new__badges {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
  margin-bottom: .75rem;
}
.badge {
  background: #e8f4ff;
  color: #0055a5;
  font-size: .7rem;
  font-weight: 700;
  padding: .15rem .65rem;
  border-radius: 999px;
  text-transform: uppercase;
  letter-spacing: .04em;
}
/* Dark mode badges */
@media (prefers-color-scheme: dark) {
  .badge { background: #0d2a4a; color: #60b0ff; }
}

.project-card-new__title {
  font-size: 1rem;
  font-weight: 700;
  margin: 0 0 .4rem;
}

.project-card-new__description {
  font-size: .875rem;
  color: var(--pico-muted-color);
  margin-bottom: .75rem;
  line-height: 1.5;
}

.project-card-new__features {
  font-size: .82rem;
  padding-left: 1.1rem;
  margin: 0 0 1rem;
  flex: 1;
  line-height: 1.6;
}
.project-card-new__features li { margin-bottom: .2rem; }

/* Tech icons */
.project-card-new__tech {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .4rem;
  padding-top: .85rem;
  margin-top: auto;
  border-top: 1px solid var(--pico-muted-border-color);
}
.project-card-new__tech img {
  width: 28px;
  height: 28px;
  border-radius: 4px;
}
.project-card-new__tech .tech-text {
  font-size: .72rem;
  font-weight: 700;
  background: var(--pico-code-background-color);
  color: var(--pico-muted-color);
  padding: .15rem .55rem;
  border-radius: 4px;
}

/* Links dentro de tarjetas */
.project-link {
  font-size: .82rem;
  color: #0077cc;
  text-decoration: none;
  font-weight: 600;
}
.project-link:hover { text-decoration: underline; }
</style>

<!-- Filtros de categoría -->
<div class="category-filters">
  <button class="filter-btn active" data-filter="all">Todos los proyectos</button>
  <button class="filter-btn" data-filter="python">Python</button>
  <button class="filter-btn" data-filter="fastapi">FastAPI</button>
  <button class="filter-btn" data-filter="data-bi">Data &amp; BI</button>
  <button class="filter-btn" data-filter="automatizacion">Automatización</button>
</div>

<!-- Grid de proyectos -->
<div class="projects-grid">

  <!-- Plataforma Intranet JIS Parking -->
  <article class="project-card-new" data-category="python fastapi data-bi" data-priority="5">
    <div class="project-card-new__body">
      <div class="project-card-new__badges">
        <span class="badge">Producción</span>
        <span class="badge">FastAPI</span>
        <span class="badge">BI</span>
      </div>
      <h3 class="project-card-new__title">Plataforma Intranet JIS Parking</h3>
      <p class="project-card-new__description">Sistema interno que digitaliza operaciones críticas: ventas, inventarios, rendiciones y facturación electrónica.</p>
      <ul class="project-card-new__features">
        <li>Control de ventas y cierre de caja en tiempo real</li>
        <li>Gestión de inventarios y rendiciones de gastos</li>
        <li>Integración con Webpay (facturación electrónica)</li>
        <li>Dashboards Power BI conectados a MySQL — KPIs en tiempo real</li>
        <li>~30% reducción en tiempos de procesamiento manual</li>
      </ul>
      <div class="project-card-new__tech">
        <img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python" title="Python">
        <img src="https://skillicons.dev/icons?i=fastapi&theme=light" alt="FastAPI" title="FastAPI">
        <img src="https://skillicons.dev/icons?i=mysql&theme=light" alt="MySQL" title="MySQL">
        <span class="tech-text">Power BI</span>
      </div>
    </div>
  </article>

  <!-- Framework de Gestión -->
  <article class="project-card-new" data-category="python fastapi automatizacion" data-priority="5">
    <div class="project-card-new__body">
      <div class="project-card-new__badges">
        <span class="badge">FastAPI</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Full-Stack</span>
      </div>
      <h3 class="project-card-new__title">Framework de Gestión Empresarial</h3>
      <p class="project-card-new__description">Framework modular y reutilizable para dashboards de Control de Gestión con autenticación JWT y gestión de datos maestros.</p>
      <ul class="project-card-new__features">
        <li>Arquitectura de microservicios: FastAPI + Streamlit + MySQL + Docker</li>
        <li>Autenticación con JWT (SQLAlchemy + Pydantic + OAuth2)</li>
        <li>Endpoints CRUD completos para todas las entidades del negocio</li>
        <li>Plan de cuentas, sucursales, clientes, proveedores, períodos contables</li>
      </ul>
      <div class="project-card-new__tech">
        <img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python" title="Python">
        <img src="https://skillicons.dev/icons?i=fastapi&theme=light" alt="FastAPI" title="FastAPI">
        <img src="https://skillicons.dev/icons?i=mysql&theme=light" alt="MySQL" title="MySQL">
        <img src="https://skillicons.dev/icons?i=docker&theme=light" alt="Docker" title="Docker">
      </div>
    </div>
  </article>

  <!-- Dashboard KPIs Liliapp -->
  <article class="project-card-new" data-category="python fastapi data-bi" data-priority="4">
    <div class="project-card-new__body">
      <div class="project-card-new__badges">
        <span class="badge">ETL</span>
        <span class="badge">Firebase</span>
        <span class="badge">Startup Chile</span>
      </div>
      <h3 class="project-card-new__title">Dashboard KPIs — Liliapp</h3>
      <p class="project-card-new__description">Plataforma ETL y dashboards de KPIs para startup del programa Startup Chile. Backend FastAPI + Streamlit frontend.</p>
      <ul class="project-card-new__features">
        <li>ETL modular Jumpseller → Firestore con validación de consistencia</li>
        <li>Dashboards de KPIs en tiempo real (FastAPI + Streamlit)</li>
        <li>Autenticación y auditoría con Firebase Auth</li>
        <li>Endpoints CRUD para catálogo de servicios y clientes</li>
      </ul>
      <div class="project-card-new__tech">
        <img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python" title="Python">
        <img src="https://skillicons.dev/icons?i=fastapi&theme=light" alt="FastAPI" title="FastAPI">
        <img src="https://skillicons.dev/icons?i=firebase&theme=light" alt="Firebase" title="Firebase">
        <span class="tech-text">Streamlit</span>
      </div>
    </div>
  </article>

  <!-- Carrusel de Inspiración -->
  <article class="project-card-new" data-category="python fastapi automatizacion" data-priority="3">
    <div class="project-card-new__body">
      <div class="project-card-new__badges">
        <span class="badge">Demo Live</span>
        <span class="badge">Full-Stack</span>
      </div>
      <h3 class="project-card-new__title">Carrusel de Inspiración Diaria</h3>
      <p class="project-card-new__description">App web que muestra frases motivacionales con imágenes de fondo dinámicas desde la API de Unsplash.</p>
      <ul class="project-card-new__features">
        <li>Backend FastAPI sirviendo datos desde MySQL</li>
        <li>Frontend Streamlit con auto-refresh y diseño visual</li>
        <li>Integración con API de Unsplash para imágenes de fondo</li>
      </ul>
      <div class="project-card-new__tech">
        <img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python" title="Python">
        <img src="https://skillicons.dev/icons?i=fastapi&theme=light" alt="FastAPI" title="FastAPI">
        <img src="https://skillicons.dev/icons?i=mysql&theme=light" alt="MySQL" title="MySQL">
        <span class="tech-text">Streamlit</span>
      </div>
      <div style="margin-top:.75rem;">
        <a href="https://inspiracion-diaria.streamlit.app/" class="project-link" target="_blank">🌐 Demo en vivo</a>
        &nbsp;·&nbsp;
        <a href="https://github.com/rodrigocabezasz/inspiracion-diaria-fastapi-streamlit" class="project-link" target="_blank">GitHub</a>
      </div>
    </div>
  </article>

  <!-- Scraper Multi-Fuente -->
  <article class="project-card-new" data-category="python automatizacion data-bi" data-priority="2">
    <div class="project-card-new__body">
      <div class="project-card-new__badges">
        <span class="badge">ETL</span>
        <span class="badge">Automatización</span>
      </div>
      <h3 class="project-card-new__title">Scraper Multi-Fuente de Imágenes</h3>
      <p class="project-card-new__description">Script ETL que obtiene datos e imágenes de 4 APIs distintas, los normaliza y almacena en MySQL.</p>
      <ul class="project-card-new__features">
        <li>Integración con 4 APIs (Unsplash, Pexels, Pixabay, NASA APOD)</li>
        <li>Manejo robusto de errores y rate limiting</li>
        <li>Gestión segura de credenciales con variables de entorno</li>
      </ul>
      <div class="project-card-new__tech">
        <img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python" title="Python">
        <img src="https://skillicons.dev/icons?i=mysql&theme=light" alt="MySQL" title="MySQL">
      </div>
      <div style="margin-top:.75rem;">
        <a href="https://github.com/rodrigocabezasz/scraper-multifuente-imagenes" class="project-link" target="_blank">GitHub</a>
      </div>
    </div>
  </article>

  <!-- Cerebro Perdurable -->
  <article class="project-card-new" data-category="python automatizacion" data-priority="4">
    <div class="project-card-new__body">
      <div class="project-card-new__badges">
        <span class="badge">IA Generativa</span>
        <span class="badge">Automatización</span>
      </div>
      <h3 class="project-card-new__title">Sistema Cerebro Perdurable</h3>
      <p class="project-card-new__description">Sistema PKM que conecta Google Drive, NotebookLM y Gemini API para generar ideas de posts con contexto real de proyectos y aprendizajes semanales.</p>
      <ul class="project-card-new__features">
        <li>Cerebro local en Markdown sincronizado con Google Drive</li>
        <li>Script <code>gemini_ask.py</code>: 4 modos (semanal, serie, evergreen, trimestral)</li>
        <li>Cierre del ciclo: post publicado → cerebro → nuevas sugerencias</li>
        <li>30 min/semana de mantenimiento, efecto compuesto creciente</li>
      </ul>
      <div class="project-card-new__tech">
        <img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python" title="Python">
        <span class="tech-text">Gemini API</span>
        <span class="tech-text">NotebookLM</span>
        <span class="tech-text">Drive API</span>
      </div>
      <div style="margin-top:.75rem;">
        <a href="./cerebro-perdurable-notebooklm-gemini.html" class="project-link">Post del blog</a>
      </div>
    </div>
  </article>

  <!-- Agregador RSS -->
  <article class="project-card-new" data-category="python fastapi automatizacion" data-priority="2">
    <div class="project-card-new__body">
      <div class="project-card-new__badges">
        <span class="badge">Microservicio</span>
        <span class="badge">FastAPI</span>
      </div>
      <h3 class="project-card-new__title">Agregador de Noticias RSS</h3>
      <p class="project-card-new__description">Microservicio con FastAPI que extrae y normaliza noticias de múltiples fuentes RSS, consumible por cualquier cliente.</p>
      <ul class="project-card-new__features">
        <li>API REST que agrega múltiples feeds RSS en un solo endpoint</li>
        <li>Normalización de fechas, autores y categorías entre fuentes</li>
        <li>Frontend Streamlit para visualización con filtros</li>
      </ul>
      <div class="project-card-new__tech">
        <img src="https://skillicons.dev/icons?i=py&theme=light" alt="Python" title="Python">
        <img src="https://skillicons.dev/icons?i=fastapi&theme=light" alt="FastAPI" title="FastAPI">
        <span class="tech-text">Streamlit</span>
      </div>
      <div style="margin-top:.75rem;">
        <a href="https://github.com/rodrigocabezasz/agregador-noticias-fastapi-streamlit" class="project-link" target="_blank">GitHub</a>
      </div>
    </div>
  </article>

</div>

<!-- Script de filtrado y ordenamiento -->
<script>
(function() {
  var filterButtons = document.querySelectorAll('.filter-btn');
  var projectCards  = Array.from(document.querySelectorAll('.project-card-new'));
  var grid          = document.querySelector('.projects-grid');

  function getCategories(card) {
    return (card.getAttribute('data-category') || '').split(/\s+/).map(function(c){ return c.trim().toLowerCase(); });
  }
  function getPriority(card) {
    return parseInt(card.getAttribute('data-priority') || '0', 10);
  }

  filterButtons.forEach(function(btn) {
    btn.addEventListener('click', function() {
      var filter = btn.getAttribute('data-filter').toLowerCase();

      filterButtons.forEach(function(b){ b.classList.remove('active'); });
      btn.classList.add('active');

      var visible = projectCards.filter(function(card) {
        var cats = getCategories(card);
        return filter === 'all' || cats.indexOf(filter) !== -1;
      });

      visible.sort(function(a, b){ return getPriority(b) - getPriority(a); });

      projectCards.forEach(function(card){ card.setAttribute('data-hidden', 'true'); });
      visible.forEach(function(card){
        card.setAttribute('data-hidden', 'false');
        grid.appendChild(card);
      });
    });
  });

  document.querySelector('.filter-btn[data-filter="all"]').click();
})();
</script>
