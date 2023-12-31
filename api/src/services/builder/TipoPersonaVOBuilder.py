from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.services.vos.TipoPersonaVO import TipoPersonaVO
from src.daos.models.TipoPersona import TipoPersona

class TipoPersonaVOBuilder(ma.ModelSchema):

	class Meta:
		model = TipoPersona
		ordered = True

	tipoPersona = None
	tipoPersonas = None

	#Schema
	##Modelo - Dato a mostrar
	cod_tipo_persona = fields.Integer(data_key="codigoTipoPersona")
	glosa = fields.String()
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromTipoPersona(tipoPersona):		
		TipoPersonaVOBuilder.tipoPersona = tipoPersona
		return TipoPersonaVOBuilder()

	@staticmethod
	def fromTipoPersonas(tipoPersonas):		
		TipoPersonaVOBuilder.tipoPersonas = tipoPersonas
		return TipoPersonaVOBuilder()

	@staticmethod
	def build():		
		if(TipoPersonaVOBuilder.tipoPersona is None):
			print("No se puede contruir TipoPersonaVO")
			return None
		else:
			try:
				return TipoPersonaVOBuilder().dump(TipoPersonaVOBuilder.tipoPersona)
			except Exception as e:
				print(colored("No se puede contruir TipoPersonaVO. Error en TipoPersonaVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(TipoPersonaVOBuilder.tipoPersonas is None):
			print("No se puede contruir TipoPersonaVO. tipoPersonas is None")
			return None
		else:
			try:
				return TipoPersonaVOBuilder(many=True).dump(TipoPersonaVOBuilder.tipoPersonas)
			except Exception as e:
				print(colored("No se puede contruir TipoPersonaVO. Error en TipoPersonaVOBuilder: {}".format(e), 'red'))
