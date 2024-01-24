from termcolor import colored

from src.daos.models.Correo import Correo
from src.daos.CorreoDAO import CorreoDAO
from src.services.vos.CorreoVO import CorreoVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class CorreoService():

	#def __init__(self):
		#print('EnteFiscalizadorService')

	@staticmethod
	def guardar(request):
		print(colored("CorreoService: guardar(); {}".format(request.get_json()), 'cyan'))
		idFiscalizador = request.get_json()["idFiscalizador"] if 'idFiscalizador' in request.get_json() else None
		glosa = request.get_json()["glosa"] if 'glosa' in request.get_json() else None
		#fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		#fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagPrincipal = request.get_json()["flagPrincipal"] if 'flagPrincipal' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idFiscalizador==None):
			enviar = False
			mensajes +="\nFiscalizador"
		if(glosa==None):
			enviar = False
			mensajes +="\nCorreo"
		if(enviar):
			correoVO = CorreoVO()
			correoVO.idFiscalizador = idFiscalizador
			correoVO.glosa = glosa
			#correoVO.fechaCreacion = fechaCreacion
			#correoVO.fechaModificacion = fechaModificacion
			correoVO.flagPrincipal = flagPrincipal
			correoVO.flagActivo = True
			respuesta = CorreoDAO.guardar(correoVO)
			if(respuesta["result"]):
				respuesta["correo"] = VOBuilderFactory().getCorreoVOBuilder().fromCorreo(respuesta["correo"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("CorreoService: obtener();", 'cyan'))
		correos = CorreoDAO.obtener()
		if len(correos)>0:
			data = {
				"result":True,
				"correos":VOBuilderFactory().getCorreoVOBuilder().fromCorreos(correos).builds(),
				"mensajes":"Se encontraron entes fiscalizadores"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron entes fiscalizadores"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("CorreoService: obtenerSegunId(); {}".format(id), 'cyan'))
		correo = CorreoDAO.obtenerSegunId(id)
		if(correo):
			data = {
				"result":True,
				"correo":VOBuilderFactory().getCorreoVOBuilder().fromCorreo(correo).build(),
				"mensajes":"Se encontró ente fiscalizador con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró ente fiscalizador con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunIdFiscalizador(idFiscalizador):
		print(colored("CorreoService: obtenerSegunIdFiscalizador(); {}".format(idFiscalizador), 'cyan'))
		correos = CorreoDAO.obtenerSegunIdFiscalizador(idFiscalizador)
		if len(correos)>0:
			data = {
				"result":True,
				"correos":VOBuilderFactory().getCorreoVOBuilder().fromCorreos(correos).builds(),
				"mensajes":"Se encontraron correos para el fiscalizador con id {}".format(idFiscalizador)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron correos para el fiscalizador con id {}".format(idFiscalizador)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("CorreoService: actualizar(); {}".format(request.get_json()), 'cyan'))
		id = request.get_json()["id"] if 'id' in request.get_json() else None
		idFiscalizador = request.get_json()["idFiscalizador"] if 'idFiscalizador' in request.get_json() else None
		glosa = request.get_json()["glosa"] if 'glosa' in request.get_json() else None
		#fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		#fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagPrincipal = request.get_json()["flagPrincipal"] if 'flagPrincipal' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(idFiscalizador==None):
			enviar = False
			mensajes +="\nFiscalizador"
		if(glosa==None):
			enviar = False
			mensajes +="\nGlosa del correo"
		'''
		if(fechaCreacion==None):
			enviar = False
			mensajes +="\n Fecha de creación"
		'''

		if(enviar):
			correoVO = CorreoVO()
			correoVO.id = id
			correoVO.idFiscalizador = idFiscalizador
			correoVO.glosa = glosa
			#correoVO.fechaCreacion = fechaCreacion
			#correoVO.fechaModificacion = fechaModificacion
			correoVO.flagPrincipal = flagPrincipal
			correoVO.flagActivo = flagActivo
			respuesta = CorreoDAO.actualizar(correoVO)
			if(respuesta["result"]):
				respuesta["correo"] = VOBuilderFactory().getCorreoVOBuilder().fromCorreo(respuesta["correo"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("CorreoService: eliminar(); {}".format(id), 'cyan'))
		respuesta = CorreoDAO.eliminar(id)
		return respuesta
