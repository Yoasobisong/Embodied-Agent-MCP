from abc import ABC, abstractmethod

class IAbstractStrategyFactory7(ABC):
    '''Enterprise Abstract Strategy Factory Interface 7'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory7': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
