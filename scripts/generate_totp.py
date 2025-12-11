from app.totp_utils import generate_totp_code, get_seconds_remaining
from pathlib import Path

seed_path = "/data/seed.txt"

seed = Path(seed_path).read_text().strip()

code = generate_totp_code(seed)
print(code)
