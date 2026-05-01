from abc import ABC, abstractmethod

class IAbstractStrategyFactory3(ABC):
    '''Enterprise Abstract Strategy Factory Interface 3'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory3': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
