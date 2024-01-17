from termcolor import colored

from src.daos.models.EstadoEnvioCorreo import EstadoEnvioCorreo
from src.daos.EstadoEnvioCorreoDAO import EstadoEnvioCorreoDAO
from src.services.vos.EstadoEnvioCorreoVO import EstadoEnvioCorreoVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class EstadoEnvioCorreoService():

	#def __init__(self):
		#print('EstadoEnvioCorreoService')

	@staticmethod
	def obtener():
		print(colored("EstadoEnvioCorreoService: obtener();", 'cyan'))
		estadosEnvioCorreo = EstadoEnvioCorreoDAO.obtener()
		if len(estadosEnvioCorreo)>0:
			data = {
				"result":True,
				"estadosEnvioCorreo":VOBuilderFactory().getEstadoEnvioCorreoVOBuilder().fromEstadosEnvioCorreo(estadosEnvioCorreo).builds(),
				"mensajes":"Se encontraron estados de envío de correo"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron estados de envío de correo"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(codigo):
		print(colored("EstadoEnvioCorreoService: obtenerSegunCodigo(); {}".format(codigo), 'cyan'))
		estadoEnvioCorreo = EstadoEnvioCorreoDAO.obtenerSegunCodigo(codigo)
		if(estadoEnvioCorreo):
			data = {
				"result":True,
				"estadoEnvioCorreo":VOBuilderFactory().getEstadoEnvioCorreoVOBuilder().fromEstadoEnvioCorreo(estadoEnvioCorreo).build(),
				"mensajes":"Se encontró estado de envío de correo con código {}".format(codigo)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró estado de envío de correo con código {}".format(codigo)
			}

		return data