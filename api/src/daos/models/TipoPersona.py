from src.app import db

class TipoPersona(db.Model):
	__tablename__ = 'TIPO_PERSONA'

	cod_tipo_persona = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, cod_tipo_persona, glosa, flag_activo):
		self.cod_tipo_persona = cod_tipo_persona
		self.glosa = glosa
		self.flag_activo = flag_activo
