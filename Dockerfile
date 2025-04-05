# Usar a imagem oficial Python como base
FROM python:3.10-slim

# Definir diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar as dependências
RUN pip install --no-cache-dir pytest

# Expor a porta caso seja necessário no futuro
# EXPOSE 8000

# Comando para executar a aplicação
CMD ["python", "app.py"]
