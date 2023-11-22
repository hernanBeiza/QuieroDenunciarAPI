from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.daos.models.TipoParte import TipoParte

class TipoParteVOBuilder(ma.ModelSchema):

	class Meta:
		model = TipoParte
		ordered = True

	tipoParte = None
	tipoPartes = None

	#Schema
	##Modelo - Dato a mostrar
	cod_tipo_parte = fields.Integer(data_key="codigoTipoParte")
	glosa = fields.String()
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromTipoParte(tipoParte):		
		TipoParteVOBuilder.tipoParte = tipoParte
		return TipoParteVOBuilder()

	@staticmethod
	def fromTipoPartes(tipoPartes):		
		TipoParteVOBuilder.tipoPartes = tipoPartes
		return TipoParteVOBuilder()

	@staticmethod
	def build():		
		if(TipoParteVOBuilder.tipoParte is None):
			print("No se puede contruir TipoPersonaVO")
			return None
		else:
			try:
				return TipoParteVOBuilder().dump(TipoParteVOBuilder.tipoParte)
			except Exception as e:
				print(colored("No se puede contruir TipoParteVO. Error en TipoParteVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(TipoParteVOBuilder.tipoPartes is None):
			print("No se puede contruir TipoPersonaVO. tipoPartes is None")
			return None
		else:
			try:
				return TipoParteVOBuilder(many=True).dump(TipoParteVOBuilder.tipoPartes)
			except Exception as e:
				print(colored("No se puede contruir TipoParteVO. Error en TipoParteVOBuilder; {}".format(e), 'red'))
