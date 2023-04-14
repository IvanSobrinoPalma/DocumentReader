import pdfplumber
import IOpen

class OpenPDF(IOpen):
    def open(path):
        file = pdfplumber.open(path)
        return file
