from abc import ABC, abstractmethod

class IAbstractStrategyFactory36(ABC):
    '''Enterprise Abstract Strategy Factory Interface 36'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory36': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
