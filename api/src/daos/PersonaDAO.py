#from mysql.connector.errors import IntegrityError
from sqlalchemy.exc import IntegrityError
from termcolor import colored

from src.db import db
from src.daos.models.Persona import Persona

class PersonaDAO():

	#def __init__(self):
		#print('PersonaDAO')

	@staticmethod
	def guardar(personaVO):
		print(colored("PersonaDAO: guardar(); {}".format(personaVO), 'magenta'))
		try:
			persona = Persona(None, personaVO.rut, personaVO.dv, personaVO.nombre, personaVO.nombreSegundo, personaVO.apellidoPaterno, personaVO.apellidoMaterno, personaVO.fechaCreacion, personaVO.fechaModificacion, personaVO.codigoTipoPersona, 1)
			db.session.add(persona)
			db.session.commit()
			print(colored("PersonaDAO: persona guardada correctamente", 'magenta'))
			result = True
			mensajes = "Persona guardada correctamente"
			respuesta = {"result": result,"mensajes": mensajes, "persona": persona}
			return respuesta
		except IntegrityError as e:
			error = "PersonaDAO: La persona no se pudo guardar. Error: {}".format(e.orig)
			errorVisualizable = "La persona no se pudo guardar"
			if "Duplicate entry" in str(e.orig):
				errorVisualizable = "La persona no se pudo guardar. Ya existe una persona con ese RUT ingresada"
			print(colored(error, 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			respuesta = {"result": result, "error": errorVisualizable, "codigo": 500}
			raise Exception(error, respuesta)

	@staticmethod
	def obtener():
		print(colored("PersonaDAO: obtener();", 'yellow'))
		return Persona.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("PersonaDAO: obtenerSegunId(); {}".format(id), 'magenta'))
		return Persona.query.get(id)

	@staticmethod
	def obtenerSegunRut(rut):
		print(colored("PersonaDAO: obtenerSegunRut(); {}".format(rut), 'magenta'))
		return Persona.query.filter_by(rut=rut).first()

	@staticmethod
	def actualizar(personaVO):
		print(colored("PersonaDAO: actualizar(); {}".format(personaVO), 'magenta'))
		try:
			persona = Persona.query.get(personaVO.id)
			persona.cod_tipo_persona = personaVO.codigoTipoPersona
			persona.rut = personaVO.rut
			persona.dv = personaVO.dv
			persona.nombre = personaVO.nombre
			persona.nombre_segundo = personaVO.nombreSegundo
			persona.apellido_paterno = personaVO.apellidoPaterno
			persona.apellido_materno = personaVO.apellidoMaterno
			persona.fecha_creacion = personaVO.fechaCreacion
			#persona.fecha_modificacion = personaVO.fechaModificacion
			db.session.commit()
			print(colored("PersonaDAO: persona editada correctamente", 'magenta'))
			result = True
			mensajes = "Persona editada correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "persona":persona}
		except Exception as e:
			print(colored("PersonaDAO: La persona con id {} no se pudo editar. Error: {}".format(personaVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			error = "La persona no se pudo editar"
			respuesta = {"result": result, "error": error}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("PersonaDAO: eliminar(); {}".format(id), 'magenta'))
		persona = Persona.query.get(id)
		if(persona is not None):
			try:
				result = True
				mensajes = "Persona con id {} eliminada correctamente".format(id)
				db.session.delete(persona)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("PersonaDAO: La persona con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "La Persona con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "La Persona con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta