from fastapi import FastAPI, Request
from sheets import registrar_presenca

app = FastAPI()

@app.post("/registrar")
def registrar(req: Request):
    data = req.json()
    resultado = registrar_presenca(data)
    return {"resultado": resultado}