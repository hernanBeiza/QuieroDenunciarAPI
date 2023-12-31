from mysql.connector.errors import IntegrityError
from sqlalchemy.exc import IntegrityError
from termcolor import colored

from src.db import db
from src.daos.models.Usuario import Usuario

class UsuarioDAO():

	#def __init__(self):
		#print('UsuarioDAO')

	@staticmethod
	def guardar(usuarioVO):
		print(colored("UsuarioDAO: guardar(); {}".format(usuarioVO), 'magenta'))
		try:
			usuario = Usuario(None, usuarioVO.codigoRol, usuarioVO.nombre, usuarioVO.usuario, usuarioVO.contrasena, usuarioVO.fechaCreacion, usuarioVO.fechaModificacion, 2)
			db.session.add(usuario)
			db.session.commit()
			print(colored("UsuarioDAO: usuario guardado correctamente", 'magenta'))
			result = True
			mensajes = "Usuario guardado correctamente"
			respuesta = {"result": result,"mensajes": mensajes, "usuario": usuario}
			return respuesta
		except IntegrityError as e:
			error = "UsuarioDAO: El usuario no se pudo guardar. Error: {}".format(e.orig)
			errorVisualizable = "El usuario no se pudo guardar"
			if "Duplicate entry" in str(e.orig):
				errorVisualizable = "El usuario no se pudo guardar. Ya existe"
			print(colored(error, 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			respuesta = {"result": result, "error": errorVisualizable, "codigo": 500}
			raise Exception(error, respuesta)

	@staticmethod
	def obtener():
		print(colored("UsuarioDAO: obtener();", 'yellow'))
		return Usuario.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("UsuarioDAO: obtenerSegunId(); {}".format(id), 'magenta'))
		return Usuario.query.get(id)

	@staticmethod
	def obtenerSegunUsuarioContrasena(usuario, contrasena):
		print(colored("UsuarioDAO: obtenerSegunUsuarioContrasena(); {} {}".format(usuario, contrasena), 'magenta'))
		return Usuario.query.filter_by(usuario=usuario, contrasena=contrasena).first()

	@staticmethod
	def actualizar(usuarioVO):
		print(colored("UsuarioDAO: actualizar(); {}".format(usuarioVO), 'magenta'))
		try:
			usuario = Usuario.query.get(usuarioVO.id)
			usuario.cod_tipo_persona = usuarioVO.codigoRol
			usuario.nombre = usuarioVO.nombre
			usuario.usuario = usuarioVO.usuario
			usuario.contrasena = usuarioVO.contrasena
			#usuario.fecha_creacion = usuarioVO.fechaCreacion
			#persona.fecha_modificacion = personaVO.fechaModificacion
			db.session.commit()
			print(colored("UsuarioDAO: persona editada correctamente", 'magenta'))
			result = True
			mensajes = "Usuario editado correctamente"
			respuesta = {"result": result, "mensajes": mensajes, "usuario": usuario}
		except Exception as e:
			print(colored("UsuarioDAO: El usuario con id {} no se pudo editar. Error: {}".format(usuarioVO.id, e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			error = "El usuario no se pudo editar"
			respuesta = {"result": result, "error": error}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("UsuarioDAO: eliminar(); {}".format(id), 'magenta'))
		persona = Usuario.query.get(id)
		if(persona is not None):
			try:
				result = True
				mensajes = "Usuario con id {} eliminada correctamente".format(id)
				db.session.delete(persona)
				db.session.commit()
				respuesta = {"result": result, "mensajes": mensajes}
			except Exception as e:
				print(colored("UsuarioDAO: El usuario con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "El usuario con id {} no se pudo eliminar".format(id)
				respuesta = {"result": result, "errores": mensajes}
		else:
			result = False
			mensajes = "El usuario con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result": result, "errores": mensajes}
		return respuesta