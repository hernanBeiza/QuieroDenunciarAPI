from termcolor import colored

from src.daos.models.TipoPersona import TipoPersona
from src.daos.TipoPersonaDAO import TipoPersonaDAO
from src.services.vos.TipoPersonaVO import TipoPersonaVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class TipoPersonaService():

	#def __init__(self):
		#print('MateriaService')

	@staticmethod
	def obtener():
		print(colored("TipoPersonaService: obtener();", 'cyan'))
		tipoPersonas = TipoPersonaDAO.obtener()
		if len(tipoPersonas)>0:
			data = {
				"result":True,
				"tipoPersonas":VOBuilderFactory().getTipoPersonaVOBuilder().fromTipoPersonas(tipoPersonas).builds(),
				"mensajes":"Se encontraron tipos de personas"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron tipos de personas"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(codigo):
		print(colored("TipoPersonaService: obtenerSegunCodigo(); {}".format(codigo), 'cyan'))
		tipoPersona = TipoPersonaDAO.obtenerSegunCodigo(codigo)
		if(tipoPersona):
			data = {
				"result":True,
				"tipoPersona":VOBuilderFactory().getTipoPersonaVOBuilder().fromTipoPersona(tipoPersona).build(),
				"mensajes":"Se encontró tipo de persona con código {}".format(codigo)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró tipo de persona con código {}".format(codigo)
			}

		return data;