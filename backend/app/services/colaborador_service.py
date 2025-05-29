from sqlalchemy.orm import Session
from app.models import Colaborador
from app.utils import verificar_senha
from fastapi import HTTPException

def login_colaborador(cpf: str, senha: str, db: Session):
    cpf = ''.join(filter(str.isdigit, cpf))  # normaliza CPF
    colaborador = db.query(Colaborador).filter(Colaborador.cpf_col == cpf).first()

    if not colaborador:
        raise HTTPException(status_code=401, detail="Colaborador não encontrado")

    if not verificar_senha(senha, colaborador.senha_col):
        raise HTTPException(status_code=401, detail="Senha incorreta")

    return colaborador
