import re
from interface.IParagraph import IParagraph

class Paragraph(IParagraph):
    def get_paragraphs(content, start_regex :re, end_regex :re = None, paragraph_title :re = None):
        end_regex = start_regex if end_regex is None else end_regex
        paragraphs = []
        paragraph = ""
        current_title = ""
        content_list = content.split("\n")
        for i, line in enumerate(content_list):
            if(end_regex.match(line) and line != current_title and current_title != ""):
                paragraphs.append(paragraph)
                paragraph = ""
                current_title = line
            if(start_regex.match(line)):
                paragraph += line + " \n"
                current_title = line
            if(current_title and not start_regex.match(line)):
                paragraph += line + " \n"
            if(i == len(content_list)-1):
                paragraphs.append(paragraph)

        return paragraphs