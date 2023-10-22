import datetime

from src.app import db
from src.daos.models.TipoDireccion import TipoDireccion

class Direccion(db.Model):
	__tablename__ = 'DIRECCION'

	id_direccion = db.Column(db.Integer, primary_key=True)
	#id_comuna = db.Column(db.Integer, unique=False, nullable=False)
	#cod_tipo_direccion = db.Column(db.Integer, unique=False, nullable=False)
	cod_tipo_direccion = db.Column(db.Integer, db.ForeignKey('TIPO_DIRECCION.cod_tipo_direccion'), nullable=False)
	id_comuna = db.Column(db.Integer, db.ForeignKey('COMUNA.id_comuna'), nullable=False)

	calle = db.Column(db.String(255), unique=False, nullable=False)
	numero = db.Column(db.Integer, unique=False, nullable=False)
	departamento = db.Column(db.Integer, unique=False, nullable=False)
	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	#TODO Debe llamarse igual al declarado en el objeto DireccionVOBuilder
	comuna = db.relationship('Comuna', lazy=True, uselist=False)
	tipoDireccion = db.relationship('TipoDireccion', lazy=True, uselist=False)

	def __init__(self, id_direccion, cod_tipo_direccion, id_comuna, calle, numero, departamento, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_direccion = id_direccion
		self.cod_tipo_direccion = cod_tipo_direccion
		self.id_comuna = id_comuna
		self.calle = calle
		self.numero = numero
		self.departamento = departamento
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
