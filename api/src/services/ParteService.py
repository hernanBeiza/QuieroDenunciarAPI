from src.app import db
from termcolor import colored

from src.daos.models.Parte import Parte
from src.daos.ParteDAO import ParteDAO
from src.services.vos.ParteVO import ParteVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class ParteService():

	#def __init__(self):
		#print('ParteService')

	@staticmethod
	def guardar(request):
		print(colored("ParteService: guardar(); {}".format(request.get_json()), 'cyan'))
		idPersona = request.get_json()["idPersona"] if 'idPersona' in request.get_json() else None
		idDireccion = request.get_json()["idDireccion"] if 'idDireccion' in request.get_json() else None
		codigoTipoParte = request.get_json()["codigoTipoParte"] if 'codigoTipoParte' in request.get_json() else None
		correo = request.get_json()["correo"] if 'correo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idPersona==None):
			enviar = False
			mensajes +="\nPersona"
		if(idDireccion==None):
			enviar = False
			mensajes +="\nDirección"
		if(codigoTipoParte==None):
			enviar = False
			mensajes +="\nCódigo de tipo de parte"

		if(enviar):
			parteVO = ParteVO()
			parteVO.idPersona = idPersona
			parteVO.idDireccion = idDireccion
			parteVO.codigoTipoParte = codigoTipoParte
			parteVO.correo = correo
			respuesta = ParteDAO.guardar(parteVO)
			if(respuesta["result"]):
				respuesta["parte"] = VOBuilderFactory().getParteVOBuilder().fromParte(respuesta["parte"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("ParteService: obtener();", 'cyan'))
		partes = ParteDAO.obtener()
		if len(partes)>0:
			data = {
				"result":True,
				"partes":VOBuilderFactory().getParteVOBuilder().fromPartes(partes).builds(),
				"mensajes":"Se encontraron partes"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron partes"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("ParteService: obtenerSegunId(); {}".format(id), 'cyan'))
		parte = ParteDAO.obtenerSegunId(id)
		if(parte):
			data = {
				"result":True,
				"parte":VOBuilderFactory().getParteVOBuilder().fromParte(parte).build(),
				"mensajes":"Se encontró parte con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró parte con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunIdPersona(idPersona):
		print(colored("ParteService: obtenerSegunIdPersona(); {}".format(idPersona), 'cyan'))
		parte = ParteDAO.obtenerSegunIdPersona(idPersona)
		if(parte):
			data = {
				"result":True,
				"parte":VOBuilderFactory().getParteVOBuilder().fromPartes(parte).builds(),
				"mensajes":"Se encontró parte con id de persona {}".format(idPersona)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró parte con id de persona {}".format(idPersona)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("ParteService: actualizar(); {}".format(request.get_json()), 'cyan'))
		id = request.get_json()["id"] if 'id' in request.get_json() else None
		idPersona = request.get_json()["idPersona"] if 'idPersona' in request.get_json() else None
		idDireccion = request.get_json()["idDireccion"] if 'idDireccion' in request.get_json() else None
		codigoTipoParte = request.get_json()["codigoTipoParte"] if 'codigoTipoParte' in request.get_json() else None
		correo = request.get_json()["correo"] if 'correo' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(idPersona==None):
			enviar = False
			mensajes +="\nPersona"
		if(idDireccion==None):
			enviar = False
			mensajes +="\nDirección"
		if(codigoTipoParte==None):
			enviar = False
			mensajes +="\nCódigo tipo de parte"
		if(enviar):
			parteVO = ParteVO()
			parteVO.id = id
			parteVO.idPersona = idPersona
			parteVO.idDireccion = idDireccion
			parteVO.codigoTipoParte = codigoTipoParte
			parteVO.correo = correo
			parteVO.fechaCreacion = fechaCreacion
			parteVO.fechaModificacion = fechaModificacion
			parteVO.flagActivo = flagActivo
			respuesta = ParteDAO.actualizar(parteVO)
			if(respuesta["result"]):
				respuesta["parte"] = VOBuilderFactory().getParteVOBuilder().fromParte(respuesta["parte"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("ParteService: eliminar(); {}".format(id), 'cyan'))
		respuesta = ParteDAO.eliminar(id)
		return respuesta
