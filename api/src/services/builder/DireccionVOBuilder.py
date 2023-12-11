from marshmallow import Schema, fields
from termcolor import colored

from src.ma import ma
from src.daos.models.Direccion import Direccion
from src.services.vos.DireccionVO import DireccionVO

from src.services.builder.ComunaVOBuilder import ComunaVOBuilder
from src.services.builder.TipoDireccionVOBuilder import TipoDireccionVOBuilder

class DireccionVOBuilder(ma.ModelSchema):

	class Meta:
		model = Direccion
		ordered = True

	direccion = None
	direcciones = None

	#Schema
	##Modelo - Dato a mostrar
	id_direccion = fields.Integer(data_key="id")
	cod_tipo_direccion = fields.Integer(data_key="codigoTipoDireccion")
	id_comuna = fields.Integer(data_key="idComuna")
	calle = fields.String()
	numero = fields.Integer()
	departamento = fields.Integer()
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")

	#TODO Debe llamarse igual al declarado en el modelo Direccion
	comuna = fields.Nested(ComunaVOBuilder)
	tipoDireccion = fields.Nested(TipoDireccionVOBuilder)

	#def __init__(self):

	@staticmethod
	def fromDireccion(direccion):		
		DireccionVOBuilder.direccion = direccion
		return DireccionVOBuilder()

	@staticmethod
	def fromDirecciones(direcciones):		
		DireccionVOBuilder.direcciones = direcciones
		return DireccionVOBuilder()

	@staticmethod
	def build():		
		if(DireccionVOBuilder.direccion is None):
			print("No se puede contruir DireccionVO")
			return None
		else:
			try:
				return DireccionVOBuilder().dump(DireccionVOBuilder.direccion)
			except Exception as e:
				print(colored("No se puede contruir DireccionVO. Error en DireccionVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(DireccionVOBuilder.direcciones is None):
			print("No se puede contruir DireccionVO. direcciones is None")
			return None
		else:
			try:
				return DireccionVOBuilder(many=True).dump(DireccionVOBuilder.direcciones)
			except Exception as e:
				print(colored("No se puede contruir DireccionVO. Error en DireccionVOBuilder; {}".format(e), 'red'))
