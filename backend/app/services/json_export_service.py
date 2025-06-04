from sqlalchemy.orm import Session
from collections import defaultdict
from datetime import datetime
from app.models import RegistroPonto, Colaborador

def gerar_json_registros_segmentado(inicio: datetime, fim: datetime, db: Session):
    registros = db.query(RegistroPonto).filter(
        RegistroPonto.timestamp_reg >= inicio,
        RegistroPonto.timestamp_reg <= fim
    ).order_by(RegistroPonto.timestamp_reg.asc()).all()

    agrupado = defaultdict(list)
    for reg in registros:
        agrupado[reg.colaborador_id].append(reg)

    resultado = []

    for colab_id, eventos in agrupado.items():
        colaborador = db.query(Colaborador).filter(Colaborador.id_col == colab_id).first()
        entrada = None
        pontos = []
        observacoes = []

        for evento in eventos:
            if evento.tipo_reg == "entrada":
                entrada = evento.timestamp_reg
            elif evento.tipo_reg == "saida":
                saida = evento.timestamp_reg
                if entrada:
                    if entrada.date() == saida.date():
                        pontos.append({
                            "data_entrada": entrada.date().isoformat(),
                            "hora_entrada": entrada.time().strftime("%H:%M:%S"),
                            "data_saida": saida.date().isoformat(),
                            "hora_saida": saida.time().strftime("%H:%M:%S")
                        })
                    else:
                        # Divide em dois dias
                        pontos.append({
                            "data_entrada": entrada.date().isoformat(),
                            "hora_entrada": entrada.time().strftime("%H:%M:%S"),
                            "data_saida": entrada.date().isoformat(),
                            "hora_saida": "23:59:00"
                        })
                        pontos.append({
                            "data_entrada": saida.date().isoformat(),
                            "hora_entrada": "00:00:00",
                            "data_saida": saida.date().isoformat(),
                            "hora_saida": saida.time().strftime("%H:%M:%S")
                        })
                        observacoes.append(
                            f"Turno dividido entre {entrada.date()} e {saida.date()} por ultrapassar a meia-noite."
                        )
                    entrada = None
                else:
                    # Saída sem entrada: completar com 00:00
                    pontos.append({
                        "data_entrada": saida.date().isoformat(),
                        "hora_entrada": "00:00:00",
                        "data_saida": saida.date().isoformat(),
                        "hora_saida": saida.time().strftime("%H:%M:%S")
                    })
                    observacoes.append(
                        f"Saída sem entrada em {saida.date()} às {saida.time()} - completado com 00:00:00"
                    )

        if entrada:
            # Entrada sem saída: completar com 23:59
            pontos.append({
                "data_entrada": entrada.date().isoformat(),
                "hora_entrada": entrada.time().strftime("%H:%M:%S"),
                "data_saida": entrada.date().isoformat(),
                "hora_saida": "23:59:00"
            })
            observacoes.append(
                f"Entrada sem saída em {entrada.date()} às {entrada.time()} - completado com 23:59:00"
            )

        resultado.append({
            "nome_colaborador": colaborador.nome_col,
            "cpf_colaborador": colaborador.cpf_col,
            "registro_pontos": pontos,
            "observacao": observacoes
        })

    return resultado
