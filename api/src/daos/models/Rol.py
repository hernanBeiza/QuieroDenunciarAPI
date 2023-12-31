import datetime

from src.db import db

class Rol(db.Model):
	__tablename__ = 'ROL'

	cod_rol = db.Column(db.Integer, primary_key=True)
	glosa = db.Column(db.String(45), nullable=False)
	flag_activo = db.Column(db.Integer, nullable=False)

	def __init__(self, cod_rol, nombre, flag_activo):
		self.cod_rol = cod_rol
		self.nombre = nombre
		self.flag_activo = flag_activo
