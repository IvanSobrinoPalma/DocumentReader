from interface.IFilter import IFilter

class Filter(IFilter):
    def filter_info(paragraphs, dictionary):
        result = {}
        final_result = []
        for paragraph in paragraphs:
            result = {}
            for line in paragraph.split("\n"):
                for key in dictionary:
                    data = dictionary[key].findall(line)
                    if(len(data) > 0):
                        result[key] = data
            final_result.append(result)
        print(final_result)
        return final_result