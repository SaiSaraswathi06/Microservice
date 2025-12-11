import base64
import pyotp
import time

def hex_to_base32(hex_seed: str) -> str:
    """
    Convert a 64-character hex seed to base32 string for TOTP use.
    """
    raw_bytes = bytes.fromhex(hex_seed)
    base32_seed = base64.b32encode(raw_bytes).decode("utf-8")
    return base32_seed

def generate_totp_code(hex_seed: str) -> str:
    """
    Generate current 6-digit TOTP code.
    """
    base32_seed = hex_to_base32(hex_seed)
    totp = pyotp.TOTP(base32_seed, digits=6, interval=30)
    return totp.now()

def verify_totp_code(hex_seed: str, code: str, valid_window: int = 1) -> bool:
    """
    Verify a given TOTP code (±1 interval tolerance).
    """
    base32_seed = hex_to_base32(hex_seed)
    totp = pyotp.TOTP(base32_seed, digits=6, interval=30)
    return totp.verify(code, valid_window=valid_window)

def get_seconds_remaining() -> int:
    """
    Returns how many seconds remain in the current 30-second TOTP window.
    """
    return 30 - (int(time.time()) % 30)
