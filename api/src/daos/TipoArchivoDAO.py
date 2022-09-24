from termcolor import colored

from ..app import db
from ..daos.models.TipoArchivo import TipoArchivo

class TipoArchivoDAO():

	#def __init__(self):
		#print('MateriaDAO')

	@staticmethod
	def obtener():
		print(colored("TipoArchivoDAO: obtener();", 'yellow'))
		return TipoArchivo.query.all()

	@staticmethod
	def obtenerSegunCodigo(codigoTipoArchivo):
		print(colored("TipoArchivoDAO: obtenerSegunCodigo(); {}".format(codigoTipoArchivo), 'yellow'))
		return TipoArchivo.query.get(codigoTipoArchivo)
