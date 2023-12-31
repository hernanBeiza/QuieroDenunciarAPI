from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.app import app

from src.services.DireccionService import DireccionService

direccionBluePrint = Blueprint('direccion', 'direccion', url_prefix='/direccion')

class DireccionController():

	@direccionBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("DireccionController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(DireccionService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@direccionBluePrint.route('/', methods=['GET'])
	@jwt_required()
	def obtener():
		print(colored("DireccionController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(DireccionService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@direccionBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("DireccionController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DireccionService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
	@direccionBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("DireccionController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DireccionService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)
		
	@direccionBluePrint.route('/<int:id>', methods=['DELETE'])
	@jwt_required()
	def eliminar(id):
		print(colored("DireccionController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DireccionService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(direccionBluePrint)