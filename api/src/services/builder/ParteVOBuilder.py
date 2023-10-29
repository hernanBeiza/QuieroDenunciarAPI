from marshmallow import Schema, fields
from termcolor import colored

from src.app import ma
from src.daos.models.Parte import Parte
from src.services.vos.ParteVO import ParteVO
from src.services.builder.TipoParteVOBuilder import TipoParteVOBuilder

class ParteVOBuilder(ma.ModelSchema):

	class Meta:
		model = Parte
		ordered = True

	parte = None
	partes = None

	#Schema
	##Modelo - Dato a mostrar
	id_parte = fields.Integer(data_key="id")
	id_persona = fields.Integer(data_key="idPersona")
	id_direccion = fields.Integer(data_key="idDireccion")
	cod_tipo_parte = fields.Integer(data_key="codigoTipoParte")
	correo = fields.String(data_key="correo")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")
	#TODO llamarse igual al declarado en el modelo Parte
	tipoParte = fields.Nested(TipoParteVOBuilder)

	#def __init__(self):

	@staticmethod
	def fromParte(parte):		
		ParteVOBuilder.parte = parte
		return ParteVOBuilder()

	@staticmethod
	def fromPartes(partes):		
		ParteVOBuilder.partes = partes
		return ParteVOBuilder()

	@staticmethod
	def build():		
		if(ParteVOBuilder.parte is None):
			print("No se puede contruir ParteVO")
			return None
		else:
			try:
				return ParteVOBuilder().dump(ParteVOBuilder.parte)
			except Exception as e:
				print(colored("No se puede contruir ParteVO. Error en ParteVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(ParteVOBuilder.partes is None):
			print("No se puede contruir ParteVO. partes is None")
			return None
		else:
			try:
				return ParteVOBuilder(many=True).dump(ParteVOBuilder.partes)
			except Exception as e:
				print(colored("No se puede contruir ParteVO. Error en ParteVOBuilder; {}".format(e), 'red'))
