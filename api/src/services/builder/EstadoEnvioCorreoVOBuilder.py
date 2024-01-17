from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.daos.models.EstadoEnvioCorreo import EstadoEnvioCorreo

class EstadoEnvioCorreoVOBuilder(ma.ModelSchema):

	class Meta:
		model = EstadoEnvioCorreo
		ordered = True

	estadoEnvioCorreo = None
	estadosEnvioCorreo = None

	#Schema
	##Modelo - Dato a mostrar
	cod_estado_envio_correo = fields.Integer(data_key="codigo")
	glosa = fields.String()
	flag_activo = fields.Boolean(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromEstadoEnvioCorreo(estadoEnvioCorreo):
		EstadoEnvioCorreoVOBuilder.estadoEnvioCorreo = estadoEnvioCorreo
		return EstadoEnvioCorreoVOBuilder()

	@staticmethod
	def fromEstadosEnvioCorreo(estadosEnvioCorreo):
		EstadoEnvioCorreoVOBuilder.estadosEnvioCorreo = estadosEnvioCorreo
		return EstadoEnvioCorreoVOBuilder()

	@staticmethod
	def build():		
		if EstadoEnvioCorreoVOBuilder.estadoEnvioCorreo is None:
			print("No se puede contruir EstadoEnvioCorreoVO")
			return None
		else:
			try:
				return EstadoEnvioCorreoVOBuilder().dump(EstadoEnvioCorreoVOBuilder.estadoEnvioCorreo)
			except Exception as e:
				print(colored("No se puede contruir EstadoEnvioCorreoVO. Error en EstadoEnvioCorreoVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if EstadoEnvioCorreoVOBuilder.estadosEnvioCorreo is None:
			print("No se puede contruir EstadoEnvioCorreoVO. estadosEnvioCorreo is None")
			return None
		else:
			try:
				return EstadoEnvioCorreoVOBuilder(many=True).dump(EstadoEnvioCorreoVOBuilder.estadosEnvioCorreo)
			except Exception as e:
				print(colored("No se puede contruir EstadoDenunciaVO. Error en EstadoEnvioCorreoVOBuilder: {}".format(e), 'red'))
