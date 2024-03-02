from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.run import app

from src.services.UsuarioService import UsuarioService

usuarioBluePrint = Blueprint('usuario', 'usuario', url_prefix='/usuario')

class UsuarioController():

	@usuarioBluePrint.route('/', methods=['POST'])
	@jwt_required()
	def guardar():
		print(colored("UsuarioController: guardar();", 'green'))
		return app.response_class(
			response=json.dumps(UsuarioService().guardar(request), sort_keys=False),
			status=200,
			mimetype='application/json'
		)

	@usuarioBluePrint.route('/', methods=['GET'])
	@jwt_required()
	def obtener():
		print(colored("UsuarioController: obtener();", 'green'))
		return app.response_class(
			response=json.dumps(UsuarioService().obtener(), sort_keys=False),
			status=200,
			mimetype='application/json'
		)

	@usuarioBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("UsuarioController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response=json.dumps(UsuarioService().obtenerSegunId(id), sort_keys=False),
			status=200,
			mimetype='application/json'
		)

	@usuarioBluePrint.route('/login', methods=['POST'])
	def login():
		print(colored("UsuarioController: login(); {}".format(request), 'green'))
		return app.response_class(
			response=json.dumps(UsuarioService().iniciarSesion(request), sort_keys=False),
			status=200,
			mimetype='application/json'
		)

	@usuarioBluePrint.route('/verificar-token', methods=['POST'])
	@jwt_required()
	def verificarToken():
		print(colored("UsuarioController: verificarToken(); {}".format(request), 'green'))
		return app.response_class(
			response=json.dumps(UsuarioService().verificarToken(request), sort_keys=False),
			status=200,
			mimetype='application/json'
		)

	@usuarioBluePrint.route('/<int:id>', methods=['PUT'])
	@jwt_required()
	def actualizar(id):
		print(colored("UsuarioController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response=json.dumps(UsuarioService().actualizar(request), sort_keys=False),
			status=200,
			mimetype='application/json'
		)
		
	@usuarioBluePrint.route('/<int:id>', methods=['DELETE'])
	@jwt_required()
	def eliminar(id):
		print(colored("UsuarioController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response=json.dumps(UsuarioService().eliminar(id), sort_keys=False),
			status=200,
			mimetype='application/json'
		)

app.register_blueprint(usuarioBluePrint)