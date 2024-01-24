from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.app import app

from src.services.CorreoService import CorreoService

correoBluePrint = Blueprint('correo', 'correo', url_prefix='/correo')

class CorreoController():

	@correoBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("CorreoController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(CorreoService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@correoBluePrint.route('/', methods=['GET'])
	@jwt_required()
	def obtener():
		print(colored("CorreoController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(CorreoService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@correoBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("CorreoController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(CorreoService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@correoBluePrint.route('/fiscalizador/<int:idFiscalizador>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdFiscalizador(idFiscalizador):
		print(colored("CorreoController: obtenerSegunIdFiscalizador(); {}".format(idFiscalizador), 'green'))
		return app.response_class(
			response = json.dumps(CorreoService().obtenerSegunIdFiscalizador(idFiscalizador),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@correoBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("CorreoController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(CorreoService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@correoBluePrint.route('/<int:id>', methods=['DELETE'])
	@jwt_required()
	def eliminar(id):
		print(colored("CorreoController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(CorreoService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(correoBluePrint)