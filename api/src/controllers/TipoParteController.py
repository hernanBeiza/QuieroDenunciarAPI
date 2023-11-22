from src.app import app
from termcolor import colored
from flask import jsonify
from flask import json
from flask import Blueprint

from src.services.TipoParteService import TipoParteService

tipoParteBluePrint = Blueprint('tipo-parte', 'tipo-parte', url_prefix='/tipo-parte')

class TipoParteController():

	@tipoParteBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("TipoParteController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(TipoParteService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@tipoParteBluePrint.route('/<int:codigoTipoParte>', methods=['GET'])
	def obtenerSegunCodigo(codigoTipoParte):
		print(colored("TipoParteController: obtenerSegunCodigo(); {}".format(codigoTipoParte), 'green'))
		return app.response_class(
			response = json.dumps(TipoParteService().obtenerSegunCodigo(codigoTipoParte),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
app.register_blueprint(tipoParteBluePrint)