from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Colaborador
from app.schemas import ColaboradorCreate
from app.utils import gerar_senha, hash_senha

def cadastrar_novo_colaborador(dados: ColaboradorCreate, db: Session) -> str:

    existente = db.query(Colaborador).filter(
        (Colaborador.cpf_col == dados.cpf) | (Colaborador.email_col == dados.email)
    ).first()

    if existente:
        raise HTTPException(status_code=400, detail="Colaborador já cadastrado")

    senha = gerar_senha()
    senha_criptografada = hash_senha(senha)

    novo = Colaborador(
        nome_col=dados.nome,
        cpf_col=dados.cpf,
        email_col=dados.email,
        senha_col=senha_criptografada
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return senha
