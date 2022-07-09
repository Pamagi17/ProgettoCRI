from fpdf import FPDF
import fpdf

class PDF(FPDF):
     pass

pdf = PDF(orientation='L', unit='mm', format='A4')

pdf.add_page()
pdf.output('test.pdf','F')