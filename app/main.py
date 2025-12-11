from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

from app.crypto_utils import decrypt_and_store_from_b64
from app.totp_utils import generate_totp_code, verify_totp_code, get_seconds_remaining

SEED_PATH = "/data/seed.txt"

app = FastAPI()

# ------------------ Models ------------------

class DecryptRequest(BaseModel):
    encrypted_seed: str

class VerifyRequest(BaseModel):
    code: str


# ------------------ Endpoints ------------------

@app.get("/")
def root():
    return {"message": "2FA Microservice is running"}


# 1️⃣ POST /decrypt-seed
@app.post("/decrypt-seed")
def decrypt_seed(req: DecryptRequest):
    try:
        seed = decrypt_and_store_from_b64(req.encrypted_seed)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Decryption failed: {str(e)}")


# 2️⃣ GET /generate-2fa
@app.get("/generate-2fa")
def generate_2fa():
    if not os.path.exists(SEED_PATH):
        raise HTTPException(status_code=500, detail="Seed not decrypted yet")

    with open(SEED_PATH, "r") as f:
        hex_seed = f.read().strip()

    try:
        code = generate_totp_code(hex_seed)
        valid_for = get_seconds_remaining()
        return {"code": code, "valid_for": valid_for}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating code: {str(e)}")


# 3️⃣ POST /verify-2fa
@app.post("/verify-2fa")
def verify_2fa(req: VerifyRequest):
    if req.code is None or req.code.strip() == "":
        raise HTTPException(status_code=400, detail="Missing code")

    if not os.path.exists(SEED_PATH):
        raise HTTPException(status_code=500, detail="Seed not decrypted yet")

    with open(SEED_PATH, "r") as f:
        hex_seed = f.read().strip()

    try:
        is_valid = verify_totp_code(hex_seed, req.code)
        return {"valid": is_valid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Verification error: {str(e)}")
