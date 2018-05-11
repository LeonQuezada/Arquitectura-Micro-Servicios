# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: sv_tweets.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Yair,Luis,Daniel & Leon
# Version: 1.0 Mayo 2018
# Descripción:
#
#   Este archivo crea un servico para obtener y almacenar los cometarios de https://twitter.com/
#   
#   
#
#                                        sv_tweets.py
#           +-----------------------+-------------------------+----------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades           |
#           +-----------------------+-------------------------+----------------------------+
#           |                       |  - Obtner y guardar     | - Utiliza el API de        |
#           |    obtener y guarda   | comentarios de twitter  |   Twitter                  | 
#           |    comentarios        |       en una bd         | - Obtine y guarda en una db|
#           |     en Twitter        |                         |   los tweets y comentarios |
#           |                       |                         |   mas recientes de la serie|
#           |                       |                         |   o pelicula en cuestión.  |
#           |                       |                         |                            |
#           +-----------------------+-------------------------+----------------------------+
#
#   Ejemplo de gurdar : Abrir navegador e ingresar a http://localhost:8083/api/v1/tweets/set?t=matrix movie
#
import os
import sys
from flask import Flask, abort, render_template, request
import urllib, json
import settings
#import conexion
import tweepy
import json
from tweepy import OAuthHandler



app = Flask (__name__)

@app.route("/api/v1/tweets/get", methods=['GET'])
def set_information():
        #autentifica el sistema en twitter
        auth = OAuthHandler(settings.CONSUMER_KEY,settings.CONSUMER_SECRET)
        auth.set_access_token(settings.ACCESS_TOKEN,settings.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        #obtener variable del url
        title = request.args.get("t")
        api = tweepy.API(auth)
        #Numero de tweets que se van a obtener
        max_tweets=100
        #variable para almacenar los comentarios
        tweets_json=[]
        if title is not None:
            #obtener los tweets
            searched_tweets = [status._json for status in tweepy.Cursor(api.search,q=title,count=100,tweet_mode='extended',lang='es').items(max_tweets)]
            #recorrer los tweets
            for tweet in searched_tweets:
                    tweets_json.append({'text':tweet['full_text']})
            #convertir a json 
            json_api=json.dumps(tweets_json,ensure_ascii=False)
            return (json_api, 200)       
        else:
            abort(400)


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8083))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
app.run(host='0.0.0.0', port=port)
