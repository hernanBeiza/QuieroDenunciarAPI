from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.app import app

from src.services.FiscalizadorService import FiscalizadorService

fiscalizadorBluePrint = Blueprint('fiscalizador', 'fiscalizador', url_prefix='/fiscalizador')

class FiscalizadorController():

	@fiscalizadorBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("FiscalizadorController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(FiscalizadorService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@fiscalizadorBluePrint.route('/', methods=['GET'])
	@jwt_required()
	def obtener():
		print(colored("FiscalizadorController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(FiscalizadorService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@fiscalizadorBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("FiscalizadorController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(FiscalizadorService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@fiscalizadorBluePrint.route('/comuna/<int:idComuna>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdComuna(idComuna):
		print(colored("FiscalizadorController: obtenerSegunIdComuna(); {}".format(idComuna), 'green'))
		return app.response_class(
			response = json.dumps(FiscalizadorService().obtenerSegunIdComuna(idComuna),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@fiscalizadorBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("FiscalizadorController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(FiscalizadorService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@fiscalizadorBluePrint.route('/<int:id>', methods=['DELETE'])
	@jwt_required()
	def eliminar(id):
		print(colored("FiscalizadorController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(FiscalizadorService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(fiscalizadorBluePrint)