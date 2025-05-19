from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import ColaboradorCreate
from app.database import get_db
from app.services.user_service import cadastrar_novo_colaborador

router = APIRouter()

@router.post("/cadastro")
def cadastrar_colaborador(dados: ColaboradorCreate, db: Session = Depends(get_db)):
    senha = cadastrar_novo_colaborador(dados, db)
    return {
        "mensagem": "Colaborador cadastrado com sucesso",
        "senha_gerada": senha
    }
