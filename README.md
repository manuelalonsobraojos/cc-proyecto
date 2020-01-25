# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

[![Build Status](https://travis-ci.org/manuelalonsobraojos/cc-proyecto.svg?branch=master)](https://travis-ci.org/manuelalonsobraojos/cc-proyecto) [![CircleCI](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto.svg?style=svg)](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto) 

En el siguiente enlace podemos consultar la documentación correspondiente a la primera entrega en la que se especifica la arquitectura:

![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/arquitectura.png)

[primera entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme1.md)

En el siguiente enlace podemos consultar la documentación correspondiente a la segunda entrega:

[segunda entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme2.md)

La herramienta de construcción utilizada y desarrollada en la segunda entrega fue la siguiente:
```
buildtool: Makefile
```

En el siguiente enlace podemos consultar la documentación correspondiente a la tercera entrega:

[tercera entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme3.md)

Cada vez que se realice un push al repositorio de GitHub se realizará la construcción de la imagen en DockerHub.
```
Contenedor: https://hub.docker.com/r/manuelalonsobraojos/cc-proyecto
```

En el siguiente enlace podemos consultar la documentación correspondiente a la cuarta entrega:

[cuarta entrega](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme3.md)


El archivo el que se establece la configuración para realizar un análisis de lal prestaciones es el siguiente:
```
Prestaciones: fichero_taurus.yml
```

### Implementación del microservicio **Clasificacion**:

Para la implementación de este microservicio se ha utilizado el Framework de Python [Sanic](https://sanic.readthedocs.io/en/latest/), que ha diferencia del microframework flask, es asíncrono.

La arquitectura de este microservicio, al igual que la del microservicio **Result** está compuesta por tres capas:
* **Capa de servicio**: es la capa que se encarga de dar acceso al microservicio y se encarga de intermediar la comuniacación entre *la capa de presentación* (corresponde con la interfaz que interactua con el usuario) y la **capa de negocio**. [app.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/clasificacion/clasificacionRest.py)
* **Capa de lógica de negocio**: es la capa que contiene una serie de subrutinas que regulan la acciones de los usuarios e interactuan con las entidades de negocio. [resultservice.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/clasificacion/service/ClasificacionService.py)
* **Capa de base de datos**: contiene las entidades que interactuan con la base de daos. [result.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/clasificacion/model/Clasificacion.py).

Además de la implementación del segundo microservicio, se ha llevado a cabo la implementación de un **Gateway**, utilizando [nginx](https://www.nginx.com/). La configuración de este gateway se puede ver en el archivo [nginx.conf](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/nginx.conf).

### Provisionamiento de máquinas virtuales

Como último paso en el desarrollo de este proyecto se ha procedido al despliegue en una máquina virtual de los dos microservicios implementados y del Gateway. El despliegue en una máquina virtual se ha llevado a cabo en la plataforma [Google Cloud](https://cloud.google.com/).

Para la configuración y el aprovisionamiento de la máquina virtual se ha utilizado [Vagrant](https://www.vagrantup.com/) y [Ansible](https://www.ansible.com/).

La documentacion de como se ha llevado a cabo la creación y aprovisionamiento de la máquina virtual viene detalladado en el siguiente enlace: [Documentación](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/Readme5.md)
