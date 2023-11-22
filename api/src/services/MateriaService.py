from termcolor import colored

from src.daos.models.Materia import Materia
from src.daos.MateriaDAO import MateriaDAO
from src.services.vos.MateriaVO import MateriaVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class MateriaService():

	#def __init__(self):
		#print('MateriaService')

	@staticmethod
	def obtener():
		print(colored("MateriaService: obtener();", 'cyan'))
		materias = MateriaDAO.obtener()
		if len(materias)>0:
			data = {
				"result":True,
				"materias":VOBuilderFactory().getMateriaVOBuilder().fromMaterias(materias).builds(),
				"mensajes":"Se encontraron materias"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron materias"
			}

		return data

	@staticmethod
	def obtenerConPagina(pagina):
		print(colored("MateriaService: obtenerConPagina();", 'cyan'))
		materias = MateriaDAO.obtenerConPagina(pagina)

		if len(materias)>0:
			data = {
				"result":True,
				"materias":VOBuilderFactory().getMateriaVOBuilder().fromMaterias(materias).builds(),
				"mensajes":"Se encontraron materias"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron materias"
			}

		return data

	@staticmethod
	def obtenerSegunCodigo(codigoMateria):
		print(colored("MateriaService: obtenerSegunCodigo(); {}".format(codigoMateria), 'cyan'))
		materia = MateriaDAO.obtenerSegunCodigo(codigoMateria)
		if(materia):
			data = {
				"result":True,
				"materias":VOBuilderFactory().getMateriaVOBuilder().fromMateria(materia).build(),
				"mensajes":"Se encontró materia con código {}".format(codigoMateria)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró materia con código {}".format(codigoMateria)
			}

		return data;