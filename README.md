# sitio_personal

Este repositorio contiene el código fuente y los posts de mi blog personal generado con [Pelican](https://blog.getpelican.com/).

## Estructura
- `content/`: Entradas del blog y páginas.
- `output/`: Archivos generados del sitio.
- `pelicanconf.py`: Configuración principal de Pelican.
- `publishconf.py`: Configuración para publicar.
- `Makefile`: Tareas automatizadas.

## Publicación
Para publicar cambios:
1. Realiza tus modificaciones o agrega nuevos posts en `content/blog/`.
2. Genera el sitio con Pelican:
   ```powershell
   pelican content
   ```
3. Sube los cambios a GitHub:
   ```powershell
   git add .
   git commit -m "Actualización del sitio o nuevo post"
   git push origin master
   ```

## Recomendación
Usa un entorno virtual (venv) para instalar Pelican y dependencias:
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install pelican
```

## Autor
Rodrigo Cabezas
