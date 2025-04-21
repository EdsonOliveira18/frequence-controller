from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import qrcode
import io

app = FastAPI()

# Configura pasta de templates e arquivos estáticos
app.mount("/static", StaticFiles(directory="web_service/static"), name="static")
templates = Jinja2Templates(directory="web_service/templates")

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

@app.get("/qrcode", response_class=StreamingResponse)
def gerar_qrcode():
    url = "http://192.168.18.47/?slide=form"
    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")

@app.get("/formulario", response_class=HTMLResponse)
def formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})
