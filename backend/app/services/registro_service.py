from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime, date
from app import models

def registrar_ponto(colaborador_id: int, db: Session) -> models.RegistroPonto:
    # Verifica se o colaborador existe
    colaborador = db.query(models.Colaborador).filter(models.Colaborador.id_col == colaborador_id).first()
    if not colaborador:
        raise ValueError("Colaborador não encontrado.")

    print("✅ Colaborador encontrado:", colaborador.nome_col)
    
    # Busca o último registro (qualquer data)
    registros_todos = db.query(models.RegistroPonto).filter(
        models.RegistroPonto.colaborador_id == colaborador_id
    ).order_by(models.RegistroPonto.timestamp_reg.desc()).all()

    print(f"📋 Todos os registros do colaborador {colaborador_id}:")
    for r in registros_todos:
        print(f" - {r.tipo_reg} às {r.timestamp_reg}")

    ultimo_registro = registros_todos[0] if registros_todos else None

    # Define tipo com base no último registro
    if not ultimo_registro or ultimo_registro.tipo_reg == "saida":
        tipo = "entrada"
    else:
        tipo = "saida"

    print("🧠 Tipo definido para novo registro:", tipo)

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

    print("💾 Novo registro salvo:", novo_registro.tipo_reg, "às", novo_registro.timestamp_reg)

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