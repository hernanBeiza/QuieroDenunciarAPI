from flask import Blueprint
from flask_jwt_extended import jwt_required

from termcolor import colored

from src.app import app

from src.services.DocumentoService import DocumentoService

documentoBluePrint = Blueprint('documento', 'documento', url_prefix='/documento')

class DocumentoController():

	@documentoBluePrint.route('/denuncia/<int:idDenuncia>', methods=['GET'])
	@jwt_required()
	def generarSegunIdDenuncia(idDenuncia):
		print(colored("DocumentoController: generarSegunIdDenuncia(); {}".format(idDenuncia), 'green'))
		return DocumentoService().generarSegunIdDenuncia(idDenuncia)

app.register_blueprint(documentoBluePrint)