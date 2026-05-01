from abc import ABC, abstractmethod

class IAbstractStrategyFactory37(ABC):
    '''Enterprise Abstract Strategy Factory Interface 37'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory37': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
