# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

### Introducción

Desde 2015, se pueden utilizar en Telegram los llamados bots, los cuales son programas que nos permiten conseguir funciones distintas en los chats y grupos que tengamos en Telegram. El desarrollo de estos de bots es totalmente **Libre** y cualquiera puede desarrollar uno. Además, la misma aplicación explica todo lo necesario para la creación de un bot.

Para este proyecto retomaré un bot de creación propia que muestre los resultados, clasificación y estadísticas de la primera división de futbol española y de la segunda división, y que tenía el problema de que la respuestas eran demasiado lentas debido a que el mismo bot además de atender peticiones debía de actualizar los datos.

### Arquitectura

Para la realización de este proyecto se va utilizar una arquitectura basada en microservicios, ya que permite modularizar las distintas partes de la aplicación y desplegarlas por separado.

Los microservicios con los que contará el proyecto serán dos, cada uno con una base de datos independiente, y con los que se comunicará el bot para la obtención de determinados resultados, mediante el uso de una API-Rest.

Además se pretenderá de incorporar al proyecto, la novedosa herramienta **Zuul**, la cual se define como un *edge service* que va a permitir enrutar y filtrar las conexiones del bot a los distintos microservicios.

Como sistema de almacenamiento de datos se utilizará **postgresql**.

### Tecnicas a emplear

Además de la arquitectura, cabe destacar el uso de **web scraping** para la obtención de los datos que se quieren manejar.






