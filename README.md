# Arquitectura-Micro-Servicios
Repositorio de la tarea 2

## Sistema de Procesamiento de Comentarios

Antes de ejecutar el código asegurate de instalar los prerrequisitos del sistema ejecutando:
> sudo pip install -r requirements.txt  

Los paquetes que se instalarán son los siguientes:

Paquete 		| Versión | Descripción
----------------|---------|----------------------------------------------------------------------------------
Flask   		| 0.10.1  | Micro framework de desarrollo
requests		| 2.12.4  | API interna utilizada en Flask para trabajar con las peticiones hacia el servidor
tweepy          | 3.6.0   | API para trabajar con twitter
Flask-SQLAlchemy| 2.3.2   | modulo para mapeo objeto-relacional 
mysqlclient		| 1.3.12  | conector a mysql
textblob		| 0.15.1  | API analizador de sentimientos

*__Nota__: También puedes instalar éstos prerrequisitos manualmente ejecutando los siguientes comandos*   
> sudo pip install Flask==0.10.1
> sudo pip install requests==2.12.4
> sudo pip install tweepy==3.6.0
> sudo pip install Flask-SQLAlchemy==2.3.2
> sudo pip install mysqlclient==1.3.12
> sudo pip install textblob=0.15.1

Una vez instalados los prerrequisitos es momento de ejcutar el sistema siguiendo los siguientes pasos:  
1. Ejecutar el servicio:  
   > python micro_servicios/sv_information.py 
   > python micro_servicios/sv_sentiment_analysis.py 
   > python micro_servicios/sv_twitter.py  
1. Ejecutar el GUI:  
   > python gui.py  
1. Abrir el navegador
1. Acceder a la url del sistema:
   > http://localhost:8000/ - página de inicio!
