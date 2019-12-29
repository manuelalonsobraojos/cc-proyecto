# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

[![Build Status](https://travis-ci.org/manuelalonsobraojos/cc-proyecto.svg?branch=master)](https://travis-ci.org/manuelalonsobraojos/cc-proyecto) [![CircleCI](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto.svg?style=svg)](https://circleci.com/gh/manuelalonsobraojos/cc-proyecto) 

En el siguiente enlace podemos consultar la documentación correspondiente a la primera entrega:

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

### Evaluación de prestaciones

```
Prestaciones: https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/fichero_taurus.yml
```

La evaluación de las prestaciones del microservicio creado, se ha realizado con la herramienta [Taurus](https://gettaurus.org/). El objetivo principal es que el microsevicio creado de `resultados`soporte 1000 peticiones por segundo con 10 usuarios concurrentes.

Tras realizar un análisis de las prestaciones se puede observar como el microservicio durante un espacio de tiempo es capaz de soportar más de 1000 peticiones por segundo.
 
 ![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/captura_prueba_2.PNG)

En el siguiente enlace podemos ver las distinas pruebas realizadas junto con las modificaciones llevadas a cabo para el análisis de las prestaciones y la consecución de unas mejores prestaciones: [análisis de prestaciones](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/docs/prestaciones.md).