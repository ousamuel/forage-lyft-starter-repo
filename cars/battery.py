from serviceable import Serviceable
from datetime import date

class Battery(Serviceable):
    def __init__(self, last_service_date: date, current_date: date, service_interval_days: int):
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_interval_days = service_interval_days

    def needs_service(self) -> bool:
        difference = self.current_date - self.last_service_date
        return difference.days > self.service_interval_days

    def set_service_interval(self, new_interval_days: int):
        self.service_interval_days = new_interval_days

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date, current_date, 365 * 3)

class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        super().__init__(last_service_date, current_date, 365 * 4)
