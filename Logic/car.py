from battery import Battery , SpindlerBattery , NubbinBattery
from engine import Engine , CapuletEngine , WilloughbyEngine , SternmanEngine

class Car : 
    def __init__(self , battery:Battery , engine:Engine ): 
        self.battery = battery 
        self.engine = engine 

    def needs_service(self): 
        return self.battery.needs_service or self.engine.needs_service
    

class factory : 
    def __init__(self) -> None:
        pass

    def create_calliope()-> Car:
        return Car()

    def create_calliope()-> Car:
        return Car()
    
    def create_calliope()-> Car:
        return Car()
    

    def create_calliope()-> Car:
        return Car()

    
    def create_calliope()-> Car:
        return Car()
    