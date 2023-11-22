import os

from termcolor import colored

from src.daos.models.Antecedente import Antecedente
from src.daos.AntecedenteDAO import AntecedenteDAO
from src.services.vos.AntecedenteVO import AntecedenteVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class AntecedenteService():

	#def __init__(self):
		#print('AntecedenteService')

	@staticmethod
	def guardar(request):
		print(colored("AntecedenteService: guardar(); {}".format(request.get_json()), 'cyan'))

		idDenuncia = request.get_json()["idDenuncia"] if 'idDenuncia' in request.get_json() else None
		descripcion = request.get_json()["descripcion"] if 'descripcion' in request.get_json() else None
		fecha = request.get_json()["fecha"] if 'fecha' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nDenuncia"
		if(descripcion==None):
			enviar = False
			mensajes +="\nDescripción del antecedente"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"

		if(enviar):
			antecedenteVO = AntecedenteVO()
			antecedenteVO.idDenuncia = idDenuncia
			antecedenteVO.descripcion = descripcion
			antecedenteVO.fecha = fecha
			antecedenteVO.flagActivo = 1
			respuesta = AntecedenteDAO.guardar(antecedenteVO)
			if(respuesta["result"]):
				respuesta["antecedente"] = VOBuilderFactory().getAntecedenteVOBuilder().fromAntecedente(respuesta["antecedente"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("AntecedenteService: obtener();", 'cyan'))
		antecedentes = AntecedenteDAO.obtener()
		if len(antecedentes)>0:
			data = {
				"result":True,
				"antecedentes":VOBuilderFactory().getAntecedenteVOBuilder().fromAntecedentes(antecedentes).builds(),
				"mensajes":"Se encontraron antecedentes"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron antecedentes"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("AntecedenteService: obtenerSegunId(); {}".format(id), 'cyan'))
		antecedente = AntecedenteDAO.obtenerSegunId(id)
		if(antecedente):
			data = {
				"result":True,
				"antecedente":VOBuilderFactory().getAntecedenteVOBuilder().fromAntecedente(antecedente).build(),
				"mensajes":"Se encontró antecedente con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró antecedente con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("AntecedenteService: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'cyan'))
		antecedentes = AntecedenteDAO.obtenerSegunIdDenuncia(idDenuncia)
		if(antecedentes):
			data = {
				"result":True,
				"antecedentes":VOBuilderFactory().getAntecedenteVOBuilder().fromAntecedentes(antecedentes).builds(),
				"mensajes":"Se encontraron antecedentes con id de denuncia {}".format(idDenuncia)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron antecedentes con id de denuncia {}".format(idDenuncia)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("AntecedenteService: actualizar(); {}".format(request.get_json()), 'cyan'))

		id = request.get_json()["id"] if 'id' in request.get_json() else None
		idDenuncia = request.get_json()["idDenuncia"] if 'idDenuncia' in request.get_json() else None
		descripcion = request.get_json()["descripcion"] if 'descripcion' in request.get_json() else None
		fecha = request.get_json()["fecha"] if 'fecha' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nDenuncia"
		if(descripcion==None):
			enviar = False
			mensajes +="\nDescripción del antecedente"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"
		if(fechaCreacion==None):
			enviar = False
			mensajes +="\nFecha de creación"
		if(enviar):
			antecedenteVO = AntecedenteVO()
			antecedenteVO.id = id
			antecedenteVO.idDenuncia = idDenuncia
			antecedenteVO.descripcion = descripcion
			antecedenteVO.fecha = fecha

			antecedenteVO.fechaCreacion = fechaCreacion
			antecedenteVO.flagActivo = flagActivo
			respuesta = AntecedenteDAO.actualizar(antecedenteVO)
			if(respuesta["result"]):
				respuesta["antecedente"] = VOBuilderFactory().getAntecedenteVOBuilder().fromAntecedente(respuesta["antecedente"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("AntecedenteService: eliminar(); {}".format(id), 'cyan'))
		respuesta = AntecedenteDAO.eliminar(id)
		return respuesta
