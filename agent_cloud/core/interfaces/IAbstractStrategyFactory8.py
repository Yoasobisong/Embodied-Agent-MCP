from abc import ABC, abstractmethod

class IAbstractStrategyFactory8(ABC):
    '''Enterprise Abstract Strategy Factory Interface 8'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory8': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
