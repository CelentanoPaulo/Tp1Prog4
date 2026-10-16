from pydantic import BaseModel


class Usuario(BaseModel):
    id: int
    nombre: str
    activo: bool = True


class UsuarioActualizar(BaseModel):
    nombre: str
    activo: bool = True