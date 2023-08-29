from marshmallow import Schema, fields
from termcolor import colored

from src.app import ma
from src.daos.models.Antecedente import Antecedente
from src.services.vos.AntecedenteVO import AntecedenteVO
from src.services.builder.ArchivoVOBuilder import ArchivoVOBuilder

class AntecedenteVOBuilder(ma.ModelSchema):

	class Meta:
		model = Antecedente
		ordered = True

	archivo = None
	archivos = None

	#Schema
	##Modelo - Dato a mostrar
	id_antecedente = fields.Integer(data_key="idAntecedente")
	id_denuncia = fields.Integer(data_key="idDenuncia")
	descripcion = fields.String(data_key="descripcion")
	fecha = fields.DateTime(data_key="fecha")
	fecha_creacion = fields.DateTime(data_key="fechaCreacion")
	fecha_modificacion = fields.DateTime(data_key="fechaModificacion")
	flag_activo = fields.Integer(data_key="flagActivo")

	#TODO Debe llamarse igual al declarado como relación en el modelo Antecedente
	archivos = fields.List(fields.Nested(ArchivoVOBuilder))
	
	#def __init__(self):

	@staticmethod
	def fromAntecedente(antecedente):		
		AntecedenteVOBuilder.antecedente = antecedente
		return AntecedenteVOBuilder()

	@staticmethod
	def fromAntecedentes(antecedentes):		
		AntecedenteVOBuilder.antecedentes = antecedentes
		return AntecedenteVOBuilder()

	@staticmethod
	def build():		
		if(AntecedenteVOBuilder.antecedente is None):
			print("No se puede contruir AntecedenteVO")
			return None
		else:
			try:
				return AntecedenteVOBuilder().dump(AntecedenteVOBuilder.antecedente)
			except Exception as e:
				print(colored("No se puede contruir AntecedenteVO. Error en AntecedenteVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(AntecedenteVOBuilder.antecedentes is None):
			print("No se puede contruir AntecedenteVO. antecedentes is None")
			return None
		else:
			try:
				return AntecedenteVOBuilder(many=True).dump(AntecedenteVOBuilder.antecedentes)
			except Exception as e:
				print(colored("No se puede contruir AntecedenteVO. Error en AntecedenteVOBuilder; {}".format(e), 'red'))
