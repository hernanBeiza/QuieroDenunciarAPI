from src.app import app

from termcolor import colored
from flask import jsonify
from flask import json
from flask import Blueprint

from src.services.EstadoDenunciaService import EstadoDenunciaService

estadoDenunciaBluePrint = Blueprint('estado-denuncia', 'estado-denuncia', url_prefix='/estado-denuncia')

class EstadoDenunciaController():

	@estadoDenunciaBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("EstadoDenunciaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(EstadoDenunciaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@estadoDenunciaBluePrint.route('/<int:codigoEstadoDenuncia>', methods=['GET'])
	def obtenerSegunCodigo(codigoEstadoDenuncia):
		print(colored("EstadoDenunciaController: obtenerSegunCodigo(); {}".format(codigoEstadoDenuncia), 'green'))
		return app.response_class(
			response = json.dumps(EstadoDenunciaService().obtenerSegunCodigo(codigoEstadoDenuncia),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
app.register_blueprint(estadoDenunciaBluePrint)