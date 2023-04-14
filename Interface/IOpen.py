from abc import ABC, abstractclassmethod

class IOpen(ABC):
    @abstractclassmethod
    def open_file(path):
        return path
