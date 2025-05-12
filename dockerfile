FROM python:3.11-slim

# evita bytecode e habilita logs em tempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# instalar compiladores e headers para psycopg2 puro (opcional)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# copiar e instalar dependências Python
COPY requirements.txt ./
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# copiar código-fonte
COPY . .

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]