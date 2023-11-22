import os

from src.app import app
from src.db import db
from src.ma import ma

from src.utils.Config import Config
from src.utils.ArchivoUtils import ArchivoUtils

print("run.py")

#app = flask.Flask(__name__)
Config().iniciarConApp(app)
ArchivoUtils().verificarCarpetas(app)

#db = SQLAlchemy(app)
db.init_app(app)

#ma = Marshmallow(app)
ma.init_app(app)

#Importar archivos de Controllers
from src.routes import *

#Solo para ejecutar en PyCharm
if __name__ == "__main__":
  print("run.py: Iniciar en PyCharm")
  host = os.environ.get("FLASK_RUN_HOST")
  port = os.environ.get("FLASK_RUN_PORT")
  print(colored("run.py: Iniciar app en {}:{}".format(host, port), 'yellow'))
  app.run(host=host, port=port)
  #app.run()
