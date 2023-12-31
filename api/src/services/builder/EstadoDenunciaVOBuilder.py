from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.services.vos.EstadoDenunciaVO import EstadoDenunciaVO
from src.daos.models.EstadoDenuncia import EstadoDenuncia

class EstadoDenunciaVOBuilder(ma.ModelSchema):

	class Meta:
		model = EstadoDenuncia
		ordered = True

	estadoDenuncia = None
	estadosDenuncias = None

	#Schema
	##Modelo - Dato a mostrar
	cod_estado_denuncia = fields.Integer(data_key="codigo")
	glosa = fields.String()
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromEstadoDenuncia(estadoDenuncia):		
		EstadoDenunciaVOBuilder.estadoDenuncia = estadoDenuncia
		return EstadoDenunciaVOBuilder()

	@staticmethod
	def fromEstadosDenuncias(estadosDenuncias):		
		EstadoDenunciaVOBuilder.estadosDenuncias = estadosDenuncias
		return EstadoDenunciaVOBuilder()

	@staticmethod
	def build():		
		if(EstadoDenunciaVOBuilder.estadoDenuncia is None):
			print("No se puede contruir EstadoDenunciaVO")
			return None
		else:
			try:
				return EstadoDenunciaVOBuilder().dump(EstadoDenunciaVOBuilder.estadoDenuncia)
			except Exception as e:
				print(colored("No se puede contruir EstadoDenunciaVO. Error en EstadoDenunciaVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(EstadoDenunciaVOBuilder.estadosDenuncias is None):
			print("No se puede contruir EstadoDenunciaVO. estadosDenuncias is None")
			return None
		else:
			try:
				return EstadoDenunciaVOBuilder(many=True).dump(EstadoDenunciaVOBuilder.estadosDenuncias)
			except Exception as e:
				print(colored("No se puede contruir EstadoDenunciaVO. Error en EstadoDenunciaVOBuilder: {}".format(e), 'red'))
