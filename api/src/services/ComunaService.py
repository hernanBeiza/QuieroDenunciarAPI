from termcolor import colored

from src.daos.models.Comuna import Comuna
from src.daos.ComunaDAO import ComunaDAO
from src.services.vos.ComunaVO import ComunaVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class ComunaService():

	#def __init__(self):
		#print('MateriaService')

	@staticmethod
	def obtener():
		print(colored("ComunaService: obtener();", 'cyan'))
		comunas = ComunaDAO.obtener()
		if len(comunas)>0:
			data = {
				"result":True,
				"comunas":VOBuilderFactory().getComunaVOBuilder().fromComunas(comunas).builds(),
				"mensajes":"Se encontraron comunas"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron comunas"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(idComuna):
		print(colored("ComunaService: obtenerSegunCodigo(); {}".format(idComuna), 'cyan'))
		comuna = ComunaDAO.obtenerSegunCodigo(idComuna)
		if(comuna):
			data = {
				"result":True,
				"comuna":VOBuilderFactory().getComunaVOBuilder().fromComuna(comuna).build(),
				"mensajes":"Se encontró comuna con código {}".format(idComuna)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró comuna con código {}".format(idComuna)
			}

		return data;

	@staticmethod
	def obtenerSegunIdProvincia(idProvincia):
		print(colored("ComunaService: obtenerSegunIdProvincia(); {}".format(idProvincia), 'cyan'))
		comunas = ComunaDAO.obtenerSegunIdProvincia(idProvincia)
		if len(comunas)>0:
			data = {
				"result":True,
				"comunas":VOBuilderFactory().getComunaVOBuilder().fromComunas(comunas).builds(),
				"mensajes":"Se encontraron comuna con id provincia {}".format(idProvincia)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró comunas la provincia con id {}".format(idProvincia)
			}

		return data;