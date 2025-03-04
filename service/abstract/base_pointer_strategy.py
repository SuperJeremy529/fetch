from abc import ABC, abstractmethod
from dto.receipts import RecepientDTO

class BasePointerStrategy(ABC):
    @abstractmethod
    def calculate(self, recepient_dto: RecepientDTO):
        ...

    def execute(self, recepient_dto: RecepientDTO):
        return self.calculate(recepient_dto=recepient_dto)

