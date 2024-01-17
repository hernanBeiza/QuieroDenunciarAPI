from src.app import app

from termcolor import colored
from flask import jsonify
from flask import json
from flask import Blueprint

from src.services.EstadoEnvioCorreoService import EstadoEnvioCorreoService

estadoEnvioCorreoBluePrint = Blueprint('estado-envio-correo', 'estado-envio-correo', url_prefix='/estado-envio-correo')

class EstadoEnvioCorreoController():

	@estadoEnvioCorreoBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("EstadoEnvioCorreoController: obtener();", 'green'))
		return app.response_class(
			response=json.dumps(EstadoEnvioCorreoService().obtener(),sort_keys=False),
			status=200,
			mimetype='application/json'
		)

	@estadoEnvioCorreoBluePrint.route('/<int:codigoEstadoEnvioCorreo>', methods=['GET'])
	def obtenerSegunCodigo(codigoEstadoEnvioCorreo):
		print(colored("EstadoDenunciaController: obtenerSegunCodigo(); {}".format(codigoEstadoEnvioCorreo), 'green'))
		return app.response_class(
			response=json.dumps(EstadoEnvioCorreoService().obtenerSegunCodigo(codigoEstadoEnvioCorreo),sort_keys=False),
			status=200,
			mimetype='application/json'
		)
		
app.register_blueprint(estadoEnvioCorreoBluePrint)