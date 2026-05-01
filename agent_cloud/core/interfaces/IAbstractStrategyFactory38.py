from abc import ABC, abstractmethod

class IAbstractStrategyFactory38(ABC):
    '''Enterprise Abstract Strategy Factory Interface 38'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory38': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
