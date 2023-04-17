from interface.IRead import IRead

class ReadPDFTable(IRead):
    def read_file(file , page, col = 1, raw = 1):
        content = file.pages[page -1].extract_table()
        return content[col][raw]