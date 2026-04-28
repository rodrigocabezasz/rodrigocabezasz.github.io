Title: Mi CV
Slug: cv
Sortorder: 2
Status: published

<style>
.header-profesional {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 40px 20px;
    margin-bottom: 40px;
    color: white;
    text-align: center;
    position: relative;
    border-radius: 12px;
}
.header-container { max-width: 800px; margin: 0 auto; position: relative; z-index: 2; }
.profile-image {
    width: 150px; height: 150px; border-radius: 50%;
    border: 4px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    object-fit: cover; margin-bottom: 20px;
}
.cv-name { font-size: 2.2em; font-weight: 300; margin: 16px 0 8px; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }
.cv-subtitle { font-size: 1.2em; font-weight: 500; margin-bottom: 20px; opacity: .95; }
.cv-contact { display: flex; justify-content: center; flex-wrap: wrap; gap: 24px; margin: 20px 0; font-size: .95em; }
.cv-contact-item { display: flex; align-items: center; gap: 6px; }
.cv-social { display: flex; justify-content: center; gap: 16px; margin-top: 24px; flex-wrap: wrap; }
.cv-social-link {
    background: rgba(255,255,255,0.2); color: white; padding: 10px 22px;
    text-decoration: none; border-radius: 25px; font-weight: 500;
    border: 1px solid rgba(255,255,255,0.3); transition: background .2s;
}
.cv-social-link:hover { background: rgba(255,255,255,0.35); color: white; }
@media(max-width:600px){
    .cv-name{font-size:1.7em;}
    .cv-contact{flex-direction:column;gap:10px;}
    .cv-social{flex-direction:column;align-items:center;}
}
</style>

<div class="header-profesional">
  <div class="header-container">
    <img src="/images/perfil.jpg" alt="Rodrigo Cabezas Zúñiga" class="profile-image">
    <h1 class="cv-name">Rodrigo Cabezas Zúñiga</h1>
    <div class="cv-subtitle">Ingeniero en Control de Gestión &amp; Data Scientist</div>
    <div class="cv-contact">
      <div class="cv-contact-item"><span>📍</span><span>Santiago, Chile</span></div>
      <div class="cv-contact-item"><span>📱</span><span>+569 9020 2757</span></div>
      <div class="cv-contact-item"><span>✉️</span><span>rorocabezas@gmail.com</span></div>
    </div>
    <div class="cv-social">
      <a href="mailto:rorocabezas@gmail.com" class="cv-social-link">📧 Email</a>
      <a href="https://www.linkedin.com/in/rodrigo-cabezas-zu%C3%B1iga-698a8532/" class="cv-social-link" target="_blank">💼 LinkedIn</a>
      <a href="https://github.com/rodrigocabezasz" class="cv-social-link" target="_blank">💻 GitHub</a>
    </div>
  </div>
</div>

## 🧑‍💼 Resumen Profesional

Ingeniero en Control de Gestión con más de 15 años de experiencia liderando la planificación estratégica y la optimización de procesos. Mi enfoque se centra en potenciar la toma de decisiones a través del análisis avanzado de datos, utilizando herramientas como **Power BI, SQL y Python**. Actualmente complemento mi rol gerencial aplicando activamente habilidades de **Ciencia de Datos y desarrollo de software (FastAPI, Streamlit)** en proyectos de alto impacto.

## 💼 Experiencia Profesional

### Gerente de Planificación y Control de Gestión
*JIS Parking* | Marzo 2015 – Actualidad

- **Planificación y Control Presupuestario:** Lideré el ciclo completo de planificación presupuestaria anual y el seguimiento mensual de desviaciones, presentando informes al directorio.
- **Desarrollo de BI:** Diseñé e implemento un sistema de reporting integral con **Power BI** y **Excel (Power Pivot)** conectado a MySQL, monitoreando KPIs de ventas, costos y eficiencia en tiempo real.
- **Plataforma Intranet (FastAPI):** Arquitecté una plataforma interna que digitaliza control de ventas, inventarios, rendiciones y facturación electrónica — reduciendo tiempos de procesamiento en ~30%.

### Data Scientist (Experiencia Práctica Concurrente)
*Liliapp (Startup Chile)* | Abril 2024 – Actualidad

