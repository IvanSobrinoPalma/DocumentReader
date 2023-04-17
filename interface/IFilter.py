from abc import ABC, abstractmethod

class IFilter(ABC):
    @abstractmethod
    def get_filter_info(paragraphs, diccionary):
        pass
