from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.routes import colaboradores, user_register
from app.database import Base, engine
from app import models  # Isso garante que Base conheça os modelos

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa no início da aplicação
    Base.metadata.create_all(bind=engine)
    print("✅ Banco de dados conectado com sucesso.")
    yield
    # Aqui executaria código de finalização se necessário (ex: db.close())

# Criação única da aplicação com lifespan
app = FastAPI(
    title="Sistema de Controle de Ponto - GAMT",
    lifespan=lifespan
)

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restrinja para os domínios do front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas do módulo user_register
app.include_router(user_register.router)
app.include_router(colaboradores.router)

# Rota principal
@app.get("/")
def read_root():
    return {"mensagem": "API iniciada com sucesso"}
