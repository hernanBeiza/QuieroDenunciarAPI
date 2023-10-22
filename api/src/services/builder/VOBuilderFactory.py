from src.services.builder.AntecedenteVOBuilder import AntecedenteVOBuilder
from src.services.builder.ArchivoVOBuilder import ArchivoVOBuilder
from src.services.builder.ComunaVOBuilder import ComunaVOBuilder
from src.services.builder.DenunciaMateriaVOBuilder import DenunciaMateriaVOBuilder
from src.services.builder.DenunciaVOBuilder import DenunciaVOBuilder
from src.services.builder.DireccionVOBuilder import DireccionVOBuilder
from src.services.builder.MateriaVOBuilder import MateriaVOBuilder
from src.services.builder.ParteVOBuilder import ParteVOBuilder
from src.services.builder.PersonaVOBuilder import PersonaVOBuilder
from src.services.builder.TipoArchivoVOBuilder import TipoArchivoVOBuilder
from src.services.builder.TipoDireccionVOBuilder import TipoDireccionVOBuilder
from src.services.builder.TipoParteVOBuilder import TipoParteVOBuilder
from src.services.builder.TipoPersonaVOBuilder import TipoPersonaVOBuilder

class VOBuilderFactory():

	#def __init__(self):

	@staticmethod
	def VOBuilderFactory():
		print("VOBuilderFactory")

	@staticmethod
	def getAntecedenteVOBuilder():
		return AntecedenteVOBuilder()

	@staticmethod
	def getArchivoVOBuilder():
		return ArchivoVOBuilder()

	@staticmethod
	def getComunaVOBuilder():
		return ComunaVOBuilder()

	@staticmethod
	def getDenunciaMateriaVOBuilder():
		return DenunciaMateriaVOBuilder()

	@staticmethod
	def getDenunciaVOBuilder():
		return DenunciaVOBuilder()

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
	def getTipoDireccionVOBuilder():
		return TipoDireccionVOBuilder()

	@staticmethod
	def getTipoParteVOBuilder():
		return TipoParteVOBuilder()

	@staticmethod
	def getTipoPersonaVOBuilder():
		return TipoPersonaVOBuilder()

