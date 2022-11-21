from marshmallow import Schema, fields
from termcolor import colored

from src.app import ma
from src.services.vos.TipoArchivoVO import TipoArchivoVO
from src.daos.models.TipoArchivo import TipoArchivo

class TipoArchivoVOBuilder(ma.ModelSchema):

	class Meta:
		model = TipoArchivo
		ordered = True

	tipoArchivo = None
	tipoArchivos = None

	#Schema
	##Modelo - Dato a mostrar
	cod_tipo_archivo = fields.Integer(data_key="codigoTipoArchivo")
	glosa = fields.String()
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromTipoArchivo(tipoArchivo):		
		TipoArchivoVOBuilder.tipoArchivo = tipoArchivo
		return TipoArchivoVOBuilder()

	@staticmethod
	def fromTipoArchivos(tipoArchivos):		
		TipoArchivoVOBuilder.tipoArchivos = tipoArchivos
		return TipoArchivoVOBuilder()

	@staticmethod
	def build():		
		if(TipoArchivoVOBuilder.tipoArchivo is None):
			print("No se puede contruir TipoArchivoVO")
			return None
		else:
			try:
				return TipoArchivoVOBuilder().dump(TipoArchivoVOBuilder.tipoArchivo)
			except Exception as e:
				print(colored("No se puede contruir TipoArchivVO. Error en TipoArchivoVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(TipoArchivoVOBuilder.tipoArchivos is None):
			print("No se puede contruir TipoArchivoVO. tipoArchivos is None")
			return None
		else:
			try:
				return TipoArchivoVOBuilder(many=True).dump(TipoArchivoVOBuilder.tipoArchivos)
			except Exception as e:
				print(colored("No se puede contruir TipoArchivVO. Error en TipoArchivoVOBuilder; {}".format(e), 'red'))
