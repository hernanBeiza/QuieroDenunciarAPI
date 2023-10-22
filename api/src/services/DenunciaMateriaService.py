import os

from src.app import app
from termcolor import colored

from src.daos.models.DenunciaMateria import DenunciaMateria
from src.daos.DenunciaMateriaDAO import DenunciaMateriaDAO
from src.services.vos.DenunciaMateriaVO import DenunciaMateriaVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class DenunciaMateriaService():

	#def __init__(self):
		#print('DenunciaMateriaService')

	@staticmethod
	def guardar(request):
		print(colored("DenunciaMateriaService: guardar(); {}".format(request.get_json()), 'cyan'))

		idDenuncia = request.get_json()["idDenuncia"] if 'idDenuncia' in request.get_json() else None
		codigoMateria = request.get_json()["codigoMateria"] if 'codigoMateria' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nDenuncia"
		if(codigoMateria==None):
			enviar = False
			mensajes +="\nCódigo de la materia"

		if(enviar):
			denunciaMateriaVO = DenunciaMateriaVO()
			denunciaMateriaVO.idDenuncia = idDenuncia
			denunciaMateriaVO.codigoMateria = codigoMateria
			#TODO Definir estado
			denunciaMateriaVO.flagActivo = 2

			respuesta = DenunciaMateriaDAO.guardar(denunciaMateriaVO)
			if(respuesta["result"]):
				respuesta["denunciaMateria"] = VOBuilderFactory().getDenunciaMateriaVOBuilder().fromDenunciaMateria(respuesta["denunciaMateria"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("DenunciaMateriaService: obtener();", 'cyan'))
		denunciasMaterias = DenunciaMateriaDAO.obtener()
		if len(denunciasMaterias)>0:
			data = {
				"result":True,
				"denunciasMaterias":VOBuilderFactory().getDenunciaMateriaVOBuilder().fromDenunciasMaterias(denunciasMaterias).builds(),
				"mensajes":"Se encontraron {} DenunciaMateria".format((len(denunciasMaterias)))
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron DenunciaMateria"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("DenunciaMateriaService: obtenerSegunId(); {}".format(id), 'cyan'))
		denunciaMateria = DenunciaMateriaDAO.obtenerSegunId(id)
		if(denunciaMateria):
			data = {
				"result":True,
				"denunciaMateria":VOBuilderFactory().getDenunciaMateriaVOBuilder().fromDenunciaMateria(denunciaMateria).build(),
				"mensajes":"Se encontró DenunciaMateria con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró DenunciaMateria con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("DenunciaMateriaService: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'cyan'))
		denunciasMaterias = DenunciaMateriaDAO.obtenerSegunIdDenuncia(idDenuncia)
		if len(denunciasMaterias)>0:
			data = {
				"result":True,
				"denunciasMaterias":VOBuilderFactory().getDenunciaMateriaVOBuilder().fromDenunciasMaterias(denunciasMaterias).builds(),
				"mensajes":"Se encontraron DenunciaMateria con id de denuncia {}".format(idDenuncia)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron DenunciaMateria con id de denuncia {}".format(idDenuncia)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("DenunciaMateriaService: actualizar(); {}".format(request.get_json()), 'cyan'))

		id = request.get_json()["id"] if 'id' in request.get_json() else None
		idDenuncia = request.get_json()["idDenuncia"] if 'idDenuncia' in request.get_json() else None
		codigoMateria = request.get_json()["codigoMateria"] if 'codigoMateria' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId de la denuncia materia"			
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nId de la denuncia"
		if(codigoMateria==None):
			enviar = False
			mensajes +="\nCódigo de la materia"
		if(enviar):
			denunciaMateriaVO = DenunciaMateriaVO()
			denunciaMateriaVO.id = id
			denunciaMateriaVO.idDenuncia = idDenuncia
			denunciaMateriaVO.codigoMateria = codigoMateria

			denunciaMateriaVO.fechaCreacion = fechaCreacion
			denunciaMateriaVO.fechaModificacion = fechaModificacion
			denunciaMateriaVO.flagActivo = flagActivo

			respuesta = DenunciaMateriaDAO.actualizar(denunciaMateriaVO)
			if(respuesta["result"]):
				respuesta["denunciaMateria"] = VOBuilderFactory().getDenunciaMateriaVOBuilder().fromDenunciaMateria(respuesta["denunciaMateria"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("DenunciaMateriaService: eliminar(); {}".format(id), 'cyan'))
		respuesta = DenunciaMateriaDAO.eliminar(id)
		return respuesta
