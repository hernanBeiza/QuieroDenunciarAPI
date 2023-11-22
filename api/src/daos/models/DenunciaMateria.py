import datetime

from src.db import db

class DenunciaMateria(db.Model):
	__tablename__ = 'DENUNCIA_MATERIA'

	id_denuncia_materia = db.Column(db.Integer, primary_key=True)
	#id_denuncia = db.Column(db.Integer, nullable=False)
	id_denuncia = db.Column(db.Integer, db.ForeignKey('DENUNCIA.id_denuncia'), nullable=False)
	#cod_materia = db.Column(db.Integer, nullable=False)
	cod_materia = db.Column(db.Integer, db.ForeignKey('MATERIA.cod_materia'), nullable=False)	
	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	#denuncia = db.relationship('Denuncia', backref=db.backref("Denuncia", cascade="all, delete-orphan"))
	#denuncia = db.relationship('Denuncia', lazy=True)
	materia = db.relationship('Materia', lazy=True)

	def __init__(self, id_denuncia_materia, id_denuncia, cod_materia, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_denuncia_materia = id_denuncia_materia
		self.id_denuncia = id_denuncia
		self.cod_materia = cod_materia
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
