# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests
import os
import sys
from flask import Flask, abort, render_template, request
import settings



app = Flask (__name__)


@app.route("/api/v1/sentiment_analysis/get", methods=['GET'])
def get_sentiment_analysis():

	text = request.args.get("t")
	url = "http://api.meaningcloud.com/sentiment-2.1"
	payload = "key="+settings.KEY_VALUE+"&lang=es&txt="+text
	headers = {'content-type': 'application/x-www-form-urlencoded'}
	response = requests.request("POST", url, data=payload, headers=headers,timeout=2)
	return (response.text, 200) 


if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8082))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
app.run(host='0.0.0.0', port=port)