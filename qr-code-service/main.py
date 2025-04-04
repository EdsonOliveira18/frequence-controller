from fastapi import FastAPI
import qrcode
import io
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/generate-qr")
def generate_qr(data: str):
    img = qrcode.make(data)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")