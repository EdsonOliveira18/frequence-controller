from pydantic import BaseModel, EmailStr

class ColaboradorCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr

class LoginRequest(BaseModel):
    cpf: str
    senha: str