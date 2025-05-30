from pydantic import BaseModel, Field, constr, field_validator
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
    timestamp_reg: datetime = Field(
        example="2025-05-25T00:00:00",
        description="Horário completo no formato ISO8601. NÃO incluir fuso horário (timezone)."
    )

    @field_validator("tipo_reg")
    @classmethod
    def validar_tipo_reg(cls, v: str) -> str:
        v_lower = v.lower()
        if v_lower not in {"entrada", "saida"}:
            raise ValueError("O campo 'tipo_reg' deve ser 'entrada' ou 'saida'.")
        return v_lower
