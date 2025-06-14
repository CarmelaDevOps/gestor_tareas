# Utiliza una imagen oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY main.py ./
COPY tareas.txt ./
COPY requirements.txt ./

# Crea la carpeta para logs dentro del contenedor
RUN mkdir -p logs

# Instala las dependencias (aunque por ahora no tenemos ninguna)
RUN pip install --no-cache-dir -r requirements.txt || true

# Comando que se ejecuta al iniciar el contenedor
CMD ["python", "main.py"]
