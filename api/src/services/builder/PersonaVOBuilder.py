from marshmallow import Schema, fields
from termcolor import colored

from src.app import ma
from src.services.vos.PersonaVO import PersonaVO
from src.daos.models.Persona import Persona

class PersonaVOBuilder(ma.ModelSchema):

	class Meta:
		model = Persona
		ordered = True

	persona = None
	personas = None

	#Schema
	##Modelo - Dato a mostrar
	id = fields.Integer()
	rut = fields.Integer()
	dv = fields.String()
	nombre = fields.String()
	nombre_segundo = fields.String(data_key="nombreSegundo")
	apellido_paterno = fields.String(data_key="apellidoPaterno")
	apellido_materno = fields.String(data_key="apellidoMaterno")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	cod_tipo_persona = fields.Integer(data_key="codigoTipoPersona")
	flag_activo = fields.Integer(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromPersona(persona):		
		PersonaVOBuilder.persona = persona
		return PersonaVOBuilder()

	@staticmethod
	def fromPersonas(personas):		
		PersonaVOBuilder.personas = personas
		return PersonaVOBuilder()

	@staticmethod
	def build():		
		if(PersonaVOBuilder.persona is None):
			print("No se puede contruir PersonaVO")
			return None
		else:
			try:
				return PersonaVOBuilder().dump(PersonaVOBuilder.persona)
			except Exception as e:
				print(colored("No se puede contruir PersonaVO. Error en PersonaVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(PersonaVOBuilder.personas is None):
			print("No se puede contruir PersonaVO. personas is None")
			return None
		else:
			try:
				return PersonaVOBuilder(many=True).dump(PersonaVOBuilder.personas)
			except Exception as e:
				print(colored("No se puede contruir PersonaVO. Error en PersonaVOBuilder; {}".format(e), 'red'))
