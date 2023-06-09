import re
from service.OpenPDF import OpenPDF
from service.Paragraph import Paragraph
from service.ReadPdfTable import ReadPDFTable
from service.ReadPdfText import ReadPDFText
from service.Filter import Filter
from service.FilterDSCC import FilterDSCC
from service.FilterESCC import FilterESCC




file_name = "./files/DSCCFile.pdf"
file_name_2 = "./files/esccrpqpl005iss235.pdf"
file_name_3 = "./files/esccrpqpl005iss234_jan_23.pdf"

file_read = OpenPDF.open(file_name_2)

content = ReadPDFTable.read_file(file_read, 3)

dictionary = {"Title": re.compile(r'[A-Z][a-zA-Z -]+(?=:\s?\n)'), 
              "Certificate": re.compile(r'\d{2,3}[A-Z](?:[rev]{3}\d)?(?=, )'),
              "Revesion": re.compile(r'rev\d{1}'),
              "Manufacturer": re.compile(r'[^ ,][a-zA-Z!@#$&()\\-`+\’ ]+\([a-zA-Z]+\)')}

dictionary_2 = {"Document": re.compile(r'^Document:\s*[a-zA-Z0-9!@#$&()\\-`+\/’, -]+'), 
              "Description": re.compile(r'^Description:\s*[a-zA-Z0-9!@#$&()\\-`+\/’, -]+'),
              "URL": re.compile(r'^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\/Downloads\/[a-zA-Z0-9-.? \/]+'),
              "File Size": re.compile(r'^File size: [0-9 ]+ [kmghe]b'),
              "More Info": re.compile(r'^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\/Programs\/[a-zA-Z0-9-.? \/]+')}
titles = ["Document", "Description","URL","File size", "More Info"]

CERTIFICATE = re.compile(r'[A-Z][a-zA-Z -]+:\s*')
CORREO = re.compile(r'Document:\s*')

paragraphs = Paragraph.get_paragraphs(content, CERTIFICATE)

certificates = FilterESCC.get_certificate(paragraphs, dictionary["Title"], dictionary["Certificate"] )
description = FilterESCC.get_description(paragraphs, certificates)
#print(description)
    # for line in paragraph:
    #     print(line + ": ")
    #     print(paragraph[line])

