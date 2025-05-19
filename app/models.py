from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class Colaborador(Base): 
    __tablename__ = "colaboradores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha_hash = Column(String, nullable=False)

class Ponto(Base):
    __tablename__ = "ponto"

    id = Column(Integer, primary_key=True, index=True)
    fk_colaborador = Column(Integer, ForeignKey("colaboradores.id"), nullable=False)
    entrada = Column(DateTime, nullable=False)
    saida = Column(DateTime, nullable=True)
