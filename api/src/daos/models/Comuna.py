from ...app import db

class Comuna(db.Model):
	__tablename__ = 'COMUNA'

	id_comuna = db.Column(db.Integer, primary_key=True)
	id_provincia = db.Column(db.Integer, unique=False, nullable=False)
	comuna = db.Column(db.String, unique=False, nullable=False)

	def __init__(self, id_comuna, id_provincia, comuna):
		self.id_comuna = id_comuna
		self.id_provincia = id_provincia
		self.comuna = comuna
