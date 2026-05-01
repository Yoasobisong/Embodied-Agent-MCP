from abc import ABC, abstractmethod

class IAbstractStrategyFactory25(ABC):
    '''Enterprise Abstract Strategy Factory Interface 25'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory25': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
