FROM python:3.8-alpine

# Instalar dependências
RUN pip install mysql-connector

# Copiar o script Python
COPY script.py /app/script.py

# Definir o diretório de trabalho
WORKDIR /app

# Rodar o script Python
CMD ["python", "script.py"]
