# TP1 - ABM con FastAPI

Trabajo práctico de Programación 4 (TUP - UTN Paraná).

API hecha con **FastAPI** y **Pydantic** que tiene dos ABM con almacenamiento en memoria:

- **Usuarios**: alta, listado, modificación, baja y filtro por estado (activos, inactivos o todos).
- **Libros**: alta, listado, obtener por id, modificación, baja y búsqueda por autor.

## Requisitos

- Python 3.10 o superior
- Git

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/CelentanoPaulo/Tp1Prog4.git
cd Tp1Prog4
```

2. Crear el entorno virtual:

```bash
python -m venv .venv
```

3. Activar el entorno virtual:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

Con el entorno virtual activado:

```bash
fastapi dev main.py
```

La API queda disponible en `http://127.0.0.1:8000`.

## Documentación interactiva (Swagger)

Entrar a `http://127.0.0.1:8000/docs` para ver y probar todos los endpoints.
En cada uno: **Try it out** → completar los datos → **Execute**.

## Endpoints

### Usuarios

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/usuarios` | Listar usuarios. Filtro opcional `?estado=activos`, `inactivos` o `todos` |
| POST | `/usuarios` | Crear usuario |
| PUT | `/usuarios/{usuario_id}` | Modificar usuario |
| DELETE | `/usuarios/{usuario_id}` | Eliminar usuario |

### Libros

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/libros` | Listar libros. Filtro opcional `?autor=nombre` |
| GET | `/libros/{libro_id}` | Obtener un libro por id |
| POST | `/libros` | Crear libro |
| PUT | `/libros/{libro_id}` | Modificar libro |
| DELETE | `/libros/{libro_id}` | Eliminar libro |

## Nota

Los datos se guardan en memoria: al reiniciar el servidor vuelven a los valores iniciales.