from ..app import app;
from termcolor import colored
from flask import jsonify;
from flask import json;
from flask import Blueprint

from ..services.TipoArchivoService import TipoArchivoService

tipoArchivoBluePrint = Blueprint('tipo-archivo', 'tipo-archivo', url_prefix='/tipo-archivo')

class TipoArchivoController():

	@tipoArchivoBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("TipoArchivoController: obtener();", 'green'))
		return app.response_class(
			response = json.dumps(TipoArchivoService().obtener(),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

	@tipoArchivoBluePrint.route('/<int:codigoTipoArchivo>', methods=['GET'])
	def obtenerSegunCodigo(codigoTipoArchivo):
		print(colored("TipoArchivoController: obtenerSegunCodigo(); {}".format(codigoTipoArchivo), 'green'))
		#print(MateriaService().obtener(pagina))
		#print(jsonify(MateriaService().obtener(pagina)))
		#print(json.dumps(MateriaService().obtener(pagina)))
		#return jsonify((MateriaService().obtener(pagina)))
		return app.response_class(
			response = json.dumps(TipoArchivoService().obtenerSegunCodigo(codigoTipoArchivo),sort_keys=False),
			status = 200,
			mimetype = 'application/json'
		)

app.register_blueprint(tipoArchivoBluePrint)