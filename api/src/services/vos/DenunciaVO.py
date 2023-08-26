import json

class DenunciaVO():
	idDenuncia = None
	idDenunciado = None
	idDenunciante = None
	idDireccion = None
	codigoMateria = None
	codigoEstado = None
	descripcion = None
	fecha = None

	fechaCreacion = None
	fechaModificacion = None
	flagActivo = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)
