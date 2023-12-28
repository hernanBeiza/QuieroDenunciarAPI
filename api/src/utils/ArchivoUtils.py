import os
from flask_dotenv import DotEnv
from termcolor import colored
import uuid

class ArchivoUtils:

	@staticmethod
	def verificarCarpetas(app):
		try:
			print("ArchivoUtils: Crear carpeta de imágenes en: {}".format(app.config['CARPETA_IMAGENES']))
			os.makedirs(app.config['CARPETA_IMAGENES'])
			print(colored("ArchivoUtils: Carpeta de imágenes creada correctamente en: {}".format(app.config['CARPETA_IMAGENES']), 'green'))
			return True
		except Exception as e:
			print(colored("ArchivoUtils: La carpeta de imágenes no se pudo crear. Error: {}".format(e), 'red'))
			return False

	@staticmethod
	def guardar(ruta, archivo):
		try:
			if not os.path.exists(ruta):				
				archivo.save(ruta)
				print(colored("ArchivoUtils: El archivo en ruta {} ha sido guardado correctamente.".format(ruta),'green'))
			else:
				print(colored("ArchivoUtils: El archivo en ruta {} no existe. No se ha podido guardar.".format(ruta),'red'))
			return True
		except Exception as e:
			print(colored("ArchivoUtils: El archivo no se ha podido guardar. Error: {}".format(e), 'red'))
			return False

	@staticmethod
	def eliminar(ruta):
		try:
			if os.path.exists(ruta):
				os.remove(ruta)
				print(colored("ArchivoUtils: El archivo en ruta {} ha sido eliminado correctamente.".format(ruta),'green'))
			else:
				print(colored("ArchivoUtils: El archivo en ruta {} no existe. No se ha podido eliminar.".format(ruta),'red'))
			return True
		except Exception as e:
			print(colored("ArchivoUtils: El archivo no se ha podido eliminar. Error: {}".format(e), 'red'))
			return False

	@staticmethod
	def crearNombre(nombreArchivo):
		print("ArchivoUtils: Crear nombre de archivo para: {}".format(nombreArchivo))
		return str(uuid.uuid4())+"-"+nombreArchivo
