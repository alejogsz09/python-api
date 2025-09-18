# Usa una imagen base de Python 3.7.11 
FROM python:3.7.11-slim

# Establece el directorio de trabajo dentro del contenedor donde se ejecutará
WORKDIR /python-api

# Copia el archivo de dependencias  requirements.txt
COPY requirements.txt requirements.txt

# Instala las dependencias 
RUN pip install -r requirements.txt

# Copia el resto de los archivos del proyecto 
COPY . .

# ejecuta los comandos en flask
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

