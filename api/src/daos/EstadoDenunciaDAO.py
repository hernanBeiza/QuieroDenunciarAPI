from termcolor import colored

from src.daos.models.EstadoDenuncia import EstadoDenuncia

class EstadoDenunciaDAO():

	#def __init__(self):
		#print('TipoParteDAO')

	@staticmethod
	def obtener():
		print(colored("EstadoDenunciaDAO: obtener();", 'yellow'))
		return EstadoDenuncia.query.all()

	@staticmethod
	def obtenerSegunCodigo(codigoEstadoDenuncia):
		print(colored("EstadoDenunciaDAO: obtenerSegunCodigo(); {}".format(codigoEstadoDenuncia), 'yellow'))
		return EstadoDenuncia.query.get(codigoEstadoDenuncia)
