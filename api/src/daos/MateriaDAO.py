from termcolor import colored

from src.daos.models.Materia import Materia

class MateriaDAO():

	#def __init__(self):
		#print('MateriaDAO')

	@staticmethod
	def obtener():
		print(colored("MateriaDAO: obtener();", 'yellow'))
		return Materia.query.all()

	@staticmethod
	def obtenerConPagina(pagina):
		print(colored("MateriaDAO: obtenerConPagina();", 'yellow'))
		totalPorPagina = 2
		return Materia.query.paginate(pagina,int(totalPorPagina), False).items

	@staticmethod
	def obtenerSegunCodigo(codigoMateria):
		print(colored("MateriaDAO: obtenerSegunCodigo(); {}".format(codigoMateria), 'yellow'))
		return Materia.query.get(codigoMateria)
