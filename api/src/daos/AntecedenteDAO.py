from termcolor import colored

from src.app import db
from src.daos.models.Antecedente import Antecedente

class AntecedenteDAO():

	#def __init__(self):
		#print('AntecedenteDAO')

	@staticmethod
	def guardar(antecedenteVO):
		print(colored("AntecedenteDAO: guardar(); {}".format(antecedenteVO), 'yellow'))

		try:
			antecedente = Antecedente(None, antecedenteVO.idDenuncia, antecedenteVO.descripcion, antecedenteVO.fecha, antecedenteVO.fechaCreacion, antecedenteVO.fechaModificacion, 1)
			db.session.add(antecedente)
			db.session.commit()
			print(colored("AntecedenteDAO: antecedente guardado correctamente", 'yellow'))
			result = True
			mensajes = "Antecedente guardado correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "antecedente":antecedente}
		except Exception as e:
			print(colored("AntecedenteDAO: El antecedente no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El antecedente no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("AntecedenteDAO: obtener();", 'yellow'))
		return Antecedente.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("AntecedenteDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Antecedente.query.get(id)

	@staticmethod
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("AntecedenteDAO: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'yellow'))
		return Antecedente.query.filter_by(id_denuncia=idDenuncia).all()

	@staticmethod
	def actualizar(antecedenteVO):
		print(colored("AntecedenteDAO: actualizar(); {}".format(antecedenteVO), 'yellow'))
		try:
			antecedente = Antecedente.query.get(antecedenteVO.id)
			antecedente.id_antecedente = antecedenteVO.id
			antecedente.id_denuncia = antecedenteVO.idDenuncia
			antecedente.fecha = antecedenteVO.fecha
			antecedente.descripcion = antecedenteVO.descripcion
			antecedente.fecha_creacion = antecedenteVO.fechaCreacion
			antecedente.flag_activo = antecedenteVO.flagActivo
			#antecedente.fecha_modificacion = antecedenteVO.fechaModificacion
			db.session.commit()
			print(colored("AntecedenteDAO: antecedente editado correctamente", 'yellow'))
			result = True
			mensajes = "Archivo editado correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "antecedente":antecedente}
		except Exception as e:
			print(colored("AntecedenteDAO: El antecedente con id {} no se pudo editar. Error: {}".format(antecedenteVO.idAntecedente,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "El antecedente no se pudo editar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("AntecedenteDAO: eliminar(); {}".format(id), 'yellow'))
		antecedente = Antecedente.query.get(id)
		if(antecedente is not None):
			try:
				result = True
				mensajes = "Antecedente con id {} eliminado correctamente".format(id)
				db.session.delete(antecedente)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("AntecedenteDAO: El antecedente con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "El antecedente con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "El antecedente con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta