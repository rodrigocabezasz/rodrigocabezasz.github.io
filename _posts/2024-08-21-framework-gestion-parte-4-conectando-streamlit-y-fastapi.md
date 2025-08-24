---
layout: post
title: "Framework de Gestión (Parte 4): Conectando Streamlit y FastAPI"
subtitle: "Dando vida a la interfaz: cómo crear formularios en Streamlit para consumir una API REST y gestionar datos en tiempo real."
date: 2024-08-21 20:00:00 -0400
author: "Rodrigo Cabezas Zúñiga"
background: '/assets/img/posts/framework-frontend.jpg' # Sugerencia de nombre de imagen
categories: framework-de-gestion
---

En los [posts anteriores](/framework-de-gestion/), construimos un backend robusto con FastAPI, sentando las bases para la autenticación y la gestión de datos. Pero una API, por potente que sea, no es nada sin una interfaz que permita a los usuarios interactuar con ella. En esta cuarta parte de la serie, finalmente cruzamos el puente y conectamos nuestro frontend de **Streamlit** con el backend.

El objetivo de este hito fue implementar la funcionalidad para que un administrador pueda configurar los datos de su empresa y empezar a gestionar sus "Datos Maestros" directamente desde la aplicación web.

### La Lógica del Frontend: Peticiones HTTP con `requests`

Toda la comunicación entre Streamlit (el cliente) y FastAPI (el servidor) se realiza a través de peticiones HTTP. La librería `requests` de Python es la herramienta perfecta para esto. Cada formulario en Streamlit ahora tiene una lógica que, al ser enviada, empaqueta los datos y los envía al endpoint correspondiente de nuestra API.

### Implementación 1: Configuración de la Empresa

La primera funcionalidad que construí fue la página de "Configuración de Empresa". Esto implicó desarrollar un nuevo conjunto de archivos en el backend (`models/empresa.py`, `schemas/empresa.py`, `api/empresa.py`) para manejar los datos específicos de la empresa.

En el frontend (`pages/configuracion_empresa.py`), creé un formulario simple con Streamlit. Al hacer clic en "Guardar", se ejecutan dos acciones principales:

1.  **Enviar los datos de texto:** Se empaquetan los datos del formulario en un diccionario y se envían mediante una petición `POST` al endpoint del backend.
2.  **Subir el archivo del logo:** Si el usuario sube un logo, se gestiona como una petición `POST` separada de tipo `multipart/form-data`, que es el estándar para la subida de archivos.

```python
# frontend/app/pages/configuracion_empresa.py (Lógica de envío)

if st.button("Guardar Configuración"):
    # 1. Envía los datos del formulario como JSON
    config_data = {
        "nombre": nombre, "descripcion": descripcion, 
        "direccion": direccion, "telefono": telefono, "email": email
    }
    response = requests.post("http://localhost:8000/empresa/config", json=config_data)

    if response.status_code == 200:
        st.success("Configuración de texto guardada.")
    
    # 2. Sube el archivo del logo si se proporcionó uno
    if logo_uploader is not None:
        files = {"file": logo_uploader.getvalue()}
        logo_response = requests.post("http://localhost:8000/empresa/logo", files=files)
        if logo_response.status_code == 200:
            st.success("Logo subido correctamente.")
```

### Implementación 2: Gestión de Datos Maestros

Siguiendo el mismo patrón, creé la página para gestionar "Datos Maestros" (`pages/datos_maestros.py`). Esta página demuestra dos interacciones clave con la API:

1.  **Crear (Create):** Un formulario permite al usuario añadir un nuevo dato maestro. Al enviarlo, una petición `POST` envía la información al backend.
2.  **Leer (Read):** Justo debajo del formulario, la aplicación realiza una petición `GET` para obtener todos los datos maestros existentes y los muestra en una tabla usando `st.table()`. Esto proporciona un feedback inmediato al usuario de que su dato fue agregado correctamente.

```python
# frontend/app/pages/datos_maestros.py (Lógica de lectura)

st.subheader("Listado de Datos Maestros")
try:
    response = requests.get("http://localhost:8000/datos_maestros")
    response.raise_for_status() # Lanza un error si la petición falla
    
    datos = response.json()
    st.table(datos)

except requests.exceptions.RequestException as e:
    st.error(f"No se pudo obtener el listado: {e}")
```

### Próximos Pasos

Con esta integración funcional, el framework ya se siente como una aplicación real. Los usuarios pueden configurar y empezar a poblar el sistema con sus datos.

Los siguientes pasos se centrarán en refinar la experiencia de usuario con mejores validaciones, implementar la gestión de usuarios y roles en el frontend, y finalmente, empezar a construir los dashboards de visualización que consumirán todos estos datos. ¡Cada vez estamos más cerca del objetivo final!