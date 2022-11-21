import datetime

from src.app import db

class Parte(db.Model):
	__tablename__ = 'PARTE'

	id = db.Column(db.Integer, primary_key=True)
	rut = db.Column(db.String(8), unique=True, nullable=False)
	id_direccion = db.Column(db.Integer, unique=False, nullable=False)
	#cod_tipo_parte = db.Column(db.Integer, unique=False, nullable=False)
	cod_tipo_parte = db.Column(db.Integer, db.ForeignKey('TIPO_PARTE.cod_tipo_parte'), nullable=False)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	tipoParte = db.relationship('TipoParte', lazy=True, uselist=False)

	def __init__(self, id, rut, id_direccion, cod_tipo_parte, fecha_creacion, fecha_modificacion, flag_activo):
		self.id = id
		self.rut = rut
		self.id_direccion = id_direccion
		self.cod_tipo_parte = cod_tipo_parte
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
