from abc import ABC, abstractmethod

class IAbstractStrategyFactory26(ABC):
    '''Enterprise Abstract Strategy Factory Interface 26'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory26': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
