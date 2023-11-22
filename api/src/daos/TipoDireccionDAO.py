from termcolor import colored

from src.daos.models.TipoDireccion import TipoDireccion

class TipoDireccionDAO():

	#def __init__(self):
		#print('TipoParteDAO')

	@staticmethod
	def obtener():
		print(colored("TipoDireccionDAO: obtener();", 'yellow'))
		return TipoDireccion.query.all()

	@staticmethod
	def obtenerSegunCodigo(codigoTipoDireccion):
		print(colored("TipoDireccionDAO: obtenerSegunCodigo(); {}".format(codigoTipoDireccion), 'yellow'))
		return TipoDireccion.query.get(codigoTipoDireccion)
