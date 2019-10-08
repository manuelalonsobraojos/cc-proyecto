# cc-proyecto
Repositorio para el proyecto de la asignatura Cloud Computing

### Introducción

Desde 2015, se pueden utilizar en Telegram los llamados bots, los cuales son programas que nos permiten conseguir funciones distintas en los chats y grupos que tengamos en Telegram. El desarrollo de estos de bots es totalmente **Libre** y cualquiera puede desarrollar uno. Además, la misma aplicación explica todo lo necesario para la creación de un bot.

Para este proyecto retomaré un bot de creación propia que muestre los resultados, clasificación y estadísticas de la primera división de futbol española y de la segunda división, y que tenía el problema de que la respuestas eran demasiado lentas debido a que el mismo bot además de atender peticiones debía de actualizar los datos.

### Arquitectura

Para la realización de este proyecto se va utilizar una arquitectura basada en microservicios, ya que permite modularizar las distintas partes de la aplicación y desplegarlas por separado.

El proyecto se desarrollará en python y contará con dos microservicios desarrollados con el microframework escrito en python **flask**, cada uno con un sistema de almacenamiento de datos, en concreto  **postgresql**. Uno de los microservicios se encargará de la gestión de los datos correspondientes a las estadísticas de la liga de primera división y el otro microservicio se encargará de gestionar los datos correspondientes a las estadísticas de la liga de segunda división. El bot se comunicará con estos dos microservicios a traves de una API.

Además se pretenderá de incorporar al proyecto, la novedosa herramienta **Zuul**, la cual se define como un *edge service* que va a permitir enrutar y filtrar las conexiones del bot a los distintos microservicios.

Como sistema de almacenamiento de datos se utilizará **postgresql**.

### Tecnicas a emplear

Además de la arquitectura, cabe destacar el uso de **web scraping** para la obtención de los datos que se quieren manejar, que serán extraidos de la web del diario AS.






