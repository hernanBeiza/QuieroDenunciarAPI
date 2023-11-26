from flask_cors import CORS
import os
from dotenv import load_dotenv, find_dotenv, dotenv_values

from termcolor import colored

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
		load_dotenv(encontradoENV)
		config = dotenv_values(encontradoENV)
		app.config.from_mapping(config)
		print("Config: Version: {}".format(app.config["VERSION"]))

		#CORS
		CORS(app)
