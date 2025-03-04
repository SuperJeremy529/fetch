from abc import ABC, abstractmethod



class BaseRepository(ABC):
    @abstractmethod
    def create(self): ...

    @abstractmethod
    def get(self): ...

    