import os
import markdown
import datetime
from flask_mail import Mail, Message
from termcolor import colored

from src.app import app
from src.mail import mail
from src.utils.DocumentoUtils import DocumentoUtils
from src.daos.EnvioCorreoFiscalizadorDAO import EnvioCorreoFiscalizadorDAO
from src.daos.FiscalizadorDAO import FiscalizadorDAO
from src.daos.DenunciaDAO import DenunciaDAO
from src.daos.DireccionDAO import DireccionDAO
from src.services.vos.EnvioCorreoFiscalizadorVO import EnvioCorreoFiscalizadorVO
from src.services.vos.DenunciaVO import DenunciaVO
from src.services.builder.VOBuilderFactory import VOBuilderFactory

class EnvioCorreoFiscalizadorService():

	#def __init__(self):
		#print('EnvioCorreoFiscalizadorService')

	@staticmethod
	def guardar(request):
		print(colored("EnvioCorreoFiscalizadorService: guardar(); {}".format(request.get_json()), 'cyan'))

		idFiscalizador = request.get_json()["idFiscalizador"] if 'idFiscalizador' in request.get_json() else None
		idDenuncia = request.get_json()["idDenuncia"] if 'idDenuncia' in request.get_json() else None
		codigoEstadoEnvioCorreo = request.get_json()["codigoEstadoEnvioCorreo"] if 'codigoEstadoEnvioCorreo' in request.get_json() else 1
		fechaEnvio = request.get_json()["fechaEnvio"] if 'fechaEnvio' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(idFiscalizador==None):
			enviar = False
			mensajes +="\nFiscalizador"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nDenuncia"
		if(codigoEstadoEnvioCorreo==None):
			enviar = False
			mensajes +="\nCódigo de estado de envíó"
		if(fechaEnvio==None):
			enviar = False
			mensajes +="\nFecha de envíó"

		if(enviar):
			envioCorreoFiscalizadorVO = EnvioCorreoFiscalizadorVO()
			envioCorreoFiscalizadorVO.idFiscalizador = idFiscalizador
			envioCorreoFiscalizadorVO.idDenuncia = idDenuncia
			envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo = codigoEstadoEnvioCorreo
			envioCorreoFiscalizadorVO.fechaEnvio = fechaEnvio
			envioCorreoFiscalizadorVO.flagActivo = 1
			
			respuesta = EnvioCorreoFiscalizadorDAO.guardar(envioCorreoFiscalizadorVO)
			if(respuesta["result"]):
				respuesta["envioCorreoFiscalizador"] = VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizador(respuesta["envioCorreoFiscalizador"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("EnvioCorreoFiscalizadorService: obtener();", 'cyan'))
		envioCorreosFiscalizadores = EnvioCorreoFiscalizadorDAO.obtener()
		if len(envioCorreosFiscalizadores)>0:
			data = {
				"result":True,
				"envioCorreosFiscalizadores":VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizadores(envioCorreosFiscalizadores).builds(),
				"mensajes":"Se encontraron envíos de correo"
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron envíos de correo"
			}
		return data

	@staticmethod
	def obtenerPaginadas(pagina):
		print(colored("EnvioCorreoFiscalizadorService: obtenerPaginadas(); {}".format(pagina), 'cyan'))
		try:
			paginacion = EnvioCorreoFiscalizadorDAO.obtenerPaginadas(pagina)
			if len(paginacion.items)>0:
				data = {
					"result":True,
					"envioCorreosFiscalizadores":VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizadores(paginacion.items).builds(),
					"mensajes":"Se encontraron envíos de correos de la página {}".format(pagina),
					"paginas":paginacion.pages
				}
			else:
				data = {
					"result":False,
					"errores":"No se encontraron envíos de correo en la página {}".format(pagina)
				}
		except Exception as e:
			print(colored("EnvioCorreoFiscalizadorService: No se encontraron denuncias en la página {}. Error: {}".format(pagina, e), 'red'))
			data = {
				"result":False,
				"errores":"No se encontraron denuncias en la página {}".format(pagina)
			}
		return data;

	@staticmethod
	def obtenerSegunId(id):
		print(colored("EnvioCorreoFiscalizadorService: obtenerSegunId(); {}".format(id), 'cyan'))
		envioCorreoFiscalizador = EnvioCorreoFiscalizadorDAO.obtenerSegunId(id)
		if(envioCorreoFiscalizador):
			data = {
				"result":True,
				"envioCorreoFiscalizador":VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizador(envioCorreoFiscalizador).build(),
				"mensajes":"Se encontró envío de correo con id {}".format(id)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontró envío de correo con id {}".format(id)
			}

		return data;

	@staticmethod
	def obtenerSegunIdFiscalizador(idFiscalizador):
		print(colored("EnvioCorreoFiscalizadorService: obtenerSegunIdFiscalizador(); {}".format(idFiscalizador), 'cyan'))
		envioCorreosFiscalizadores = EnvioCorreoFiscalizadorDAO.obtenerSegunIdFiscalizador(idFiscalizador)
		if(envioCorreosFiscalizadores):
			data = {
				"result":True,
				"envioCorreosFiscalizadores":VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizadores(envioCorreosFiscalizadores).builds(),
				"mensajes":"Se encontraron denuncias con id de denunciado {}".format(idFiscalizador)
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron envíos de correo con id fiscalizador {}".format(idFiscalizador)
			}

		return data;

	@staticmethod
	def obtenerSegunIdDenuncia(idDenuncia):
		print(colored("EnvioCorreoFiscalizadorService: obtenerSegunIdDenuncia(); {}".format(idDenuncia), 'cyan'))
		envioCorreoFiscalizadores = EnvioCorreoFiscalizadorDAO.obtenerSegunIdDenuncia(idDenuncia)
		if len(envioCorreoFiscalizadores)>0:
			data = {
				"result":True,
				"envioCorreosFiscalizadores":VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizadores(envioCorreoFiscalizadores).builds(),
				"mensajes":"Se encontraron envíos de correo con id de denuncia {}".format(idDenuncia)
			}
		else:
			data = {
				"result":False,
				"errores": "No se encontraron envíos de correo con id de denuncia {}".format(idDenuncia)
			}

		return data;

	@staticmethod
	def actualizar(request):
		print(colored("DenunciaService: actualizar(); {}".format(request.get_json()), 'cyan'))

		id = request.get_json()["id"] if 'id' in request.get_json() else None
		idFiscalizador = request.get_json()["idFiscalizador"] if 'idFiscalizador' in request.get_json() else None
		idDenuncia = request.get_json()["idDenuncia"] if 'idDenuncia' in request.get_json() else None
		codigoEstadoEnvioCorreo = request.get_json()["codigoEstadoEnvioCorreo"] if 'codigoEstadoEnvioCorreo' in request.get_json() else 1
		fechaEnvio = request.get_json()["fechaEnvio"] if 'fechaEnvio' in request.get_json() else None

		fechaCreacion = request.get_json()["fechaCreacion"] if 'fechaCreacion' in request.get_json() else None
		fechaModificacion = request.get_json()["fechaModificacion"] if 'fechaModificacion' in request.get_json() else None
		flagActivo = request.get_json()["flagActivo"] if 'flagActivo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId del envío de correo"
		if(idFiscalizador==None):
			enviar = False
			mensajes +="\nFiscalizador"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nDenuncia"
		if(codigoEstadoEnvioCorreo==None):
			enviar = False
			mensajes +="\nCódigo de estado de envíó"
		if(fechaEnvio==None):
			enviar = False
			mensajes +="\nFecha de envíó"

		if(enviar):
			envioCorreoFiscalizadorVO = EnvioCorreoFiscalizadorVO()
			envioCorreoFiscalizadorVO.id = id
			envioCorreoFiscalizadorVO.idFiscalizador = idFiscalizador
			envioCorreoFiscalizadorVO.idDenuncia = idDenuncia
			envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo = codigoEstadoEnvioCorreo
			envioCorreoFiscalizadorVO.fechaEnvio = fechaEnvio
			envioCorreoFiscalizadorVO.fechaCreacion = fechaCreacion
			envioCorreoFiscalizadorVO.fechaModificacion = fechaModificacion
			envioCorreoFiscalizadorVO.flagActivo = flagActivo

			respuesta = EnvioCorreoFiscalizadorDAO.actualizar(envioCorreoFiscalizadorVO)
			if(respuesta["result"]):
				respuesta["envioCorreoFiscalizador"] = VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizador(respuesta["envioCorreoFiscalizador"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def actualizarEstado(request):
		print(colored("EnvioCorreoFiscalizadorService: actualizarEstado(); {}".format(request.get_json()), 'cyan'))

		id = request.get_json()["id"] if 'id' in request.get_json() else None
		codigoEstadoEnvioCorreo = request.get_json()["codigoEstadoEnvioCorreo"] if 'codigoEstadoEnvioCorreo' in request.get_json() else None

		enviar = True
		mensajes = "Faltó:"
		if(id==None):
			enviar = False
			mensajes +="\nId del envío de correo a actualizar"
		if(codigoEstadoEnvioCorreo==None):
			enviar = False
			mensajes +="\nCódigo de estado de la denuncia"
		if(enviar):
			envioCorreoFiscalizadorVO = EnvioCorreoFiscalizadorVO()
			envioCorreoFiscalizadorVO.id = id
			envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo = codigoEstadoEnvioCorreo
			respuesta = EnvioCorreoFiscalizadorDAO.actualizarEstado(envioCorreoFiscalizadorVO)
			if(respuesta["result"]):
				respuesta["envioCorreoFiscalizador"] = VOBuilderFactory().getEnvioCorreoFiscalizadorVOBuilder().fromEnvioCorreoFiscalizador(respuesta["envioCorreoFiscalizador"]).build()
			else:
				respuesta = {"result":False, "errores":respuesta["errores"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def enviarCorreoFiscalizadorDenuncia(idFiscalizador, idDenuncia):
		print(colored("EnvioCorreoFiscalizadorService: enviarCorreoFiscalizadorDenuncia(); idFiscalizador:{} idDenuncia: {}".format(idFiscalizador,idDenuncia), 'green'))

		enviar = True
		mensajes = "Faltó:"
		if(idFiscalizador==None):
			enviar = False
			mensajes +="\nId del fiscalizador"
		if(idDenuncia==None):
			enviar = False
			mensajes +="\nId de la denuncia"
		if(enviar):
			denuncia = DenunciaDAO.obtenerSegunId(idDenuncia)
			direccionDenunciada = DireccionDAO.obtenerSegunId(denuncia.denunciado.id_direccion)
			fiscalizador = FiscalizadorDAO.obtenerSegunId(idFiscalizador)
			respuestaEnviarCorreo = EnvioCorreoFiscalizadorService.construirCorreo(denuncia, direccionDenunciada, fiscalizador)
			# Guardar EnvioCorreoFiscalizador
			envioCorreoFiscalizadorVO = EnvioCorreoFiscalizadorVO()
			envioCorreoFiscalizadorVO.idDenuncia = idDenuncia
			envioCorreoFiscalizadorVO.idFiscalizador = idFiscalizador
			# TODO Crear ENUM
			envioCorreoFiscalizadorVO.codigoEstadoEnvioCorreo = 1 if respuestaEnviarCorreo['result'] is True else 2
			envioCorreoFiscalizadorVO.fechaEnvio = datetime.datetime.now()
			EnvioCorreoFiscalizadorDAO.guardar(envioCorreoFiscalizadorVO)
			# Actualizar estado de Denuncia
			denunciaVO = DenunciaVO()
			denunciaVO.id = denuncia.id_denuncia
			#TODO Crear ENUM
			denunciaVO.codigoEstadoDenuncia = 3
			DenunciaDAO.actualizarEstado(denunciaVO)
			return respuestaEnviarCorreo
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def construirCorreo(denuncia, direccion, fiscalizador):
		print(colored("EnvioCorreoFiscalizadorService: construirCorreo(); denuncia:{} fiscalizador: {}".format(denuncia,fiscalizador), 'green'))
		asunto = 'QuieroDenunciar - Denuncia N°{}'.format(denuncia.id_denuncia)
		print("Construyendo correo: {}".format(asunto))
		msg = Message(subject=asunto, sender=app.config['MAIL_USERNAME'], bcc=[app.config['EMAIL_COPIA']])
		#Agregar adjuntos
		for archivo in denuncia.archivos:
			if archivo.cod_tipo_archivo == 1:
				tipo = "image/{}".format(archivo.extension_archivo)
			elif archivo.cod_tipo_archivo == 2:
				tipo = "video/{}".format(archivo.extension_archivo)
			elif archivo.cod_tipo_archivo == 3:
				tipo = "doc/{}".format(archivo.extension_archivo)
			elif archivo.cod_tipo_archivo == 4:
				tipo = "doc/{}".format(archivo.extension_archivo)
			else:
				tipo = "doc/{}".format(archivo.extension_archivo)

			try:
				print("Intentando abrir archivo en ruta: {}".format(os.path.join("..",archivo.ruta_archivo,archivo.nombre_archivo)))
				with app.open_resource(os.path.join("..",archivo.ruta_archivo,archivo.nombre_archivo)) as fp:
					print(colored("Archivo en ruta: {} adjuntado correctamente".format(os.path.join("..", archivo.ruta_archivo, archivo.nombre_archivo)),"green"))
					msg.attach(archivo.nombre_archivo, tipo, fp.read())
			except:
				print(colored("Error al intentar abrir archivo en ruta: {}".format(os.path.join("..",archivo.ruta_archivo,archivo.nombre_archivo)),"red"))

		#Agregar destinatarios
		for correo in fiscalizador.correos:
			msg.add_recipient(correo.glosa)

		#msg.body = "Probando el envío de correo desde Flask"

		formatoDenuncia = ['# {} Denuncia N°{}'.format(denuncia.fecha_creacion.strftime("%d-%m-%Y"),denuncia.id_denuncia),
											 '* Número denuncia: {}'.format(denuncia.id_denuncia),
											 '* Fecha: {}'.format(denuncia.fecha_creacion.strftime("%d-%m-%Y"))]
		datosDenuncia = ''
		for dato in formatoDenuncia:
			datosDenuncia+="\n{}".format(dato)

		formatoDenunciante = ['## Denunciante', '* Nombre: {}'.format(denuncia.denunciante.persona.nombre + " " + denuncia.denunciante.persona.apellido_paterno if denuncia.denunciante is not None else 'Anónimo')]
		datosDenunciante = ''
		for dato in formatoDenunciante:
			datosDenunciante+="\n{}".format(dato)

		formatoDenunciado = ['## Denunciado', '* Nombre: {} {}'.format(denuncia.denunciado.persona.nombre, denuncia.denunciado.persona.apellido_paterno if denuncia.denunciado.persona.apellido_paterno is not None else "")]
		datosDenunciado = ''
		for dato in formatoDenunciado:
			datosDenunciado+="\n{}".format(dato)

		formatoDireccionDeLosHechos = ['## Dirección de los hechos denunciados', '* Comuna: {}'.format(direccion.comuna.comuna), '* Calle: {} {}'.format(direccion.calle, direccion.numero), '* Tipo dirección: {}'.format(direccion.tipoDireccion.glosa)]
		datosDireccionDeLosHechos = ''
		for dato in formatoDireccionDeLosHechos:
			datosDireccionDeLosHechos+="\n{}".format(dato)

		datosDenunciaMaterias = '\n'
		datosDenunciaMaterias+='## Hechos denunciados'
		datosDenunciaMaterias+='\n'
		datosDenunciaMaterias+='### Materias relacionadas'
		datosDenunciaMaterias+='\n'

		for denunciaMateria in denuncia.denunciasMaterias:
			datosDenunciaMaterias+="* {}\n".format(denunciaMateria.materia.glosa)

		datosDescripcionDenuncia='\n'
		datosDescripcionDenuncia+='## Descripción de los hechos denunciados'
		datosDescripcionDenuncia+='\n*{}*'.format(denuncia.descripcion)

		datosArchivos='\n\n\n\n'
		if len(denuncia.archivos)>0:
			datosArchivos+='**Atención: El denunciante provee documentación que respalda su denuncia, por lo que se solicita revisar los archivos adjuntos en este correo.**'

		cuerpoMarkdown = '{} {} {} {} {} {} {}'.format(datosDenuncia, datosDenunciante, datosDenunciado, datosDireccionDeLosHechos, datosDenunciaMaterias, datosDescripcionDenuncia, datosArchivos)

		#Crear documento en PDF
		DocumentoUtils.crearDocumentoPDFConMarkdown(app, cuerpoMarkdown, denuncia)

		#print(cuerpoMarkdown)
		cuerpoMarkdownHTML = markdown.markdown(cuerpoMarkdown)
		#print(cuerpoMarkdownHTML)
		msg.html = cuerpoMarkdownHTML

		#Enviar
		print("Enviando correo de idDenuncia:{} a idFiscalizador:{}".format(denuncia.id_denuncia, fiscalizador.id_fiscalizador))
		#TODO Se desactiva envío
		#mail.send(msg)
		return {"result": True, "mensajes": "Correo enviado correctamente"}

	@staticmethod
	def eliminar(id):
		print(colored("EnvioCorreoFiscalizadorService: eliminar(); {}".format(id), 'cyan'))
		respuesta = EnvioCorreoFiscalizadorDAO.eliminar(id)
		return respuesta
1