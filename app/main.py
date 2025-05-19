from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sistema de Controle de Ponto - GAMT")

# Configuração de CORS (permite front acessar o backend local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, defina domínios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensagem": "API iniciada com sucesso"}
