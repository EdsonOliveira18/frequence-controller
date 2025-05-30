from pydantic import BaseModel, constr, field_validator
from datetime import datetime
from typing import Annotated

NovaSenhaType = Annotated[str, constr(min_length=8)]

class AcessoAdminBase(BaseModel):
    admin_key: str

class RedefinirSenhaRequest(AcessoAdminBase):
    colaborador_id: int
    nova_senha: NovaSenhaType

class RegistroPontoManualRequest(AcessoAdminBase):
    colaborador_id: int
    tipo_reg: str
    timestamp_reg: datetime

    @field_validator("tipo_reg")
    @classmethod
    def validar_tipo_reg(cls, v: str) -> str:
        v_lower = v.lower()
        if v_lower not in {"entrada", "saida"}:
            raise ValueError("O campo 'tipo_reg' deve ser 'entrada' ou 'saida'.")
        return v_lower
