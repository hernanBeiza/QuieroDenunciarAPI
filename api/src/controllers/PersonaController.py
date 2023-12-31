from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.run import app

from src.services.PersonaService import PersonaService

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
	@jwt_required()
	def obtener():
		print(colored("PersonaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@personaBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("PersonaController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@personaBluePrint.route('/rut/<string:rut>', methods=['GET'])
	@jwt_required()
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
	@jwt_required()
	def eliminar(id):
		print(colored("PersonaController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(PersonaService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(personaBluePrint)