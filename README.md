# 🔐 PKI-Based 2FA Microservice

A complete microservice implementing RSA cryptography, seed decryption, TOTP generation, verification APIs, and automated cron-based logging — containerized using Docker.

---

## 🚀 Features

### ✔ RSA 4096-bit key pair  
Used to authenticate student identity and decrypt the instructor-provided encrypted seed.

### ✔ Seed Decryption (RSA–OAEP–SHA256)  
Encrypted seed is securely decrypted inside the service and stored in `/data/seed.txt`.

### ✔ TOTP Generation (RFC-6238)  
Generates 6-digit 2FA codes every 30 seconds using SHA-1, period = 30s.

### ✔ API Endpoints (FastAPI)
| Endpoint | Method | Description |
|---------|--------|-------------|
| `/decrypt-seed` | POST | Decrypts seed and stores it |
| `/generate-2fa` | GET | Generates current TOTP |
| `/verify-2fa` | POST | Verifies submitted code |

### ✔ Cron Job  
Logs a new TOTP code every minute into `/cron/last_code.txt`.

### ✔ Dockerized Microservice  
Runs both API server and cron service in one container.

---

## 📁 File Structure

```
Microservice/
│── app/
│   ├── crypto_utils.py
│   ├── totp_utils.py
│   └── main.py
│── scripts/
│   ├── request_seed.py
│   └── log_2fa_cron.py
│── cron/
│   └── 2fa-cron
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── student_private.pem
│── student_public.pem
│── instructor_public.pem
```

---

# ✅ Submission Details (REQUIRED)

### **GitHub Repository URL**
```
https://github.com/SaiSaraswathi06/Microservice
```

### **Commit Hash (40-char)**
```
2b524f70484df161aa351f61b10f514be0ebdf55
```

### **Encrypted Signature (64-char)**
```
c5df0107e126c632377876ab90616ffb94a12c8e9c00d89a7820f1fce7136e35
```

### **Student Public Key (PEM)**  
(Multi-line version)
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAp+3oz0uqhbXx5XezxXaU
KlRWYH82l/td2RJ2Y8MGQkNEazpFw8TVMFSyC60MeayCv9lwwq4atCcxp7wgv0pv
xq2e78gVABjXdZdhkZvJkKVggZRb1E+cySzqs5Qu30j2YCQRJKSG/UOySMRK4qhf
5QksAExppRhKyhdBp32F3JZzwZ+SObABb3EIf1tRi70dB/1YUjobXZprjKiZZPTP
zQwmZ6lrE2/JDvRKh0yYMMmejkXrgABSpCHSzxS0a8IEPpYwKodteGD50q8qdVkw
E/oMJDdJRp+padI9qiPLb5TxV4kVfEIdk6xSxpAi63nPVy0rMZK1fQFLVqGyX+rw
coWSQwRw0ty5Aczih2PBhrLckM8JmR6w9ZajkKwdP02TkIrrFeHU+fXYlUUphuUe
j2kt2bmXhANFHyZS0lYfzKk/4z4LEOKLmlSpaD3QXpSKFg322vxENHGRzUxPhobX
DyvC4Kdah5bPUuF/z9f5DouQFtb/NzcOvyizTs83uW331Cw09aeB5svRjZ+mwvxg
mnBk6WEBqJhA7y3S/L+l8Yiw7zGqNyAiwNak/m6yWsDtAOY6QjVH/qWGVIIZIw98
nu/7mErxXDeumOHqPBZJlBACQqBUdTB7rnmhvsUJFWx3KyJpHFNVKfvTCD2dqFKo
ToNDUtGnkGNnqP56eErZD38CAwEAAQ==
-----END PUBLIC KEY-----
```

---

# 🛡 Production Improvements (What I Would Improve)

- Load RSA keys from AWS Secrets Manager (never inside image)  
- Enforce HTTPS, HSTS, and mTLS for internal services  
- Rate-limit API and add API keys/JWT auth  
- Move seed + logs to encrypted database  
- Run service as non-root  
- Add Prometheus + Grafana monitoring  
- Deploy using Kubernetes with auto-scaling  
- Add vulnerability scanning in CI/CD  

---

# 🎯 **Task Completed Successfully**

 

