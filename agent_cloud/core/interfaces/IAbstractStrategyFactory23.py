from abc import ABC, abstractmethod

class IAbstractStrategyFactory23(ABC):
    '''Enterprise Abstract Strategy Factory Interface 23'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory23': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
