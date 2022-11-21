import datetime

from src.app import db

class Persona(db.Model):
	__tablename__ = 'PERSONA'

	id = db.Column(db.Integer, primary_key=True)
	rut = db.Column(db.String(8), unique=True, nullable=False)
	dv = db.Column(db.String(1), unique=False, nullable=False)
	nombre = db.Column(db.String(100), unique=False, nullable=False)
	nombre_segundo = db.Column(db.String(100), unique=False, nullable=False)
	apellido_paterno = db.Column(db.String(100), unique=False, nullable=False)
	apellido_materno = db.Column(db.String(100), unique=False, nullable=False)
	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	cod_tipo_persona = db.Column(db.Integer, unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, id, rut, dv, nombre, nombreSegundo, apellidoPaterno, apellidoMaterno, fecha_creacion, fecha_modificacion, cod_tipo_persona, flag_activo):
		self.id = id
		self.rut = rut
		self.dv = dv
		self.nombre = nombre
		self.nombre_segundo = nombreSegundo
		self.apellido_paterno = apellidoPaterno
		self.apellido_materno = apellidoMaterno
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.cod_tipo_persona = cod_tipo_persona
		self.flag_activo = flag_activo
