from termcolor import colored

from src.daos.models.Fiscalizador import Fiscalizador
from src.daos.FiscalizadorDAO import FiscalizadorDAO
from src.services.vos.FiscalizadorVO import FiscalizadorVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class FiscalizadorService():

	#def __init__(self):
		#print('EnteFiscalizadorService')

	@staticmethod
	def guardar(request):
		print(colored("FiscalizadorService: guardar(); {}".format(request.get_json()), 'cyan'))
		idComuna = request.get_json()["idComuna"] if 'idComuna' in request.get_json() else None
		nombre = request.get_json()["nombre"] if 'nombre' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		#fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idComuna==None):
			enviar = False
			mensajes +="\nComuna"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre"
		if(enviar):
			fiscalizadorVO = FiscalizadorVO()
			fiscalizadorVO.idComuna = idComuna
			fiscalizadorVO.nombre = nombre
			fiscalizadorVO.fechaCreacion = fechaCreacion
			#fiscalizadorVO.fechaModificacion = fechaModificacion
			fiscalizadorVO.flagActivo = True
			respuesta = FiscalizadorDAO.guardar(fiscalizadorVO)
			if(respuesta["result"]):
				respuesta["fiscalizador"] = VOBuilderFactory().getFiscalizadorVOBuilder().fromFiscalizador(respuesta["fiscalizador"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("FiscalizadorService: obtener();", 'cyan'))
		fiscalizadores = FiscalizadorDAO.obtener()
		if len(fiscalizadores)>0:
			data = {
				"result":True,
				"fiscalizadores":VOBuilderFactory().getFiscalizadorVOBuilder().fromFiscalizadores(fiscalizadores).builds(),
				"mensajes":"Se encontraron fiscalizadores"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron fiscalizadores"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("FiscalizadorService: obtenerSegunId(); {}".format(id), 'cyan'))
		fiscalizador = FiscalizadorDAO.obtenerSegunId(id)
		if(fiscalizador):
			data = {
				"result":True,
				"fiscalizador":VOBuilderFactory().getFiscalizadorVOBuilder().fromFiscalizador(fiscalizador).build(),
				"mensajes":"Se encontró fiscalizador con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró fiscalizador con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunIdComuna(idComuna):
		print(colored("FiscalizadorService: obtenerSegunIdComuna(); {}".format(idComuna), 'cyan'))
		fiscalizadores = FiscalizadorDAO.obtenerSegunIdComuna(idComuna)
		if len(fiscalizadores)>0:
			data = {
				"result":True,
				"fiscalizadores":VOBuilderFactory().getFiscalizadorVOBuilder().fromFiscalizadores(fiscalizadores).builds(),
				"mensajes":"Se encontraron fiscalizadores para la comuna con id {}".format(idComuna)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron fiscalizadores para la comuna con id {}".format(idComuna)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("FiscalizadorService: actualizar(); {}".format(request.get_json()), 'cyan'))
		id = request.get_json()["id"] if 'id' in request.get_json() else None
		idComuna = request.get_json()["idComuna"] if 'idComuna' in request.get_json() else None
		nombre = request.get_json()["nombre"] if 'nombre' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(idComuna==None):
			enviar = False
			mensajes +="\nComuna"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre"
		if(fechaCreacion==None):
			enviar = False
			mensajes +="\n Fecha de creación"
		if(enviar):
			fiscalizadorVO = FiscalizadorVO()
			fiscalizadorVO.id = id
			fiscalizadorVO.idComuna = idComuna
			fiscalizadorVO.nombre = nombre
			fiscalizadorVO.fechaCreacion = fechaCreacion
			#fiscalizadorVO.fechaModificacion = fechaModificacion
			fiscalizadorVO.flagActivo = flagActivo
			respuesta = FiscalizadorDAO.actualizar(fiscalizadorVO)
			if(respuesta["result"]):
				respuesta["fiscalizador"] = VOBuilderFactory().getFiscalizadorVOBuilder().fromFiscalizador(respuesta["fiscalizador"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("FiscalizadorService: eliminar(); {}".format(id), 'cyan'))
		respuesta = FiscalizadorDAO.eliminar(id)
		return respuesta
