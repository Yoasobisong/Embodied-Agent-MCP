from abc import ABC, abstractmethod

class IAbstractStrategyFactory31(ABC):
    '''Enterprise Abstract Strategy Factory Interface 31'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory31': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
