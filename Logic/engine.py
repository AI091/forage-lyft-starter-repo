from abc import ABC, abstractmethod


class Engine() : 
    @abstractmethod 
    def needs_service(self): 
        pass 

class CapuletEngine(Engine): 
    def __init__(self,last_service_mileage: int , current_milage: int ) -> None:
        self.last_service_mileage= last_service_mileage
        self.current_milage=current_milage
    
    def needs_service(self): 
        return self.current_milage-self.last_service_mileage >= 3e4 

class WilloughbyEngine(Engine): 
    def __init__(self,last_service_mileage: int , current_milage: int ) -> None:
        self.last_service_mileage= last_service_mileage
        self.current_milage=current_milage
    
    def needs_service(self): 
        return self.current_milage-self.last_service_mileage >= 6e4


class SternmanEngine(Engine): 
    def __init__(self,warning_indicator:bool ) -> None:
        self.warning_indicator=warning_indicator
    
    def needs_service(self): 
        return self.warning_indicator


class EngineFactory(): 

    def create_capulet(last_service_mileage: int ,current_milage: int ): 
        return CapuletEngine(last_service_mileage ,current_milage )

    def create_willough(last_service_mileage: int ,current_milage: int):
        return CapuletEngine(last_service_mileage ,current_milage )
    
    def create_sternman(warning_indicator:bool ): 
        return SternmanEngine(warning_indicator )









