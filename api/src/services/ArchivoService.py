import os

from termcolor import colored

from src.utils.ArchivoUtils import ArchivoUtils

from src.daos.ArchivoDAO import ArchivoDAO
from src.services.vos.ArchivoVO import ArchivoVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class ArchivoService():

	#def __init__(self):
		#print('ArchivoService')

	@staticmethod
	def guardar(request):
		print(colored("ArchivoService: guardar(); {}".format(request.form), 'cyan'))
		print(colored("ArchivoService: guardar(); {}".format(request.files), 'cyan'))

		idAntecedente = request.form.get("idAntecedente", None)
		codigoTipoArchivo = request.form.get("idAntecedente", None)
		archivo = request.files.get("archivo", None)
		nombreArchivo = archivo.filename if archivo else None
		extensionArchivo = archivo.filename.rsplit('.', 1)[1].lower() if archivo else None
		fecha = request.form.get("fecha", None)

		extensionesPermitidas = app.config['EXTENSIONES_PERMITIDAS']
		print(extensionesPermitidas)

		enviar = True
		mensajes = "Faltó:"
		if(idAntecedente==None):
			enviar = False
			mensajes +="\nAntecedente"
		if(archivo==None):
			enviar = False
			mensajes +="\nArchivo"
		if(codigoTipoArchivo==None):
			enviar = False
			mensajes +="\nTipo de archivo"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"
		if(extensionArchivo not in extensionesPermitidas):
			enviar = False
			mensajes +="\nTipo de archivo no permitido"

		if(enviar):
			archivoVO = ArchivoVO()
			archivoVO.idAntecedente = idAntecedente
			archivoVO.codigoTipoArchivo = codigoTipoArchivo
			archivoVO.nombreArchivo = ArchivoUtils.crearNombre(nombreArchivo)
			rutaArchivo = app.config['CARPETA_IMAGENES']
			archivoVO.rutaArchivo = rutaArchivo+archivoVO.nombreArchivo
			archivoVO.extensionArchivo = extensionArchivo
			archivoVO.fecha = fecha
			archivoVO.flagActivo = 0
			respuesta = ArchivoDAO.guardar(archivoVO)
			if(respuesta["result"]):
				try:
					#TODO Revisar si se implementa función de guardar en ArchivoUtils
					archivo.save(os.path.join(app.config['CARPETA_IMAGENES'],archivoVO.nombreArchivo))
					respuesta["archivo"] = VOBuilderFactory().getArchivoVOBuilder().fromArchivo(respuesta["archivo"]).build()
				except Exception as e:
					print(colored("ArchivoService: El archivo no se pudo guardar. Error: {}".format(e), 'red'))
					respuesta = {"result":False, "errores":e}
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("ArchivoService: obtener();", 'cyan'))
		archivos = ArchivoDAO.obtener()
		if len(archivos)>0:
			data = {
				"result":True,
				"archivos":VOBuilderFactory().getArchivoVOBuilder().fromArchivos(archivos).builds(),
				"mensajes":"Se encontraron archivos"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron archivos"
			}
		return data

	@staticmethod
	def obtenerSegunId(id):
		print(colored("ArchivoService: obtenerSegunId(); {}".format(id), 'cyan'))
		archivo = ArchivoDAO.obtenerSegunId(id)
		if(archivo):
			data = {
				"result":True,
				"archivo":VOBuilderFactory().getArchivoVOBuilder().fromArchivo(archivo).build(),
				"mensajes":"Se encontró archivo con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró archivo con id {}".format(id)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("ArchivoService: actualizar(); {}".format(request.form), 'cyan'))
		print(colored("ArchivoService: actualizar(); {}".format(request.files), 'cyan'))

		idArchivo = request.form.get("id", None)
		idAntecedente = request.form.get("idAntecedente", None)
		codigoTipoArchivo = request.form.get("codigoTipoArchivo", None)
		archivo = request.files.get("archivo", None)
		nombreArchivo = archivo.filename if archivo else None
		extensionArchivo = archivo.filename.rsplit('.', 1)[1].lower() if archivo else None
		fecha = request.form.get("fecha", None)
		fechaCreacion = request.form.get("fechaCreacion", None)
		flagActivo = request.form.get("flagActivo", None)

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId"
		if(idAntecedente==None):
			enviar = False
			mensajes +="\nAntecedente"
		if(codigoTipoArchivo==None):
			enviar = False
			mensajes +="\nTipo de archivo"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"
		if(fechaCreacion==None):
			enviar = False
			mensajes +="\n Fecha de creación"
		if(enviar):
			archivoVO = ArchivoVO()
			archivoVO.idArchivo = idArchivo
			archivoVO.idAntecedente = idAntecedente
			archivoVO.codigoTipoArchivo = codigoTipoArchivo
			archivoVO.archivo = archivo
			archivoVO.nombreArchivo = ArchivoUtils.crearNombre(nombreArchivo)
			rutaArchivo = app.config['CARPETA_IMAGENES']
			archivoVO.rutaArchivo = rutaArchivo
			archivoVO.extensionArchivo = extensionArchivo
			archivoVO.fecha = fecha

			archivoVO.fechaCreacion = fechaCreacion
			archivoVO.flagActivo = flagActivo
			respuesta = ArchivoDAO.actualizar(archivoVO)
			if(respuesta["result"]):
				#TODO Eliminar archivo anterior
				#TODO Mover nuevo archivo a carpeta de imágenes
				respuesta["archivo"] = VOBuilderFactory().getArchivoVOBuilder().fromArchivo(respuesta["archivo"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("ArchivoService: eliminar(); {}".format(id), 'cyan'))
		respuesta = ArchivoDAO.eliminar(id)
		return respuesta