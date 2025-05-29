from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import LoginRequest, ColaboradorOut
from app.database import get_db
from app.services.colaborador_service import login_colaborador  # novo import

router = APIRouter()

@router.post("/login", response_model=ColaboradorOut)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    colaborador = login_colaborador(login_data.cpf, login_data.senha, db)
    return colaborador
