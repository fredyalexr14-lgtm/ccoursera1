# Imagen base oficial de Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos los archivos de la aplicación
COPY . .

# Crear usuario no root para mayor seguridad
RUN useradd -m appuser
USER appuser

# Exponer el puerto de la aplicación
EXPOSE 8080

# Comando de inicio
CMD ["python", "app.py"]

