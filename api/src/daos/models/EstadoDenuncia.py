from src.db import db

class EstadoDenuncia(db.Model):
	__tablename__ = 'ESTADO_DENUNCIA'

	cod_estado_denuncia = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, cod_estado_denuncia, glosa, flag_activo):
		self.cod_estado_denuncia = cod_estado_denuncia
		self.glosa = glosa
		self.flag_activo = flag_activo
