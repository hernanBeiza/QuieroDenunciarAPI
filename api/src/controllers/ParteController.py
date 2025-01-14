from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from src.app import app;

from src.services.ParteService import ParteService

parteBluePrint = Blueprint('parte', 'parte', url_prefix='/parte')

class ParteController():

	@parteBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("ParteController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(ParteService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@parteBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("ParteController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(ParteService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@parteBluePrint.route('/<int:id>', methods=['GET'])
	def obtenerSegunId(id):
		print(colored("ParteController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ParteService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@parteBluePrint.route('/rut/<string:rut>', methods=['GET'])
	def obtenerSegunRut(rut):
		print(colored("ParteController: obtenerSegunRut(); {}".format(rut), 'green'))
		return app.response_class(
			response = json.dumps(ParteService().obtenerSegunRut(rut),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@parteBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("ParteController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ParteService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
	@parteBluePrint.route('/<int:id>', methods=['DELETE'])
	def eliminar(id):
		print(colored("ParteController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ParteService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
app.register_blueprint(parteBluePrint)