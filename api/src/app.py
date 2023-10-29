import flask

from termcolor import colored

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from src.Config import Config
from src.ArchivoUtils import ArchivoUtils

print("app.py");
app = flask.Flask(__name__)
Config().iniciarConApp(app);
ArchivoUtils().verificarCarpetas(app);
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .routes import *
#import routes;

#app.run(host='localhost', port=3000)