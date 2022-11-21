import flask
from termcolor import colored

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from src.Config import Config

print("app.py");
app = flask.Flask(__name__)	
Config().iniciarConApp(app);
#Configurado desde ENV
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:0C3v8ea0@192.168.56.101/tareadb'
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .routes import *
#import routes;

#app.run(host='localhost', port=3000)