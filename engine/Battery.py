from abc import ABC, abstractmethod
from datetime import date

class Battery(ABC):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date.year - self.last_service_date.year) >= 2

class NubbinBattery(Battery):
    def needs_service(self) -> bool:
        return (self.current_date.year - self.last_service_date.year) >= 4
