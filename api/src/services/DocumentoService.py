import os
import markdown
from termcolor import colored
from flask import send_from_directory

from src.app import app
from src.daos.DenunciaDAO import DenunciaDAO
from src.daos.DireccionDAO import DireccionDAO
from src.utils.DocumentoUtils import DocumentoUtils

class DocumentoService():

	#def __init__(self):
		#print('DocumentoService')

	@staticmethod
	def generarConDenuncia(denuncia):
		direccion = DireccionDAO.obtenerSegunId(denuncia.denunciado.id_direccion)

		formatoDenuncia = [
			'# {} Denuncia N°{}'.format(denuncia.fecha_creacion.strftime("%d-%m-%Y"), denuncia.id_denuncia),
			'* Número denuncia: {}'.format(denuncia.id_denuncia),
			'* Fecha: {}'.format(denuncia.fecha_creacion.strftime("%d-%m-%Y"))]
		datosDenuncia = ''
		for dato in formatoDenuncia:
			datosDenuncia += "\n{}".format(dato)

		formatoDenunciante = ['## Denunciante', '* Nombre: {}'.format(
			denuncia.denunciante.persona.nombre + " " + denuncia.denunciante.persona.apellido_paterno if denuncia.denunciante is not None else 'Anónimo')]
		datosDenunciante = ''
		for dato in formatoDenunciante:
			datosDenunciante += "\n{}".format(dato)

		formatoDenunciado = ['## Denunciado', '* Nombre: {} {}'.format(denuncia.denunciado.persona.nombre,
																																	 denuncia.denunciado.persona.apellido_paterno if denuncia.denunciado.persona.apellido_paterno is not None else "")]
		datosDenunciado = ''
		for dato in formatoDenunciado:
			datosDenunciado += "\n{}".format(dato)

		formatoDireccionDeLosHechos = ['## Dirección de los hechos denunciados',
																	 '* Comuna: {}'.format(direccion.comuna.comuna),
																	 '* Calle: {} {}'.format(direccion.calle, direccion.numero),
																	 '* Tipo dirección: {}'.format(direccion.tipoDireccion.glosa)]
		datosDireccionDeLosHechos = ''
		for dato in formatoDireccionDeLosHechos:
			datosDireccionDeLosHechos += "\n{}".format(dato)

		datosDenunciaMaterias = '\n'
		datosDenunciaMaterias += '## Hechos denunciados'
		datosDenunciaMaterias += '\n'
		datosDenunciaMaterias += '### Materias relacionadas'
		datosDenunciaMaterias += '\n'

		for denunciaMateria in denuncia.denunciasMaterias:
			datosDenunciaMaterias += "* {}\n".format(denunciaMateria.materia.glosa)

		datosDescripcionDenuncia = '\n'
		datosDescripcionDenuncia += '## Descripción de los hechos denunciados'
		datosDescripcionDenuncia += '\n*{}*'.format(denuncia.descripcion)

		datosArchivos = '\n\n\n\n'
		if len(denuncia.archivos) > 0:
			datosArchivos += '**Atención: El denunciante provee documentación que respalda su denuncia, por lo que se solicita revisar los archivos adjuntos en este correo.**'

		cuerpoMarkdown = '{} {} {} {} {} {} {}'.format(datosDenuncia, datosDenunciante, datosDenunciado,
																									 datosDireccionDeLosHechos, datosDenunciaMaterias,
																									 datosDescripcionDenuncia, datosArchivos)

		print(cuerpoMarkdown)
		return cuerpoMarkdown

	@staticmethod
	def generarSegunIdDenuncia(idDenuncia):
		print(colored("DocumentoService: generarSegunIdDenuncia(); {}".format(idDenuncia), 'cyan'))
		denuncia = DenunciaDAO.obtenerSegunId(idDenuncia)

		cuerpoMarkdown = DocumentoService.generarConDenuncia(denuncia)

		carpetaRelativa = os.path.join("..", app.config['CARPETA_DOCUMENTOS'])
		rutaCompletaPDF = DocumentoUtils.crearDocumentoPDFConMarkdown(app, cuerpoMarkdown, denuncia, True)
		#print(rutaCompletaPDF)
		partes = os.path.split(rutaCompletaPDF)
		#print(partes)
		#print(partes[1])
		print("Mostrando documento tempora ubicado en: {}".format(rutaCompletaPDF))
		return send_from_directory(carpetaRelativa, partes[1], as_attachment=True)

