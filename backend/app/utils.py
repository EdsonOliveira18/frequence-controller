import random
import string
import bcrypt

#Função responsável por gerar a senha de forma randomica com 8 caracteres.
def gerar_senha(tamanho: int = 8) -> str:
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=tamanho))

#Função responsável por cifrar a senha com o bcrypt, usando hash.
def hash_senha(senha: str) -> str:
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

#Função para verificar se o hash da senha corresponde ao que está no BD.
def verificar_senha(senha_plain: str, senha_hash: str) -> bool:
    return bcrypt.checkpw(senha_plain.encode('utf-8'), senha_hash.encode('utf-8'))