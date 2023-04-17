from interface.IFilter import IFilter

class Filter(IFilter):
    def filter_info(paragraphs, dictionary):
        for paragraph in paragraphs:
            for line in paragraph.split("\n"):
                for key in dictionary:
                    key = dictionary[key].findall(line)
                    print(key)
        return dictionary