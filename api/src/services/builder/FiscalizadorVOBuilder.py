from marshmallow import fields
from termcolor import colored

from src.ma import ma
from src.daos.models.Fiscalizador import Fiscalizador

class FiscalizadorVOBuilder(ma.ModelSchema):

	class Meta:
		model = Fiscalizador
		ordered = True

	fiscalizador = None
	fiscalizadores = None

	#Schema
	##Modelo - Dato a mostrar
	id_fiscalizador = fields.Integer(data_key="id")
	id_comuna = fields.Integer(data_key="idComuna")
	nombre = fields.String(data_key="nombre")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Boolean(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromFiscalizador(fiscalizador):
		FiscalizadorVOBuilder.fiscalizador = fiscalizador
		return FiscalizadorVOBuilder()

	@staticmethod
	def fromFiscalizadores(fiscalizadores):
		FiscalizadorVOBuilder.fiscalizadores = fiscalizadores
		return FiscalizadorVOBuilder()

	@staticmethod
	def build():		
		if FiscalizadorVOBuilder.fiscalizador is None:
			print("No se puede contruir FiscalizadorVO")
			return None
		else:
			try:
				return FiscalizadorVOBuilder().dump(FiscalizadorVOBuilder.fiscalizador)
			except Exception as e:
				print(colored("No se puede contruir FiscalizadorVO. Error en FiscalizadorVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if FiscalizadorVOBuilder.fiscalizadores is None:
			print("No se puede contruir FiscalizadorVO. fiscalizadores is None")
			return None
		else:
			try:
				return FiscalizadorVOBuilder(many=True).dump(FiscalizadorVOBuilder.fiscalizadores)
			except Exception as e:
				print(colored("No se puede contruir EnteFiscalizadorVO. Error en EnteFiscalizadorVOBuilder: {}".format(e), 'red'))
