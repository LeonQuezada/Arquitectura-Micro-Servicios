# -*- coding: utf-8 -*-
#!/usr/bin/env python

import requests
import os
import sys
from flask import Flask, abort, render_template, request
import settings
from textblob import TextBlob
import json



app = Flask (__name__)


@app.route("/api/v1/sentiment_analysis/get", methods=['GET'])
def analysis():
	text = request.args.get("t")
	analysis_json=[]
	analysis = TextBlob(text)
	    # set sentiment
	if analysis.sentiment.polarity > 0:
		#return 'positive'
		analysis_json.append({'polaridad':'positive'})
	elif analysis.sentiment.polarity == 0:
		#return 'neutral'
		analysis_json.append({'polaridad':'neutral'})
	else:
		#return 'negative'
		analysis_json.append({'polaridad':'negative'})
	json_api=json.dumps(analysis_json,ensure_ascii=False)
	return (json_api, 200)



if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el servicio
    port = int(os.environ.get('PORT', 8082))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
app.run(host='0.0.0.0', port=port)