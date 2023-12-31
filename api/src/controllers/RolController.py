from src.app import app
from termcolor import colored
from flask import jsonify
from flask import json
from flask import Blueprint

from src.services.RolService import RolService

rolBluePrint = Blueprint('rol', 'rol', url_prefix='/rol')

class RolController():

	@rolBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("RolController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(RolService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@rolBluePrint.route('/<int:codigo>', methods=['GET'])
	def obtenerSegunCodigo(codigo):
		print(colored("RolController: obtenerSegunCodigo(); {}".format(codigo), 'green'))
		return app.response_class(
			response = json.dumps(RolService().obtenerSegunCodigo(codigo),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(rolBluePrint)