import json

class ComunaVO():
	idComuna = None
	idProvincia = None
	comuna = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)