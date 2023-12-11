import json

class DireccionVO():
	id = None
	codigoTipoDireccion = None
	idComuna = None
	calle = None
	numero = None
	departamento = None
	fechaCreacion = None
	fechaModificacion = None
	flagActivo = None
	comuna = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)