from termcolor import colored

from src.app import app
from src.db import db
from src.daos.models.EnvioCorreoFiscalizador import EnvioCorreoFiscalizador

class EnvioCorreoFiscalizadorDAO():

	#def __init__(self):
		#print('EnvioCorreoFiscalizadorDAO')

	@staticmethod
	def guardar(envioCorreoFiscalizadorVO):
		print(colored("EnvioCorreoFiscalizadorDAO: guardar(); {}".format(envioCorreoFiscalizadorVO), 'yellow'))
		try:
			envioCorreoFiscalizador = EnvioCorreoFiscalizador(None, envioCorreoFiscalizadorVO.idFiscalizador, envioCorreoFiscalizadorVO.idDenuncia, envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo, envioCorreoFiscalizadorVO.fechaEnvio, envioCorreoFiscalizadorVO.fechaCreacion, envioCorreoFiscalizadorVO.fechaModificacion, 1)
			db.session.add(envioCorreoFiscalizador)
			db.session.commit()
			print(colored("EnvioCorreoFiscalizadorDAO: Envío de correo guardado correctamente", 'yellow'))
			result = True
			mensajes = "Envio de correo guardado correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "envioCorreoFiscalizador":envioCorreoFiscalizador}
		except Exception as e:
			print(colored("EnvioCorreoFiscalizadorDAO: El envío de correo no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El envío de correo no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("EnvioCorreoFiscalizadorDAO: obtener();", 'yellow'))
		return EnvioCorreoFiscalizador.query.all()

	@staticmethod
	def obtenerPaginadas(pagina):
		print(colored("EnvioCorreoFiscalizadorDAO: obtenerPaginadas(); {}".format(pagina), 'yellow'))
		return EnvioCorreoFiscalizador.query.order_by(EnvioCorreoFiscalizador.id_envio_correo_fiscalizador.desc()).paginate(page=pagina, per_page=5)

	@staticmethod
	def obtenerSegunId(id):
		print(colored("EnvioCorreoFiscalizadorDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return EnvioCorreoFiscalizador.query.get(id)

	@staticmethod
	def obtenerSegunIdFiscalizador(idFiscalizador):
		print(colored("EnvioCorreoFiscalizadorDAO: obtenerSegunIdFiscalizador(); {}".format(idFiscalizador), 'yellow'))
		return EnvioCorreoFiscalizador.query.filter_by(id_fiscalizador=idFiscalizador).all()

	@staticmethod
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("EnvioCorreoFiscalizadorDAO: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'yellow'))
		return EnvioCorreoFiscalizador.query.filter_by(id_denuncia=idDenuncia).all()

	@staticmethod
	def obtenerSegunCodigoPagina(codigoEstadoEnvioCorreo, pagina):
		print(colored("EnvioCorreoFiscalizadorDAO: obtenerSegunCodigoPagina(); {} {}".format(codigoEstadoEnvioCorreo, pagina), 'yellow'))
		try:
			resultadosPorPagina = int(app.config["RESULTADOS_POR_PAGINA"])
			return EnvioCorreoFiscalizador.query.filter_by(cod_estado_envio_correo=codigoEstadoEnvioCorreo).paginate(page=pagina, per_page=resultadosPorPagina)
		except Exception as e:
			print(colored("EnvioCorreoFiscalizadorDAO: Error al intentar obtener según codigoEstadoEnvioCorreo {} y página {}. Error: {}".format(codigoEstadoEnvioCorreo, pagina, e), 'red'))
			return None

	@staticmethod
	def actualizar(envioCorreoFiscalizadorVO):
		print(colored("EnvioCorreoFiscalizadorDAO: actualizar(); {}".format(envioCorreoFiscalizadorVO), 'yellow'))
		try:
			envioCorreoFiscalizador = EnvioCorreoFiscalizador.query.get(envioCorreoFiscalizadorVO.id)
			envioCorreoFiscalizador.id_fiscalizador = envioCorreoFiscalizadorVO.idFiscalizador
			envioCorreoFiscalizador.id_denuncia = envioCorreoFiscalizadorVO.idDenuncia
			envioCorreoFiscalizador.cod_estado_envio_correo = envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo
			envioCorreoFiscalizador.fecha_envio = envioCorreoFiscalizadorVO.fechaEnvio
			#envioCorreoFiscalizador.fecha_creacion = denunciaVO.fechaCreacion
			#envioCorreoFiscalizador.fecha_modificacion = denunciaVO.fechaModificacion
			envioCorreoFiscalizador.flag_activo = envioCorreoFiscalizadorVO.flagActivo
			db.session.commit()
			print(colored("EnvioCorreoFiscalizadorDAO: Envio de correo actualizada correctamente", 'yellow'))
			result = True
			mensajes = "Envió de correo actualizado correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "envioCorreoFiscalizador":envioCorreoFiscalizador}
		except Exception as e:
			print(colored("EnvioCorreoFiscalizadorDAO: El envio de correo con id {} no se pudo actualizar. Error: {}".format(envioCorreoFiscalizadorVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El envío de correo no se pudo actualizar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def actualizarEstado(envioCorreoFiscalizadorVO):
		print(colored("EnvioCorreoFiscalizadorDAO: actualizarEstado(); id:{} idDenuncia:{} codigoEstadoEnvio:{}".format(envioCorreoFiscalizadorVO.id,envioCorreoFiscalizadorVO.idDenuncia,envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo), 'yellow'))
		try:
			envioCorreoFiscalizador = EnvioCorreoFiscalizador.query.get(envioCorreoFiscalizadorVO.id)
			if envioCorreoFiscalizador is not None:
				envioCorreoFiscalizador.cod_estado_envio_correo = envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo
				db.session.commit()
				print(colored("DenunciaDAO: El estado de envio de correo ha sido actualizado correctamente", 'yellow'))
				result = True
				mensajes = "Estado de denuncia actualizado correctamente"
				respuesta = {"result":result, "mensajes":mensajes, "envioCorreoFiscalizador":envioCorreoFiscalizador}
			else:
				print(colored("DenunciaDAO: El estado de envio de correo no se pudo actualizar. No existe envio de correo con id: {}".format(envioCorreoFiscalizadorVO.id), 'red'))
				result = False
				errores = "El estado del enevío de correo no se pudo actualizar. No existe envio de correo con id {}".format(envioCorreoFiscalizadorVO.id)
				respuesta = {"result":result, "errores":errores}
		except Exception as e:
			print(colored("EnvioCorreoFiscalizadorDAO: El estado del envío de correo con id {} y estado {} no se pudo actualizar. Error: {}".format(envioCorreoFiscalizadorVO.id, envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo, e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El estado del envío de correo no se pudo actualizar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("EnvioCorreoFiscalizadorDAO: eliminar(); {}".format(id), 'yellow'))
		envioCorreoFiscalizador = EnvioCorreoFiscalizador.query.get(id)
		if(envioCorreoFiscalizador is not None):
			try:
				result = True
				mensajes = "Envio de correo con id {} eliminado correctamente".format(id)
				db.session.delete(envioCorreoFiscalizador)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("EnvioCorreoFiscalizadorDAO: La denuncia con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "El envío de correo con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "El envío de correo con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta