from ..app import app;
from termcolor import colored
from flask import jsonify;
from flask import json;
from flask import Blueprint

from ..services.MateriaService import MateriaService

materiaBluePrint = Blueprint('materia', 'materia', url_prefix='/materia')

class MateriaController():

	@materiaBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("MateriaController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(MateriaService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@materiaBluePrint.route('/pagina/<int:pagina>', methods=['GET'])
	def obtenerConPagina(pagina):
		print(colored("MateriaController: obtenerConPagina();", 'green'))
		return app.response_class(
			response = json.dumps(MateriaService().obtenerConPagina(pagina),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@materiaBluePrint.route('/<int:codigoMateria>', methods=['GET'])
	def obtenerSegunCodigo(codigoMateria):
		print(colored("MateriaController: obtenerSegunCodigo(); {}".format(codigoMateria), 'green'))
		#print(MateriaService().obtener(pagina))
		#print(jsonify(MateriaService().obtener(pagina)))
		#print(json.dumps(MateriaService().obtener(pagina)))
		#return jsonify((MateriaService().obtener(pagina)))
		return app.response_class(
			response = json.dumps(MateriaService().obtenerSegunCodigo(codigoMateria),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(materiaBluePrint)