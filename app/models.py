import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
from datetime import datetime, date
from sqlalchemy.orm import relationship
from app.database import Base

class Colaborador(Base): 
    __tablename__ = "colaborador"

    id_col = Column(Integer, primary_key=True, index=True)
    nome_col = Column(String, nullable=False)
    cpf_col = Column(String, unique=True, nullable=False)
    email_col = Column(String, unique=True, nullable=False)
    senha_col = Column(String, nullable=False)

    registros = relationship("RegistroPonto", back_populates="colaborador")

class RegistroPonto(Base):
    __tablename__ = "registro_ponto"

    id_reg = Column(Integer, primary_key=True, index=True)
    colaborador_id = Column(Integer, ForeignKey("colaborador.id_col"))
    tipo_reg = Column(String)                                                   # "entrada" ou "saida"
    timestamp_reg = Column(DateTime, default=datetime.utcnow)
    data_reg = Column(Date)                                                   # Apenas a data (YYYY-MM-DD) para facilitar agrupamentos

    colaborador = relationship("Colaborador", back_populates="registros")