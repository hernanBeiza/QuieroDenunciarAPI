import datetime

from src.db import db
#Se importa para poder usar la clase Materia en la relació
from src.daos.models.Materia import Materia
#Se importa para poder usar la clase Parte en la relació
from src.daos.models.Parte import Parte
#Se importa para poder usar la clase DenunciaMateria en la relación
from src.daos.models.DenunciaMateria import DenunciaMateria
#Se importa para poder usar la clase EstadoDenuncia en la relación
from src.daos.models.EstadoDenuncia import EstadoDenuncia

class Denuncia(db.Model):
	__tablename__ = 'DENUNCIA'

	id_denuncia = db.Column(db.Integer, primary_key=True)
	#id_denunciado = db.Column(db.Integer, nullable=False)
	id_denunciado = db.Column(db.Integer, db.ForeignKey('PARTE.id_parte'), nullable=False)
	#id_denunciante = db.Column(db.Integer, nullable=False)
	id_denunciante = db.Column(db.Integer, db.ForeignKey('PARTE.id_parte'), nullable=True)
	#cod_estado_denuncia = db.Column(db.Integer, nullable=False)
	cod_estado_denuncia = db.Column(db.Integer, db.ForeignKey('ESTADO_DENUNCIA.cod_estado_denuncia'), nullable=False)
	descripcion = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime(), unique=False, nullable=False)

	fecha_creacion = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	fecha_modificacion = db.Column(db.DateTime(), unique=False, nullable=True, default=None, onupdate=datetime.datetime.utcnow)
	flag_activo = db.Column(db.Integer, unique=False, nullable=False)

	#TODO Relaciona la tabla hija con esta
	denunciado = db.relationship('Parte', foreign_keys=[id_denunciado], lazy=True)
	denunciante = db.relationship('Parte', foreign_keys=[id_denunciante], lazy=True)
	estadoDenuncia = db.relationship('EstadoDenuncia', lazy=True)

	denunciasMaterias = db.relationship('DenunciaMateria', uselist=True, lazy=True)
	archivos = db.relationship('Archivo', uselist=True, lazy=True)

	def __init__(self, id_denuncia, id_denunciado, id_denunciante, cod_estado_denuncia, descripcion, fecha, fecha_creacion, fecha_modificacion, flag_activo):
		self.id_denuncia = id_denuncia
		self.id_denunciado = id_denunciado
		self.id_denunciante = id_denunciante
		self.cod_estado_denuncia = cod_estado_denuncia
		self.descripcion = descripcion
		self.fecha = fecha
		self.fecha_creacion = fecha_creacion
		self.fecha_modificacion = fecha_modificacion
		self.flag_activo = flag_activo
