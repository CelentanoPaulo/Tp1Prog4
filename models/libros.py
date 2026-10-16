from pydantic import BaseModel


class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    anio: int
    disponible: bool = True


class LibroActualizar(BaseModel):
    titulo: str
    autor: str
    anio: int
    disponible: bool = True