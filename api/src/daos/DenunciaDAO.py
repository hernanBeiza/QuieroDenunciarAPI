from termcolor import colored

from src.db import db
from src.daos.models.Denuncia import Denuncia

class DenunciaDAO():

	#def __init__(self):
		#print('DenunciaDAO')

	@staticmethod
	def guardar(denunciaVO):
		print(colored("DenunciaDAO: guardar(); {}".format(denunciaVO), 'yellow'))
		try:
			denuncia = Denuncia(None, denunciaVO.idDenunciado, denunciaVO.idDenunciante, denunciaVO.idDireccion, denunciaVO.codigoEstadoDenuncia, denunciaVO.descripcion, denunciaVO.fecha, denunciaVO.fechaCreacion, denunciaVO.fechaModificacion, 1)
			db.session.add(denuncia)
			db.session.commit()
			print(colored("DenunciaDAO: denuncia guardado correctamente", 'yellow'))
			result = True
			mensajes = "Denuncia guardada correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "denuncia":denuncia}
		except Exception as e:
			print(colored("DenunciaDAO: La denuncia no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La denuncia no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("DenunciaDAO: obtener();", 'yellow'))
		return Denuncia.query.all()

	@staticmethod
	def obtenerPaginadas(pagina):
		print(colored("DenunciaDAO: obtenerPaginadas(); {}".format(pagina), 'yellow'))
		return Denuncia.query.order_by(Denuncia.id_denuncia.desc()).paginate(page=pagina, per_page=5)

	@staticmethod
	def obtenerSegunId(id):
		print(colored("DenunciaDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Denuncia.query.get(id)

	@staticmethod
	def obtenerSegunIdDenunciado(idDenunciado):
		print(colored("DenunciaDAO: obtenerSegunIdDenunciado(); {}".format(idDenunciado), 'yellow'))
		return Denuncia.query.filter_by(id_denunciado=idDenunciado).all()


	@staticmethod
	def obtenerSegunIdDenunciante(idDenunciante):
		print(colored("DenunciaDAO: obtenerSegunIdDenunciante(); {}".format(idDenunciante), 'yellow'))
		return Denuncia.query.filter_by(id_denunciante=idDenunciante).all()

	@staticmethod
	def actualizar(denunciaVO):
		print(colored("DenunciaDAO: actualizar(); {}".format(denunciaVO), 'yellow'))
		try:
			denuncia = Denuncia.query.get(denunciaVO.id)
			denuncia.id_denuncia = denunciaVO.id
			denuncia.id_denunciado = denunciaVO.idDenunciado
			denuncia.id_denunciante = denunciaVO.idDenunciante
			denuncia.id_direccion = denunciaVO.idDireccion
			denuncia.cod_estado = denunciaVO.codigoEstado
			denuncia.descripcion = denunciaVO.descripcion
			denuncia.fecha = denunciaVO.fecha
			denuncia.fecha_creacion = denunciaVO.fechaCreacion
			denuncia.flag_activo = denunciaVO.flagActivo
			#denuncia.fecha_modificacion = denunciaVO.fechaModificacion
			db.session.commit()
			print(colored("DenunciaDAO: denuncia actualizada correctamente", 'yellow'))
			result = True
			mensajes = "Denuncia editada correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "denuncia":denuncia}
		except Exception as e:
			print(colored("DenunciaDAO: La denuncia con id {} no se pudo actualizar. Error: {}".format(denunciaVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La denuncia no se pudo editar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def actualizarEstado(denunciaVO):
		print(colored("DenunciaDAO: actualizarEstado(); idDenuncia:{} codigoEstado:{}".format(denunciaVO.id,denunciaVO.codigoEstado), 'yellow'))
		try:
			denuncia = Denuncia.query.get(denunciaVO.id)
			if denuncia is not None:
				denuncia.id_denuncia = denunciaVO.id
				denuncia.cod_estado = denunciaVO.codigoEstado
				db.session.commit()
				print(colored("DenunciaDAO: El estado de denuncia ha sido actualizado correctamente", 'yellow'))
				result = True
				mensajes = "Estado de denuncia actualizado correctamente"
				respuesta = {"result":result, "mensajes":mensajes, "denuncia":denuncia}
			else:
				print(colored("DenunciaDAO: El estado de la denuncia no se pudo actualizar. No existe denuncia con id: {}".format(denunciaVO.idDenuncia), 'red'))
				result = False
				errores = "El estado de la denuncia no se pudo actualizar. No existe denuncia con id {}".format(denunciaVO.idDenuncia)
				respuesta = {"result":result, "errores":errores}
		except Exception as e:
			print(colored("DenunciaDAO: El estado de la denuncia con id {} y estado {} no se pudo actualizar. Error: {}".format(denunciaVO.idDenuncia, denunciaVO.codigoEstado, e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El estado de la denuncia no se pudo actualizar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("DenunciaDAO: eliminar(); {}".format(id), 'yellow'))
		denuncia = Denuncia.query.get(id)
		if(denuncia is not None):
			try:
				result = True
				mensajes = "Denuncia con id {} eliminado correctamente".format(id)
				db.session.delete(denuncia)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("DenunciaDAO: La denuncia con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "La denuncia con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "La denuncia con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta