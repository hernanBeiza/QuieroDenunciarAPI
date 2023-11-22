import datetime

from src.db import db

class Antecedente(db.Model):
	__tablename__ = 'ANTECEDENTE'

	id_antecedente = db.Column(db.Integer, primary_key=True)
	#id_denuncia = db.Column(db.Integer, nullable=False)
	id_denuncia = db.Column(db.Integer, db.ForeignKey('DENUNCIA.id_denuncia'), nullable=False)
	descripcion = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime(), unique=False, nullable=False)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)
	#Relaciona la tabla hija con esta
	archivos = db.relationship('Archivo', lazy=True)

	def __init__(self, id_antecedente, id_denuncia, descripcion, fecha, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_antecedente = id_antecedente
		self.id_denuncia = id_denuncia
		self.descripcion = descripcion
		self.fecha = fecha
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
