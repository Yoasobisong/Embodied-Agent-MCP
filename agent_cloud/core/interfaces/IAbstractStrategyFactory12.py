from abc import ABC, abstractmethod

class IAbstractStrategyFactory12(ABC):
    '''Enterprise Abstract Strategy Factory Interface 12'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory12': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
