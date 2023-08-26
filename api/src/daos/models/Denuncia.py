import datetime

from src.app import db

class Denuncia(db.Model):
	__tablename__ = 'DENUNCIA'

	id_denuncia = db.Column(db.Integer, primary_key=True)
	id_denunciado = db.Column(db.Integer, nullable=False)
	id_denunciante = db.Column(db.Integer, nullable=False)
	id_direccion = db.Column(db.Integer, nullable=False)
	cod_materia = db.Column(db.Integer, nullable=False)
	cod_estado = db.Column(db.Integer, nullable=False)
	descripcion = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime(), unique=False, nullable=False)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	#Relaciona la tabla hija con esta
	#antecedentes = db.relationship('Antecedente', backref='Denuncia', lazy=True)

	def __init__(self, id_denuncia, id_denunciado, id_denunciante, id_direccion, cod_materia, cod_estado, descripcion, fecha, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_denuncia = id_denuncia
		self.id_denunciado = id_denunciado
		self.id_denunciante = id_denunciante
		self.id_direccion = id_direccion
		self.cod_materia = cod_materia
		self.cod_estado = cod_estado
		self.descripcion = descripcion
		self.fecha = fecha
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
