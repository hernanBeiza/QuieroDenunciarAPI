from src.app import app

class IndexService():

	def __init__(self):
		print('IndexService __init__()')

	@staticmethod
	def saludar():
		data = {
			"result": True,
			"mensajes": "Bienvenido a la API de Denuncias de La Florida",
			"version": app.config["VERSION"]
		}
		return data
