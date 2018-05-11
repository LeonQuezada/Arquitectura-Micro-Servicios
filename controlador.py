from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

#formato de la conexion mysql://username:password@localhost/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sentiment_analysis:sentiment_analysis@localhost/sentiment_analysis'

#Linea para eviar un warning.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#conexion a la base de datos
db = SQLAlchemy(app)



class sentiment_analysis(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	tweets = db.Column(db.String(200),unique=True)
	sentiment = db.Column(db.Integer)

	def __init__(self,tweets,sentiment):
		self.tweets = tweets
		self.sentiment = sentiment

	def __repr__(self):
		return '<sentiment_analysis %r>' % self.tweets

#crea las tablas nesesarias
db.create_all()