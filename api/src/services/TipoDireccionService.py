from termcolor import colored

from src.daos.models.TipoDireccion import TipoDireccion
from src.daos.TipoDireccionDAO import TipoDireccionDAO
from src.services.vos.TipoDireccionVO import TipoDireccionVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class TipoDireccionService():

	#def __init__(self):
		#print('MateriaService')

	@staticmethod
	def obtener():
		print(colored("TipoDireccionService: obtener();", 'cyan'))
		tipoDirecciones = TipoDireccionDAO.obtener()
		if len(tipoDirecciones)>0:
			data = {
				"result":True,
				"tipoDirecciones":VOBuilderFactory().getTipoDireccionVOBuilder().fromTipoDirecciones(tipoDirecciones).builds(),
				"mensajes":"Se encontraron tipos de direcciones"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron tipos de direcciones"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(codigo):
		print(colored("TipoDireccionService: obtenerSegunCodigo(); {}".format(codigo), 'cyan'))
		tipoDireccion = TipoDireccionDAO.obtenerSegunCodigo(codigo)
		if(tipoDireccion):
			data = {
				"result":True,
				"tipoDireccion":VOBuilderFactory().getTipoDireccionVOBuilder().fromTipoDireccion(tipoDireccion).build(),
				"mensajes":"Se encontró tipo de dirección con código {}".format(codigo)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró tipo de dirección con código {}".format(codigo)
			}

		return data;