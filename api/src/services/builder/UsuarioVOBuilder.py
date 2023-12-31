from marshmallow import fields
from termcolor import colored

from src.ma import ma
from src.services.vos.UsuarioVO import UsuarioVO
from src.daos.models.Usuario import Usuario
from src.services.builder.RolVOBuilder import RolVOBuilder

class UsuarioVOBuilder(ma.ModelSchema):

	class Meta:
		model = Usuario
		ordered = True
		exclude=['contrasena']

	usuario = None
	usuarios = None

	#Schema
	##Modelo - Dato a mostrar
	id_usuario = fields.Integer(data_key="id")
	cod_rol = fields.Integer(data_key="codigoRol")
	nombre = fields.String()
	usuario = fields.String()
	contrasena = fields.String()
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")
	rol = fields.Nested(RolVOBuilder)

	#def __init__(self):

	@staticmethod
	def fromUsuario(usuario):
		UsuarioVOBuilder.usuario = usuario
		return UsuarioVOBuilder()

	@staticmethod
	def fromUsuarios(usuarios):
		UsuarioVOBuilder.usuarios = usuarios
		return UsuarioVOBuilder()

	@staticmethod
	def build():		
		if(UsuarioVOBuilder.usuario is None):
			print("No se puede contruir UsuarioVO")
			return None
		else:
			try:
				return UsuarioVOBuilder().dump(UsuarioVOBuilder.usuario)
			except Exception as e:
				print(colored("No se puede contruir UsuarioVO. Error en UsuarioVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(UsuarioVOBuilder.usuarios is None):
			print("No se puede contruir UsuarioVO. usuarios is None")
			return None
		else:
			try:
				return UsuarioVOBuilder(many=True).dump(UsuarioVOBuilder.usuarios)
			except Exception as e:
				print(colored("No se puede contruir UsuarioVO. Error en UsuarioVOBuilder: {}".format(e), 'red'))
