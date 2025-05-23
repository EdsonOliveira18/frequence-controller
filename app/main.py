from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

from app.routes import colaboradores, user_register
from app.database import Base, engine
from app import models

load_dotenv()

frontend_origins = os.getenv("FRONTEND_ORIGINS", "").split(",")

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

# Rota principal
@app.get("/")
def read_root():
    return {"mensagem": "API iniciada com sucesso"}
