from termcolor import colored

from src.daos.models.Direccion import Direccion
from src.daos.DireccionDAO import DireccionDAO
from src.services.vos.DireccionVO import DireccionVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class DireccionService():

	#def __init__(self):
		#print('DireccionService')

	@staticmethod
	def guardar(request):
		print(colored("DireccionService: guardar(); {}".format(request.get_json()), 'cyan'))
		codigoTipoDireccion = request.get_json()["codigoTipoDireccion"] if 'codigoTipoDireccion' in request.get_json() else None
		idComuna = request.get_json()["idComuna"] if 'idComuna' in request.get_json() else None
		calle = request.get_json()["calle"] if 'calle' in request.get_json() else None
		numero = request.get_json()["numero"] if 'numero' in request.get_json() else None
		departamento = request.get_json()["departamento"] if 'departamento' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(codigoTipoDireccion==None):
			enviar = False
			mensajes +="\nTipo de dirección"
		if(idComuna==None):
			enviar = False
			mensajes +="\nComuna"
		if(calle==None):
			enviar = False
			mensajes +="\nCalle"
		if(numero==None):
			enviar = False
			mensajes +="\nNúmero"
		if(enviar):
			direccionVO = DireccionVO()
			direccionVO.codigoTipoDireccion = codigoTipoDireccion
			direccionVO.idComuna = idComuna
			direccionVO.calle = calle
			direccionVO.numero = numero
			direccionVO.departamento = departamento
			direccionVO.fechaCreacion = fechaCreacion
			direccionVO.fechaModificacion = fechaModificacion
			direccionVO.flagActivo = True
			respuesta = DireccionDAO.guardar(direccionVO)
			if(respuesta["result"]):
				respuesta["direccion"] = VOBuilderFactory().getDireccionVOBuilder().fromDireccion(respuesta["direccion"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("DireccionService: obtener();", 'cyan'))
		direcciones = DireccionDAO.obtener()
		if len(direcciones)>0:
			data = {
				"result":True,
				"direcciones":VOBuilderFactory().getDireccionVOBuilder().fromDirecciones(direcciones).builds(),
				"mensajes":"Se encontraron direcciones"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron direcciones"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("DireccionService: obtenerSegunId(); {}".format(id), 'cyan'))
		direccion = DireccionDAO.obtenerSegunId(id)
		if(direccion):
			data = {
				"result":True,
				"direccion":VOBuilderFactory().getDireccionVOBuilder().fromDireccion(direccion).build(),
				"mensajes":"Se encontró dirección con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró dirección con id {}".format(id)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("DireccionService: actualizar(); {}".format(request.get_json()), 'cyan'))
		id = request.get_json()["id"] if 'id' in request.get_json() else None
		codigoTipoDireccion = request.get_json()["codigoTipoDireccion"] if 'codigoTipoDireccion' in request.get_json() else None
		idComuna = request.get_json()["idComuna"] if 'idComuna' in request.get_json() else None
		calle = request.get_json()["calle"] if 'calle' in request.get_json() else None
		numero = request.get_json()["numero"] if 'numero' in request.get_json() else None
		departamento = request.get_json()["departamento"] if 'departamento' in request.get_json() else None
		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(codigoTipoDireccion==None):
			enviar = False
			mensajes +="\nTipo de dirección"
		if(idComuna==None):
			enviar = False
			mensajes +="\nComuna"
		if(calle==None):
			enviar = False
			mensajes +="\nCalle"
		if(numero==None):
			enviar = False
			mensajes +="\nNúmero"
		if(fechaCreacion==None):
			enviar = False
			mensajes +="\n Fecha de creación"
		if(enviar):
			direccionVO = DireccionVO()
			direccionVO.id = id
			direccionVO.codigoTipoDireccion = codigoTipoDireccion
			direccionVO.idComuna = idComuna
			direccionVO.calle = calle
			direccionVO.numero = numero
			direccionVO.departamento = departamento
			direccionVO.fechaCreacion = fechaCreacion
			direccionVO.fechaModificacion = fechaModificacion
			direccionVO.flagActivo = flagActivo
			respuesta = DireccionDAO.actualizar(direccionVO)
			if(respuesta["result"]):
				respuesta["direccion"] = VOBuilderFactory().getDireccionVOBuilder().fromDireccion(respuesta["direccion"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("DireccionService: eliminar(); {}".format(id), 'cyan'))
		respuesta = DireccionDAO.eliminar(id)
		return respuesta
