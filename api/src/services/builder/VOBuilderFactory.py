from .ComunaVOBuilder import ComunaVOBuilder
from .MateriaVOBuilder import MateriaVOBuilder
from .TipoArchivoVOBuilder import TipoArchivoVOBuilder
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
	def getTipoArchivoVOBuilder():
		return TipoArchivoVOBuilder()

	@staticmethod
	def getTipoPersonaVOBuilder():
		return TipoPersonaVOBuilder()

