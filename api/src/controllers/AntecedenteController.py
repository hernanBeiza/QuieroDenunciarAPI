from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from src.app import app

from src.services.AntecedenteService import AntecedenteService

antecedenteBluePrint = Blueprint('antecedente', 'antecedente', url_prefix='/antecedente')

class AntecedenteController():

	@antecedenteBluePrint.route('/', methods=['POST'])
	def guardar():
		print(colored("AntecedenteController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(AntecedenteService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@antecedenteBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("AntecedenteController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(AntecedenteService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@antecedenteBluePrint.route('/<int:id>', methods=['GET'])
	def obtenerSegunId(id):
		print(colored("AntecedenteController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(AntecedenteService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)


	@antecedenteBluePrint.route('/denuncia/<int:idDenuncia>', methods=['GET'])
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("AntecedenteController: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'green'))
		return app.response_class(
			response = json.dumps(AntecedenteService().obtenerSegunIdDenuncia(idDenuncia),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@antecedenteBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("AntecedenteController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(AntecedenteService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@antecedenteBluePrint.route('/<int:id>', methods=['DELETE'])
	def eliminar(id):
		print(colored("AntecedenteController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(AntecedenteService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(antecedenteBluePrint)