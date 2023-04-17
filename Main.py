import re
from service.OpenPDF import OpenPDF
from service.Paragraph import Paragraph
from service.ReadPdfTable import ReadPDFTable
from service.ReadPdfText import ReadPDFText
from service.Filter import Filter




file_name = "./files/DSCCFile.pdf"
file_name_2 = "./files/esccrpqpl005iss235.pdf"

file_read = OpenPDF.open(file_name_2)

content = ReadPDFTable.read_file(file_read, 3)

dictionary = {"Title": re.compile(r'[A-Z][a-zA-Z -]+(?=:\s*)'), 
              "Certificate": re.compile(r'\d{2,3}[A-Z](?:[rev]{3}\d)?(?=, )'), 
              "Manufacturer": re.compile(r'[^ ,][a-zA-Z!@#$&()\\-`+\’ ]+\([a-zA-Z]+\)')}
dictionary_2 = {"Document": re.compile(r'Document:\s*[a-zA-Z0-9!@#$&()\\-`+\/’, -]+'), 
              "Description": re.compile(r'Description:\s*[a-zA-Z0-9!@#$&()\\-`+\/’, -]+')}

CERTIFICATE = re.compile(r'[A-Z][a-zA-Z -]+:\s*')
CORREO = re.compile(r'Document:\s*')

paragraphs = Paragraph.get_paragraphs(content, CERTIFICATE)

for line in Filter.filter_info(paragraphs, dictionary):
    print(line)
