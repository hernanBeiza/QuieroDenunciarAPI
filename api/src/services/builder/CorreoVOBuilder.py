from marshmallow import fields
from termcolor import colored

from src.ma import ma
from src.daos.models.Correo import Correo

class CorreoVOBuilder(ma.ModelSchema):

	class Meta:
		model = Correo
		ordered = True

	correo = None
	correos = None

	#Schema
	##Modelo - Dato a mostrar
	id_correo = fields.Integer(data_key="id")
	id_fiscalizador = fields.Integer(data_key="idFiscalizador")
	flosa = fields.String(data_key="nombre")
	#fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	#fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_principal = fields.Boolean(data_key="flagPrincipal")
	flag_activo = fields.Boolean(data_key="flagActivo")

	#def __init__(self):

	@staticmethod
	def fromCorreo(correo):
		CorreoVOBuilder.correo = correo
		return CorreoVOBuilder()

	@staticmethod
	def fromCorreos(correos):
		CorreoVOBuilder.correos = correos
		return CorreoVOBuilder()

	@staticmethod
	def build():		
		if CorreoVOBuilder.correo is None:
			print("No se puede contruir CorreoVOBuilder")
			return None
		else:
			try:
				return CorreoVOBuilder().dump(CorreoVOBuilder.correo)
			except Exception as e:
				print(colored("No se puede contruir CorreoVOBuilder. Error en CorreoVOBuilder: {}".format(e), 'red'))

	@staticmethod
	def builds():
		if CorreoVOBuilder.correos is None:
			print("No se puede contruir CorreoVO. correos is None")
			return None
		else:
			try:
				return CorreoVOBuilder(many=True).dump(CorreoVOBuilder.correos)
			except Exception as e:
				print(colored("No se puede contruir CorreoVOBuilder. Error en CorreoVOBuilder: {}".format(e), 'red'))
