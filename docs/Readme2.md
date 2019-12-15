# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

[![Build Status](https://travis-ci.org/manuelalonsobraojos/cc-proyecto.svg?branch=master)](https://travis-ci.org/manuelalonsobraojos/cc-proyecto) [![CircleCI](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto.svg?style=svg)](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto) 

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
