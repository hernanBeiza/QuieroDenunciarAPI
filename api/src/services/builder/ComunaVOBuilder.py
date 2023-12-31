from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.services.vos.ComunaVO import ComunaVO
from src.daos.models.Comuna import Comuna

class ComunaVOBuilder(ma.ModelSchema):

	class Meta:
		model = Comuna
		ordered = True

	comuna = None
	comunas = None

	#Schema
	##Modelo - Dato a mostrar
	id_comuna = fields.Integer(data_key="idComuna")
	id_provincia = fields.Integer(data_key="idProvincia")
	comuna = fields.String(data_key="comuna")

	#def __init__(self):

	@staticmethod
	def fromComuna(comuna):		
		ComunaVOBuilder.comuna = comuna
		return ComunaVOBuilder()

	@staticmethod
	def fromComunas(comunas):		
		ComunaVOBuilder.comunas = comunas
		return ComunaVOBuilder()

	@staticmethod
	def build():		
		if(ComunaVOBuilder.comuna is None):
			print("No se puede contruir ComunaVO")
			return None
		else:
			try:
				return ComunaVOBuilder().dump(ComunaVOBuilder.comuna)
			except Exception as e:
				print(colored("No se puede contruir ComunaVO. Error en ComunaVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(ComunaVOBuilder.comunas is None):
			print("No se puede contruir ComunaVO. comunas is None")
			return None
		else:
			try:
				return ComunaVOBuilder(many=True).dump(ComunaVOBuilder.comunas)
			except Exception as e:
				print(colored("No se puede contruir ComunaVO. Error en ComunaVOBuilder: {}".format(e), 'red'))
