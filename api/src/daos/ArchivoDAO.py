from termcolor import colored

from src.db import db
from src.daos.models.Archivo import Archivo
from src.utils.ArchivoUtils import ArchivoUtils

class ArchivoDAO():

	#def __init__(self):
		#print('ArchivoDAO')

	@staticmethod
	def guardar(archivoVO):
		print(colored("ArchivoDAO: guardar(); {}".format(archivoVO), 'yellow'))
		try:
			archivo = Archivo(None, archivoVO.idDenuncia, archivoVO.codigoTipoArchivo, archivoVO.rutaArchivo, archivoVO.nombreArchivo, archivoVO.extensionArchivo, archivoVO.descripcion, archivoVO.fecha, archivoVO.fechaCreacion, archivoVO.fechaModificacion, 1)
			db.session.add(archivo)
			db.session.commit()
			print(colored("ArchivoDAO: Datos de archivo guardados correctamente", 'yellow'))
			result = True
			mensajes = "Datos de archivo guardados correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "archivo":archivo}
		except Exception as e:
			print(colored("ArchivoDAO: Los datos del archivo no se han podido guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "Los datos del archivo con nombre {} no se han podido guardar".format(archivoVO.nombreArchivo)
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("ArchivoDAO: obtener();", 'yellow'))
		return Archivo.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("ArchivoDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Archivo.query.get(id)

	@staticmethod
	def actualizar(archivoVO):
		print(colored("ArchivoDAO: actualizar(); {}".format(archivoVO), 'yellow'))
		try:
			archivo = Archivo.query.get(archivoVO.id)
			archivo.id_denuncia = archivoVO.idDenuncia
			archivo.cod_tipo_archivo = archivoVO.codigoTipoArchivo
			archivo.ruta_archivo = archivoVO.rutaArchivo
			archivo.nombre_archivo = archivoVO.nombreArchivo
			archivo.extension_archivo = archivoVO.extensionArchivo
			archivo.descripcion = archivoVO.descripcion
			archivo.fecha = archivoVO.fecha
			archivo.fecha_creacion = archivoVO.fechaCreacion
			archivo.flag_activo = archivoVO.flagActivo
			#archivo.fecha_modificacion = archivoVO.fechaModificacion
			db.session.commit()
			print(colored("ArchivoDAO: Datos de archivo editados correctamente", 'yellow'))
			result = True
			mensajes = "Datos de archivo editados correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "archivo":archivo}
		except Exception as e:
			print(colored("ArchivoDAO: Los datos del archivo con id {} no se pudieron editar. Error: {}".format(archivoVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "Los datos del archivo no se pudieron editar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("ArchivoDAO: eliminar(); {}".format(id), 'yellow'))
		archivo = Archivo.query.get(id)
		if(archivo is not None):
			try:
				result = True
				mensajes = "Datos de archivo con id {} eliminados correctamente".format(id)
				db.session.delete(archivo)
				db.session.commit()
				ArchivoUtils.eliminar(archivo.ruta_archivo)
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("ArchivoDAO: Los datos del archivo con id {} no se pudieron eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "Los datos del archivo con id {} no se pudieron eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "Los datos del archivo con id {} no se ha podido encontrar. No se pudieron eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta