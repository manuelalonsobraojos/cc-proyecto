FROM ubuntu:16.04

#Creación de directorio de trabajo
RUN mkdir -p /home/cc-proyecto

#Copia de archivos necesarios al directorio de trabajo
COPY docker_run /home/cc-proyecto/
COPY Makefile /home/cc-proyecto/
COPY setup.py /home/cc-proyecto/
COPY /bot/. /home/cc-proyecto/bot/

#Permiso de Script de dependencias
RUN chmod a+x /home/cc-proyecto/docker_run

#Ejecución de script de dependencias
RUN cd /home/cc-proyecto && ./docker_run

#Ejecución de microservicio
CMD cd /home/cc-proyecto && cd bot && python3 app.py
