# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

[![Build Status](https://travis-ci.org/manuelalonsobraojos/cc-proyecto.svg?branch=master)](https://travis-ci.org/manuelalonsobraojos/cc-proyecto) [![CircleCI](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto.svg?style=svg)](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto) 

En el siguiente enlace podemos consultar la documentación correspondiente a la primera entrega:

[primera entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/hito1.md)

En el siguiente enlace podemos consultar la documentación correspondiente a la segunda entrega:

[segunda entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/hito2.md)

La herramienta de construcción utilizada y desarrollada en la segunda entrega fue la siguiente:
```
buildtool: Makefile
```

### Microservicio y tests
Para la ejecución del microservicio se debe de ejecutar el comando ```make ejecutar```, una vez ejecutado se desplegará el microservicio el cual tiene varias rutas implementadas:
```
http://localhost:5000/result/get/<id>           # Se muestra un resultado por su id 
http://localhost:5000/result/visit/<local>   # Se muestra un resultado por su equipo local
http://localhost:5000/result/local/<visit>   # Se muestra un resultado por su equipo visitante
http://localhost:5000/result/getall             # Se muestran todos los resultados de la jornada
```

Para la ejecución de los test implementados para distintas comprobaciones, se debe de ejecutar el comando ```make test```.

### Contenedores
Para subir el proyecto a docker primero deberemos registrarnos en DockerHub, crear un repositorio y vincularlo con el repositorio de github. Para la configuración del contenedor de docker crearemos en nuestro repositorio un archivo Dockerfile, que contendrá todas las tareas de construcción del contenedor. En el archivo dockerfile se hará referencia a un script al que se le ha llamado *docker_run* que instalará todo las dependencias necesarias para preparar el contenedor..

En los siguientes en enlaces podemos encontrar el [Dockerfile](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/Dockerfile) y el script [docker_run](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docker_run). Para la creación del contenedor se ha utilizado una contenedor base de **ubuntu 16.04**. A continuación podemos ver el código del archivo dockerfile en el que se comenta lo que se quiere hacer en cada linea:
```
FROM ubuntu:16.04

#Creación de directorio de trabajo
RUN mkdir -p /home/cc-proyecto

#Se establece un directorio de trabajo
WORKDIR /home/cc-proyecto

#Copia de archivos necesarios al directorio de trabajo
COPY docker_run ./
COPY Makefile ./
COPY setup.py ./
# Se copia el contenido del directorio bot que contiene la aplicación, 
#el servicio y el modelo
COPY /bot/. ./bot/

#Permiso de Script de dependencias
RUN chmod a+x docker_run

#Ejecución de script de dependencias
RUN ./docker_run

#Ejecución de microservicio
CMD python3 bot/app.py
```

Cada vez que se realice un push al repositorio de GitHub se realizará la construcción de la imagen en DockerHub.
```
Contenedor: https://hub.docker.com/r/manuelalonsobraojos/cc-proyecto
```

### Arquitectura de por capas

La arquitectura de este microservicio está compuesta por tres capas:
* **Capa de servicio**: es la capa que se encarga de dar acceso al microservicio y se encarga de intermediar la comuniacación entre *la capa de presentación* (corresponde con la interfaz que interactua con el usuario) y la **capa de negocio**. [app.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/bot/app.py)
* **Capa de lógica de negocio**: es la capa que contiene una serie subrutinas que regulan la acciones de los usuarios e interactuan con las entidades de negocio. [resultservice.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/bot/service/ResultService.py)
* **Capa de base de datos**: contiene las entidades que interactuan con la base de daos. [result.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/bot/model/Result.py)
 
### Despliegue en Heroku

Para el despliegue en heroku se ha creado el archivo [heroku.yml](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/heroku.yml), en el que se indica la construcción y despliegue del contenedor mediante el archivo **Dockerfile**.

En el siguiente enlace se puede ver como se muestran todos los resultados de la jornada: [https://microservice-results.herokuapp.com/result/getall](https://microservice-results.herokuapp.com/result/getall)

