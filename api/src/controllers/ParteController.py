from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.run import app

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
	@jwt_required()
	def obtener():
		print(colored("ParteController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(ParteService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@parteBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("ParteController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ParteService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@parteBluePrint.route('/persona/<string:idPersona>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdPersona(idPersona):
		print(colored("ParteController: obtenerSegunIdPersona(); {}".format(idPersona), 'green'))
		return app.response_class(
			response = json.dumps(ParteService().obtenerSegunIdPersona(idPersona),sort_keys=False),
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
	@jwt_required()
	def eliminar(id):
		print(colored("ParteController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(ParteService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(parteBluePrint)