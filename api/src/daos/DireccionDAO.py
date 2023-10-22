from termcolor import colored

from src.app import db
from src.daos.models.Direccion import Direccion

class DireccionDAO():

	#def __init__(self):
		#print('ParteDAO')

	@staticmethod
	def guardar(direccionVO):
		print(colored("DireccionDAO: guardar(); {}".format(direccionVO), 'yellow'))

		try:
			direccion = Direccion(None, direccionVO.codigoTipoDireccion, direccionVO.idComuna, direccionVO.calle, direccionVO.numero, direccionVO.departamento, direccionVO.fechaCreacion, direccionVO.fechaModificacion, 1)
			db.session.add(direccion)
			db.session.commit()
			print(colored("DireccionDAO: dirección guardada correctamente", 'yellow'))
			result = True
			mensajes = "Dirección guardada correctamente"
			respuesta = {"result":result,"mensajes":mensajes, "direccion":direccion}
		except Exception as e:
			print(colored("DireccionDAO: La dirección no se pudo guardar. Error: {}".format(e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La dirección no se pudo guardar"
			respuesta = {"result":result,"errores":errores}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("DireccionDAO: obtener();", 'yellow'))
		return Direccion.query.all()

	@staticmethod
	def obtenerSegunId(id):
		print(colored("DireccionDAO: obtenerSegunId(); {}".format(id), 'yellow'))
		return Direccion.query.get(id)

	@staticmethod
	def actualizar(direccionVO):
		print(colored("DireccionDAO: actualizar(); {}".format(direccionVO), 'yellow'))
		try:
			direccion = Direccion.query.get(direccionVO.id)
			direccion.cod_tipo_direccion = direccionVO.codigoTipoDireccion
			direccion.id_comuna = direccionVO.idComuna
			direccion.calle = direccionVO.calle
			direccion.numero = direccionVO.numero
			direccion.departamento = direccionVO.departamento
			#direccion.fecha_creacion = parteVO.fechaCreacion
			#direccion.fecha_modificacion = parteVO.fechaModificacion
			direccion.flag_activo = direccionVO.flagActivo
			db.session.commit()
			print(colored("DireccionDAO: dirección editada correctamente", 'yellow'))
			result = True
			mensajes = "Dirección editada correctamente"
			respuesta = {"result":result, "mensajes":mensajes, "direccion":direccion}
		except Exception as e:
			print(colored("DireccionDAO: La dirección con id {} no se pudo editar. Error: {}".format(parteVO.id,e), 'red'))
			db.session.rollback()
			db.session.flush()
			result = False
			errores = "La dirección no se pudo editar"
			respuesta = {"result":result, "errores":errores}
		return respuesta

	@staticmethod
	def eliminar(id):
		print(colored("DireccionDAO: eliminar(); {}".format(id), 'yellow'))
		direccion = Direccion.query.get(id)
		if(direccion is not None):
			try:
				result = True
				mensajes = "Dirección con id {} eliminada correctamente".format(id)
				db.session.delete(direccion)
				db.session.commit()
				respuesta = {"result":result, "mensajes":mensajes}
			except Exception as e:
				print(colored("DireccionDAO: La dirección con id {} no se pudo eliminar. Error: {}".format(id,e), 'red'))
				db.session.rollback()
				db.session.flush()
				result = False
				mensajes = "La dirección con id {} no se pudo eliminar".format(id)
				respuesta = {"result":result, "errores":mensajes}
		else:
			result = False
			mensajes = "La dirección con id {} no se ha podido encontrar. No se pudo eliminar".format(id)
			respuesta = {"result":result, "errores":mensajes}
		return respuesta