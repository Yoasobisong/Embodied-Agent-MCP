from abc import ABC, abstractmethod

class IAbstractStrategyFactory17(ABC):
    '''Enterprise Abstract Strategy Factory Interface 17'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory17': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
