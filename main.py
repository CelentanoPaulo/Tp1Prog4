from fastapi import FastAPI

app = FastAPI()


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