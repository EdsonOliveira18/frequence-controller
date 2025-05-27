from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime, date
from typing import Optional

class ColaboradorCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    
    @field_validator("cpf")
    @classmethod
    def normalizar_cpf(cls, v: str) -> str:
        return ''.join(filter(str.isdigit, v))
    
class LoginRequest(BaseModel):
    cpf: str
    senha: str

# Schema para entrada de dados no registro de ponto
class RegistroPontoCreate(BaseModel):
    colaborador_id: int

# Schema para saída de dados (retorno do backend)
class RegistroPontoOut(BaseModel):
    id_reg: int
    colaborador_id: int
    tipo_reg: str
    timestamp_reg: datetime
    data_reg: date

    class Config:
        orm_mode = True

# Schema para testes com o controle de ponto.
class RegistroPontoDebug(BaseModel):
    colaborador_id: int
    timestamp_manual: Optional[datetime] = None  # Pode ser omitido