from termcolor import colored

from src.app import db
from src.daos.models.Archivo import Archivo

class ArchivoDAO():

	#def __init__(self):
		#print('ArchivoDAO')

	@staticmethod
	def guardar(archivoVO):
		print(colored("ArchivoDAO: guardar(); {}".format(archivoVO), 'yellow'))

		try:
			archivo = Archivo(None, archivoVO.idAntecedente, archivoVO.codigoTipoArchivo, archivoVO.rutaArchivo, archivoVO.nombreArchivo, archivoVO.extensionArchivo, archivoVO.fecha, archivoVO.fechaCreacion, archivoVO.fechaModificacion, 1)
			db.session.add(archivo)
			db.session.commit()
			print(colored("ArchivoDAO: archivo guardado correctamente", 'yellow'))
			result = True
			mensajes = "Archivo guardado correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "archivo":archivo}
		except Exception as e:
			print(colored("ArchivoDAO: El archivo no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El archivo no se pudo guardar"
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
			archivo = Archivo.query.get(archivoVO.idArchivo)
			archivo.id_antecedente = archivoVO.idAntecedente
			archivo.cod_tipo_archivo = archivoVO.codigoTipoArchivo
			archivo.ruta_archivo = archivoVO.rutaArchivo
			archivo.nombre_archivo = archivoVO.nombreArchivo
			archivo.extension_archivo = archivoVO.extensionArchivo
			archivo.fecha = archivoVO.fecha
			archivo.fecha_creacion = archivoVO.fechaCreacion
			archivo.flag_activo = archivoVO.flagActivo
			#archivo.fecha_modificacion = archivoVO.fechaModificacion
			db.session.commit()
			print(colored("ArchivoDAO: archivo editado correctamente", 'yellow'))
			result = True
			mensajes = "Archivo editado correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "archivo":archivo}
		except Exception as e:
			print(colored("ArchivoDAO: El archivo con id {} no se pudo editar. Error: {}".format(archivoVO.idArchivo,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El archivo no se pudo editar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("ArchivoDAO: eliminar(); {}".format(id), 'yellow'))
		archivo = Archivo.query.get(id)
		if(archivo is not None):
			try:
				result = True
				mensajes = "Archivo con id {} eliminado correctamente".format(id)
				db.session.delete(archivo)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("ArchivoDAO: La archivo con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "El archivo con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "El archivo con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta