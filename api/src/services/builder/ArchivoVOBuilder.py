from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.daos.models.Archivo import Archivo
from src.services.vos.ArchivoVO import ArchivoVO
from src.services.builder.TipoArchivoVOBuilder import TipoArchivoVOBuilder

class ArchivoVOBuilder(ma.ModelSchema):

	class Meta:
		model = Archivo
		ordered = True

	archivo = None
	archivos = None

	#Schema
	##Modelo - Dato a mostrar
	id_archivo = fields.Integer(data_key="id")
	id_denuncia = fields.Integer(data_key="idDenuncia")
	cod_tipo_archivo = fields.Integer(data_key="codigoTipoArchivo")
	ruta_archivo = fields.String(data_key="rutaArchivo")
	nombre_archivo = fields.String(data_key="nombreArchivo")
	extension_archivo = fields.String(data_key="extensionArchivo")
	descripcion = fields.String(data_key="descripcion")
	fecha = fields.DateTime(data_key="fecha")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")

	tipoArchivo = fields.Nested(TipoArchivoVOBuilder)

	#def __init__(self):

	@staticmethod
	def fromArchivo(archivo):		
		ArchivoVOBuilder.archivo = archivo
		return ArchivoVOBuilder()

	@staticmethod
	def fromArchivos(archivos):		
		ArchivoVOBuilder.archivos = archivos
		return ArchivoVOBuilder()

	@staticmethod
	def build():		
		if(ArchivoVOBuilder.archivo is None):
			print("No se puede contruir ArchivoVO")
			return None
		else:
			try:
				return ArchivoVOBuilder().dump(ArchivoVOBuilder.archivo)
			except Exception as e:
				print(colored("No se puede contruir ArchivoVO. Error en ArchivoVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(ArchivoVOBuilder.archivos is None):
			print("No se puede contruir ArchivoVO. archivos is None")
			return None
		else:
			try:
				return ArchivoVOBuilder(many=True).dump(ArchivoVOBuilder.archivos)
			except Exception as e:
				print(colored("No se puede contruir ArchivoVO. Error en ArchivoVOBuilder: {}".format(e), 'red'))
