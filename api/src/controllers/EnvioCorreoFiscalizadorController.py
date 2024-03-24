from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.app import app

from src.services.EnvioCorreoFiscalizadorService import EnvioCorreoFiscalizadorService

envioCorreoFiscalizadorBluePrint = Blueprint('envio-correo-fiscalizador', 'envio-correo-fiscalizador', url_prefix='/envio-correo-fiscalizador')

class EnvioCorreoFiscalizadorController():

	@envioCorreoFiscalizadorBluePrint.route('/', methods=['POST'])
	@jwt_required()
	def guardar():
		print(colored("EnvioCorreoFiscalizadorController: guardar();", 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().guardar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/', methods=['GET'])
	@jwt_required()
	def obtener():
		print(colored("EnvioCorreoFiscalizadorController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/pagina/<int:pagina>', methods=['GET'])
	@jwt_required()
	def obtenerPaginadas(pagina):
		print(colored("EnvioCorreoFiscalizadorController: obtenerPaginadas();", 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().obtenerPaginadas(pagina),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/<int:id>', methods=['GET'])
	@jwt_required()
	def obtenerSegunId(id):
		print(colored("EnvioCorreoFiscalizadorController: obtenerSegunId(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().obtenerSegunId(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/fiscalizador/<int:idFiscalizador>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdFiscalizador(idFiscalizador):
		print(colored("EnvioCorreoFiscalizadorController: obtenerSegunIdFiscalizador(); {}".format(idFiscalizador), 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().obtenerSegunIdFiscalizador(idFiscalizador),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/denuncia/<int:idDenuncia>', methods=['GET'])
	@jwt_required()
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("EnvioCorreoFiscalizadorController: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().obtenerSegunIdDenuncia(idDenuncia),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/<int:codigoEstadoEnvioCorreo>/<int:pagina>', methods=['GET'])
	def obtenerSegunCodigoPagina(codigoEstadoEnvioCorreo, pagina):
		print(colored("EnvioCorreoFiscalizadorController: obtenerSegunCodigoPagina(); {} {}".format(codigoEstadoEnvioCorreo, pagina), 'green'))
		return app.response_class(
			response=json.dumps(EnvioCorreoFiscalizadorService().obtenerSegunCodigoPagina(codigoEstadoEnvioCorreo, pagina),sort_keys=False),
			status=200,
			mimetype='application/json'
		)		

	@envioCorreoFiscalizadorBluePrint.route('/<int:id>', methods=['PUT'])
	def actualizar(id):
		print(colored("EnvioCorreoFiscalizadorController: actualizar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().actualizar(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/estado/<int:id>/<int:codigoEstadoEnvioCorreo>', methods=['PUT'])
	@jwt_required()
	def actualizarEstado(id, codigoEstadoEnvioCorreo):
		print(colored("EnvioCorreoFiscalizadorController: actualizarEstado(); id:{} codigoEstadoEnvioCorreo: {}".format(id,codigoEstadoEnvioCorreo), 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().actualizarEstado(request),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/enviar-correo/fiscalizador/denuncia/<int:idFiscalizador>/<int:idDenuncia>', methods=['PUT'])
	@jwt_required()
	def enviarCorreoFiscalizadorDenuncia(idFiscalizador,idDenuncia):
		print(colored("EnvioCorreoFiscalizadorController: enviarCorreoFiscalizadorDenuncia(); idFiscalizador:{} idDenuncia: {}".format(idFiscalizador,idDenuncia), 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().enviarCorreoFiscalizadorDenuncia(idFiscalizador,idDenuncia),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@envioCorreoFiscalizadorBluePrint.route('/<int:id>', methods=['DELETE'])
	@jwt_required()
	def eliminar(id):
		print(colored("EnvioCorreoFiscalizadorController: eliminar(); {}".format(id), 'green'))
		return app.response_class(
			response = json.dumps(EnvioCorreoFiscalizadorService().eliminar(id),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(envioCorreoFiscalizadorBluePrint)