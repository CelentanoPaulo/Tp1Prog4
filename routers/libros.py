from fastapi import APIRouter, HTTPException

from models.libros import Libro, LibroActualizar

router = APIRouter(tags=["Libros"])

libros: list[Libro] = [
    Libro(id=1, titulo="Rayuela", autor="Julio Cortazar", anio=1963),
    Libro(id=2, titulo="Ficciones", autor="Jorge Luis Borges", anio=1944),
    Libro(id=3, titulo="El Aleph", autor="Jorge Luis Borges", anio=1949),
]


@router.get("/libros")
def listar_libros(autor: str = ""):
    if autor == "":
        return libros

    resultado = []
    for libro in libros:
        if autor.lower() in libro.autor.lower():
            resultado.append(libro)
    return resultado


@router.get("/libros/{libro_id}")
def obtener_libro(libro_id: int):
    for libro in libros:
        if libro.id == libro_id:
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")


@router.post("/libros")
def crear_libro(libro: Libro):
    libros.append(libro)
    return {"mensaje": "Libro creado"}


@router.put("/libros/{libro_id}")
def modificar_libro(libro_id: int, datos: LibroActualizar):
    for libro in libros:
        if libro.id == libro_id:
            libro.titulo = datos.titulo
            libro.autor = datos.autor
            libro.anio = datos.anio
            libro.disponible = datos.disponible
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")


@router.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    for libro in libros:
        if libro.id == libro_id:
            libros.remove(libro)
            return {"mensaje": "Libro eliminado"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")