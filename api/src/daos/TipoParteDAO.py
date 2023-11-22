from termcolor import colored

from src.daos.models.TipoParte import TipoParte

class TipoParteDAO():

	#def __init__(self):
		#print('TipoParteDAO')

	@staticmethod
	def obtener():
		print(colored("TipoParteDAO: obtener();", 'yellow'))
		return TipoParte.query.all()

	@staticmethod
	def obtenerSegunCodigo(codigoTipoParte):
		print(colored("TipoParteDAO: obtenerSegunCodigo(); {}".format(codigoTipoParte), 'yellow'))
		return TipoParte.query.get(codigoTipoParte)
