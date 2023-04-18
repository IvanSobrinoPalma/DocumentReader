from interface.IFilter import IFilter

class FilterDSCC(IFilter):
    def filter_info(paragraphs, dictionary):
        final_result = []
        for paragraph in paragraphs:
            result = {}
            data = ""
            for line in paragraph.split("\n"):
                match_regex = False
                for key in dictionary:
                    current_regex = None
                    if len(dictionary[key].findall(line)) > 0:
                        match_regex = True 
                        current_regex = dictionary[key]
                        data = dictionary[key].findall(line)[0]
                        if key in result:
                            final_result.append(result)
                            result = {}
                        result[key] = data
                            
                if match_regex == False:
                    data += line
                    result[key] = data

            final_result.append(result)
        return final_result