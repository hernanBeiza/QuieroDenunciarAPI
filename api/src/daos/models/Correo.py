import datetime

from src.db import db

class Correo(db.Model):
	__tablename__ = 'CORREO'

	id_correo = db.Column(db.Integer, primary_key=True)
	id_ente_fiscalizador = db.Column(db.Integer, nullable=False)
	#id_ente_fiscalizador = db.Column(db.Integer, db.ForeignKey('ENTE_FISCALIZADOR.id_ente_fiscalizador'), nullable=False)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	#fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	#fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_principal = db.Column(db.Integer, unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, id_correo, id_ente_fiscalizador, glosa, flag_principal, flag_activo):
		self.id_correo = id_correo
		self.id_ente_fiscalizador = id_ente_fiscalizador
		self.glosa = glosa
		#self.fechaCreacion = fechaCreacion
		#self.fechaModificacion = fechaModificacion
		self.flag_principal = flag_principal
		self.flag_activo = flag_activo
