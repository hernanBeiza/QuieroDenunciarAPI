from termcolor import colored

from ..app import db
from ..daos.models.Materia import Materia

class MateriaDAO():

	#def __init__(self):
		#print('MateriaDAO')

	@staticmethod
	def obtener():
		print(colored("MateriaDAO: obtener();", 'yellow'))
		materias = Materia.query.all()
		return materias

	@staticmethod
	def obtenerConPagina(pagina):
		print(colored("MateriaDAO: obtenerConPagina();", 'yellow'))
		totalPorPagina = 2
		materias = Materia.query.paginate(pagina,int(totalPorPagina), False).items
		return materias

	@staticmethod
	def obtenerSegunCodigo(codigoMateria):
		print(colored("MateriaDAO: obtenerSegunCodigo(); {}".format(codigoMateria), 'yellow'))
		materiaEncontrada = Materia.query.get(codigoMateria)
		return materiaEncontrada