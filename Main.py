from abc import ABC, abstractmethod
import pdfplumber
import re


class IOpen(ABC):
    @abstractmethod
    def open_file(path):
        pass

class IRead(ABC):
    @abstractmethod
    def read_file(name, page):
        pass

class IParagraph(ABC):
    @abstractmethod
    def get_paragraphs():
        pass



class OpenPDF(IOpen):
    def open(path):
        file = pdfplumber.open(path)
        return file

class ReadPDF(IRead):
    def read_file(file , page):
        content = file.pages[page -1].extract_text()
        return content

class Paragraph(IParagraph):
    def get_paragraphs(content, start_regex :re, end_regex :re):
        paragraphs = []
        paragraph = ""
        current_title = ""
        for line in content.split("\n"):
            if(end_regex.match(line) and line != current_title and current_title != ""):
                paragraphs.append(paragraph)
                paragraph = ""
                current_title = line
            if(start_regex.match(line)):
                paragraph += line + "\n"
                current_title = line
        return paragraphs

file_name = "files/esccrpqpl005iss235.pdf"


file_read = OpenPDF.open(file_name)

content = ReadPDF.read_file(file_read, 3)

paragraphs = Paragraph.get_paragraphs(content, re.compile(r'[A-Z][a-zA-Z -]+:\s*$'), re.compile(r'[A-Z][a-zA-Z -]+:\s*$'))

print(paragraphs)