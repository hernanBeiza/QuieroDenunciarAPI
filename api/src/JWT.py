import os
from flask_dotenv import DotEnv
from termcolor import colored
from flask_cors import CORS
from flask import json
from flask import request
from flask import jsonify
from flask_jwt_extended import JWTManager

#from src.run import app

class JWT:

	def __init__(self):
		print('JWT()')

	@staticmethod
	def iniciarConApp(app):
		print(colored("JWT: iniciarConApp()", 'yellow'))
		#Configuración token JWT Flask-JWT-Extended
		app.config["JWT_SECRET_KEY"] = "super-secret"
		app.config["JWT_ERROR_MESSAGE_KEY"] = "mensajes"
		#TODO Revisar esto
		#app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

		jwt = JWTManager(app)

		@jwt.unauthorized_loader
		def unauthorized(mensajeError):
			print(colored("JWT: unauthorized: {}".format(mensajeError), 'red'))
			data = {"result":False, "mensajes":mensajeError}
			return data
			"""
			return app.response_class(
				response=json.dumps(data, sort_keys=False),
				status=401,
				mimetype='application/json'
			)
			"""
		@jwt.invalid_token_loader
		def invalid(mensajeError):
			print(colored("JWT: invalid: {}".format(mensajeError), 'red'))
			data = {"result":False, "mensajes":mensajeError}
			return data
			"""
			return app.response_class(
				response=json.dumps(data, sort_keys=False),
				status=401,
				mimetype='application/json'
			)
			"""

		@jwt.expired_token_loader
		def expired(headerData, payload):
			print(colored("JWT: expired", 'red'))
			data = {"result":False, "mensajes":"Token expirado"}
			return data
			"""
			return app.response_class(
				response=json.dumps(data, sort_keys=False),
				status=401,
				mimetype='application/json'
			)
			"""

