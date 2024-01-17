from termcolor import colored

from src.daos.models.EstadoEnvioCorreo import EstadoEnvioCorreo

class EstadoEnvioCorreoDAO():

	#def __init__(self):
		#print('EstadoEnvioCorreoDAO')

	@staticmethod
	def obtener():
		print(colored("EstadoEnvioCorreoDAO: obtener();", 'yellow'))
		return EstadoEnvioCorreo.query.all()

	@staticmethod
	def obtenerSegunCodigo(codigoEstadoEnvioCorreo):
		print(colored("EstadoEnvioCorreoDAO: obtenerSegunCodigo(); {}".format(codigoEstadoEnvioCorreo), 'yellow'))
		return EstadoEnvioCorreo.query.get(codigoEstadoEnvioCorreo)
