from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.services.vos.TipoDireccionVO import TipoDireccionVO
from src.daos.models.TipoDireccion import TipoDireccion

class TipoDireccionVOBuilder(ma.ModelSchema):

	class Meta:
		model = TipoDireccion
		ordered = True

	tipoDireccion = None
	tiposDirecciones = None

	#Schema
	##Modelo - Dato a mostrar
	cod_tipo_direccion = fields.Integer(data_key="codigoTipoDireccion")
	glosa = fields.String()
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromTipoDireccion(tipoDireccion):		
		TipoDireccionVOBuilder.tipoDireccion = tipoDireccion
		return TipoDireccionVOBuilder()

	@staticmethod
	def fromTipoDirecciones(tiposDirecciones):		
		TipoDireccionVOBuilder.tiposDirecciones = tiposDirecciones
		return TipoDireccionVOBuilder()

	@staticmethod
	def build():		
		if(TipoDireccionVOBuilder.tipoDireccion is None):
			print("No se puede contruir TipoDireccionVO")
			return None
		else:
			try:
				return TipoDireccionVOBuilder().dump(TipoDireccionVOBuilder.tipoDireccion)
			except Exception as e:
				print(colored("No se puede contruir TipoDireccionVO. Error en TipoDireccionVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(TipoDireccionVOBuilder.tiposDirecciones is None):
			print("No se puede contruir TipoDireccionVO. tiposDirecciones is None")
			return None
		else:
			try:
				return TipoDireccionVOBuilder(many=True).dump(TipoDireccionVOBuilder.tiposDirecciones)
			except Exception as e:
				print(colored("No se puede contruir TipoDireccionVO. Error en TipoDireccionVOBuilder; {}".format(e), 'red'))
