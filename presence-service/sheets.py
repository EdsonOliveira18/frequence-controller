import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()

sheet_id = os.getenv("GOOGLE_SHEET_ID")
cred_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(sheet_id).sheet1

def registrar_presenca(data):
    try:
        cpf = data["cpf"]
        nome = data["nome"]
        horario = data["horario"]
        local = data["local"]

        sheet.append_row([cpf, nome, horario, local])
        return "Presença registrada com sucesso."
    except Exception as e:
        return f"Erro: {str(e)}"
