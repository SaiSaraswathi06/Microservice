import requests
import json

API_URL = "https://eajeyq4r3zljoq4rpovy2nthda0vtjqf.lambda-url.ap-south-1.on.aws"

student_id = "239A1A0594"
repo_url = "https://github.com/SaiSaraswathi06/Microservice"

# Read public key EXACTLY as-is (no replace)
with open("student_public.pem", "r") as f:
    public_key = f.read()

print("DEBUG RAW PUBLIC KEY:")
print(public_key)

payload = {
    "student_id": student_id,
    "github_repo_url": repo_url,
    "public_key": public_key  # <-- RAW, NOT MODIFIED
}

response = requests.post(API_URL, json=payload)
print("API Response:", response.text)

try:
    encrypted_seed = response.json().get("encrypted_seed")
    if encrypted_seed:
        with open("encrypted_seed.txt", "w") as f:
            f.write(encrypted_seed)
        print("Saved encrypted_seed.txt")
    else:
        print("No encrypted seed returned.")
except:
    print("Error parsing JSON response.")

