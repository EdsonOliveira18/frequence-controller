from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"])  

@app.get("/ping")
def ping():
    return {"message": "API Gateway funcionando!"}

@app.post("/registrar-presenca")
def registrar_presenca(dados: dict):
    response = requests.post("http://localhost:8003/registrar", json=dados)
    return response.json()