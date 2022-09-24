from ..app import app;
from termcolor import colored
from flask import jsonify;
from flask import json;
from flask import Blueprint

from ..services.TipoPersonaService import TipoPersonaService

tipoPersonaBluePrint = Blueprint('tipo-persona', 'tipo-persona', url_prefix='/tipo-persona')

class TipoPersonaController():

	@tipoPersonaBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("TipoPersonaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(TipoPersonaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@tipoPersonaBluePrint.route('/<int:codigoTipoPersona>', methods=['GET'])
	def obtenerSegunCodigo(codigoTipoPersona):
		print(colored("TipoPersonaController: obtenerSegunCodigo(); {}".format(codigoTipoPersona), 'green'))
		return app.response_class(
			response = json.dumps(TipoPersonaService().obtenerSegunCodigo(codigoTipoPersona),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
app.register_blueprint(tipoPersonaBluePrint)