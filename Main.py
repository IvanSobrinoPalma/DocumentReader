import re
from service.OpenPDF import OpenPDF
from service.Paragraph import Paragraph
from service.ReadPdfTable import ReadPDFTable
from service.Filter import Filter




file_name = "./files/esccrpqpl005iss235.pdf"

file_read = OpenPDF.open(file_name)

content = ReadPDFTable.read_file(file_read, 3)

dictionary = {"Title": re.compile(r'[A-Z][a-zA-Z -]+:\s*'), "Certificate": re.compile(r'\d{2,3}[A-Z](?:[rev]{3}\d)?')}

CERTIFICATE = re.compile(r'[A-Z][a-zA-Z -]+:\s*')
CORREO = re.compile(r'Document:\s*')

paragraphs = Paragraph.get_paragraphs(content, CERTIFICATE)

Filter.filter_info(Paragraph.get_paragraphs(content, CERTIFICATE), dictionary)
