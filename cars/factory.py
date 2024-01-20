from datetime import date
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
# Capulet Engine	Once every 30,000 miles
# Willoughby Engine	Once every 60,000 miles
# Sternman Engine	Only when the warning indicator is on

# Spindler Battery	Once every 2 years
# Nubbin Battery	Once every 4 years
# ----------------
# Car	Engine	Battery
# Calliope	Capulet Engine	Spindler Battery

# Glissade	Willoughby Engine	Spindler Battery

# Palindrome	Sternman Engine	Spindler Battery

# Rorschach	Willoughby Engine	Nubbin Batte

# Thovex	Capulet Engine	Nubbin Battery