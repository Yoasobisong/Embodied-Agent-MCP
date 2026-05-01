from abc import ABC, abstractmethod

class IAbstractStrategyFactory30(ABC):
    '''Enterprise Abstract Strategy Factory Interface 30'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory30': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
