from termcolor import colored

from src.app import db
from src.daos.models.Persona import Persona

class PersonaDAO():

	#def __init__(self):
		#print('PersonaDAO')

	@staticmethod
	def guardar(personaVO):
		print(colored("PersonaDAO: guardar(); {}".format(personaVO), 'yellow'))
		try:
			persona = Persona(None, personaVO.rut, personaVO.dv, personaVO.nombre, personaVO.nombreSegundo, personaVO.apellidoPaterno, personaVO.apellidoMaterno, personaVO.fechaCreacion, personaVO.fechaModificacion, personaVO.codigoTipoPersona, 1)
			db.session.add(persona)
			db.session.commit()
			print(colored("PersonaDAO: persona guardada correctamente", 'yellow'))
			result = True
			mensajes = "Persona guardada correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "persona":persona}
		except Exception as e:
			print(colored("PersonaDAO: La persona no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La persona no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("PersonaDAO: obtener();", 'yellow'))
		return Persona.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("PersonaDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Persona.query.get(id)

	@staticmethod
	def obtenerSegunRut(rut):
		print(colored("PersonaDAO: obtenerSegunRut(); {}".format(rut), 'yellow'))
		return Persona.query.filter_by(rut=rut).all()

	@staticmethod
	def actualizar(personaVO):
		print(colored("PersonaDAO: actualizar(); {}".format(personaVO), 'yellow'))
		try:
			persona = Persona.query.get(personaVO.id)
			persona.rut = personaVO.rut
			persona.dv = personaVO.dv
			persona.nombre = personaVO.nombre
			persona.nombre_segundo = personaVO.nombreSegundo
			persona.apellido_paterno = personaVO.apellidoPaterno
			persona.apellido_materno = personaVO.apellidoMaterno
			persona.fecha_creacion = personaVO.fechaCreacion
			#persona.fecha_modificacion = personaVO.fechaModificacion
			persona.cod_tipo_persona = personaVO.codigoTipoPersona
			db.session.commit()
			print(colored("PersonaDAO: persona editada correctamente", 'yellow'))
			result = True
			mensajes = "Persona editada correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "persona":persona}
		except Exception as e:
			print(colored("PersonaDAO: La persona con id {} no se pudo editar. Error: {}".format(personaVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La persona no se pudo editar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("PersonaDAO: eliminar(); {}".format(id), 'yellow'))
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