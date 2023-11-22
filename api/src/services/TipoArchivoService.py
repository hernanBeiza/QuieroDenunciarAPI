from src.run import db
from termcolor import colored

from src.daos.models.TipoArchivo import TipoArchivo
from src.daos.TipoArchivoDAO import TipoArchivoDAO
from src.services.vos.TipoArchivoVO import TipoArchivoVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class TipoArchivoService():

	#def __init__(self):
		#print('MateriaService')

	@staticmethod
	def obtener():
		print(colored("TipoArchivoService: obtener();", 'cyan'))
		tipoArchivos = TipoArchivoDAO.obtener()
		if len(tipoArchivos)>0:
			data = {
				"result":True,
				"tipoArchivos":VOBuilderFactory().getTipoArchivoVOBuilder().fromTipoArchivos(tipoArchivos).builds(),
				"mensajes":"Se encontraron tipoArchivos"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron tipos de archivo"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(codigo):
		print(colored("TipoArchivoService: obtenerSegunCodigo(); {}".format(codigo), 'cyan'))
		tipoArchivo = TipoArchivoDAO.obtenerSegunCodigo(codigo)
		if(tipoArchivo):
			data = {
				"result":True,
				"tipoArchivo":VOBuilderFactory().getTipoArchivoVOBuilder().fromTipoArchivo(tipoArchivo).build(),
				"mensajes":"Se encontró tipo de archivo con código {}".format(codigo)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró tipo de archivo con código {}".format(codigo)
			}

		return data;