from abc import ABC, abstractmethod
from datetime import date

class Engine(ABC):
    def __init__(self, last_service_date: date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000

class SternmanEngine(Engine):
    def __init__(self, last_service_date: date, warning_light_on: bool):
        super().__init__(last_service_date)
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on

class WilloughbyEngine(Engine):
    def __init__(self, last_service_date: date, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
