from src.app import db

class TipoDireccion(db.Model):
	__tablename__ = 'TIPO_DIRECCION'

	cod_tipo_direccion = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, cod_tipo_direccion, glosa, flag_activo):
		self.cod_tipo_direccion = cod_tipo_direccion
		self.glosa = glosa
		self.flag_activo = flag_activo
