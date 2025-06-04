import csv
import io
from collections import defaultdict
from datetime import datetime
from sqlalchemy.orm import Session
from app.models import RegistroPonto, Colaborador

def calcular_duracao_em_minutos(entrada: datetime, saida: datetime) -> int:
    if entrada and saida:
        return int((saida - entrada).total_seconds() / 60)
    return 0

def gerar_csv_from_json_segmentado(json_data: list) -> io.StringIO:
    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow([
        "nome_colaborador", "CPF",
        "data_entrada", "hora_entrada",
        "data_saida", "hora_saida",
        "duracao_turno_min"
    ])

    for colaborador in json_data:
        nome = colaborador["nome_colaborador"]
        cpf = colaborador["cpf_colaborador"]
        for ponto in colaborador["registro_pontos"]:
            entrada_str = f"{ponto['data_entrada']} {ponto['hora_entrada']}" if ponto['data_entrada'] and ponto['hora_entrada'] else None
            saida_str = f"{ponto['data_saida']} {ponto['hora_saida']}" if ponto['data_saida'] and ponto['hora_saida'] else None

            entrada_dt = datetime.strptime(entrada_str, "%Y-%m-%d %H:%M:%S") if entrada_str else None
            saida_dt = datetime.strptime(saida_str, "%Y-%m-%d %H:%M:%S") if saida_str else None
            duracao = calcular_duracao_em_minutos(entrada_dt, saida_dt)

            writer.writerow([
                nome,
                cpf,
                ponto["data_entrada"],
                ponto["hora_entrada"],
                ponto["data_saida"],
                ponto["hora_saida"],
                duracao
            ])

    output.seek(0)
    return output

