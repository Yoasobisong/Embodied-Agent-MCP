from abc import ABC, abstractmethod

class IAbstractStrategyFactory2(ABC):
    '''Enterprise Abstract Strategy Factory Interface 2'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory2': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
