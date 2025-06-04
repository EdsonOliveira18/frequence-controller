from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from datetime import date, datetime, time
from app.database import get_db
from app.models import RegistroPonto
from fastapi.responses import JSONResponse
from app.services.json_export_service import gerar_json_registros_segmentado
from app.services.export_service import gerar_csv_from_json_segmentado

router = APIRouter(prefix="/admin", tags=["Exportação"])

from app.services.export_service import gerar_csv_from_json_segmentado

@router.get("/exportar-csv-segmentado")
def exportar_csv_segmentado(
    inicio: date = Query(..., description="Data inicial do intervalo"),
    fim: date = Query(..., description="Data final do intervalo"),
    db: Session = Depends(get_db)
):
    inicio_dt = datetime.combine(inicio, time.min)
    fim_dt = datetime.combine(fim, time.max)

    json_data = gerar_json_registros_segmentado(inicio_dt, fim_dt, db)

    if not json_data:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado.")

    csv_file = gerar_csv_from_json_segmentado(json_data)

    filename = f"registros_segmentado_{inicio.isoformat()}_a_{fim.isoformat()}.csv"
    return StreamingResponse(
        content=csv_file,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"}
    )


@router.get("/gerar-json-segmentado")
def gerar_json_segmentado(
    inicio: date = Query(..., description="Data inicial do intervalo"),
    fim: date = Query(..., description="Data final do intervalo"),
    db: Session = Depends(get_db)
):
    inicio_dt = datetime.combine(inicio, time.min)
    fim_dt = datetime.combine(fim, time.max)

    resultado_json = gerar_json_registros_segmentado(inicio_dt, fim_dt, db)

    if not resultado_json:
        raise HTTPException(status_code=404, detail="Nenhum dado encontrado.")

    return JSONResponse(content=resultado_json)