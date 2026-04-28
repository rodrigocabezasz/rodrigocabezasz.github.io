Title: Framework de Gestión (Parte 5) — Gestionando los Datos Maestros del Negocio
Date: 2024-08-22 20:00
Category: Python
Tags: fastapi, datos-maestros, crud, arquitectura
Slug: framework-gestion-parte-5-gestionando-datos-maestros
Summary: Expandiendo el framework con módulos CRUD para las entidades clave de la empresa — desde el plan de cuentas hasta los clientes.

![Datos Maestros]({static}/images/framework-data.jpg)

Con un sistema de autenticación funcional, nuestro framework ya es seguro. Pero para ser verdaderamente útil, necesita gestionar la información fundamental que impulsa a cualquier negocio: los **Datos Maestros**.

El objetivo fue crear un sistema modular y escalable. En lugar de una solución monolítica, desarrollé un módulo independiente para cada tipo de dato maestro. Cada módulo es un microcosmos de nuestra arquitectura completa.

## La Anatomía de un Módulo de Datos Maestros

Para cada entidad de negocio, el proceso siguió un patrón consistente de 4 capas:

### 1. Modelo de Datos (`models/`)

```python
# models/sucursal.py
class Sucursal(Base):
    __tablename__ = "sucursales"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
```

### 2. Esquemas de API (`schemas/`)

Modelos Pydantic para validación: `SucursalCreate`, `SucursalUpdate`, `SucursalRead`.

### 3. Endpoints CRUD (`api/`)

```python
# api/plan_cuentas.py
@router.post("/plan_cuentas", response_model=CuentaContableRead)
def crear_cuenta(cuenta: CuentaContableCreate, db: Session = Depends(get_db)):
    db_cuenta = db.query(CuentaContable).filter(
        CuentaContable.codigo == cuenta.codigo
    ).first()
    if db_cuenta:
        raise HTTPException(status_code=400, detail="El código de cuenta ya existe")
    
    nueva_cuenta = CuentaContable(**cuenta.dict())
    db.add(nueva_cuenta)
    db.commit()
    db.refresh(nueva_cuenta)
    return nueva_cuenta
```

### 4. Interfaz de Usuario (`pages/`)

```python
# pages/gestion_clientes.py
with st.form("form_cliente"):
    nombre = st.text_input("Nombre")
    rut = st.text_input("RUT/ID")
    tipo = st.selectbox("Tipo", ["Cliente", "Proveedor"])
    submit = st.form_submit_button("Guardar")
```

## Módulos Implementados

Siguiendo este patrón, implementé la gestión completa para:

- **Sucursales y Centros de Costo**
- **Plan de Cuentas Contables**
- **Productos y Servicios**
- **Clientes y Proveedores**
- **Unidades de Negocio y Áreas**
- **Períodos Contables**

## ¿Qué sigue?

Con los datos maestros gestionables a través de la interfaz, el framework tiene una madurez funcional real. El siguiente paso natural: construir los **dashboards de visualización** que consumirán todos estos datos y mostrarán el verdadero poder de la plataforma.

Esta serie documenta el proceso completo de construcción. Si quieres explorar el código, los primeros posts [Parte 1](../framework-gestion-parte-1-arquitectura/) y [Parte 2](../framework-gestion-parte-2-autenticacion-con-fastapi-y-jwt/) cubren la arquitectura y la autenticación.
