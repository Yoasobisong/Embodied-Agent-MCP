from abc import ABC, abstractmethod

class IAbstractStrategyFactory11(ABC):
    '''Enterprise Abstract Strategy Factory Interface 11'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory11': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
