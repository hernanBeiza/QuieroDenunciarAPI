from src.app import app;
from termcolor import colored
from flask import jsonify;
from flask import json;
from flask import Blueprint

from src.services.TipoDireccionService import TipoDireccionService

tipoDireccionBluePrint = Blueprint('tipo-direccion', 'tipo-direccion', url_prefix='/tipo-direccion')

class TipoDireccionController():

	@tipoDireccionBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("TipoDireccionController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(TipoDireccionService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@tipoDireccionBluePrint.route('/<int:codigoTipoDireccion>', methods=['GET'])
	def obtenerSegunCodigo(codigoTipoDireccion):
		print(colored("TipoDireccionController: obtenerSegunCodigo(); {}".format(codigoTipoDireccion), 'green'))
		return app.response_class(
			response = json.dumps(TipoDireccionService().obtenerSegunCodigo(codigoTipoDireccion),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
app.register_blueprint(tipoDireccionBluePrint)