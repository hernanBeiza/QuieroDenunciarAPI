from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.services.vos.MateriaVO import MateriaVO
from src.daos.models.Materia import Materia

class MateriaVOBuilder(ma.ModelSchema):

	class Meta:
		model = Materia
		ordered = True

	materia = None
	materias = None

	#Schema
	##Modelo - Dato a mostrar
	cod_materia = fields.Integer(data_key="codigoMateria")
	glosa = fields.String()
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):
	#
	@staticmethod
	def fromMateria(materia):
		MateriaVOBuilder.materia = materia
		return MateriaVOBuilder()

	@staticmethod
	def fromMaterias(materias):
		MateriaVOBuilder.materias = materias
		return MateriaVOBuilder()

	@staticmethod
	def build():		
		if(MateriaVOBuilder.materia is None):
			print("No se puede contruir MateriaVO")
			return None
		else:
			try:
				return MateriaVOBuilder().dump(MateriaVOBuilder.materia)
			except Exception as e:
				print(colored("No se puede contruir MateriaVO. Error en MateriaVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(MateriaVOBuilder.materias is None):
			print("No se puede contruir MateriaVO. materias is None")
			return None
		else:
			try:
				return MateriaVOBuilder(many=True).dump(MateriaVOBuilder.materias)
			except Exception as e:
				print(colored("No se puede contruir MateriaVO. Error en MateriaVOBuilder; {}".format(e), 'red'))
