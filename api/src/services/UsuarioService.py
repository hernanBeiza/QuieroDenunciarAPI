from termcolor import colored
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
import bcrypt

from src.daos.UsuarioDAO import UsuarioDAO
from src.services.vos.UsuarioVO import UsuarioVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class UsuarioService():

	#def __init__(self):
		#print('UsuarioService')

	@staticmethod
	def guardar(request):
		print(colored("UsuarioService: guardar(); {}".format(request.get_json()), 'cyan'))
		codigoRol = request.get_json()["codigoRol"] if 'codigoRol' in request.get_json() else None
		nombre = request.get_json()["nombre"] if 'nombre' in request.get_json() else None
		usuario = request.get_json()["usuario"] if 'usuario' in request.get_json() else None
		contrasena = request.get_json()["contrasena"] if 'contrasena' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"

		if(codigoRol==None):
			enviar = False
			mensajes +="\nTipo de usuario"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre de usuario"
		if(usuario==None):
			enviar = False
			mensajes +="\nUsuario"
		if(contrasena==None):
			enviar = False
			mensajes +="\nContraseña"

		if(enviar):
			usuarioVO = UsuarioVO()
			usuarioVO.codigoRol = codigoRol
			usuarioVO.nombre = nombre
			usuarioVO.usuario = usuario
			usuarioVO.contrasena = bcrypt.hashpw(contrasena.encode('utf8'), bcrypt.gensalt())
			respuesta = UsuarioDAO.guardar(usuarioVO)
			if(respuesta["result"]):
				respuesta["usuario"] = VOBuilderFactory().getUsuarioVOBuilder().fromUsuario(respuesta["usuario"]).build()
			else:
				respuesta = {"result": False, "errores": respuesta["errores"]}
		else:
			respuesta = {"result": False, "errores": mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("UsuarioService: obtener();", 'cyan'))
		usuarios = UsuarioDAO.obtener()
		if len(usuarios) > 0:
			data = {
				"result":True,
				"usuarios": VOBuilderFactory().getUsuarioVOBuilder().fromUsuarios(usuarios).builds(),
				"mensajes": "Se encontraron usuarios"
			}
		else:
			data = {
				"result": False,
				"errores": "No se encontraron usuarios"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("UsuarioService: obtenerSegunId(); {}".format(id), 'cyan'))
		usuario = UsuarioDAO.obtenerSegunId(id)
		if(usuario):
			data = {
				"result": True,
				"usuario": VOBuilderFactory().getUsuarioVOBuilder().fromUsuario(usuario).build(),
				"mensajes": "Se encontró usuario con id {}".format(id)
			}
		else:
			data = {
				"result": False,
				"errores": "No se encontró usuario con id {}".format(id)
			}

		return data

	@staticmethod
	def iniciarSesion(request):
		print(colored("UsuarioService: iniciarSesion(); {}".format(request.get_json()), 'cyan'))
		usuario = request.get_json()["usuario"] if 'usuario' in request.get_json() else None
		contrasena = request.get_json()["contrasena"] if 'contrasena' in request.get_json() else None

		usuarioEncontrado = UsuarioDAO.obtenerSegunUsuario(usuario)
		if(usuarioEncontrado):
			if bcrypt.checkpw(contrasena.encode("utf8"), usuarioEncontrado.contrasena.encode("utf8")):
				token = create_access_token(identity=usuarioEncontrado.id_usuario)
				data = {
					"result": True,
					"usuario": VOBuilderFactory().getUsuarioVOBuilder().fromUsuario(usuarioEncontrado).build(),
					"token": token,
					"mensajes": "Bienvenido {}".format(usuario)
				}
			else:
				data = {
					"result": False,
					"errores": "No se encontró usuario"
				}				
		else:
			data = {
				"result": False,
				"errores": "No se encontró usuario"
			}

		return data

	@staticmethod
	def actualizar(request):
		print(colored("UsuarioService: actualizar(); {}".format(request.get_json()), 'cyan'))
		id = request.get_json()["id"] if 'id' in request.get_json() else None
		codigoRol = request.get_json()["codigoRol"] if 'codigoRol' in request.get_json() else None
		nombre = request.get_json()["nombre"] if 'nombre' in request.get_json() else None
		usuario = request.get_json()["usuario"] if 'usuario' in request.get_json() else None
		contrasena = request.get_json()["contrasena"] if 'contrasena' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(codigoRol==None):
			enviar = False
			mensajes +="\nTipo de usuario"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre de usuario"
		if(usuario==None):
			enviar = False
			mensajes +="\nUsuario"
		if(contrasena==None):
			enviar = False
			mensajes +="\nContraseña"

		if(enviar):
			usuarioVO = UsuarioVO()
			usuarioVO.id = id
			usuarioVO.codigoTipoPersona = codigoRol
			usuarioVO.nombre = nombre
			usuarioVO.usuario = usuario
			usuarioVO.contrasena = bcrypt.hashpw(contrasena.encode('utf8'), bcrypt.gensalt())
			usuarioVO.fechaCreacion = fechaCreacion
			respuesta = UsuarioDAO.actualizar(usuarioVO)
			if(respuesta["result"]):
				respuesta["usuario"] = VOBuilderFactory().getUsuarioVOBuilder().fromUsuario(respuesta["usuario"]).build()
			else:
				respuesta = {"result": False, "errores": respuesta["errores"]}
		else:
			respuesta = {"result": False, "errores": mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("UsuarioService: eliminar(); {}".format(id), 'cyan'))
		respuesta = UsuarioDAO.eliminar(id)
		return respuesta
