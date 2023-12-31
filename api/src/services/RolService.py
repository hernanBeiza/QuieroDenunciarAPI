
from termcolor import colored

from src.daos.RolDAO import RolDAO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class RolService():

	#def __init__(self):
		#print('RolService')

	@staticmethod
	def obtener():
		print(colored("RolService: obtener();", 'cyan'))
		roles = RolDAO.obtener()
		if len(roles) > 0:
			data = {
				"result": True,
				"roles": VOBuilderFactory().getRolVOBuilder().fromRoles(roles).builds(),
				"mensajes": "Se encontraron roles"
			}
		else:
			data = {
				"result": False,
				"errores": "No se encontraron roles"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(codigo):
		print(colored("RolService: obtenerSegunCodigo(); {}".format(codigo), 'cyan'))
		rol = RolDAO.obtenerSegunCodigo(codigo)
		if(rol):
			data = {
				"result": True,
				"rol": VOBuilderFactory().getRolVOBuilder().fromRol(rol).build(),
				"mensajes": "Se encontró rol con código {}".format(id)
			}
		else:
			data = {
				"result": False,
				"errores": "No se encontró rol con código {}".format(id)
			}

		return data
