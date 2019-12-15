FROM ubuntu:16.04

#Creación de directorio de trabajo
RUN mkdir -p /home/cc-proyecto

#Establecimiento de directorio de trabajo
WORKDIR /home/cc-proyecto

#Copia de archivos necesarios al directorio de trabajo
COPY docker_run Makefile setup.py bot/* ./

#Permiso de Script de dependencias
RUN chmod a+x docker_run

#Ejecución de script de dependencias
RUN ./docker_run

#Ejecución de microservicio
CMD python3 bot/app.py
