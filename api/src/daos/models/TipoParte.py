from ...app import db

class TipoParte(db.Model):
	__tablename__ = 'TIPO_PARTE'

	cod_tipo_parte = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)
	
	def __init__(self, cod_tipo_parte, glosa, flag_activo):
		self.cod_tipo_parte = cod_tipo_parte
		self.glosa = glosa
		self.flag_activo = flag_activo
