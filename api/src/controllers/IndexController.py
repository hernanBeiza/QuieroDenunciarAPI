from src.app import app
from flask import jsonify
from flask import json

from src.services.IndexService import IndexService

class MateriaController():

	@app.route('/', endpoint='/', methods = ['GET'])
	def saludar():
		'''return IndexService().saludar()'''
		return app.response_class(
			response = json.dumps(IndexService().saludar()),
			status = 200,
			mimetype = 'application/json'
		)
