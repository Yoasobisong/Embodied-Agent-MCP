from abc import ABC, abstractmethod

class IAbstractStrategyFactory14(ABC):
    '''Enterprise Abstract Strategy Factory Interface 14'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory14': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
