from fastapi import FastAPI

app = FastAPI()


frutas:list[str] = ["manzana", "banana", "naranja"]


@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI"}


@app.get("/health")
def get_health():
    return {"status": "ok"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hola {name}"}


@app.get("/square/{number}")
def get_square(number: int):
    return {"number": number, "square": number * number}


@app.get("/frutas")
def get_frutas():
    return {"frutas": frutas}


@app.post("/frutas")
def add_fruit(name:str):
    frutas.append(name)
    return {"message": f"{name} agregada", "frutas": frutas}