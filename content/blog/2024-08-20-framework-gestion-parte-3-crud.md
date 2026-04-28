Title: Framework de Gestión (Parte 3) — Refinando los Endpoints CRUD
Date: 2024-08-20 20:00
Category: Python
Tags: fastapi, sqlalchemy, pydantic, crud
Slug: framework-gestion-parte-3-gestion-de-datos-con-endpoints-crud
Summary: De la teoría a la práctica — ajustando los modelos de SQLAlchemy para una gestión de datos robusta con endpoints CRUD completos en FastAPI.

![CRUD]({static}/images/framework-crud.jpg)

En los posts anteriores, sentamos las bases y construimos un sistema de autenticación. Ahora es el momento de darle a nuestra aplicación la capacidad de gestionar datos con endpoints **CRUD**: **C**reate, **R**ead, **U**pdate y **D**elete.

## El Desafío: Modelos Implícitos vs. Explícitos

Mi primera versión de los modelos `User` y `Role` confiaba en el comportamiento implícito de SQLAlchemy. Si bien funcionaba para operaciones simples, se volvía ambiguo al interactuar con Pydantic en operaciones de actualización complejas.

La solución fue redefinir los modelos con un **constructor explícito (`__init__`)**:

```python
# models/user.py — Modelo User corregido
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, nullable=True)

    def __init__(self, username, email, hashed_password, is_active=True, role_id=None):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.role_id = role_id
```

## El Ciclo CRUD: Endpoints Refinados

### Crear y Leer

```python
@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role_id=user.role_id
    )
    db.add(new_user)
    db.commit()
    return new_user
```

### Actualizar: La Prueba de Fuego

El endpoint `PUT` fue el que más se benefició de la refactorización. La asignación de nuevos valores al objeto `db_user` es ahora directa y sin ambigüedades:

```python
@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
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

## Lección aprendida

Ser explícito en el código es fundamental cuando se integran librerías tan potentes como SQLAlchemy y Pydantic. La claridad en los modelos previene bugs difíciles de rastrear en operaciones de actualización complejas.

En el próximo artículo, cruzamos el puente hacia el **frontend con Streamlit**.
