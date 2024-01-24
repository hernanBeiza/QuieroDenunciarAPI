import json

class EnvioCorreoFiscalizadorVO():
	id = None
	idFiscalizador = None
	idDenuncia = None
	codigoEstadoEnvioCorreo = None
	fechaEnvio = None
	fechaCreacion = None
	fechaModificacion = None
	flagActivo = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)