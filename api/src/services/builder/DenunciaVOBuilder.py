from marshmallow import Schema, fields
from termcolor import colored

from src.app import ma
from src.daos.models.Denuncia import Denuncia
from src.services.vos.DenunciaVO import DenunciaVO
from src.services.builder.ParteVOBuilder import ParteVOBuilder
from src.services.builder.DenunciaMateriaVOBuilder import DenunciaMateriaVOBuilder
from src.services.builder.AntecedenteVOBuilder import AntecedenteVOBuilder
from src.services.builder.DireccionVOBuilder import DireccionVOBuilder

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
	id_direccion = fields.Integer(data_key="idDireccion")
	cod_estado = fields.Integer(data_key="codigoEstado")
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
	antecedentes = fields.List(fields.Nested(AntecedenteVOBuilder))

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