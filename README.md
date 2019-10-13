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

Como sistema de almacenamiento de datos se utilizará **postgresql**, puesto además de que es OpenSource, tiene un alto rendimiento manejando un gran volumen de datos.

La principal ventaja que se obtiene con esta arquitectura de microservicios es una mayor rapidez en las consultas y la fiabilidad de que en caso de que una de las dos bases de datos tenga algun problema el bot seguirá funcionando mostrando información de la base de datos que haya operativa  

### Tecnicas a emplear

Además de la arquitectura, cabe destacar el uso de **web scraping** para la obtención de los datos que se quieren manejar, que serán extraidos de la web del periódico deportivo AS.







