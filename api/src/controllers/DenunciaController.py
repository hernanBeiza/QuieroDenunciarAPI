from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.app import app

from src.services.DenunciaService import DenunciaService

denunciaBluePrint = Blueprint('denuncia', 'denuncia', url_prefix='/denuncia')

class DenunciaController():

	@denunciaBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("DenunciaController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/', methods=['GET'])
	@jwt_required()
	def obtener():
		print(colored("DenunciaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/pagina/<int:pagina>', methods=['GET'])
	@jwt_required()
	def obtenerPaginadas(pagina):
		print(colored("DenunciaController: obtenerPaginadas();", 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().obtenerPaginadas(pagina),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("DenunciaController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/denunciado/<int:idDenunciado>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdDenunciado(idDenunciado):
		print(colored("DenunciaController: obtenerSegunIdDenunciado(); {}".format(idDenunciado), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().obtenerSegunIdDenunciado(idDenunciado),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/denunciante/<int:idDenunciante>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdDenunciante(idDenunciante):
		print(colored("DenunciaController: obtenerSegunIdDenunciante(); {}".format(idDenunciante), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().obtenerSegunIdDenunciante(idDenunciante),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("DenunciaController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/estado/<int:id>/<int:codigoEstado>', methods=['PUT'])
	@jwt_required()
	def actualizarEstado(id, codigoEstado):
		print(colored("DenunciaController: actualizarEstado(); id:{} codigoEstado: {}".format(id,codigoEstado), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().actualizarEstado(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaBluePrint.route('/<int:id>', methods=['DELETE'])
	@jwt_required()
	def eliminar(id):
		print(colored("DenunciaController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(denunciaBluePrint)