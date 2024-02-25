import os
from termcolor import colored
import uuid
from markdown_pdf import MarkdownPdf, Section

class DocumentoUtils:

	@staticmethod
	def crearDocumentoPDFConMarkdown(app, cuerpoMarkdown, denuncia, temporal=False):
		print('DocumentoUtils: crearGuardarDocumentoPDFConMarkdown()')
		pdf = MarkdownPdf(toc_level=2)
		pdf.add_section(Section(cuerpoMarkdown))
		if len(denuncia.archivos)>0:
			archivos = ""
			for archivo in denuncia.archivos:
				rutaArchivo = os.path.join(archivo.ruta_archivo, archivo.nombre_archivo)
				#Verificar que existe el archivo y que el tipo sea Imagen ó 1
				if os.path.isfile(rutaArchivo) & archivo.cod_tipo_archivo is 1:
					print("DocumentoUtils: Archivo encontrado en ruta: {}".format(rutaArchivo))
					archivos+='![Archivo: {}]({})\n'.format(archivo.nombre_archivo,rutaArchivo)
					archivos+='*{}*\n'.format(archivo.descripcion)
				else:
					print("DocumentoUtils: Archivo no encontrado en ruta: {}".format(rutaArchivo))
		pdf.add_section(Section("## Archivos\n{}".format(archivos)))
		rutaDocumento = os.path.join(app.config['CARPETA_DOCUMENTOS'], DocumentoUtils.crearNombre(denuncia) if not temporal else "temporal.pdf")
		pdf.save(rutaDocumento)
		return rutaDocumento

	@staticmethod
	def crearNombre(denuncia):
		print("DocumentoUtils: Crear nombre para documento de denuncia: {}".format(denuncia.id_denuncia))
		return '{}-Denuncia-{}.pdf'.format(denuncia.fecha_creacion.strftime("%Y-%m-%d"),denuncia.id_denuncia)
