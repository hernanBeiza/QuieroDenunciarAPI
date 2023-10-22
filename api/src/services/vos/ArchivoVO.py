import json

class ArchivoVO():
	idArchivo = None
	idAntecedente = None
	codigoTipoArchivo = None
	rutaArchivo = None
	nombreArchivo = None
	extensionArchivo = None
	fecha = None
	fechaCreacion = None
	fechaModificacion = None
	flagActivo = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)