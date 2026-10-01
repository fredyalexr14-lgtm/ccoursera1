
# Usa una imagen base oficial de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expone el puerto de la aplicación
EXPOSE 8080

# Comando de inicio
CMD ["python", "app.py"]


git add Dockerfile
git commit -m "Add Dockerfile for image build"
git push origin main

