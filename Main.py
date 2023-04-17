import re
from service.OpenPDF import OpenPDF
from service.Paragraph import Paragraph
from service.ReadPdfTable import ReadPDFTable

file_name = "files\DSCCFile.pdf"
file_esa = "files\esccrpqpl005iss235.pdf"

file_read = OpenPDF.open(file_esa)

content = ReadPDFTable.read_file(file_read, 3)

TITLE = re.compile(r'^[a-zA-Z\s]+:')
CERTIFICATE = re.compile(r'\d{2,3}[a-zA-Z](?:[rev]{3}\d?)?+,')
CORREO = re.compile(r'Document:\s*')

for line in Paragraph.get_paragraphs(content, TITLE):
    print(line)
    print("================================================================")
