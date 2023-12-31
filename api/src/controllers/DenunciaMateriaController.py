from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.app import app

from src.services.DenunciaMateriaService import DenunciaMateriaService

denunciaMateriaBluePrint = Blueprint('denuncia-materia', 'denuncia-materia', url_prefix='/denuncia-materia')

class DenunciaMateriaController():

	@denunciaMateriaBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("DenunciaMateriaController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(DenunciaMateriaService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaMateriaBluePrint.route('/', methods=['GET'])
	@jwt_required()
	def obtener():
		print(colored("DenunciaMateriaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(DenunciaMateriaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaMateriaBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("DenunciaMateriaController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaMateriaService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaMateriaBluePrint.route('/denuncia/<int:idDenuncia>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("DenunciaMateriaController: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaMateriaService().obtenerSegunIdDenuncia(idDenuncia),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaMateriaBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("DenunciaMateriaController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaMateriaService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@denunciaMateriaBluePrint.route('/<int:id>', methods=['DELETE'])
	@jwt_required()
	def eliminar(id):
		print(colored("DenunciaMateriaController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(DenunciaMateriaService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(denunciaMateriaBluePrint)