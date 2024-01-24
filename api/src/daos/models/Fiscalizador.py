import datetime

from src.db import db

class Fiscalizador(db.Model):
	__tablename__ = 'FISCALIZADOR'

	id_fiscalizador = db.Column(db.Integer, primary_key=True)
	id_comuna = db.Column(db.Integer, nullable=False)
	#id_comuna = db.Column(db.Integer, db.ForeignKey('COMUNA.id_comuna'), nullable=False)
	nombre = db.Column(db.String(100), unique=False, nullable=False)
	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	correos = db.relationship('Correo', uselist=True, lazy=True)

	def __init__(self, id_fiscalizador, id_comuna, nombre, fechaCreacion, fechaModificacion, flag_activo):
		self.id_fiscalizador = id_fiscalizador
		self.id_comuna = id_comuna
		self.nombre = nombre
		self.fechaCreacion = fechaCreacion
		self.fechaModificacion = fechaModificacion
		self.flag_activo = flag_activo
