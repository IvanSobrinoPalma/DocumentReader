from abc import ABC, abstractmethod

class IParagraph(ABC):
    @abstractmethod
    def get_paragraphs():
        pass