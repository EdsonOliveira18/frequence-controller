from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Colaborador, RegistroPonto
from app.utils import hash_senha
from app.schemas.adm_schema import RedefinirSenhaRequest, RegistroPontoManualRequest
from datetime import datetime
from app.utils import validar_senha_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.post("/redefinir-senha")
def redefinir_senha(request: RedefinirSenhaRequest, db: Session = Depends(get_db)):
    if not validar_senha_admin(request.admin_key):
        raise HTTPException(status_code=403, detail="Chave de administrador incorreta.")

    colaborador = db.query(Colaborador).filter(Colaborador.id_col == request.colaborador_id).first()
    if not colaborador:
        raise HTTPException(status_code=404, detail="Colaborador não encontrado.")

    colaborador.senha_col = hash_senha(request.nova_senha)
    db.commit()
    return {"message": "Senha redefinida com sucesso.",
            "nova_senha": request.nova_senha
           }


@router.post("/registro-manual")
def registrar_ponto_manual(request: RegistroPontoManualRequest, db: Session = Depends(get_db)):
    if not validar_senha_admin(request.admin_key):
        raise HTTPException(status_code=403, detail="Chave de administrador incorreta.")

    colaborador = db.query(Colaborador).filter(Colaborador.id_col == request.colaborador_id).first()
    if not colaborador:
        raise HTTPException(status_code=404, detail="Colaborador não encontrado.")

    novo_registro = RegistroPonto(
        colaborador_id=request.colaborador_id,
        tipo_reg=request.tipo_reg,
        timestamp_reg=request.timestamp_reg,
        data_reg=request.timestamp_reg.date()
    )
    db.add(novo_registro)
    db.commit()
    return {"message": "Registro de ponto manual criado com sucesso."}
