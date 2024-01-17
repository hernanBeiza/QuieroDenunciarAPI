from src.db import db

class EstadoEnvioCorreo(db.Model):
	__tablename__ = 'ESTADO_ENVIO_CORREO'

	cod_estado_envio_correo = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, cod_estado_envio_correo, glosa, flag_activo):
		self.cod_estado_envio_correo = cod_estado_envio_correo
		self.glosa = glosa
		self.flag_activo = flag_activo
