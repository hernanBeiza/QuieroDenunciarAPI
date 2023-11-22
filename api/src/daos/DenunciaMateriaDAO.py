from termcolor import colored

from src.db import db
from src.daos.models.DenunciaMateria import DenunciaMateria

class DenunciaMateriaDAO():

	#def __init__(self):
		#print('DenunciaMateriaDAO')

	@staticmethod
	def guardar(denunciaMateriaVO):
		print(colored("DenunciaMateriaDAO: guardar(); {}".format(denunciaMateriaVO), 'yellow'))
		try:
			denunciaMateria = DenunciaMateria(None, denunciaMateriaVO.idDenuncia, denunciaMateriaVO.codigoMateria, denunciaMateriaVO.fechaCreacion, denunciaMateriaVO.fechaModificacion, denunciaMateriaVO.flagActivo)
			db.session.add(denunciaMateria)
			db.session.commit()
			print(colored("DenunciaMateriaDAO: DenunciaMateria guardado correctamente", 'yellow'))
			result = True
			mensajes = "DenunciaMateria guardada correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "denunciaMateria":denunciaMateria}
		except Exception as e:
			print(colored("DenunciaMateriaDAO: La DenunciaMateria no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La DenunciaMateria no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("DenunciaMateriaDAO: obtener();", 'yellow'))
		return DenunciaMateria.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("DenunciaMateriaDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return DenunciaMateria.query.get(id)

	@staticmethod
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("DenunciaMateriaDAO: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'yellow'))
		return DenunciaMateria.query.filter_by(id_denuncia=idDenuncia).all()

	@staticmethod
	def actualizar(denunciaMateriaVO):
		print(colored("DenunciaMateriaDAO: actualizar(); {}".format(denunciaMateriaVO), 'yellow'))
		try:
			denunciaMateria = DenunciaMateria.query.get(denunciaMateriaVO.id)
			denunciaMateria.id_denuncia_materia = denunciaMateriaVO.id
			denunciaMateria.id_denuncia = denunciaMateriaVO.idDenuncia
			denunciaMateria.cod_materia = denunciaMateriaVO.codigoMateria
			denunciaMateria.fecha_creacion = denunciaMateriaVO.fechaCreacion
			denunciaMateria.flag_activo = denunciaMateriaVO.flagActivo
			db.session.commit()
			print(colored("DenunciaMateriaDAO: DenunciaMateria actualizada correctamente", 'yellow'))
			result = True
			mensajes = "DenunciaMateria actualizada correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "denunciaMateria":denunciaMateria}
		except Exception as e:
			print(colored("DenunciaMateriaDAO: La DenunciaMateria con id {} no se pudo actualizar. Error: {}".format(denunciaMateriaVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La DenunciaMateria no se pudo actualizar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("DenunciaMateriaDAO: eliminar(); {}".format(id), 'yellow'))
		denuncia = DenunciaMateria.query.get(id)
		if(denuncia is not None):
			try:
				result = True
				mensajes = "Denuncia con id {} eliminada correctamente".format(id)
				db.session.delete(denuncia)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("DenunciaMateriaDAO: La DenunciaMateria con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "La DenunciaMateria con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "La DenunciaMateria con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta