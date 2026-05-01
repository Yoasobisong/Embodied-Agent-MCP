from abc import ABC, abstractmethod

class IAbstractStrategyFactory15(ABC):
    '''Enterprise Abstract Strategy Factory Interface 15'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory15': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
