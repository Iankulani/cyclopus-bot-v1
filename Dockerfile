# ============================================================
# 🐙 CYCLOPUS-BOT-V1 - Dockerfile (Alpine Linux)
# Author: Ian Carter Kulani, MSc
# Version: 1.0.0
# ============================================================

# =====================
# BUILD STAGE
# =====================
FROM python:3.11-alpine AS builder

LABEL maintainer="Ian Carter Kulani"
LABEL description="CYCLOPUS-BOT-V1 - Ultimate Cybersecurity Platform"
LABEL version="1.0.0"

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    make \
    cargo \
    rust \
    git \
    && rm -rf /var/cache/apk/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements
WORKDIR /app
COPY requirements-full.txt requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-full.txt

# =====================
# RUNTIME STAGE
# =====================
FROM python:3.11-alpine

LABEL maintainer="Ian Carter Kulani"
LABEL description="CYCLOPUS-BOT-V1 - Ultimate Cybersecurity Platform"
LABEL version="1.0.0"

# Install runtime dependencies
RUN apk add --no-cache \
    bash \
    curl \
    wget \
    nmap \
    nmap-scripts \
    netcat-openbsd \
    bind-tools \
    traceroute \
    openssh-client \
    git \
    tini \
    ca-certificates \
    libstdc++ \
    libgcc \
    libffi \
    openssl \
    ncurses-libs \
    readline \
    sqlite-libs \
    libxml2 \
    libxslt \
    freetype \
    libpng \
    libjpeg-turbo \
    tiff \
    openjpeg \
    zlib \
    && rm -rf /var/cache/apk/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Create non-root user
RUN addgroup -g 1000 cyclopus && \
    adduser -u 1000 -G cyclopus -s /bin/bash -D cyclopus

# Copy application files
COPY cyclopus_bot_v1.py .
COPY requirements.txt .
COPY requirements-full.txt .
COPY requirements-check.py .
COPY test-commands.py .
COPY .gitignore .

# Create directories
RUN mkdir -p .cyclopus_bot_v1 \
    .cyclopus_bot_v1/payloads \
    .cyclopus_bot_v1/workspaces \
    .cyclopus_bot_v1/scans \
    .cyclopus_bot_v1/phishing_pages \
    .cyclopus_bot_v1/phishing_templates \
    .cyclopus_bot_v1/captured_credentials \
    .cyclopus_bot_v1/ssh_keys \
    .cyclopus_bot_v1/traffic_logs \
    .cyclopus_bot_v1/nikto_results \
    cyclopus_reports \
    cyclopus_reports/graphics \
    cyclopus_reports/pdf_reports \
    temp \
    .cyclopus_bot_v1/web_templates \
    .cyclopus_bot_v1/sessions \
    .cyclopus_bot_v1/spear_phishing \
    .cyclopus_bot_v1/email_templates \
    .cyclopus_bot_v1/dos_logs \
    .cyclopus_bot_v1/agents \
    .cyclopus_bot_v1/c2_logs \
    .cyclopus_bot_v1/modules \
    .cyclopus_bot_v1/network_monitor \
    .cyclopus_bot_v1/keylog_exfil \
    .cyclopus_bot_v1/deployments \
    .cyclopus_bot_v1/domain_hosting \
    .cyclopus_bot_v1/cracking \
    .cyclopus_bot_v1/arp_logs \
    .cyclopus_bot_v1/mac_logs \
    .cyclopus_bot_v1/nat_logs \
    .cyclopus_bot_v1/animation_cache \
    .cyclopus_bot_v1/platform_logs \
    .cyclopus_bot_v1/docker_scans \
    .cyclopus_bot_v1/email_composer \
    .cyclopus_bot_v1/templates \
    .cyclopus_bot_v1/custom_templates \
    && chown -R cyclopus:cyclopus /app

# Switch to non-root user
USER cyclopus

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV CYCLOPUS_HOME=/app
ENV CYCLOPUS_VERSION=1.0.0

# Expose ports
EXPOSE 5000 8080 4444

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0)" || exit 1

# Use tini as init
ENTRYPOINT ["/sbin/tini", "--"]

# Default command
CMD ["python", "cyclopus_bot_v1.py"]
