import datetime

from src.app import db
#Se importa para poder usar la clase Direccion en la relació
from src.daos.models.Direccion import Direccion
#Se importa para poder usar la clase Materia en la relació
from src.daos.models.Materia import Materia
#Se importa para poder usar la clase Parte en la relació
from src.daos.models.Parte import Parte
#Se importa para poder usar la clase DenunciaMateria en la relación
from src.daos.models.DenunciaMateria import DenunciaMateria

class Denuncia(db.Model):
	__tablename__ = 'DENUNCIA'

	id_denuncia = db.Column(db.Integer, primary_key=True)
	#id_denunciado = db.Column(db.Integer, nullable=False)
	id_denunciado = db.Column(db.Integer, db.ForeignKey('PARTE.id_parte'), nullable=False)
	#id_denunciante = db.Column(db.Integer, nullable=False)
	id_denunciante = db.Column(db.Integer, db.ForeignKey('PARTE.id_parte'), nullable=False)
	#id_direccion = db.Column(db.Integer, nullable=False)
	id_direccion = db.Column(db.Integer, db.ForeignKey('DIRECCION.id_direccion'), nullable=False)
	cod_estado = db.Column(db.Integer, nullable=False)
	descripcion = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime(), unique=False, nullable=False)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	#TODO Relaciona la tabla hija con esta
	denunciado = db.relationship('Parte', foreign_keys=[id_denunciado], lazy=True)
	denunciante = db.relationship('Parte', foreign_keys=[id_denunciante], lazy=True)
	direccion = db.relationship('Direccion', lazy=True)
	denunciasMaterias = db.relationship('DenunciaMateria', uselist=True, lazy=True)
	antecedentes = db.relationship('Antecedente', uselist=True, lazy=True)

	def __init__(self, id_denuncia, id_denunciado, id_denunciante, id_direccion, cod_estado, descripcion, fecha, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_denuncia = id_denuncia
		self.id_denunciado = id_denunciado
		self.id_denunciante = id_denunciante
		self.id_direccion = id_direccion
		self.cod_estado = cod_estado
		self.descripcion = descripcion
		self.fecha = fecha
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
