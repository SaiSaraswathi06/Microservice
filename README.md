# Microservice
# Microservice – 2FA Authentication System

This project implements a secure Two-Factor Authentication (2FA) microservice using:
- Python (FastAPI)
- Docker & Docker Compose
- Cron job for periodic TOTP generation
- RSA-based encrypted seed exchange

---

## 📌 Features Implemented

### ✅ 1. `/decrypt-seed`  
Decrypts the encrypted seed using the student's private key.

### ✅ 2. `/generate-2fa`  
Generates a TOTP code valid for 15 seconds.

### ✅ 3. `/verify-2fa`  
Verifies a submitted 2FA code.

### ✅ 4. Cron Job  
Runs every 1 minute inside the container and logs:

```
YYYY-MM-DD HH:MM:SS – 2FA Code: XXXXXX
```

into:

```
/cron/last_code.txt
```

---

## 📁 Project Structure

```
Microservice/
│
├── app/
│   ├── main.py
│   ├── totp_utils.py
│   ├── seed_utils.py
│
├── scripts/
│   ├── log_2fa_cron.py
│   ├── request_seed.py
│   ├── verify_totp.py
│
├── cron/
│   ├── 2fa-cron
│   ├── last_code.txt (created in container)
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── encrypted_seed.txt
├── instructor_public.pem
├── student_public.pem
├── student_private.pem
└── README.md
```

---

## 🐳 Running the Microservice

### **Build & Run with Docker**
```bash
docker compose up --build
```

FastAPI runs at:

```
http://127.0.0.1:8080
```

---

## 🧪 Testing API Endpoints

### **1️⃣ Decrypt Seed**
```bash
curl -X POST http://127.0.0.1:8080/decrypt-seed \
     -H "Content-Type: application/json" \
     -d "{\"encrypted_seed\": \"$(cat encrypted_seed.txt)\"}"
```

### **2️⃣ Generate 2FA Code**
```bash
curl http://127.0.0.1:8080/generate-2fa
```

### **3️⃣ Verify Code**
```bash
curl -X POST http://127.0.0.1:8080/verify-2fa \
     -H "Content-Type: application/json" \
     -d "{\"code\": \"123456\"}"
```

---

## 🕒 View Cron Output

```bash
docker exec -it saraswathi-task sh -c "cat /cron/last_code.txt"
```

Example output:

```
2025-12-11 13:35:03 – 2FA Code: 682004
```

---

## 📌 Submission Requirements

After pushing all code to GitHub, go to the **Scaler Assignment Portal** and submit your repo link:

```
https://github.com/SaiSaraswathi06/Microservice
```

Scaler will automatically:
- Clone your repo  
- Run your microservice  
- Validate outputs  
- Generate a **64-character signature**

---

## 🔐 64-Character Signature (Fill This After Scaler Generates It)

```
<PASTE YOUR SIGNATURE HERE>
```

---

## 🔑 Commit Hash (Use Your Latest Git Commit)

Run:

```bash
git log --oneline | head -1
```

Then paste here:

```
<PASTE YOUR COMMIT HASH HERE>
```

---

## 🎉 Done!

You have successfully completed the Microservice Assignment.

