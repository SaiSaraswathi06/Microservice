import sys
sys.path.append("/app")

from app.totp_utils import generate_totp_code, get_seconds_remaining
import datetime

SEED_FILE = "/data/seed.txt"

def main():
    with open(SEED_FILE, "r") as f:
        seed = f.read().strip()

    code = generate_totp_code(seed)
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    print(f"{timestamp} - 2FA Code: {code}")

if __name__ == "__main__":
    main()
