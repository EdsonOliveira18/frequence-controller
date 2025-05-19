from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models import Colaborador
from app.schemas import ColaboradorCreate
from app.utils import gerar_senha, hash_senha

def cadastrar_novo_colaborador(dados: ColaboradorCreate, db: Session) -> str:
    """
    Realiza a lógica de cadastro de um novo colaborador:
    - Verifica se já existe CPF ou e-mail
    - Gera senha
    - Hasheia senha
    - Persiste no banco
    - Retorna a senha gerada
    """
    existente = db.query(Colaborador).filter(
        (Colaborador.cpf == dados.cpf) | (Colaborador.email == dados.email)
    ).first()

    if existente:
        raise HTTPException(status_code=400, detail="Colaborador já cadastrado")

    senha = gerar_senha()
    senha_criptografada = hash_senha(senha)

    novo = Colaborador(
        nome=dados.nome,
        cpf=dados.cpf,
        email=dados.email,
        senha_hash=senha_criptografada
    )

    db.add(novo)
    db.commit()
    db.refresh(novo)

    return senha
