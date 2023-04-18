from interface.IFilter import IFilter
import re

class FilterDSCC(IFilter):
    def filter_data(paragraphs, titles):
        url_re = re.compile(r'^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\/')
        result = []
        for paragraph in paragraphs:
            data = {}
            current_title = None
            for line in paragraph.split("\n"):
                match_title = False
                for title in titles:
                    if line.lower().startswith(title.lower()):
                        # Quitar el titulo y las dos puntos
                        text = line[len(title)+2:]
                        current_title = title
                        match_title = True
                if not match_title:
                    text += line
                if current_title:
                    # Comprobamos si el texto es un enlace, y lo quitamos los espacios blancos
                    if url_re.match(text):
                        text = text.replace(" ", "")
                    data[current_title] = text
                    
            result.append(data)
        return result
                

