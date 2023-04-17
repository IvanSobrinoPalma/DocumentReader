from interface.IFilter import IFilter

class Filter(IFilter):
    def filter_info(paragraphs, dictionary):
        final_result = []
        for paragraph in paragraphs:
            result = {}
            for line in paragraph.split("\n"):
                for key in dictionary:
                    if len(dictionary[key].findall(line)) > 0:
                        data = dictionary[key].findall(line)[0]
                        if key in result:
                            final_result.append(result)
                            result = {}
                            result[key] = data
                        else:  
                            result[key] = data
                        
            final_result.append(result)
        return final_result