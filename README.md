# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

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

**Zuul** actuará como un punto de entrada a a los microservicios, es decir, se encargará de solicitar una instancia de un microservicio concreto a **Eureka** y de su enrutamiento hacia el microservicio que se quiera consumir.

**Eureka** es un servicio *Rest* que se comporta como un servidor cuyo objetivo es registrar los microservicios en tiempo de ejecución y localizar los microservicios existentes, informar de su localización y sus datos.

La decisión de utilizar tecnologías como zuul y eureka viene dada por la sencilla configuración que requieren estas herramientas y su sencilla implementación, ya que se encuentran perfectamente integrados con el framework de java **Spring Boot**.

Como sistema de almacenamiento de datos se utilizará **postgresql**, puesto además de que es OpenSource, tiene un alto rendimiento manejando un gran volumen de datos.

La principal ventaja que se obtiene con esta arquitectura de microservicios es una mayor rapidez en las consultas y la fiabilidad de que en caso de que una de las dos bases de datos tenga algun problema el bot seguirá funcionando mostrando información de la base de datos que esté operativa.

![img](https://github.com/manuelalonsobraojos/cc-proyecto/blob/master/img/arquitectura.png)

### Tecnicas a emplear

Además de la arquitectura, cabe destacar el uso de **web scraping** para la obtención de los datos que se quieren manejar, que serán extraidos de la web del periódico deportivo AS.


### Herramientas

* **Lenguajes**: Para el desarrollo de los microservicios se utilizará **Python3** y el microframework Flask con el que desarrollar las API Rest con las que comunicarse con el microservicio.
* **Almacenamiento**: para el almacenamiento se utilizaran bases de datos **postgresql**. Para la utilización de postgresql en python se utilizará la librería **psycopg2**.
* **Entornos vituales**: para la creación de entornos virtuales se utilzará el entorno virtual de python **virtualenv**.
* **Enrutamiento**: para el enrutamiento se utilizará el API GetAway **Netflix Zuul**, que estaran desarrollados con **Java** y el framework **Spring Boot**.
* **Test e integración continua**: Para el desarrollo de los test se utilizará la biblioteca de Python **pytest**. La ejecución de estos test en futuros despliegues se realizará [travis-ci](https://travis-ci.org).
* **Web Scraping**: Se utilizará la librería **BeautifulSoup** para realizar web scraping.
* **Logs**: Para tener realizar un registro de los logs ante posibles eventos producidos en los microservicios, de utilizará la libreria de python **logging**.






