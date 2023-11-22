from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.daos.models.DenunciaMateria import DenunciaMateria
from src.daos.models.Denuncia import Denuncia
from src.services.vos.DenunciaVO import DenunciaVO
from src.services.builder.MateriaVOBuilder import MateriaVOBuilder

class DenunciaMateriaVOBuilder(ma.ModelSchema):

	class Meta:
		model = DenunciaMateria
		ordered = True

	denunciaMateria = None
	denunciasMaterias = None


	#Schema
	##Modelo - Dato a mostrar
	id_denuncia_materia = fields.Integer(data_key="id")
	id_denuncia = fields.Integer(data_key="idDenuncia")
	cod_materia = fields.Integer(data_key="codigoMateria")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")
	
	#TODO Debe llamarse igual al declarado como relación en el modelo Denuncia
	#denuncia = fields.Nested(DenunciaVOBuilder)
	materia = fields.Nested(MateriaVOBuilder)

	#def __init__(self):

	@staticmethod
	def fromDenunciaMateria(denunciaMateria):		
		DenunciaMateriaVOBuilder.denunciaMateria = denunciaMateria
		return DenunciaMateriaVOBuilder()

	@staticmethod
	def fromDenunciasMaterias(denunciasMaterias):		
		DenunciaMateriaVOBuilder.denunciasMaterias = denunciasMaterias
		return DenunciaMateriaVOBuilder()

	@staticmethod
	def build():		
		if(DenunciaMateriaVOBuilder.denunciaMateria is None):
			print("No se puede contruir DenunciaMateriaVO")
			return None
		else:
			try:
				return DenunciaMateriaVOBuilder().dump(DenunciaMateriaVOBuilder.denunciaMateria)
			except Exception as e:
				print(colored("No se puede contruir DenunciaMateriaVO. Error en DenunciaMateriaVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(DenunciaMateriaVOBuilder.denunciasMaterias is None):
			print("No se puede contruir DenunciaMateriaVO. denunciasMaterias is None")
			return None
		else:
			try:
				return DenunciaMateriaVOBuilder(many=True).dump(DenunciaMateriaVOBuilder.denunciasMaterias)
			except Exception as e:
				print(colored("No se puede contruir DenunciaMateriaVO. Error en DenunciaMateriaVOBuilder; {}".format(e), 'red'))
