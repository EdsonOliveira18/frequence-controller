from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import services
from app.services import registro_service
from app.schemas.user_schema import RegistroPontoDebug
from app.schemas import user_schema

router = APIRouter()

@router.post("/registro", response_model=user_schema.RegistroPontoOut)
def registrar_ponto_endpoint(
    registro: user_schema.RegistroPontoCreate,
    db: Session = Depends(get_db)
):
    try:
        novo_registro = registro_service.registrar_ponto(registro.colaborador_id, db)
        return novo_registro
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao registrar ponto.")
    
# Rota de debug do controle de ponto para casos onde o ponto ultrapasse a meia noite
@router.post("/registro/debug", response_model=user_schema.RegistroPontoOut)
def registrar_ponto_debug_endpoint(
    dados: RegistroPontoDebug,
    db: Session = Depends(get_db)
):
    try:
        registro = registro_service.registrar_ponto_debug(
            colaborador_id=dados.colaborador_id,
            db=db,
            timestamp_manual=dados.timestamp_manual
        )
        return registro
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao registrar ponto (debug).")
