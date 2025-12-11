# test_decrypt.py
from app.crypto_utils import decrypt_and_store_from_b64
import sys

ENC_FILE = "encrypted_seed.txt"
PRIVATE_KEY = "student_private.pem"

def main():
    try:
        with open(ENC_FILE, "r") as f:
            encrypted = f.read().strip()
    except FileNotFoundError:
        print(f"ERROR: {ENC_FILE} not found. Run the instructor API request step first.")
        sys.exit(1)

    try:
        seed = decrypt_and_store_from_b64(encrypted, PRIVATE_KEY)
        print("Decryption SUCCESS. Seed:", seed)
        print("Seed saved to /data/seed.txt")
    except Exception as e:
        print("Decryption FAILED:", str(e))
        sys.exit(2)

if __name__ == "__main__":
    main()
