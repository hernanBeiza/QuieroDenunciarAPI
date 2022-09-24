from ...app import db

class Materia(db.Model):
	__tablename__ = 'MATERIA'

	cod_materia = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(100), unique=False, nullable=False)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, cod_materia, glosa, activo):
		self.cod_materia = cod_materia
		self.glosa = glosa
		self.activo = activo
