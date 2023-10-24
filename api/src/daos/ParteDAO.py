from termcolor import colored

from src.app import db
from src.daos.models.Parte import Parte

class ParteDAO():

	#def __init__(self):
		#print('ParteDAO')

	@staticmethod
	def guardar(parteVO):
		print(colored("ParteDAO: guardar(); {}".format(parteVO), 'yellow'))
		print(colored("ParteDAO: guardar(); {}".format(parteVO.codigoTipoParte), 'yellow'))

		try:
			parte = Parte(None, parteVO.rut, parteVO.idDireccion, parteVO.codigoTipoParte, parteVO.correo, parteVO.fechaCreacion, parteVO.fechaModificacion, 1)
			db.session.add(parte)
			db.session.commit()
			print(colored("ParteDAO: parte guardada correctamente", 'yellow'))
			result = True
			mensajes = "Parte guardada correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "parte":parte}
		except Exception as e:
			print(colored("ParteDAO: La parte no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La parte no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("ParteDAO: obtener();", 'yellow'))
		return Parte.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("ParteDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Parte.query.get(id)

	@staticmethod
	def obtenerSegunRut(rut):
		print(colored("ParteDAO: obtenerSegunRut(); {}".format(rut), 'yellow'))
		return Parte.query.filter_by(rut=rut).all()

	@staticmethod
	def actualizar(parteVO):
		print(colored("ParteDAO: actualizar(); {}".format(parteVO), 'yellow'))
		try:
			parte = Parte.query.get(parteVO.id)
			parte.rut = parteVO.rut
			parte.idDireccion = parteVO.idDireccion
			parte.cod_tipo_parte = parteVO.codigoTipoParte
			parte.correo = parteVO.correo
			parte.fecha_creacion = parteVO.fechaCreacion
			#parte.fecha_modificacion = parteVO.fechaModificacion
			db.session.commit()
			print(colored("ParteDAO: parte editada correctamente", 'yellow'))
			result = True
			mensajes = "Parte editada correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "parte":parte}
		except Exception as e:
			print(colored("ParteDAO: La parte con id {} no se pudo editar. Error: {}".format(parteVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La parte no se pudo editar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("ParteDAO: eliminar(); {}".format(id), 'yellow'))
		parte = Parte.query.get(id)
		if(parte is not None):
			try:
				result = True
				mensajes = "Parte con id {} eliminada correctamente".format(id)
				db.session.delete(parte)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("ParteDAO: La parte con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "La parte con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "La parte con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta