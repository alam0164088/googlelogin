# -------------------------
# Stage 1: Build Environment
# -------------------------
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --prefix=/install -r requirements.txt


# -------------------------
# Stage 2: Runtime Environment
# -------------------------
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages
COPY --from=builder /install /usr/local
COPY . .

# Collect static files (optional)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "google_login_project.wsgi:application", "--bind", "0.0.0.0:8000"]
