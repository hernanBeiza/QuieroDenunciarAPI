from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.daos.models.Rol import Rol

class RolVOBuilder(ma.ModelSchema):

	class Meta:
		model = Rol
		ordered = True

	archivo = None
	archivos = None

	#Schema
	##Modelo - Dato a mostrar
	cod_rol = fields.Integer(data_key="codigo")
	glosa = fields.String(data_key="glosa")
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromRol(rol):
		RolVOBuilder.rol = rol
		return RolVOBuilder()

	@staticmethod
	def fromRoles(roles):
		RolVOBuilder.roles = roles
		return RolVOBuilder()

	@staticmethod
	def build():		
		if(RolVOBuilder.rol is None):
			print("No se puede contruir RolVO")
			return None
		else:
			try:
				return RolVOBuilder().dump(RolVOBuilder.rol)
			except Exception as e:
				print(colored("No se puede contruir RolVO. Error en RolVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(RolVOBuilder.roles is None):
			print("No se puede contruir RolVO. roles is None")
			return None
		else:
			try:
				return RolVOBuilder(many=True).dump(RolVOBuilder.roles)
			except Exception as e:
				print(colored("No se puede contruir RolVO. Error en RolVOBuilder; {}".format(e), 'red'))
