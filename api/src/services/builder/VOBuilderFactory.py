from src.services.builder.ComunaVOBuilder import ComunaVOBuilder
from src.services.builder.DireccionVOBuilder import DireccionVOBuilder
from src.services.builder.MateriaVOBuilder import MateriaVOBuilder
from src.services.builder.ParteVOBuilder import ParteVOBuilder
from src.services.builder.PersonaVOBuilder import PersonaVOBuilder
from src.services.builder.TipoArchivoVOBuilder import TipoArchivoVOBuilder
from src.services.builder.TipoParteVOBuilder import TipoParteVOBuilder
from src.services.builder.TipoPersonaVOBuilder import TipoPersonaVOBuilder

class VOBuilderFactory():

	#def __init__(self):

	@staticmethod
	def VOBuilderFactory():
		print("VOBuilderFactory")

	@staticmethod
	def getComunaVOBuilder():
		return ComunaVOBuilder()

	@staticmethod
	def getDireccionVOBuilder():
		return DireccionVOBuilder()

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

