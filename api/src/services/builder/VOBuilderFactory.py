from .ComunaVOBuilder import ComunaVOBuilder
from .MateriaVOBuilder import MateriaVOBuilder
from .ParteVOBuilder import ParteVOBuilder
from .PersonaVOBuilder import PersonaVOBuilder
from .TipoArchivoVOBuilder import TipoArchivoVOBuilder
from .TipoParteVOBuilder import TipoParteVOBuilder
from .TipoPersonaVOBuilder import TipoPersonaVOBuilder

class VOBuilderFactory():

	#def __init__(self):

	@staticmethod
	def VOBuilderFactory():
		print("VOBuilderFactory")

	@staticmethod
	def getComunaVOBuilder():
		return ComunaVOBuilder()

	@staticmethod
	def getMateriaVOBuilder():
		return MateriaVOBuilder()

	@staticmethod
	def getParteVOBuilder():
		return ParteVOBuilder()

	@staticmethod
	def getPersonaVOBuilder():
		return PersonaVOBuilder()

	@staticmethod
	def getTipoArchivoVOBuilder():
		return TipoArchivoVOBuilder()

	@staticmethod
	def getTipoParteVOBuilder():
		return TipoParteVOBuilder()


	@staticmethod
	def getTipoPersonaVOBuilder():
		return TipoPersonaVOBuilder()

