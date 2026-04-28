Title: Framework de Gestión (Parte 4) — Conectando Streamlit y FastAPI
Date: 2024-08-21 20:00
Category: Python
Tags: fastapi, streamlit, frontend, api
Slug: framework-gestion-parte-4-conectando-streamlit-y-fastapi
Summary: Dando vida a la interfaz — cómo crear formularios en Streamlit para consumir una API REST y gestionar datos en tiempo real.

![Frontend Streamlit + FastAPI]({static}/images/framework-frontend.jpg)

En los posts anteriores, construimos un backend robusto con FastAPI. Pero una API, por potente que sea, no es nada sin una interfaz que permita a los usuarios interactuar con ella. En esta cuarta parte, finalmente cruzamos el puente y conectamos nuestro frontend de **Streamlit** con el backend.

## La Lógica del Frontend: Peticiones HTTP con `requests`

Toda la comunicación entre Streamlit (cliente) y FastAPI (servidor) se realiza a través de peticiones HTTP. La librería `requests` es la herramienta perfecta para esto. Cada formulario en Streamlit tiene una lógica que, al ser enviada, empaqueta los datos y los envía al endpoint correspondiente.

## Implementación 1: Configuración de la Empresa

La primera funcionalidad fue la página de "Configuración de Empresa". Al hacer clic en "Guardar", se ejecutan dos acciones:

1. **Enviar los datos de texto** via `POST` al backend como JSON.
2. **Subir el archivo del logo** como `multipart/form-data` en una petición separada.

```python
# pages/configuracion_empresa.py
if st.button("Guardar Configuración"):
    config_data = {
        "nombre": nombre, "descripcion": descripcion,
        "direccion": direccion, "telefono": telefono, "email": email
    }
    response = requests.post("http://localhost:8000/empresa/config", json=config_data)
    if response.status_code == 200:
        st.success("Configuración guardada.")
    
    if logo_uploader is not None:
        files = {"file": logo_uploader.getvalue()}
        logo_response = requests.post("http://localhost:8000/empresa/logo", files=files)
        if logo_response.status_code == 200:
            st.success("Logo subido correctamente.")
```

## Implementación 2: Gestión de Datos Maestros

La página de "Datos Maestros" demuestra dos interacciones clave:

1. **Crear:** Un formulario que envía `POST` al backend.
2. **Leer:** Una petición `GET` que carga los datos existentes en una tabla con `st.table()`.

```python
# pages/datos_maestros.py
st.subheader("Listado de Datos Maestros")
try:
    response = requests.get("http://localhost:8000/datos_maestros")
    response.raise_for_status()
    datos = response.json()
    st.table(datos)
except requests.exceptions.RequestException as e:
    st.error(f"No se pudo obtener el listado: {e}")
```

Con esta integración funcional, el framework ya se siente como una aplicación real. En el próximo post, expandimos los módulos con la gestión completa de **Datos Maestros** de la empresa.
