---
layout: post
title: "Framework de Gestión (Parte 2): Construyendo el Backend de Autenticación"
subtitle: "Implementando la lógica de usuarios y seguridad con SQLAlchemy, Pydantic y JWT en FastAPI."
date: 2024-08-19 20:00:00 -0400
author: "Rodrigo Cabezas Zúñiga"
background: '/assets/img/posts/framework-auth.jpg'
categories: framework-de-gestion
---

En la [primera parte de esta serie](/framework-de-gestion/2024/08/18/framework-gestion-parte-1-arquitectura.html), sentamos las bases de nuestro framework. Ahora, es momento de darle vida al backend, construyendo el componente más crítico de cualquier aplicación empresarial: el sistema de autenticación.

El objetivo es claro: crear un servicio seguro que permita a los usuarios registrarse, iniciar sesión y recibir una "credencial" digital (un token JWT) para acceder a las partes protegidas de la aplicación. Para lograrlo, he generado la estructura base de nuestro backend FastAPI, distribuyendo la lógica en varios archivos especializados.

### Los Pilares del Backend

La implementación se basa en una separación clara de responsabilidades, materializada en los siguientes archivos y conceptos:

#### 1. `models/user.py` - El Reflejo de la Base de Datos con SQLAlchemy

Todo empieza con el modelo que representa a un usuario en nuestra base de datos. Usando el ORM de SQLAlchemy, definimos la clase `User` que se mapea a la tabla `usuarios`. Lo más importante aquí es el campo `hashed_password`, que asegura que nunca almacenaremos contraseñas en texto plano.

```python
# models/user.py (fragmento)
from sqlalchemy import Column, Integer, String, Boolean
from ..core.database import Base

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
```

#### 2. `schemas/user.py` - El Contrato de la API con Pydantic

Para asegurar que los datos que viajan a través de nuestra API tengan la forma correcta, utilicé **Pydantic**. Estos "esquemas" validan automáticamente los datos de entrada y salida.

```python
# schemas/user.py (fragmento)
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
```

#### 3. `core/security.py` - El Cerebro de la Seguridad

Este es el corazón de nuestro sistema. Contiene la lógica para hashear y verificar contraseñas con `passlib`, y para crear y decodificar JSON Web Tokens (JWT) con `python-jose`, que serán las credenciales digitales de nuestros usuarios.

#### 4. `api/user.py` - La Puerta de Entrada

Finalmente, este archivo expone la funcionalidad a través de endpoints REST. El más importante es el de login, que utiliza toda la lógica anterior para autenticar al usuario y devolver un token.

```python
# api/user.py (fragmento del endpoint de login)
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    # 1. Autentica al usuario usando la lógica de security.py
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # 2. Crea un token JWT si las credenciales son válidas
    access_token = create_access_token(data={"sub": user.username})
    
    # 3. Devuelve el token al cliente
    return {"access_token": access_token, "token_type": "bearer"}
```

### Próximos Pasos

Con el código base del backend para la autenticación ya generado, el siguiente paso es conectar nuestro **frontend de Streamlit** a esta API. En el próximo artículo, construiremos la interfaz de login y daremos los primeros pasos para proteger las páginas de nuestra aplicación.

Puedes seguir el progreso y ver el código completo en el repositorio del proyecto. *(Aquí pondremos el enlace a GitHub cuando esté listo)*.