# ============================
# Stage 1: Builder
# ============================
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt


# ============================
# Stage 2: Runtime
# ============================
FROM python:3.11-slim

ENV TZ=UTC

WORKDIR /app

# Install system packages (cron + tzdata)
RUN apt-get update && apt-get install -y --no-install-recommends \
    cron \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Set timezone
RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application source
COPY app/ /app/app/
COPY scripts/ /app/scripts/
COPY cron/ /app/cron/

# Install cron job
RUN chmod 0644 /app/cron/2fa-cron && crontab /app/cron/2fa-cron

# Create persistent directories
RUN mkdir -p /data && mkdir -p /cron

# Expose API port
EXPOSE 8080

# Start cron + FastAPI app
CMD cron && uvicorn app.main:app --host 0.0.0.0 --port 8080
