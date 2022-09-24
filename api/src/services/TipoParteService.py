from ..app import db
from termcolor import colored

from ..daos.models.TipoParte import TipoParte
from ..daos.TipoParteDAO import TipoParteDAO
from .vos.TipoParteVO import TipoParteVO
from .builder.VOBuilderFactory import VOBuilderFactory

class TipoParteService():

	#def __init__(self):
		#print('TipoParteService')

	@staticmethod
	def obtener():
		print(colored("TipoParteService: obtener();", 'cyan'))
		tipoPartes = TipoParteDAO.obtener()
		if len(tipoPartes)>0:
			data = {
				"result":True,
				"tipoPartes":VOBuilderFactory().getTipoParteVOBuilder().fromTipoPartes(tipoPartes).builds(),
				"mensajes":"Se encontraron tipos de partes"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron tipos de partes"
			}
		return data

	@staticmethod
	def obtenerSegunCodigo(codigoTipoParte):
		print(colored("TipoParteService: obtenerSegunCodigo(); {}".format(codigoTipoParte), 'cyan'))
		tipoParte = TipoParteDAO.obtenerSegunCodigo(codigoTipoParte)
		if(tipoParte):
			data = {
				"result":True,
				"tipoParte":VOBuilderFactory().getTipoParteVOBuilder().fromTipoParte(tipoParte).build(),
				"mensajes":"Se encontró tipo de parte con código {}".format(codigoTipoParte)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró tipo de parte con código {}".format(codigoTipoParte)
			}

		return data;