import os

from termcolor import colored

from src.daos.models.Denuncia import Denuncia
from src.daos.DenunciaDAO import DenunciaDAO
from src.daos.DenunciaMateriaDAO import DenunciaMateriaDAO
from src.services.vos.DenunciaVO import DenunciaVO
from src.services.vos.DenunciaMateriaVO import DenunciaMateriaVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class DenunciaService():

	#def __init__(self):
		#print('DenunciaService')

	@staticmethod
	def guardar(request):
		print(colored("DenunciaService: guardar(); {}".format(request.get_json()), 'cyan'))

		idDenunciado = request.get_json()["idDenunciado"] if 'idDenunciado' in request.get_json() else None
		idDenunciante = request.get_json()["idDenunciante"] if 'idDenunciante' in request.get_json() else None
		codigoEstadoDenuncia = request.get_json()["codigoEstadoDenuncia"] if 'codigoEstadoDenuncia' in request.get_json() else 1
		denunciasMaterias = request.get_json()["denunciasMaterias"] if 'denunciasMaterias' in request.get_json() else None
		descripcion = request.get_json()["descripcion"] if 'descripcion' in request.get_json() else None
		fecha = request.get_json()["fecha"] if 'fecha' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idDenunciado==None):
			enviar = False
			mensajes +="\nDenunciado"
		if(idDenunciante==None):
			enviar = False
			mensajes +="\nDenunciante"
		if(denunciasMaterias==None):
			enviar = False
			mensajes +="\nSeleccionar materias de la denuncia"
		if(descripcion==None):
			enviar = False
			mensajes +="\nDescripción de la denuncia"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"

		if(enviar):
			denunciaVO = DenunciaVO()
			denunciaVO.idDenunciado = idDenunciado
			denunciaVO.idDenunciante = idDenunciante
			#denunciaVO.denunciasMaterias = denunciasMaterias
			denunciaVO.codigoEstadoDenuncia = codigoEstadoDenuncia
			denunciaVO.descripcion = descripcion
			denunciaVO.fecha = fecha
			denunciaVO.flagActivo = 1
			
			respuesta = DenunciaDAO.guardar(denunciaVO)
			if(respuesta["result"]):
				denunciasMateriasVO = list(map(lambda item:VOBuilderFactory.getDenunciaMateriaVOBuilder().fromJSON(item).buildFromJSON(), denunciasMaterias))
				for denunciaMateriaVO in denunciasMateriasVO:
					denunciaMateriaVO.idDenuncia = respuesta['denuncia'].id_denuncia
				respuestaDenunciasMateria = list(map(lambda denunciaMateriaVO: DenunciaMateriaDAO.guardar(denunciaMateriaVO), denunciasMateriasVO) if denunciaMateriaVO.id is None else DenunciaMateriaDAO.actualizar(denunciaMateriaVO))
				respuesta["denuncia"] = VOBuilderFactory().getDenunciaVOBuilder().fromDenuncia(respuesta["denuncia"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("DenunciaService: obtener();", 'cyan'))
		denuncias = DenunciaDAO.obtener()
		if len(denuncias)>0:
			data = {
				"result":True,
				"denuncias":VOBuilderFactory().getDenunciaVOBuilder().fromDenuncias(denuncias).builds(),
				"mensajes":"Se encontraron denuncias"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron denuncias"
			}
		return data

	@staticmethod
	def obtenerPaginadas(pagina):
		print(colored("DenunciaService: obtenerPaginadas(); {}".format(pagina), 'cyan'))
		try:
			paginacion = DenunciaDAO.obtenerPaginadas(pagina)
			if len(paginacion.items)>0:
				data = {
					"result":True,
					"denuncias":VOBuilderFactory().getDenunciaVOBuilder().fromDenuncias(paginacion.items).builds(),
					"mensajes":"Se encontraron denuncias de la página {}".format(pagina)
				}
			else:
				data = {
					"result":False,
					"errores":"No se encontraron denuncias en la página {}".format(pagina)
				}
		except Exception as e:
			print(colored("DenunciaService: No se encontraron denuncias en la página {}. Error: {}".format(pagina, e), 'red'))
			data = {
				"result":False,
				"errores":"No se encontraron denuncias en la página {}".format(pagina)
			}
		return data;

	@staticmethod
	def obtenerSegunId(id):
		print(colored("DenunciaService: obtenerSegunId(); {}".format(id), 'cyan'))
		denuncia = DenunciaDAO.obtenerSegunId(id)
		if(denuncia):
			data = {
				"result":True,
				"denuncia":VOBuilderFactory().getDenunciaVOBuilder().fromDenuncia(denuncia).build(),
				"mensajes":"Se encontró denuncia con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró denuncia con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunIdDenunciado(idDenunciado):
		print(colored("DenunciaService: obtenerSegunIdDenunciado(); {}".format(idDenunciado), 'cyan'))
		denuncia = DenunciaDAO.obtenerSegunIdDenunciado(idDenunciado)
		if(denuncia):
			data = {
				"result":True,
				"denuncias":VOBuilderFactory().getDenunciaVOBuilder().fromDenuncias(denuncia).builds(),
				"mensajes":"Se encontraron denuncias con id de denunciado {}".format(idDenunciado)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron denuncias con id de denunciado {}".format(idDenunciado)
			}

		return data;

	@staticmethod
	def obtenerSegunIdDenunciante(idDenunciante):
		print(colored("DenunciaService: obtenerSegunIdDenunciante(); {}".format(idDenunciante), 'cyan'))
		denuncia = DenunciaDAO.obtenerSegunIdDenunciante(idDenunciante)

		if(denuncia):
			data = {
				"result":True,
				"denuncias":VOBuilderFactory().getDenunciaVOBuilder().fromDenuncias(denuncia).builds(),
				"mensajes":"Se encontraron denuncias con id de denunciante {}".format(idDenunciante)
			}
		else:
			data = {
				"result":False,
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("DenunciaService: actualizar(); {}".format(request.get_json()), 'cyan'))

		id = request.get_json()["id"] if 'id' in request.get_json() else None
		idDenunciado = request.get_json()["idDenunciado"] if 'idDenunciado' in request.get_json() else None
		idDenunciante = request.get_json()["idDenunciante"] if 'idDenunciante' in request.get_json() else None
		codigoEstadoDenuncia = request.get_json()["codigoEstadoDenuncia"] if 'codigoEstadoDenuncia' in request.get_json() else None
		denunciasMaterias = request.get_json()["denunciasMaterias"] if 'denunciasMaterias' in request.get_json() else None
		descripcion = request.get_json()["descripcion"] if 'descripcion' in request.get_json() else None
		fecha = request.get_json()["fecha"] if 'fecha' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId de la denuncia"			
		if(idDenunciado==None):
			enviar = False
			mensajes +="\nDenunciado"
		if(idDenunciante==None):
			enviar = False
			mensajes +="\nDenunciante"
		if(denunciasMaterias==None):
			enviar = False
			mensajes +="\nSeleccionar materias de la denuncia"
		if(descripcion==None):
			enviar = False
			mensajes +="\nDescripción de la denuncia"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"
		if(enviar):
			denunciaVO = DenunciaVO()
			denunciaVO.id = id
			denunciaVO.idDenunciado = idDenunciado
			denunciaVO.idDenunciante = idDenunciante
			denunciaVO.codigoEstadoDenuncia = codigoEstadoDenuncia
			denunciaVO.denunciasMaterias = denunciasMaterias
			denunciaVO.descripcion = descripcion
			denunciaVO.fecha = fecha
			denunciaVO.fechaCreacion = fechaCreacion
			denunciaVO.fechaModificacion = fechaModificacion
			denunciaVO.flagActivo = flagActivo

			respuesta = DenunciaDAO.actualizar(denunciaVO)
			if(respuesta["result"]):
				denunciasMateriasVO = list(map(lambda item:VOBuilderFactory.getDenunciaMateriaVOBuilder().fromJSON(item).buildFromJSON(), denunciasMaterias))
				for denunciaMateriaVO in denunciasMateriasVO:
					denunciaMateriaVO.idDenuncia = respuesta['denuncia'].id_denuncia
				respuestaDenunciasMateria = list(map(lambda denunciaMateriaVO: DenunciaMateriaDAO.guardar(denunciaMateriaVO), denunciasMateriasVO) if denunciaMateriaVO.id is None else DenunciaMateriaDAO.actualizar(denunciaMateriaVO))
				respuesta["denuncia"] = VOBuilderFactory().getDenunciaVOBuilder().fromDenuncia(respuesta["denuncia"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def actualizarEstado(request):
		print(colored("DenunciaService: actualizarEstado(); {}".format(request.get_json()), 'cyan'))

		idDenuncia = request.get_json()["idDenuncia"] if 'idDenuncia' in request.get_json() else None
		codigoEstadoDenuncia = request.get_json()["codigoEstadoDenuncia"] if 'codigoEstadoDenuncia' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nId de la denucia"
		if(codigoEstadoDenuncia==None):
			enviar = False
			mensajes +="\nCódigo de estado de la denuncia"
		if(enviar):
			denunciaVO = DenunciaVO()
			denunciaVO.idDenuncia = idDenuncia
			denunciaVO.codigoEstadoDenuncia = codigoEstadoDenuncia
			respuesta = DenunciaDAO.actualizarEstado(denunciaVO)
			if(respuesta["result"]):
				respuesta["denuncia"] = VOBuilderFactory().getDenunciaVOBuilder().fromDenuncia(respuesta["denuncia"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("DenunciaService: eliminar(); {}".format(id), 'cyan'))
		respuesta = DenunciaDAO.eliminar(id)
		return respuesta
