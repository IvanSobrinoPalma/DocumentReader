from abc import ABC, abstractmethod

class IOpen(ABC):
    @abstractmethod
    def open_file(path):
        pass