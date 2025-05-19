from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import Base, engine
from app import models  # Aqui, importamos os modelos, isso garante que "Base" reconheça todas as tabelas.

app = FastAPI(title="Sistema de Controle de Ponto - GAMT")

# Configuração de CORS (permite front acessar o backend local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executado no startup a criação do Banco de Dados
    Base.metadata.create_all(bind=engine)
    yield
    # Aqui seria o shutdown (se precisar fechar conexões, etc)

app = FastAPI(
    title="Sistema de Controle de Ponto - GAMT",
    lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"mensagem": "API iniciada com sucesso"}
