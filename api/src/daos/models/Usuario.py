import datetime

from src.db import db

class Usuario(db.Model):
	__tablename__ = 'USUARIO'

	id_usuario = db.Column(db.Integer, primary_key=True)

	#TODO Debe llamarse a la tabla y columna que se relaciona con la columna cod_rol de USUARIO
	cod_rol = db.Column(db.Integer, db.ForeignKey('ROL.cod_rol'), nullable=False)
	#cod_rol = db.Column(db.Integer, nullable=False)
	nombre = db.Column(db.String(45), nullable=False)
	usuario = db.Column(db.String(45), nullable=False)
	contrasena = db.Column(db.String(300), nullable=False)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	#TODO Relaciona el modelo de la tabla hija ROL con el modelo padre Usuario de tabla USUARIO
	rol = db.relationship('Rol', lazy=True)

	def __init__(self, id_usuario, cod_rol, nombre, usuario, contrasena, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_usuario = id_usuario
		self.cod_rol = cod_rol
		self.nombre = nombre
		self.usuario = usuario
		self.contrasena = contrasena
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
