from abc import ABC, abstractmethod

class filesystem(ABC):

    @abstractmethod
    def archive(self, file_name):
        pass 