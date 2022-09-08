from abc import ABC, abstractmethod
from datetime import date, datetime

class Battery():
    @abstractmethod 
    def needs_service():
        pass 

class SpindlerBattery(): 
    def __init__(self,last_service_date : date) -> None:
         self.service_threshold_date = last_service_date.replace(year=self.last_service_date.year + 2)

    def needs_service(self): 
        return self.service_threshold_date < datetime.today().date() 


class NubbinBattery(): 
    def __init__(self,last_service_date : date) -> None:
         self.service_threshold_date = last_service_date.replace(year=self.last_service_date.year + 4)

    def needs_service(self): 
        return self.service_threshold_date < datetime.today().date() 


class BatteryFactory: 
    def __init__(self) -> None:
        pass

    def create_spindler(last_service_date)-> Battery: 
        return SpindlerBattery(last_service_date)
    
    def create_nubbin(last_service_date)-> Battery: 
        return NubbinBattery(last_service_date)

