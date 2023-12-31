import json

class EstadoDenunciaVO():
	codigo = None
	glosa = None
	flagActivo = None

	#def __init__(self):
		#constructor por defecto
		#print("Constructor por defecto")

	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, indent=2)