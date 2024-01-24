import datetime

from src.db import db

class EnvioCorreoFiscalizador(db.Model):
	__tablename__ = 'ENVIO_CORREO_FISCALIZADOR'

	id_envio_correo_fiscalizador = db.Column(db.Integer, primary_key=True)
	id_fiscalizador = db.Column(db.Integer, nullable=False)
	#id_fiscalizador = db.Column(db.Integer, db.ForeignKey('FISCALIZADOR.id_fiscalizador'), nullable=False)
	id_denuncia = db.Column(db.Integer, nullable=False)
	#id_denuncia = db.Column(db.Integer, db.ForeignKey('DENUNCIA.id_denuncia'), nullable=False)
	cod_estado_envio_correo = db.Column(db.Integer, nullable=False)
	#cod_estado_envio_correo = db.Column(db.Integer, db.ForeignKey('ESTADO_ENVIO_CORREO.cod_estado_envio_correo'), nullable=False)

	fecha_envio = db.Column(db.DateTime(), unique=False, nullable=True, default=None)
	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, id_envio_correo_fiscalizador, id_fiscalizador, id_denuncia, cod_estado_envio_correo, fecha_envio, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_envio_correo_fiscalizador = id_envio_correo_fiscalizador
		self.id_fiscalizador = id_fiscalizador
		self.id_denuncia = id_denuncia
		self.cod_estado_envio_correo = cod_estado_envio_correo
		self.fecha_envio = fecha_envio
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