- Desarrollé una **plataforma ETL modular** (Jumpseller → Firestore) y dashboards KPI con FastAPI + Streamlit.
- Implementé endpoints **CRUD** para gestión de datos maestros de clientes y catálogos de servicios.
- Creé un **sistema de autenticación con Firebase Auth** y herramientas de auditoría de consistencia de datos.

### Jefe de Planificación y Control de Gestión
*Grupo AIB Fahneu* | Febrero 2014 – Febrero 2015

- Gestioné planificación de ciclos productivos y explosión de materiales (MRP) para fábricas de metal y plástico.
- Desarrollé un sistema de control de gestión con análisis de desviaciones presupuestarias y de producción.

### Analista Senior de Control de Gestión
*SMU Chile* | 2011 – Enero 2014

- Diseñé y mantuve **cubos multidimensionales (MOLAP)** para análisis de indicadores comerciales y proyecciones.
- Conduje análisis de rentabilidad por proveedor como base para negociaciones estratégicas.
- Lideré el proceso presupuestario para cuentas de ingreso comercial (2012 y 2013).

### Analista de Información — Planificación y Control de Gestión
*SMU Chile* | 2009 – Junio 2011

- Preparé y automaticé reportes para Gerencia General con indicadores de rendimiento del holding.
- Participé en la creación de cubos OLAP y en el diseño del proceso presupuestario corporativo (2010–2011).

### Experiencia Previa — D&S / Líder (2002–2008)
Coordinador de Soporte Informático, Jefe de Sistemas y Operador: gestión de ERP (SAP, AS400), soporte de infraestructura nacional y liderazgo de equipos técnicos en retail.

---

## 🚀 Proyectos Destacados

### 1. Carrusel de Inspiración Diaria (Full-Stack)
Aplicación web con FastAPI (backend) + Streamlit (frontend) que muestra frases motivacionales con imágenes de Unsplash desde MySQL.
**[Demo en Vivo](https://inspiracion-diaria.streamlit.app/)** · **[GitHub](https://github.com/rodrigocabezasz/inspiracion-diaria-fastapi-streamlit)**

### 2. Agregador de Noticias RSS (Microservicio)
API con FastAPI que extrae noticias de múltiples fuentes RSS, consumida por una app Streamlit para visualización.
**[GitHub](https://github.com/rodrigocabezasz/agregador-noticias-fastapi-streamlit)**

### 3. Scraper Multi-Fuente de Imágenes (ETL)
Script ETL que obtiene datos e imágenes de 4 APIs, procesa y almacena en MySQL con manejo robusto de errores.
**[GitHub](https://github.com/rodrigocabezasz/scraper-multifuente-imagenes)**

---

## 🎓 Formación y Certificaciones

- **Bootcamp Ciencia de Datos e IA** (280 hrs) — *Universidad del Desarrollo* (2025)
- **Diplomado Modelamiento y Análisis de Datos** (180 hrs) — *Universidad de Santiago de Chile* (2024)
- **Diplomado Diseño y Desarrollo Web** (178 hrs) — *Duoc UC* (2018)
- **Ingeniero en Control de Gestión** (Titulado con Distinción) — *UCINF* (2014)
- **Programador y Analista de Sistemas** — *IP AIEP* (2007)

**Certificaciones clave:** Power BI (UC), Python Niveles I–III (UTN.BA), Intro Machine Learning (SENCE/Telefónica), MS SQL Server Analysis & Reporting Services (New Horizons).

---

## 🛠️ Stack Tecnológico

**Lenguajes y Frameworks:** Python (FastAPI, Streamlit, Flask), JavaScript (Node.js, React, Next.js), SQL, HTML5/CSS3

**Data Science:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Jupyter, Google Colab

**Business Intelligence:** Power BI, Excel Avanzado (Power Pivot, Power Query), SAP BW/BO

**DevOps y Cloud:** Docker, Git/GitHub, GitHub Actions, Firebase (Auth, Firestore), Google Cloud Platform, REST APIs

**Otros:** ETL, Data Warehouse, Modelamiento Predictivo, Reporting Ejecutivo, MySQL, SQLite, SQL Server

---

## 🎯 Foco actual

- Automatización y análisis de datos para empresas y startups.
- Integración de APIs y microservicios con FastAPI + Streamlit.
- Machine Learning y modelos predictivos en proyectos reales.
- Proyectos open source y conocimiento compartido en GitHub.
