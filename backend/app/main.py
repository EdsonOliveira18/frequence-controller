from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os
from pathlib import Path
from app.routes import colaboradores, user_register, registro_ponto
from app.database import Base, engine
from app import models

env_path = Path(__file__).resolve().parent.parent / ".env"''''''

load_dotenv(dotenv_path=env_path,  override=True)

frontend_origins = os.getenv("FRONTEND_ORIGINS", "").split(",")
print(f"ENV: {frontend_origins}")

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("✅ Banco de dados conectado com sucesso.")
    yield

# Cria o app ANTES de tudo
app = FastAPI(
    title="Sistema de Controle de Ponto - GAMT",
    lifespan=lifespan
)

# Adiciona CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=frontend_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(user_register.router)
app.include_router(colaboradores.router)
app.include_router(registro_ponto.router)

# Rota principal
@app.get("/")
def read_root():
    return {"mensagem": "API iniciada com sucesso"}
