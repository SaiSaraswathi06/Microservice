from app.totp_utils import verify_totp_code
import sys
from pathlib import Path

seed_path = "/data/seed.txt"

seed = Path(seed_path).read_text().strip()
code = sys.argv[1]

print(verify_totp_code(seed, code))
