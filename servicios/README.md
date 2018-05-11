# Servicios
En esta carpeta se define el servicio utilizado en la tarea 2 dentro del Sistema de Procesamiento de Comentarios (SPC). La especificación del servicio del Procesador de Comentarios de IMDb se realizó utilizando blueprint de Apiary.
La especificación es la siguiente:

## Procesador de Comentarios de IMDb
  
FORMAT: 1A  
HOST: http://localhost:8081

## Information Service [/api/v1/information{?t}]

+ Parameters
    + t - Corresponde al título de la película o serie de Netflix.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "Title": "Some text",
            "Year": "Some text", 
            "Rated": "Some text",
            "Released": "Some text",
            "Runtime": "Some text",
            "Genre": "Some text",
            "Director": "Some text",
            "Writer": "Some text",
            "Actors": "Some text",
            "Plot": "Some text",
            "Language": "Some text",
            "Country": "Some text",
            "Awards": "Some text.",
            "Poster": "Some text",
            "Metascore": "Some text",
            "imdbRating": "Some text",
            "imdbVotes": "Some text",
            "imdbID": "Some text",
            "Type": "Some text",
            "totalSeasons": "Some text",
            "Response": "Some text"
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Abrir el navegador
1. Ingresar a http://localhost:8081/api/v1/information?t=Stranger+Things

















## sentiment analysis API
  
FORMAT: 1A  
HOST: http://localhost:8082

## Information Service [/api/v1/sentiment_analysis/get{?text}]

+ Parameters
    + text - Corresponde al coemtario a analizar.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "text": "Some text"
        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Abrir el navegador
1. Ingresar a http://localhost:8082/api/v1/sentiment_analysis/get?t=Stranger+Things




















## Procesador para optener de tweets de twitter
  
FORMAT: 1A  
HOST: http://localhost:8083

## optener de tweets [/api/v1/information{?t}]

+ Parameters
    + t - Corresponde al título de la película o serie de Netflix.

### Get Information [GET]

+ Response 200 (application/json)

        { 
            "Title": "Some text",

        }

+ Response 400 (text)

        {
            "title": "Bad Request"
            "message": "The browser (or proxy) sent a request that this server could not understand."
        }

Ejemplo de uso: 
1. Abrir el navegador
1. Ingresar a http://localhost:8083/api/v1/tweets/get?t=Stranger+Things
