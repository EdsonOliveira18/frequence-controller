from pydantic import BaseModel, EmailStr

class ColaboradorCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
