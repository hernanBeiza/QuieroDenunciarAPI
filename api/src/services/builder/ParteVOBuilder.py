from marshmallow import Schema, fields
from termcolor import colored

from ...app import ma
from ...daos.models.Parte import Parte
from ..vos.ParteVO import ParteVO
from .TipoParteVOBuilder import TipoParteVOBuilder

class ParteVOBuilder(ma.ModelSchema):

	class Meta:
		model = Parte
		ordered = True

	parte = None
	partes = None

	#Schema
	##Modelo - Dato a mostrar
	id = fields.Integer()
	rut = fields.Integer()
	id_direccion = fields.Integer(data_key="idDireccion")
	cod_tipo_parte = fields.Integer(data_key="codigoTipoParte")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")
	
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