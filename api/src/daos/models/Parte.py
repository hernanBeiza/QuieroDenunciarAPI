import datetime

from src.app import db
#Se importa para poder usar la TipoParte Materia en la relació
from src.daos.models.TipoParte import TipoParte

class Parte(db.Model):
	__tablename__ = 'PARTE'

	id_parte = db.Column(db.Integer, primary_key=True)
	id_persona = db.Column(db.Integer, unique=False, nullable=False)
	id_direccion = db.Column(db.Integer, unique=False, nullable=False)
	#cod_tipo_parte = db.Column(db.Integer, unique=False, nullable=False)
	cod_tipo_parte = db.Column(db.Integer, db.ForeignKey('TIPO_PARTE.cod_tipo_parte'), nullable=False)
	correo = db.Column(db.String(200), unique=False, nullable=True)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	tipoParte = db.relationship('TipoParte', lazy=True, uselist=False)

	def __init__(self, id_parte, id_persona, id_direccion, cod_tipo_parte, correo, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_parte = id_parte
		self.id_persona = id_persona
		self.id_direccion = id_direccion
		self.cod_tipo_parte = cod_tipo_parte
		self.correo = correo
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
