
## Análisis de prestaciones
### Creación de fichero Taurus

Lo primero que se debe de hacer para la medición de las prestaciones es crear un archivo `yaml` el cual contendrá el siguiente código:
```
execution:
- concurrency: 10
  ramp-up: 10s
  hold-for: 55s
  scenario: app-test

scenarios:
  app-test:
    requests:
    - url: 'http://127.0.0.1:8000/result/getall'
      method: GET

    - url: 'http://127.0.0.1:8000/result/get/1'
      method: GET

    - url: 'http://127.0.0.1:8000/result/local/valencia'
      method: GET
```
En este archivo se especifica que se quieren 10 usuarios concurrentes, lo cuales tardaran 10 segundos en conectarse todos y permanecerán 55 segundos conectados. Además se especifican las rutas del servidor a las que se realizaran las peticiones.

### Primera prueba

En un primer momento se procedío a realizar un análisis de las prestaciones del microservicio ejecutando este con el comando ```python3 bot/app.py```. Tras terminar el análisis se pudo observar que el número de peticiones soportardo era muy bajo tal y como podemos observar en la siguiente imagen.

![img]()

### Segunda prueba 

Tras ver el resultado de la primera prueba se procedió a realizar dos cambios, el primer cambio fue la imcoportación de un sistema de caché en el microservicio, mediante la biblioteca [flask-caching](https://flask-caching.readthedocs.io/en/latest/). El segundo cambio que se realizó fue la utilización de `gunicorn` para la ejecución del microservicio con la siguiente línea:
```
 gunicorn -w 5 app:app
 ```
 Con este comando se establecen 5 workers con los que se conseguirá un mejor rendimiento del microservicio. Tras realizar un análisis de las prestaciones se puede observar una mejoría y como el microservicio durante un espacio de tiempo era capaz de soportar más de 1000 peticiones por segundo.
 
 ![img]()