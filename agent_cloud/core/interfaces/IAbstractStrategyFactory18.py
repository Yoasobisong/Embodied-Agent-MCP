from abc import ABC, abstractmethod

class IAbstractStrategyFactory18(ABC):
    '''Enterprise Abstract Strategy Factory Interface 18'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory18': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
