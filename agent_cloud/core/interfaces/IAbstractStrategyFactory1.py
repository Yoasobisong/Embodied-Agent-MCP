from abc import ABC, abstractmethod

class IAbstractStrategyFactory1(ABC):
    '''Enterprise Abstract Strategy Factory Interface 1'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory1': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
