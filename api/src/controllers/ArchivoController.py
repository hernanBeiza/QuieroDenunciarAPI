from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from src.app import app

from src.services.ArchivoService import ArchivoService

archivoBluePrint = Blueprint('archivo', 'archivo', url_prefix='/archivo')

class ArchivoController():

	@archivoBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("ArchivoController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(ArchivoService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@archivoBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("ArchivoController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(ArchivoService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@archivoBluePrint.route('/<int:id>', methods=['GET'])
	def obtenerSegunId(id):
		print(colored("ArchivoController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ArchivoService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@archivoBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("ArchivoController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ArchivoService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@archivoBluePrint.route('/<int:id>', methods=['DELETE'])
	def eliminar(id):
		print(colored("ArchivoController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ArchivoService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(archivoBluePrint)