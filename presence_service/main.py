from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .sheets import registrar_presenca

app = FastAPI()

# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção: defina seu domínio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/registrar")
async def registrar(req: Request):
    data = await req.json()
    resultado = registrar_presenca(data)
    return {"resultado": resultado}
