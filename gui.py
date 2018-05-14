# -*- coding: utf-8 -*-
# !/usr/bin/env python
# ----------------------------------------------------------------------------------------------------------------
# Archivo: gui.py
# Tarea: 2 Arquitecturas Micro Servicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Autores(es) de version 1.4:Yair,Luis,Daniel & Leon
# Version: 1.3 mayo 2018
# Descripción:
#
#   Este archivo define la interfaz gráfica del usuario. Recibe dos parámetros que posteriormente son enviados
#   a servicios que la interfaz utiliza.
#   
#   
#
#                                             gui.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Porporcionar la in-  | - Consume servicios    |
#           |          GUI          |    terfaz gráfica con la|   para proporcionar    |
#           |                       |    que el usuario hará  |   información al       |
#           |                       |    uso del sistema.     |   usuario.             |
#           +-----------------------+-------------------------+------------------------+
#
import os
from flask import Flask, render_template, request
import urllib, json
import requests
from flask.ext.sqlalchemy import SQLAlchemy #SQLAlchemy es un ORM=Object-relational mapping
import json

app = Flask(__name__)

#formato de la conexion para base de datos al ORM
#mysql://username:password@localhost/db_name
#Otra opción
#postgresql://username:password@localhost/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sentiment_analysis:sentiment_analysis@localhost/sentiment_analysis'

#Linea para eviar un warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#conexion a la base de datos
db = SQLAlchemy(app)

#Creando la base de datos con un orm
class sentiment_analysis_db(db.Model):
    #Identificador entero
    id = db.Column(db.Integer, primary_key=True)
    #tweets string que guarda los comentario optenido
    tweets = db.Column(db.String(500),unique=True)
    #sentiment string que guarda la polaridad
    #negativo
    #Neutral
    #Positivo 
    sentiment = db.Column(db.String(20))
    #nombre de la pelicula
    titulo = db.Column(db.String(100))

    #Constructor del objeto
    def __init__(self,tweets,sentiment,titulo):
        self.tweets = tweets
        self.sentiment = sentiment
        self.titulo = titulo

    #Retorno para cuando se impime el objeto
    def __repr__(self):
        return '<sentiment_analysis %r>' % self.tweets

#crea las tablas nesesarias
db.create_all()



@app.route("/")
def index():
    # Método que muestra el index del GUI
    return render_template("index.html")


@app.route("/information", methods=['GET'])
def sentiment_analysis():
    # Se obtienen los parámetros que nos permitirán realizar la consulta
    title = request.args.get("t")
    if len(title) is not 0:


        # La siguiente url es para un servicio local
        url_omdb = urllib.urlopen("http://127.0.0.1:8081/api/v1/information?t=" + title)
        # Se lee la respuesta de OMDB
        json_omdb = url_omdb.read()
        # Se convierte en un JSON la respuesta leída
        omdb = json.loads(json_omdb)

        #si ya hay un análisis guardado ya no lo have otra vez
        query = sentiment_analysis_db.query.filter_by(titulo=title).first() 
        if query is None:
            #Traer los tweets con su api
            url_tweets = urllib.urlopen("http://localhost:8083/api/v1/tweets/get?t=" + title)
            # Se lee la respuesta de twitter
            json_tweets = url_tweets.read()
            # Se convierte en un JSON la respuesta leída
            #tweets=json.dumps(json_tweets,ensure_ascii=False)
            tweets  = json.loads(json_tweets)
            #iterar los elementos
            for tweet in tweets:
                #codificacion utf8 para cada comentario
                tweet_utf8=tweet['text'].encode('ascii', 'ignore').decode('utf-8')
                #Descaertar repetidos
                query = sentiment_analysis_db.query.filter_by(tweets=tweet_utf8,titulo=title).first()
                if query is None:
                    #api que analiza
                    url_analysis = urllib.urlopen("http://localhost:8082/api/v1/sentiment_analysis/get?t=" + str(tweet_utf8))
                    #leer los coemntarios
                    json_analysis = url_analysis.read()
                    #cargar los coemtarios
                    analysis  = json.loads(json_analysis)
                    #usar el ORM para guardar los datos
                    sadb = sentiment_analysis_db(tweet['text'].encode('ascii', 'ignore').decode('utf-8'),analysis[0]['polaridad'],title)
                    #agregar los elementos a la base de datos
                    db.session.add(sadb)
                    #guardar los cambios
                    db.session.commit()
        #traer los coemtarios de la base de datos
        query = sentiment_analysis_db.query.filter_by(titulo=title).all()
        neutral=0#contador de comentarios neutral
        negative=0#contador de comentarios negative
        positive=0#contador de comentarios positive

        #iterar los cometarios
        for tweet in query:
            #si el comentario es neutral
            if tweet.sentiment == 'neutral':
                #incrementar
                neutral+= 1
            #si el comentario es negative
            if tweet.sentiment == 'negative':
                #incrementar
                negative+= 1
            #si el comentario es positive
            if tweet.sentiment == 'positive':
                #incrementar
                positive+= 1
        #suma de todos los comentarios
        suma=positive+neutral+negative
        #calculo de porsentaje
        positive=float("{0:.2f}".format((float(positive)/float(suma))*100))
        neutral=float("{0:.2f}".format((float(neutral)/float(suma))*100))
        negative=float("{0:.2f}".format((float(negative)/float(suma))*100))

        # Se llena el JSON que se enviará a la interfaz gráfica para mostrársela al usuario
        json_result = {'omdb': omdb,'neutral':neutral,'negative':negative,'positive':positive}
        # Se regresa el template de la interfaz gráfica predefinido así como los datos que deberá cargar

        return render_template("status.html", result=json_result)
    else:
        return render_template("error-500.html")


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el Sistema de Procesamiento de Comentarios (SPC).
    port = int(os.environ.get('PORT', 8000))
    # Se habilita el modo debug para visualizar errores
    app.debug = True
    # Se ejecuta el GUI con un host definido cómo '0.0.0.0' para que pueda ser accedido desde cualquier IP
    app.run(host='0.0.0.0', port=port)
