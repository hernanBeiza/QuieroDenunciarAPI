import os
from flask import send_from_directory

from termcolor import colored

from src.utils.ArchivoUtils import ArchivoUtils
from src.app import app
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

		idDenuncia = request.form.get("idDenuncia", None)
		codigoTipoArchivo = request.form.get("codigoTipoArchivo", None)
		archivo = request.files.get("archivo", None)
		#TODO Manejar cuando no viene el archivo
		nombreArchivo = archivo.filename if archivo else None
		extensionArchivo = archivo.filename.rsplit('.', 1)[1].lower() if archivo else None
		print(extensionArchivo)		
		descripcion = request.form.get("descripcion", None)
		fecha = request.form.get("fecha", None)

		extensionesPermitidas = app.config['EXTENSIONES_PERMITIDAS']
		print(extensionesPermitidas)

		enviar = True
		mensajes = "Faltó:"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nDenuncia"
		if(archivo==None):
			enviar = False
			mensajes +="\nArchivo"
		if(codigoTipoArchivo==None):
			enviar = False
			mensajes +="\nTipo de archivo"
		if(descripcion==None):
			enviar = False
			mensajes +="\nDescripción de la imagen"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"
		if(extensionArchivo==None):
			enviar = False
			mensajes +="\nArchivo no enviado"
		if(extensionArchivo not in extensionesPermitidas):
			enviar = False
			mensajes +="\nTipo de archivo no permitido"

		if(enviar):
			archivoVO = ArchivoVO()
			archivoVO.idDenuncia = idDenuncia
			archivoVO.codigoTipoArchivo = codigoTipoArchivo
			archivoVO.rutaArchivo = app.config['CARPETA_IMAGENES']
			archivoVO.nombreArchivo = ArchivoUtils.crearNombre(nombreArchivo)
			archivoVO.extensionArchivo = extensionArchivo
			archivoVO.descripcion = descripcion
			archivoVO.fecha = fecha

			archivoVO.flagActivo = 2
			respuesta = ArchivoDAO.guardar(archivoVO)
			if(respuesta["result"]):
				try:
					ArchivoUtils.guardar(os.path.join(app.config['CARPETA_IMAGENES'],archivoVO.nombreArchivo), archivo)
					archivo
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
	def descargarArchivoSegunId(id):
		print(colored("ArchivoService: descargarArchivoSegunId(); {}".format(id), 'cyan'))
		archivo = ArchivoDAO.obtenerSegunId(id)
		if(archivo is not None):
			carpeta = os.path.join(app.config['CARPETA_IMAGENES'])
			rutaCompleta = os.path.join(carpeta,archivo.nombre_archivo)
			print(rutaCompleta)
			if os.path.isfile(rutaCompleta):
				print("ArchivoService: Archivo encontrado en la ruta: {}".format(rutaCompleta))
				carpetaRelativa = os.path.join("..",app.config['CARPETA_IMAGENES'])
				return send_from_directory(carpetaRelativa, archivo.nombre_archivo, as_attachment=True)
			else:
				error = "ArchivoService: No se encontró archivo con id: {} en ruta: {} ".format(id,ruta)
				print(colored(error, 'red'))
				errorVisualizable = "El archivo no se pudo descargar. No se encontró el archivo solicitado."
				print(colored(errorVisualizable, 'red'))
				result = False
				respuesta = {"result": result, "error": errorVisualizable, "codigo": 404}
				raise Exception(error, respuesta)
		else:
			error = "ArchivoService: No se encontró archivo con id: {}".format(id)
			print(colored(error, 'red'))
			errorVisualizable = "El archivo no se pudo descargar. No existe archivo con id: {}".format(id)
			print(colored(errorVisualizable, 'red'))
			result = False
			respuesta = {"result": result, "error": errorVisualizable, "codigo": 404}
			raise Exception(error, respuesta)

	@staticmethod
	def actualizar(request):
		print(colored("ArchivoService: actualizar(); {}".format(request.form), 'cyan'))
		print(colored("ArchivoService: actualizar(); {}".format(request.files), 'cyan'))

		id = request.form.get("id", None)
		idDenuncia = request.form.get("idDenuncia", None)
		descripcion = request.form.get("descripcion", None)
		fecha = request.form.get("fecha", None)
		fechaCreacion = request.form.get("fechaCreacion", None)
		flagActivo = request.form.get("flagActivo", 2)

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
			mensajes +="\nDescripción de la imagen"
		if(fecha==None):
			enviar = False
			mensajes +="\nFecha del hecho"
		if(fechaCreacion==None):
			enviar = False
			mensajes +="\n Fecha de creación"
		if(enviar):
			archivoVO = ArchivoVO()
			archivoVO.id = id
			archivoVO.idDenuncia = idDenuncia
			#Obtener datos del archivo
			archivoEncontrado = ArchivoDAO.obtenerSegunId(id);
			if(archivoEncontrado is not None):
				archivoVO.codigoTipoArchivo = archivoEncontrado.cod_tipo_archivo
				archivoVO.rutaArchivo = archivoEncontrado.ruta_archivo
				archivoVO.nombreArchivo = archivoEncontrado.nombre_archivo
				archivoVO.extensionArchivo = archivoEncontrado.extension_archivo
				archivoVO.flagActivo = archivoEncontrado.flag_activo
			else:
				print(colored("ArchivoService: actualizar(); No se encontró archivo con id: {}".format(id), 'red'))

			archivoVO.descripcion = descripcion
			archivoVO.fecha = fecha

			archivoVO.fechaCreacion = fechaCreacion
			archivoVO.flagActivo = flagActivo
			
			respuesta = ArchivoDAO.actualizar(archivoVO)
			if(respuesta["result"]):
				respuesta["archivo"] = VOBuilderFactory().getArchivoVOBuilder().fromArchivo(respuesta["archivo"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("ArchivoService: eliminar(); {}".format(id), 'cyan'))
		archivoAntiguo = ArchivoDAO.obtenerSegunId(id);
		if archivoAntiguo is not None:
			respuesta = ArchivoDAO.eliminar(id)
		else:
			print(colored("ArchivoService: El archivo con id: {} no existe. No se ha podido eliminar.".format(id), 'cyan'))
			error = "El archivo con id: {} no existe. No se ha podido eliminar.".format(id);
			respuesta = {
				"result":False,
				"errores":error
			}

		return respuesta