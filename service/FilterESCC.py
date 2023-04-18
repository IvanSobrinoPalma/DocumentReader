from interface.IFilter import IFilter
import re

class FilterESCC(IFilter):
    def filter_info(paragraphs, certificates, revision_re, manufacture_re):
        pass


    def get_certificate(paragraphs, title_re :re, certificate_re :re):
        result = {}
        for paragraph in paragraphs:
            if (len(title_re.findall(paragraph)) > 0):
                title = title_re.findall(paragraph)[0]
                result[title] = []
                result[title] = certificate_re.findall(paragraph)
        return result
    

    def get_description(paragraphs, certificates, dictionary = None):
        result = {}
        certificate_re = re.compile(r'\d{2,3}[A-Z](?:[rev]{3}\d)?(?=, )')
        for paragraph in paragraphs:
            current_certificate = None
            for line in paragraph.split("\n"):
                for title in certificates:
                    for certificate in certificates[title]:
                        if line.startswith(certificate):
                            current_certificate = certificate
                            result[current_certificate] = ""
                        elif line.find(certificate) > 0:
                            print("--"+line)
                if(not certificate_re.match(line) and current_certificate):
                    result[current_certificate] += line
        print(result)