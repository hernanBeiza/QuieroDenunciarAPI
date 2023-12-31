import json

class UsuarioVO():
	id = None
	codigoRol = None
	nombre = None
	usuario = None
	contrasena = None
	fechaCreacion = None
	fechaModificacion = None
	flagActivo = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)