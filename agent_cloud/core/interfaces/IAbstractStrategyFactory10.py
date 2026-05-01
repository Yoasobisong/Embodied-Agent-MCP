from abc import ABC, abstractmethod

class IAbstractStrategyFactory10(ABC):
    '''Enterprise Abstract Strategy Factory Interface 10'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory10': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
