# app/crypto_utils.py
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import os
import re

SEED_PATH = "/data/seed.txt"

HEX64_RE = re.compile(r"^[0-9a-f]{64}$")  # lowercase hex only

def load_private_key(path: str = "student_private.pem"):
    """
    Load PEM private key file (unencrypted).
    """
    with open(path, "rb") as f:
        key_data = f.read()
    private_key = serialization.load_pem_private_key(key_data, password=None)
    return private_key

def decrypt_seed(encrypted_seed_b64: str, private_key) -> str:
    """
    Decrypt base64-encoded encrypted seed using RSA/OAEP (SHA-256, MGF1).
    Returns: 64-character lowercase hex string.
    Raises ValueError on any validation/decryption error.
    """
    if not isinstance(encrypted_seed_b64, str) or not encrypted_seed_b64.strip():
        raise ValueError("Encrypted seed must be a non-empty base64 string")

    try:
        ciphertext = base64.b64decode(encrypted_seed_b64)
    except Exception as e:
        raise ValueError("Encrypted seed is not valid base64") from e

    try:
        plaintext = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )
    except Exception as e:
        raise ValueError("RSA decryption failed") from e

    try:
        seed_str = plaintext.decode("utf-8")
    except Exception as e:
        raise ValueError("Decrypted seed is not valid UTF-8 text") from e

    # Normalize: remove whitespace
    seed_str = seed_str.strip().lower()

    # Validate: must be exactly 64 hex lowercase chars
    if not HEX64_RE.fullmatch(seed_str):
        raise ValueError("Decrypted seed validation failed: expected 64 lowercase hex characters")

    return seed_str

def save_seed_to_data(hex_seed: str, path: str = SEED_PATH):
    """
    Save the 64-char hex seed to the persistent path (/data/seed.txt).
    Ensures directory exists and sets permissive file mode.
    """
    if not HEX64_RE.fullmatch(hex_seed):
        raise ValueError("seed must be 64 lowercase hex characters")

    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Write atomically: write to temp then rename
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(hex_seed + "\n")

    os.replace(tmp, path)

    # Set file permissions: owner read/write only (where supported)
    try:
        os.chmod(path, 0o600)
    except Exception:
        # Windows may not support chmod in the same way; ignore if fails
        pass

def decrypt_and_store_from_b64(encrypted_seed_b64: str, private_key_path: str = "student_private.pem"):
    """
    Convenience wrapper: loads private key from file, decrypts the base64 seed,
    validates it, and stores it to /data/seed.txt.
    Returns the hex seed string on success.
    """
    private_key = load_private_key(private_key_path)
    hex_seed = decrypt_seed(encrypted_seed_b64, private_key)
    save_seed_to_data(hex_seed)
    return hex_seed
