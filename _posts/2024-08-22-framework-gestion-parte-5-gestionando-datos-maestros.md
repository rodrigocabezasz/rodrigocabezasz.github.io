---
layout: post
title: "Framework de Gestión (Parte 5): Gestionando el Corazón del Negocio - Los Datos Maestros"
subtitle: "Expandiendo el framework con módulos CRUD para las entidades clave de la empresa: desde el plan de cuentas hasta los clientes."
date: 2024-08-22 20:00:00 -0400
author: "Rodrigo Cabezas Zúñiga"
background: '/assets/img/posts/framework-data.jpg' # Sugerencia de nombre de imagen
categories: framework-de-gestion
---

Con un sistema de autenticación funcional, nuestro framework ya es seguro. Pero para ser verdaderamente útil, necesita gestionar la información fundamental que impulsa a cualquier negocio: los **Datos Maestros**. En esta fase del proyecto, he construido los cimientos para que la aplicación pueda manejar las entidades críticas de una empresa.

El objetivo era crear un sistema modular y escalable. En lugar de una solución monolítica, desarrollé un módulo independiente para cada tipo de dato maestro. Cada módulo es un microcosmos de nuestra arquitectura, con su propio modelo de base de datos, esquema de API y endpoints en el backend, así como su propia página de gestión en el frontend.

### La Anatomía de un Módulo de Datos Maestros

Para cada entidad de negocio, el proceso de implementación siguió un patrón consistente:

1.  **Modelo de Datos (`models/`):** Se define la estructura de la tabla en MySQL usando SQLAlchemy. Por ejemplo, para las sucursales:

    ```python
    # backend/app/models/sucursal.py
    class Sucursal(Base):
        __tablename__ = "sucursales"
        id = Column(Integer, primary_key=True, index=True)
        codigo = Column(String(20), unique=True, nullable=False)
        nombre = Column(String(100), nullable=False)
        activo = Column(Boolean, default=True)
        # ... otros campos
    ```

2.  **Esquemas de API (`schemas/`):** Se crean los modelos Pydantic para la validación de datos en las peticiones (`SucursalCreate`, `SucursalUpdate`) y respuestas (`SucursalRead`).

3.  **Endpoints CRUD (`api/`):** Se desarrolla un router en FastAPI con los endpoints `POST`, `GET`, `PUT` y `DELETE` para esa entidad, asegurando una gestión completa.

    ```python
    # backend/app/api/plan_cuentas.py (Ejemplo de endpoint POST)
    @router.post("/plan_cuentas", response_model=CuentaContableRead)
    def crear_cuenta(cuenta: CuentaContableCreate, db: Session = Depends(get_db)):
        db_cuenta = db.query(CuentaContable).filter(CuentaContable.codigo == cuenta.codigo).first()
        if db_cuenta:
            raise HTTPException(status_code=400, detail="El código de cuenta ya existe")
        
        nueva_cuenta = CuentaContable(**cuenta.dict())
        db.add(nueva_cuenta)
        db.commit()
        db.refresh(nueva_cuenta)
        return nueva_cuenta
    ```

4.  **Interfaz de Usuario (`pages/`):** Se construye una página en Streamlit con un formulario para crear/editar registros y una tabla para listar los datos existentes, consumiendo los endpoints de la API.

    ```python
    # frontend/app/pages/gestion_clientes.py (Ejemplo de formulario Streamlit)
    with st.form("form_cliente"):
        nombre = st.text_input("Nombre")
        rut = st.text_input("RUT/ID")
        tipo = st.selectbox("Tipo", ["Cliente", "Proveedor"])
        # ... otros campos
        submit = st.form_submit_button("Guardar")

    if submit:
        # Lógica para enviar los datos al endpoint POST de /clientes
        ...
    ```

### Módulos Implementados

Siguiendo este patrón, he implementado la gestión completa para las siguientes entidades, que son la base de cualquier sistema de control de gestión:

-   **Sucursales y Centros de Costo**
-   **Plan de Cuentas Contables**
-   **Productos y Servicios**
-   **Clientes y Proveedores**
-   **Unidades de Negocio y Áreas**
-   **Períodos Contables**

### Próximos Pasos: ¡A Visualizar!

Con los datos maestros ya gestionables a través de la interfaz, el framework ha alcanzado una madurez funcional. Hemos sentado las bases para la carga de datos transaccionales y, lo más importante, para la creación de los dashboards.

En el próximo post, nos sumergiremos en la **Fase 5: Dashboards y Visualización**. Empezaremos a consumir todos estos datos para construir las visualizaciones que darán sentido al negocio y mostrarán el verdadero poder de nuestra plantilla.

Puedes seguir el progreso y ver el código completo en el repositorio del proyecto. *(Aquí pondremos el enlace a GitHub cuando esté listo)*.