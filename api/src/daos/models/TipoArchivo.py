from src.app import db

class TipoArchivo(db.Model):
	__tablename__ = 'TIPO_ARCHIVO'

	cod_tipo_archivo = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, cod_tipo_archivo, glosa, flag_activo):
		self.cod_tipo_archivo = cod_tipo_archivo
		self.glosa = glosa
		self.flag_activo = flag_activo
