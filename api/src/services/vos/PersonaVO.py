import json

class PersonaVO():
	id = None
	rut = None
	dv = None
	nombre = None
	nombreSegundo = None
	apellidoPaterno = None
	apellidoMaterno = None
	fechaCreacion = None
	fechaModificacion = None
	codigoTipoPersona = None
	flagActivo = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)