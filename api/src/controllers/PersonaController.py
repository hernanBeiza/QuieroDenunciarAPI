from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from ..app import app;

from ..services.PersonaService import PersonaService

personaBluePrint = Blueprint('persona', 'persona', url_prefix='/persona')

class PersonaController():

	@personaBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("PersonaController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@personaBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("PersonaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@personaBluePrint.route('/<int:id>', methods=['GET'])
	def obtenerSegunId(id):
		print(colored("PersonaController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@personaBluePrint.route('/rut/<string:rut>', methods=['GET'])
	def obtenerSegunRut(rut):
		print(colored("PersonaController: obtenerSegunRut(); {}".format(rut), 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().obtenerSegunRut(rut),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@personaBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("PersonaController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
	@personaBluePrint.route('/<int:id>', methods=['DELETE'])
	def eliminar(id):
		print(colored("PersonaController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
app.register_blueprint(personaBluePrint)