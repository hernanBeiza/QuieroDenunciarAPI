from termcolor import colored

from src.db import db

from src.daos.models.Correo import Correo

class CorreoDAO():

	#def __init__(self):
		#print('CorreoDAO')

	@staticmethod
	def guardar(correoVO):
		print(colored("CorreoDAO: guardar(); {}".format(correoVO), 'yellow'))

		try:
			correo = Correo(None, correoVO.idEnteFiscalizador, correoVO.glosa, correoVO.flagPrincipal, correoVO.flagActivo)
			db.session.add(correo)
			db.session.commit()
			print(colored("CorreoDAO: Correo guardado correctamente", 'yellow'))
			result = True
			mensajes = "Correo guardado correctamente"
			respuesta = {"result":result,"mensajes":mensajes,"correo":correo}
		except Exception as e:
			print(colored("CorreoDAO: El correo no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El correo no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("CorreoDAO: obtener();", 'yellow'))
		return Correo.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("CorreoDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Correo.query.get(id)

	@staticmethod
	def obtenerSegunIdEnteFiscalizador(idEnteFiscalizador):
		print(colored("CorreoDAO: idEnteFiscalizador(); {}".format(idEnteFiscalizador), 'yellow'))
		return Correo.query.filter_by(id_ente_fiscalizador=idEnteFiscalizador).all()

	@staticmethod
	def actualizar(correoVO):
		print(colored("CorreoDAO: actualizar(); {}".format(correoVO), 'yellow'))
		try:
			correo = Correo.query.get(correoVO.id)
			correo.id_ente_fiscalizador = correoVO.idEnteFiscalizador
			correo.glosa = correoVO.glosa
			#correo.fecha_creacion = correoVO.fechaCreacion
			#correo.fecha_modificacion = correoVO.fechaModificacion
			correo.flag_principal = correoVO.flagPrincipal
			correo.flag_activo = correoVO.flagActivo
			db.session.commit()
			print(colored("CorreoDAO: Ente fiscalizador editado correctamente", 'yellow'))
			result = True
			mensajes = "Correo editado correctamente"
			respuesta = {"result":result,"mensajes":mensajes,"correo":correo}
		except Exception as e:
			print(colored("CorreoDAO: El correo con id {} no se pudo editar. Error: {}".format(correoVO.id, e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El correo no se pudo editar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("CorreoDAO: eliminar(); {}".format(id), 'yellow'))
		correo = Correo.query.get(id)
		if(correo is not None):
			try:
				result = True
				mensajes = "Correo con id {} eliminado correctamente".format(id)
				db.session.delete(correo)
				db.session.commit()
				respuesta = {"result":result,"mensajes":mensajes}
			except Exception as e:
				print(colored("CorreoDAO: El correo con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "El correo con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result,"errores":mensajes}
		else:
			result = False
			mensajes = "El correo con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result,"errores":mensajes}
		return respuesta