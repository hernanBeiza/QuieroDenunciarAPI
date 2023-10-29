from flask_cors import CORS
import os
from flask_dotenv import DotEnv
from termcolor import colored

class Config:

	@staticmethod
	def iniciarConApp(app):
		#print("Config: init_app")
		#Configuracion de Flask
		print(colored("Iniciar configuración de Flash", 'yellow'))
		app.config['JSON_SORT_KEYS'] = False
		#Variables de ambiente
		environment = os.environ.get("FLASK_ENV")
		print(colored("Cargar archivo según ambiente: {}".format(environment), 'yellow'))
		env = DotEnv()
		ruta = "src/config/.env.{}".format(environment)
		print(colored("Archivo a cargar según ambiente: {}".format(ruta), 'yellow'))
		env.init_app(app, env_file=ruta, verbose_mode=True)
		#CORS
		CORS(app)
