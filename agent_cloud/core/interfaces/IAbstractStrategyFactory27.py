from abc import ABC, abstractmethod

class IAbstractStrategyFactory27(ABC):
    '''Enterprise Abstract Strategy Factory Interface 27'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory27': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
