from flask import json
from flask import Blueprint

from termcolor import colored

from src.run import app

excepcionesBluePrint = Blueprint('excepciones', 'excepciones', url_prefix='/excepciones')

class ExcepcionesController():

	@excepcionesBluePrint.app_errorhandler(Exception)
	def excepcion(exception):
		print(colored("ExcepcionesController: excepcion();", 'green'))
		print(colored("Error: {}. Tipo: {}".format(exception, type(exception)), 'red'))
		print(exception.args)
		return app.response_class(
			response=json.dumps(exception.args[1], sort_keys=False),
			status=exception.args[1]["codigo"],
			mimetype='application/json'
		)

app.register_blueprint(excepcionesBluePrint)