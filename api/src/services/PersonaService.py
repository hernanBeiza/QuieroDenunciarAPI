from ..app import db
from termcolor import colored

from ..daos.models.Persona import Persona
from ..daos.PersonaDAO import PersonaDAO
from .vos.PersonaVO import PersonaVO
from .builder.VOBuilderFactory import VOBuilderFactory

class PersonaService():

	#def __init__(self):
		#print('PersonaService')

	@staticmethod
	def guardar(request):
		print(colored("PersonaService: guardar(); {}".format(request.get_json()), 'cyan'))
		rut = request.get_json()["rut"] if 'rut' in request.get_json() else None
		dv = request.get_json()["dv"] if 'dv' in request.get_json() else None
		nombre = request.get_json()["nombre"] if 'nombre' in request.get_json() else None
		nombreSegundo = request.get_json()["nombreSegundo"] if 'nombreSegundo' in request.get_json() else None
		apellidoPaterno = request.get_json()["apellidoPaterno"] if 'apellidoPaterno' in request.get_json() else None
		apellidoMaterno = request.get_json()["apellidoMaterno"] if 'apellidoMaterno' in request.get_json() else None
		codigoTipoPersona = request.get_json()["codigoTipoPersona"] if 'codigoTipoPersona' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(rut==None):
			enviar = False
			mensajes +="\nRut"
		if(dv==None):
			enviar = False
			mensajes +="\nDV"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre"
		if(codigoTipoPersona==None):
			enviar = False
			mensajes +="\nTipo de persona"

		if(enviar):
			personaVO = PersonaVO()
			personaVO.rut = rut
			personaVO.dv = dv
			personaVO.nombre = nombre
			personaVO.nombreSegundo = nombreSegundo
			personaVO.apellidoPaterno = apellidoPaterno
			personaVO.apellidoMaterno = apellidoMaterno
			personaVO.codigoTipoPersona = codigoTipoPersona
			respuesta = PersonaDAO.guardar(personaVO)
			if(respuesta["result"]):
				respuesta["persona"] = VOBuilderFactory().getPersonaVOBuilder().fromPersona(respuesta["persona"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("PersonaService: obtener();", 'cyan'))
		personas = PersonaDAO.obtener()
		if len(personas)>0:
			data = {
				"result":True,
				"personas":VOBuilderFactory().getPersonaVOBuilder().fromPersonas(personas).builds(),
				"mensajes":"Se encontraron personas"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron personas"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("PersonaService: obtenerSegunId(); {}".format(id), 'cyan'))
		persona = PersonaDAO.obtenerSegunId(id)
		if(persona):
			data = {
				"result":True,
				"persona":VOBuilderFactory().getPersonaVOBuilder().fromPersona(persona).build(),
				"mensajes":"Se encontró persona con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró persona con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunRut(rut):
		print(colored("PersonaService: obtenerSegunRut(); {}".format(rut), 'cyan'))
		persona = PersonaDAO.obtenerSegunRut(rut)
		if(persona):
			data = {
				"result":True,
				"persona":VOBuilderFactory().getPersonaVOBuilder().fromPersona(persona).build(),
				"mensajes":"Se encontró persona con rut {}".format(rut)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró persona con rut {}".format(rut)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("PersonaService: actualizar(); {}".format(request.get_json()), 'cyan'))
		id = request.get_json()["id"] if 'id' in request.get_json() else None
		rut = request.get_json()["rut"] if 'rut' in request.get_json() else None
		dv = request.get_json()["dv"] if 'dv' in request.get_json() else None
		nombre = request.get_json()["nombre"] if 'nombre' in request.get_json() else None
		nombreSegundo = request.get_json()["nombreSegundo"] if 'nombreSegundo' in request.get_json() else None
		apellidoPaterno = request.get_json()["apellidoPaterno"] if 'apellidoPaterno' in request.get_json() else None
		apellidoMaterno = request.get_json()["apellidoMaterno"] if 'apellidoMaterno' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		codigoTipoPersona = request.get_json()["codigoTipoPersona"] if 'codigoTipoPersona' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(rut==None):
			enviar = False
			mensajes +="\nRut"
		if(dv==None):
			enviar = False
			mensajes +="\nDV"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre"
		if(codigoTipoPersona==None):
			enviar = False
			mensajes +="\nTipo de persona"

		if(enviar):
			personaVO = PersonaVO()
			personaVO.id = id
			personaVO.rut = rut
			personaVO.dv = dv
			personaVO.nombre = nombre
			personaVO.nombreSegundo = nombreSegundo
			personaVO.apellidoPaterno = apellidoPaterno
			personaVO.apellidoMaterno = apellidoMaterno
			personaVO.fechaCreacion = fechaCreacion
			personaVO.fechaModificacion = fechaModificacion
			personaVO.codigoTipoPersona = codigoTipoPersona
			respuesta = PersonaDAO.actualizar(personaVO)
			if(respuesta["result"]):
				respuesta["persona"] = VOBuilderFactory().getPersonaVOBuilder().fromPersona(respuesta["persona"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("PersonaService: eliminar(); {}".format(id), 'cyan'))
		respuesta = PersonaDAO.eliminar(id)
		return respuesta
