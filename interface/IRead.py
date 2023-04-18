from abc import ABC, abstractmethod
class IRead(ABC):
    @abstractmethod
    def read_file(name, page, col, row):
        pass