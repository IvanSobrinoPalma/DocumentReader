from interface.IRead import IRead

class ReadPDFText(IRead):
    def read_file(file , page):
        content = file.pages[page -1].extract_text()
        return content