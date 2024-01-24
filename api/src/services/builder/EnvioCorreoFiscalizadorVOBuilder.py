from marshmallow import fields
from termcolor import colored

from src.ma import ma
from src.daos.models.EnvioCorreoFiscalizador import EnvioCorreoFiscalizador

class EnvioCorreoFiscalizadorVOBuilder(ma.ModelSchema):

	class Meta:
		model = EnvioCorreoFiscalizador
		ordered = True

	envioCorreoFiscalizador = None
	envioCorreoFiscalizadores = None

	#Schema
	##Modelo - Dato a mostrar
	id_envio_correo_fiscalizador = fields.Integer(data_key="id")
	id_fiscalizador = fields.Integer(data_key="idFiscalizador")
	id_denuncia = fields.Integer(data_key="idDenuncia")
	cod_estado_envio_correo = fields.Integer(data_key="codigoEstadoEnvioCorreo")
	fecha_envio = fields.String(data_key="fechaEnvio")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Boolean(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromEnvioCorreoFiscalizador(envioCorreoFiscalizador):
		EnvioCorreoFiscalizadorVOBuilder.envioCorreoFiscalizador = envioCorreoFiscalizador
		return EnvioCorreoFiscalizadorVOBuilder()

	@staticmethod
	def fromEnvioCorreoFiscalizadores(envioCorreoFiscalizadores):
		EnvioCorreoFiscalizadorVOBuilder.envioCorreoFiscalizadores = envioCorreoFiscalizadores
		return EnvioCorreoFiscalizadorVOBuilder()

	@staticmethod
	def build():		
		if EnvioCorreoFiscalizadorVOBuilder.envioCorreoFiscalizador is None:
			print("No se puede contruir EnvioCorreoFiscalizadorVO")
			return None
		else:
			try:
				return EnvioCorreoFiscalizadorVOBuilder().dump(EnvioCorreoFiscalizadorVOBuilder.envioCorreoFiscalizador)
			except Exception as e:
				print(colored("No se puede contruir EnvioCorreoFiscalizadorVO. Error en EnvioCorreoFiscalizadorVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if EnvioCorreoFiscalizadorVOBuilder.envioCorreoFiscalizadores is None:
			print("No se puede contruir EnvioCorreoFiscalizadorVO. envioCorreoFiscalizadores is None")
			return None
		else:
			try:
				return EnvioCorreoFiscalizadorVOBuilder(many=True).dump(EnvioCorreoFiscalizadorVOBuilder.envioCorreoFiscalizadores)
			except Exception as e:
				print(colored("No se puede contruir EnvioCorreoFiscalizadorVO. Error en EnvioCorreoFiscalizadorVOBuilder: {}".format(e), 'red'))
