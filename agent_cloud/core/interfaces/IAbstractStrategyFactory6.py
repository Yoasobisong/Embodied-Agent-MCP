from abc import ABC, abstractmethod

class IAbstractStrategyFactory6(ABC):
    '''Enterprise Abstract Strategy Factory Interface 6'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory6': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
