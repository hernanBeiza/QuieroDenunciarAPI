from src.app import db
from termcolor import colored

from src.daos.models.EstadoDenuncia import EstadoDenuncia
from src.daos.EstadoDenunciaDAO import EstadoDenunciaDAO
from src.services.vos.EstadoDenunciaVO import EstadoDenunciaVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class EstadoDenunciaService():

	#def __init__(self):
		#print('EstadoDenunciaService')

	@staticmethod
	def obtener():
		print(colored("EstadoDenunciaService: obtener();", 'cyan'))
		estadosDenuncias = EstadoDenunciaDAO.obtener()
		if len(estadosDenuncias)>0:
			data = {
				"result":True,
				"estadosDenuncias":VOBuilderFactory().getEstadoDenunciaVOBuilder().fromEstadosDenuncias(estadosDenuncias).builds(),
				"mensajes":"Se encontraron estados de denuncias"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron estados de denuncia"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(codigo):
		print(colored("EstadoDenunciaService: obtenerSegunCodigo(); {}".format(codigo), 'cyan'))
		estadoDenuncia = EstadoDenunciaDAO.obtenerSegunCodigo(codigo)
		if(estadoDenuncia):
			data = {
				"result":True,
				"estadoDenuncia":VOBuilderFactory().getEstadoDenunciaVOBuilder().fromEstadoDenuncia(estadoDenuncia).build(),
				"mensajes":"Se encontró estado de denuncia con código {}".format(codigo)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró estado de denuncia con código {}".format(codigo)
			}

		return data;