# Imagen base de Python (estable y compatible)
FROM python:3.11.9

# Establecer directorio de trabajo
WORKDIR /app

# Copiar solo los archivos necesarios primero (mejora tiempos de build)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer puerto por defecto de Dash
EXPOSE 8050

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
