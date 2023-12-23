from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.daos.models.Denuncia import Denuncia
from src.services.vos.DenunciaVO import DenunciaVO
from src.services.builder.ParteVOBuilder import ParteVOBuilder
from src.services.builder.DenunciaMateriaVOBuilder import DenunciaMateriaVOBuilder
from src.services.builder.ArchivoVOBuilder import ArchivoVOBuilder
from src.services.builder.DireccionVOBuilder import DireccionVOBuilder
from src.services.builder.EstadoDenunciaVOBuilder import EstadoDenunciaVOBuilder

class DenunciaVOBuilder(ma.ModelSchema):

	class Meta:
		model = Denuncia
		ordered = True

	denuncia = None
	denuncias = None

	#Schema
	##Modelo - Dato a mostrar
	id_denuncia = fields.Integer(data_key="id")
	id_denunciado = fields.Integer(data_key="idDenunciado")
	id_denunciante = fields.Integer(data_key="idDenunciante")
	cod_estado_denuncia = fields.Integer(data_key="codigoEstadoDenuncia")
	descripcion = fields.String(data_key="descripcion")
	fecha = fields.DateTime(data_key="fecha")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")
	
	#TODO Debe llamarse igual al declarado como relación en el modelo Denuncia
	denunciado = fields.Nested(ParteVOBuilder)
	denunciante = fields.Nested(ParteVOBuilder)
	direccion = fields.Nested(DireccionVOBuilder)

	denunciasMaterias = fields.List(fields.Nested(DenunciaMateriaVOBuilder))
	archivos = fields.List(fields.Nested(ArchivoVOBuilder))
	estadoDenuncia = fields.Nested(EstadoDenunciaVOBuilder)

	#def __init__(self):

	@staticmethod
	def fromDenuncia(denuncia):		
		DenunciaVOBuilder.denuncia = denuncia
		return DenunciaVOBuilder()

	@staticmethod
	def fromDenuncias(denuncias):		
		DenunciaVOBuilder.denuncias = denuncias
		return DenunciaVOBuilder()

	@staticmethod
	def build():		
		if(DenunciaVOBuilder.denuncia is None):
			print("No se puede contruir DenunciaVO")
			return None
		else:
			try:
				return DenunciaVOBuilder().dump(DenunciaVOBuilder.denuncia)
			except Exception as e:
				print(colored("No se puede contruir DenunciaVO. Error en DenunciaVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(DenunciaVOBuilder.denuncias is None):
			print("No se puede contruir DenunciaVO. denuncias is None")
			return None
		else:
			try:
				return DenunciaVOBuilder(many=True).dump(DenunciaVOBuilder.denuncias)
			except Exception as e:
				print(colored("No se puede contruir DenunciaVO. Error en DenunciaVOBuilder; {}".format(e), 'red'))
