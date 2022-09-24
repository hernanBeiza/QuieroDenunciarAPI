from termcolor import colored

from ..app import db
from ..daos.models.Comuna import Comuna

class ComunaDAO():

	#def __init__(self):
		#print('ComunaDAO')

	@staticmethod
	def obtener():
		print(colored("ComunaDAO: obtener();", 'yellow'))
		return Comuna.query.all()

	@staticmethod
	def obtenerSegunCodigo(idComuna):
		print(colored("ComunaDAO: obtenerSegunCodigo(); {}".format(idComuna), 'yellow'))
		return Comuna.query.get(idComuna)

	@staticmethod
	def obtenerSegunIdProvincia(idProvincia):
		print(colored("ComunaDAO: obtenerSegunIdProvincia(); {}".format(idProvincia), 'yellow'))
		return Comuna.query.filter_by(id_provincia=idProvincia).all()
