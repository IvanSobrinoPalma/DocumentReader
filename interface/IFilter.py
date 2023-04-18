from abc import ABC, abstractmethod

class IFilter(ABC):
    @abstractmethod
    def filter_info(paragraphs, diccionary):
        pass
