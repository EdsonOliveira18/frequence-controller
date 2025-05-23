from pydantic import BaseModel, EmailStr, field_validator

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