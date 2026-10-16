from fastapi import APIRouter, HTTPException

from models.users import Usuario, UsuarioActualizar

router = APIRouter()

usuarios: list[Usuario] = [
    Usuario(id=1, nombre="Paulo Celentano"),
    Usuario(id=2, nombre="Pepe Mujica", activo=False),
]


@router.get("/usuarios")
def listar_usuarios(estado: str = "todos"):
    if estado == "todos":
        return usuarios

    resultado = []
    for usuario in usuarios:
        if estado == "activos" and usuario.activo:
            resultado.append(usuario)
        if estado == "inactivos" and not usuario.activo:
            resultado.append(usuario)
    return resultado


@router.post("/usuarios")
def crear_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return {"mensaje": "Usuario creado"}


@router.put("/usuarios/{usuario_id}")
def modificar_usuario(usuario_id: int, datos: UsuarioActualizar):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuario.nombre = datos.nombre
            usuario.activo = datos.activo
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


@router.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            usuarios.remove(usuario)
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")