Title: Framework de Gestión (Parte 3), Refinando los Endpoints CRUD
Date: 2024-08-20 20:00
Category: framework-de-gestion
Tags: fastapi, sqlalchemy, pydantic, crud
Slug: framework-gestion-parte-3-gestion-de-datos-con-endpoints-crud
Author: Rodrigo Cabezas Zúñiga

![CRUD](../images/framework-crud.jpg)

De la teoría a la práctica: ajustando los modelos de SQLAlchemy para una gestión de datos robusta en FastAPI.

En los posts anteriores, sentamos las bases de nuestro framework y construimos un sistema de autenticación. Ahora, es el momento de darle a nuestra aplicación la capacidad de gestionar datos. La forma estándar de hacer esto en una API REST es a través de endpoints **CRUD**: **C**reate (Crear), **R**ead (Leer), **U**pdate (Actualizar) y **D**elete (Borrar).

Comencé implementando estos endpoints para la gestión de usuarios. Sin embargo, durante el desarrollo, me encontré con un punto crucial: la definición inicial de mis modelos de SQLAlchemy no era lo suficientemente explícita, lo que causaba problemas al intentar actualizar los datos. Esto me llevó a una refactorización importante para hacer el código más claro y robusto.

### El Desafío: Modelos Implícitos vs. Explícitos

Mi primera versión de los modelos `User` y `Role` en `models/user.py` confiaba en el comportamiento implícito de SQLAlchemy. Si bien funcionaba para operaciones simples, se volvía ambiguo al interactuar con los esquemas de Pydantic en operaciones de actualización complejas.

La solución fue redefinir los modelos con un **constructor explícito (`__init__`)**. Esto me da un control total sobre cómo se crea cada objeto y asegura que cada atributo se asigne correctamente.

```python
# models/user.py (Modelo User corregido)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, nullable=True)

    def __init__(self, username, email, hashed_password, is_active=True, role_id=None):
        """
        Inicializa un nuevo usuario de forma explícita.
        """
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.role_id = role_id
```

### El Ciclo CRUD: Endpoints Refinados

Con los modelos corregidos, pude finalizar la implementación de los endpoints en `api/user.py`.

#### 1. Crear (Create) y Leer (Read)

El endpoint de registro (`POST /register`) y el de lectura (`GET /users`) se beneficiaron de la claridad de los nuevos modelos. El código ahora es más fácil de seguir y menos propenso a errores.

```python
# api/user.py (Endpoint de Registro)
@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # ... (lógica de verificación)
    hashed_password = get_password_hash(user.password)
    # Usamos el constructor explícito para crear el nuevo usuario
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role_id=user.role_id
    )
    db.add(new_user)
    db.commit()
    # ...
    return new_user
```

#### 2. Actualizar (Update): La Prueba de Fuego

El endpoint de actualización (`PUT /users/{user_id}`) fue el que más se benefició de la refactorización. Ahora, la asignación de nuevos valores al objeto `db_user` (que es una instancia de nuestro modelo `User`) es directa y sin ambigüedades.

```python
# api/user.py (Endpoint de Actualización)
@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Asignación directa y segura de los nuevos valores
    update_data = user_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        if key == "password":
            setattr(db_user, "hashed_password", get_password_hash(value))
        else:
            setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user
```

### Lecciones Aprendidas y Próximos Pasos

Esta refactorización fue una lección valiosa sobre la importancia de ser explícito en el código, especialmente cuando se integran librerías tan potentes como SQLAlchemy y Pydantic.

Con los endpoints CRUD para usuarios completamente funcionales y probados, el backend está listo para la siguiente gran fase. En el próximo artículo, finalmente nos sumergiremos en el **frontend con Streamlit**, construyendo la interfaz de usuario que consumirá esta API para gestionar usuarios.

Puedes seguir el progreso y ver el código completo en el repositorio del proyecto. *(Aquí pondremos el enlace a GitHub cuando esté listo)*.
