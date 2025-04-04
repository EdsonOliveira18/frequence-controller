from fastapi import FastAPI
import pyotp

app = FastAPI()

SECRET = pyotp.random_base32()

@app.get("/generate-secret")
def generate_secret():
    return {"secret": SECRET}

@app.get("/verify")
def verify(code: str):
    totp = pyotp.TOTP(SECRET)
    return {"valid": totp.verify(code)}