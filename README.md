# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

[![Build Status](https://travis-ci.org/manuelalonsobraojos/cc-proyecto.svg?branch=master)](https://travis-ci.org/manuelalonsobraojos/cc-proyecto) [![CircleCI](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto.svg?style=svg)](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto) 

### Introducción

Desde 2015, se pueden utilizar en Telegram los llamados bots, los cuales son programas que nos permiten conseguir funciones distintas en los chats y grupos que tengamos en Telegram. El desarrollo de estos de bots es totalmente **Libre** y cualquiera puede desarrollar uno. Además, la misma aplicación explica todo lo necesario para la creación de un bot.

Para este proyecto retomaré un bot de creación propia que muestre los resultados, clasificación y estadísticas de la primera división de futbol española.

La arquitectura que se desarrolló en su día fue una arquitectura monolítica y preentaba el problema de que la respuestas eran demasiado lentas debido a que el mismo bot además de atender peticiones debía de actualizar los datos. Ante esta situación se plantea rehacer la arquitectura, basandose en una arquitectura de microsservicios.

### Arquitectura

Para la realización de este proyecto se va utilizar una arquitectura basada en microservicios, ya que permite modularizar las distintas partes de la aplicación y desplegarlas por separado.

El proyecto se desarrollará en python y contará con dos microservicios desarrollados con el microframework escrito en python **flask**, cada uno de los microservicios contará con un sistema de almacenamiento de datos, en concreto  **postgresql**. Cada microservicio será un entidad independiente, dichas entidades serán:
* **resultado**: esta entidad representa un resultado de una de las dos categorías y en una determinada jornada.
* **Clasificación**: Esta entidad representa las estadísticas de un equipo en la tabla clasificatoria.

El bot se comunicará con estos dos microservicios a traves de **Netflix Zuul**, un edge service que va a permitir enrutar y filtrar las peticiones que realiza el bot de manera dinámica. 

**Zuul** actuará como un punto de entrada a a los microservicios, es decir, se encargará de su enrutar hacia el microservicio que se quiera consumir.

La decisión de utilizar tecnologías como zuul viene dada por la sencilla configuración que requiere esta herramientas y su sencilla implementación, ya que se encuentra perfectamente integrado con el framework de java **Spring Boot**.

Como sistema de almacenamiento de datos se utilizará **postgresql**, puesto además de que es OpenSource, tiene un alto rendimiento manejando un gran volumen de datos.

La principal ventaja que se obtiene con esta arquitectura de microservicios es una mayor rapidez en las consultas y la fiabilidad de que en caso de que una de las dos bases de datos tenga algun problema el bot seguirá funcionando mostrando información de la base de datos que esté operativa.

![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/arquitectura_n.png)


### Lenguajes y Herramientas

* **Lenguajes**: Para el desarrollo de los microservicios se utilizará **Python3** y el microframework Flask con el que desarrollar las API Rest con las que comunicarse con el microservicio.
* **Almacenamiento**: para el almacenamiento se utilizaran bases de datos **postgresql**. Para la utilización de postgresql en python se utilizará el ORM **SQLAlchemy**.
* **Entornos vituales**: para la creación de entornos virtuales se utilzará el entorno virtual de python **virtualenv**.
* **Enrutamiento**: para el enrutamiento se utilizará el API GetAway **Netflix Zuul**, que estaran desarrollados con **Java** y el framework **Spring Boot**.
* **Logs**: Para tener realizar un registro de los logs ante posibles eventos producidos en los microservicios, de utilizará la libreria de python **logging**.

### Herramientas de construcción
Como herramienta de construcción para el microservicio he utilizado un archivo Makefile y un archivo setup.py para la instalación de las dependencias. Con este archivo Makefile se podrá realizar la instalación de dependencias necesarias para la ejecución del microservicio, ejecutar los test y ejecutar el microservicio. Todo ello con las siguientes ordenes respectivamente:
* make install: para la instalación de las dependencias.
* make test: para la ejecución de los test.
* make ejecutar: para la ejecución del microserivicio

Para la realización de los test se ha utilizado la libreria unittest, para su ejecución se ha incluido un objetivo make test dentro del archivo Makefile:
```
buildtool: Makefile
```

### Integración Continua
Como sistema de integración continua se han utilizado **Travis-CI** y **CircleCi**:
* **Travis-Ci**: Se encarga de ejecutar los test unitarios creados para el proyecto. Estos test son comprobados para distintas dversiones de python, desde la *3.4* hasta la *3.7.4*. Para la configuración se ha creado un archivo llamado [.travis.yml](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/.travis.yml)
* **CircleCi**: se encarga de de ejecutar los test unitarios creados para el proyecto. Estos son comprobados para la versión 3.7.4 de python. Para la configruación se ha creado un archivo [config.yml](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/.circleci/config.yml) y que se debe de encontrar dentros de un directorio de nombre [.circleci](https://github.com/manuelalonsobraojos/cc-proyecto/tree/master/.circleci) para que circleci pueda encontrar el archivod e configuración.

### Microservicio y tests
Para la ejecución del microservicio se debe de ejecutar el comando ```make ejecutar```, una vez ejecutado se desplegará el microservicio el cual tiene varias rutas implementadas:
```
http://localhost:5000/                      # Se recolectan los datos
http://localhost:5000/insert                # Se inserta resultado por defecto
http://localhost:5000/result/<id>           # Se muestra un resultado por su id 
http://localhost:5000/resultlocal/<local>   # Se muestra un resultado por su equipo local
http://localhost:5000/resultlocal/<visit>   # Se muestra un resultado por su equipo visitante
http://localhost:5000/resultall             # Se muestran todos los resultados de la jornada
```

Para la ejecución de los test implementados para distintas comprobaciones, se debe de ejecutar el comando ```make test```.

### Contenedores
Para subir el proyecto a docker primero deberemos de crear y configurar el contenedor de docker. Para ello crearemos en nuestro repositorio un archivo Dockerfile, que contendrá todas las tareas de construcción del contenedor. En el archivo dockerfile se hará referencia a un script docker_run que instalará todo lo necesario para preparar el contenedor y llamará al archivo Makefile que instalará todos los requisitos que necesita el microservicio.

En los siguientes en enlaces podemos encontrar el [Dockerfile](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/Dockerfile) y el [docker_run](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docker_run). Para la creación del contenedor se ha utilizado una contenedor base de **ubuntu 16.04**, puesto que es el sistema operativo en el que se ha estado trabajando y se sabe que el microservicio funciona debidamente.
Una vez generada la imagen, es subida a dockerhub.
```
contenedor: https://hub.docker.com/repository/docker/manuelalonsobraojos/cc-proyecto/tags?page=1
```

### Arquitectura de por capas

La arquitectura de este microservicio está compuesta por tres capas:
* **Capa de servicio**: es la capa que se encarga de dar acceso al microservicio y se encarga de intermediar la comuniacación entre *la capa de presentación* (corresponde con la interfaz que interactua con el usuario) y la **capa de negocio**. [app.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/bot/app.py)
* **Capa de lógica de negocio**: es la capa que contiene una serie subrutinas que regulan la acciones de los usuarios e interactuan con las entidades de negocio. [resultservice.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/bot/service/ResultService.py)
* **Capa de base de datos**: contiene las entidades que interactuan con la base de daos. [result.py](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/bot/model/Result.py)