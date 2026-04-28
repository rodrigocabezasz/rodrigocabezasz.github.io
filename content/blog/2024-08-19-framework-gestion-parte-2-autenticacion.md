Title: Framework de Gestión (Parte 2) — Backend de Autenticación con FastAPI y JWT
Date: 2024-08-19 20:00
Category: Python
Tags: fastapi, autenticacion, jwt, pydantic, sqlalchemy
Slug: framework-gestion-parte-2-autenticacion-con-fastapi-y-jwt
Summary: Implementando la lógica de usuarios y seguridad con SQLAlchemy, Pydantic y JWT en FastAPI.

![Autenticación]({static}/images/framework-auth.jpg)

En la primera parte de esta serie, sentamos las bases de nuestro framework. Ahora, es momento de darle vida al backend, construyendo el componente más crítico de cualquier aplicación empresarial: el sistema de autenticación.

El objetivo es claro: crear un servicio seguro que permita a los usuarios registrarse, iniciar sesión y recibir una "credencial" digital (un token JWT) para acceder a las partes protegidas de la aplicación.

## Los Pilares del Backend

La implementación se basa en una separación clara de responsabilidades:

### 1. `models/user.py` — El Reflejo de la Base de Datos

Todo empieza con el modelo que representa a un usuario en nuestra base de datos. Usando el ORM de SQLAlchemy, definimos la clase `User` que se mapea a la tabla `usuarios`. Lo más importante: el campo `hashed_password` asegura que nunca almacenaremos contraseñas en texto plano.

```python
# models/user.py
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

### 2. `schemas/user.py` — El Contrato de la API con Pydantic

Para asegurar que los datos que viajan a través de nuestra API tengan la forma correcta, utilicé **Pydantic**. Estos "esquemas" validan automáticamente los datos de entrada y salida.

```python
# schemas/user.py
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
```

### 3. `core/security.py` — El Cerebro de la Seguridad

Contiene la lógica para hashear y verificar contraseñas con `passlib`, y para crear y decodificar JSON Web Tokens (JWT) con `python-jose`.

### 4. `api/user.py` — La Puerta de Entrada

El endpoint de login que utiliza toda la lógica anterior para autenticar al usuario y devolver un token.

```python
# api/user.py
@router.post("/token", response_model=schemas.Token)
def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
```

## Próximos Pasos

Con el sistema de autenticación listo, el siguiente paso es construir los endpoints **CRUD** para gestionar datos y conectar el frontend de Streamlit a esta API.
