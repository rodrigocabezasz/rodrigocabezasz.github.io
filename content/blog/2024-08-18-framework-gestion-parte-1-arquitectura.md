Title: Framework de Gestión (Parte 1), Arquitectura y Fundamentos
Date: 2024-08-18 20:00
Category: framework-de-gestion
Tags: fastapi, streamlit, docker, arquitectura
Slug: framework-gestion-parte-1-arquitectura
Author: Rodrigo Cabezas Zúñiga

![Arquitectura](../images/framework-arquitectura.jpg)

Diseñando un esqueleto escalable con FastAPI, Streamlit y Docker para un sistema de dashboards reutilizable.

Toda empresa, sin importar su tamaño, necesita visibilidad sobre sus operaciones. Los dashboards de control de gestión son cruciales, pero construir uno desde cero para cada necesidad específica es un proceso lento y repetitivo. ¿Y si pudiéramos crear una base sólida y reutilizable que acelere drásticamente este proceso?

Ese es el objetivo de este nuevo proyecto: desarrollar un **framework modular para dashboards de Control de Gestión**. En esta serie de posts, documentaré mi viaje construyendo esta solución, desde la arquitectura inicial hasta el despliegue.

### El Plan: Una Arquitectura de Microservicios

Antes de escribir una sola línea de código, el primer paso fue definir la arquitectura. Para garantizar la escalabilidad y un mantenimiento sencillo, opté por una estructura de **monorepo** con servicios desacoplados:

- **Backend (FastAPI):** Gestionará toda la lógica de negocio, la conexión a la base de datos y la seguridad.
- **Frontend (Streamlit):** Se encargará exclusivamente de la interfaz de usuario y la visualización de datos.
- **Base de Datos (MySQL con Docker):** Proporcionará un entorno de base de datos consistente y aislado.

La estructura de carpetas inicial quedó definida de la siguiente manera, separando claramente cada responsabilidad:

```
framework_gestion/
├── backend/
│   ├── app/
│   │   ├── models/   # Modelos de BD (SQLAlchemy)
│   │   ├── schemas/  # Modelos API (Pydantic)
│   │   └── api/      # Endpoints
│
├── frontend/
│   ├── app/
│   │   ├── pages/
│   │   └── components/
│
└── db/
    ├── init.sql
    └── docker-compose.yml
```

### El Corazón de los Datos: `init.sql` y Docker

El fundamento de cualquier sistema de gestión son sus datos. Por ello, el primer paso concreto fue diseñar el esquema SQL inicial en el archivo `db/init.sql`. Este script crea las tablas esenciales que darán soporte a todo el framework: `usuarios`, `roles`, y tablas maestras de ejemplo como `cuentas_contables`.

Para levantar la base de datos de forma local y reproducible, utilicé **Docker Compose**. Esto me permite iniciar un servicio de MySQL con un solo comando, asegurando que mi entorno de desarrollo sea idéntico al que podría usarse en producción.

Con esta base sólida —una arquitectura clara y un esquema de base de datos definido—, el esqueleto del framework estaba listo.

En el próximo post, nos sumergiremos en el código del **backend**, construyendo el sistema de autenticación y los endpoints iniciales con FastAPI. ¡No te lo pierdas!
