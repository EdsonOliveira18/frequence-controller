from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime, date
from app import models

def registrar_ponto(colaborador_id: int, db: Session) -> models.RegistroPonto:
    # Verifica se o colaborador existe
    colaborador = db.query(models.Colaborador).filter(models.Colaborador.id_col == colaborador_id).first()
    if not colaborador:
        raise ValueError("Colaborador não encontrado.")

    # Busca o último registro (qualquer data)
    ultimo_registro = (
        db.query(models.RegistroPonto)
        .filter(models.RegistroPonto.colaborador_id == colaborador_id)
        .order_by(models.RegistroPonto.timestamp_reg.desc())
        .first()
    )

    # Define tipo com base no último registro
    if not ultimo_registro or ultimo_registro.tipo_reg == "saida":
        tipo = "entrada"
    else:
        tipo = "saida"

    agora = datetime.now()

    novo_registro = models.RegistroPonto(
        colaborador_id=colaborador_id,
        tipo_reg=tipo,
        timestamp_reg=agora,
        data_reg=agora.date()  # ainda útil para agrupamentos simples
    )

    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)

    return novo_registro

# Função para testes com o timestamp manual, para casos de turnos que ultrapassem 1 dia.
def registrar_ponto_debug(colaborador_id: int, db: Session, timestamp_manual: Optional[datetime] = None) -> models.RegistroPonto:
    colaborador = db.query(models.Colaborador).filter(models.Colaborador.id_col == colaborador_id).first()
    if not colaborador:
        raise ValueError("Colaborador não encontrado.")

    ultimo_registro = (
        db.query(models.RegistroPonto)
        .filter(models.RegistroPonto.colaborador_id == colaborador_id)
        .order_by(models.RegistroPonto.timestamp_reg.desc())
        .first()
    )

    tipo = "entrada" if not ultimo_registro or ultimo_registro.tipo_reg == "saida" else "saida"

    agora = timestamp_manual or datetime.now()

    novo_registro = models.RegistroPonto(
        colaborador_id=colaborador_id,
        tipo_reg=tipo,
        timestamp_reg=agora,
        data_reg=agora.date()
    )

    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)

    return novo_registro