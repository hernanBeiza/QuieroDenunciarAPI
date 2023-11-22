from termcolor import colored

from src.daos.models.TipoPersona import TipoPersona

class TipoPersonaDAO():

	#def __init__(self):
		#print('TipoPersonaDAO')

	@staticmethod
	def obtener():
		print(colored("TipoPersonaDAO: obtener();", 'yellow'))
		return TipoPersona.query.all()

	@staticmethod
	def obtenerSegunCodigo(codigoTipoPersona):
		print(colored("TipoPersonaDAO: obtenerSegunCodigo(); {}".format(codigoTipoPersona), 'yellow'))
		return TipoPersona.query.get(codigoTipoPersona)
