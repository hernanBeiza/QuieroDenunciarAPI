from src.app import app
from termcolor import colored
from flask import jsonify
from flask import json
from flask import Blueprint

from src.services.ComunaService import ComunaService

comunaBluePrint = Blueprint('comuna', 'comuna', url_prefix='/comuna')

class ComunaController():

	@comunaBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("TipoPersonaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(ComunaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@comunaBluePrint.route('/<int:idComuna>', methods=['GET'])
	def obtenerSegunCodigo(idComuna):
		print(colored("ComunaController: obtenerSegunCodigo(); {}".format(idComuna), 'green'))
		return app.response_class(
			response = json.dumps(ComunaService().obtenerSegunCodigo(idComuna),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
	@comunaBluePrint.route('/provincia/<int:idProvincia>', methods=['GET'])
	def obtenerSegunIdProvincia(idProvincia):
		print(colored("ComunaController: obtenerSegunIdProvincia(); {}".format(idProvincia), 'green'))
		return app.response_class(
			response = json.dumps(ComunaService().obtenerSegunIdProvincia(idProvincia),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
app.register_blueprint(comunaBluePrint)