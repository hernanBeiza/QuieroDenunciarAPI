from flask_cors import CORS
import os
from dotenv import load_dotenv, find_dotenv, dotenv_values

from termcolor import colored
from distutils.util import strtobool

class Config:

	@staticmethod
	def iniciarConApp(app):
		print("Config: iniciarConApp")
		#Configuracion de Flask
		print(colored("Config: Iniciar configuración de Flask", 'yellow'))
		app.config['JSON_SORT_KEYS'] = False
		#Variables de ambiente
		environment = os.environ.get("FLASK_ENV")
		print(colored("Config: Ambiente: {}".format(environment), 'yellow'))
		archivoENV = ".env.{}".format(environment)
		print(colored("Config: Archivo: {}".format(archivoENV), 'yellow'))
		encontradoENV = find_dotenv(archivoENV)
		if encontradoENV:
			print(colored("Config: Archivo: {} encontrado".format(archivoENV), 'green'))
			load_dotenv(encontradoENV)
			config = dotenv_values(encontradoENV)
			app.config.from_mapping(config)
			print("Config: Version: {}".format(app.config["VERSION"]))
		else:
			print(colored("Config: Archivo: {} no encontrado".format(archivoENV), 'red'))
		#CORS
		CORS(app)
		#Configuración de email
		#app.config['MAIL_SERVER'] = ''
		#app.config['MAIL_PORT'] =
		#app.config['MAIL_USERNAME'] = ''
		#app.config['MAIL_PASSWORD'] = ''
		app.config['MAIL_USE_TLS'] = bool(strtobool(app.config['MAIL_USE_TLS']))
		app.config['MAIL_USE_SSL'] = bool(strtobool(app.config['MAIL_USE_SSL']))
