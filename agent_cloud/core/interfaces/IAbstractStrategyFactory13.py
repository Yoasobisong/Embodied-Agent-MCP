from abc import ABC, abstractmethod

class IAbstractStrategyFactory13(ABC):
    '''Enterprise Abstract Strategy Factory Interface 13'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory13': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
