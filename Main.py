from abc import ABC, abstractmethod
import pdfplumber


class IOpen(ABC):
    @abstractmethod
    def open_file(path):
        return path

class IRead(ABC):
    @abstractmethod
    def read_file(name, page):
        pass


class OpenPDF(IOpen):
    def open(path):
        file = pdfplumber.open(path)
        return file

class ReadPdf(IRead):
    def read_file(file , page):
        content = file.pages[page -1].extract_text()
        return content




file_name = "./files/esccrpqpl005iss235.pdf"


file_read = OpenPDF.open(file_name)

print(ReadPdf.read_file(file_read, 3))