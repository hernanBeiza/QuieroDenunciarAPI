from termcolor import colored
import os

from src.daos.models.Rol import Rol

class RolDAO():

	#def __init__(self):
		#print('RolDAO')

	@staticmethod
	def obtener():
		print(colored("RolDAO: obtener();", 'yellow'))
		return Rol.query.all()

	@staticmethod
	def obtenerSegunCodigo(codigo):
		print(colored("RolDAO: obtenerSegunCodigo(); {}".format(codigo), 'yellow'))
		return Rol.query.get(codigo)
