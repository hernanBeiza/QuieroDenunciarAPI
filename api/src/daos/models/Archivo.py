import datetime

from src.app import db

class Archivo(db.Model):
	__tablename__ = 'ARCHIVO'

	id_archivo = db.Column(db.Integer, primary_key=True)
	#id_antecedente = db.Column(db.Integer, nullable=False)
	##Debe llamarse a la tabla y columna que se relaciona con esta columna
	id_antecedente = db.Column(db.Integer,db.ForeignKey('ANTECEDENTE.id_antecedente'), nullable=True)

	cod_tipo_archivo = db.Column(db.Integer, nullable=False)
	ruta_archivo = db.Column(db.String, nullable=False)
	nombre_archivo = db.Column(db.String, nullable=False)
	extension_archivo = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime(), nullable=False)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, id_archivo, id_antecedente, cod_tipo_archivo, ruta_archivo, nombre_archivo, extension_archivo, fecha, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_archivo = id_archivo
		self.id_antecedente = id_antecedente
		self.cod_tipo_archivo = cod_tipo_archivo
		self.ruta_archivo = ruta_archivo
		self.nombre_archivo = nombre_archivo
		self.extension_archivo = extension_archivo
		self.fecha = fecha
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
