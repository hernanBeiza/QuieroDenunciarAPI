from termcolor import colored

from src.db import db

from src.daos.models.Fiscalizador import Fiscalizador

class FiscalizadorDAO():

	#def __init__(self):
		#print('FiscalizadorDAO')

	@staticmethod
	def guardar(fiscalizadorVO):
		print(colored("FiscalizadorDAO: guardar(); {}".format(fiscalizadorVO), 'yellow'))

		try:
			fiscalizador = Fiscalizador(None, fiscalizadorVO.idComuna, fiscalizadorVO.nombre, fiscalizadorVO.fechaCreacion, fiscalizadorVO.fechaModificacion, fiscalizadorVO.flagActivo)
			db.session.add(fiscalizador)
			db.session.commit()
			print(colored("FiscalizadorDAO: Ente fiscalizador guardado correctamente", 'yellow'))
			result = True
			mensajes = "Ente fiscalizador guardado correctamente"
			respuesta = {"result":result,"mensajes":mensajes,"fiscalizador":fiscalizador}
		except Exception as e:
			print(colored("FiscalizadorDAO: El ente fiscalizador no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El ente fiscalizador no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("FiscalizadorDAO: obtener();", 'yellow'))
		return Fiscalizador.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("FiscalizadorDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Fiscalizador.query.get(id)

	@staticmethod
	def obtenerSegunIdComuna(idComuna):
		print(colored("FiscalizadorDAO: obtenerSegunIdComuna(); {}".format(idComuna), 'yellow'))
		return Fiscalizador.query.filter_by(id_comuna=idComuna).all()

	@staticmethod
	def actualizar(fiscalizadorVO):
		print(colored("FiscalizadorDAO: actualizar(); {}".format(fiscalizadorVO), 'yellow'))
		try:
			fiscalizador = Fiscalizador.query.get(fiscalizadorVO.id)
			fiscalizador.nombre = fiscalizadorVO.nombre
			fiscalizador.id_comuna = fiscalizadorVO.idComuna
			#enteFiscalizador.fecha_creacion = fiscalizadorVO.fechaCreacion
			#enteFiscalizador.fecha_modificacion = fiscalizadorVO.fechaModificacion
			fiscalizador.flag_activo = fiscalizadorVO.flagActivo
			db.session.commit()
			print(colored("FiscalizadorDAO: Ente fiscalizador editado correctamente", 'yellow'))
			result = True
			mensajes = "Fiscalizador editado correctamente"
			respuesta = {"result":result,"mensajes":mensajes,"fiscalizador":fiscalizador}
		except Exception as e:
			print(colored("FiscalizadorDAO: El fiscalizador con id {} no se pudo editar. Error: {}".format(fiscalizadorVO.id, e),'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El ente fiscalizador no se pudo editar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("FiscalizadorDAO: eliminar(); {}".format(id), 'yellow'))
		enteFiscalizador = Fiscalizador.query.get(id)
		if(enteFiscalizador is not None):
			try:
				result = True
				mensajes = "Fiscalizador con id {} eliminado correctamente".format(id)
				db.session.delete(enteFiscalizador)
				db.session.commit()
				respuesta = {"result":result,"mensajes":mensajes}
			except Exception as e:
				print(colored("FiscalizadorDAO: El fiscalizador con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "El fiscalizador con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result,"errores":mensajes}
		else:
			result = False
			mensajes = "El fiscalizador con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result,"errores":mensajes}
		return respuesta