import flask
import os
from termcolor import colored

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from src.utils.Config import Config
from src.utils.ArchivoUtils import ArchivoUtils

print("app.py")

app = flask.Flask(__name__)
Config().iniciarConApp(app)
ArchivoUtils().verificarCarpetas(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

#Importar archivos de Controllers
from src.routes import *
#Solo para ejecutar en PyCharm
if __name__ == "__main__":
  print("app.py: Iniciar en PyCharm")
  host = os.environ.get("FLASK_RUN_HOST")
  port = os.environ.get("FLASK_RUN_PORT")
  print(colored("app.py: Iniciar app en {}:{}".format(host, port), 'yellow'))
  app.run(host=host, port=port)
  #app.run()
