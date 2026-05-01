from abc import ABC, abstractmethod

class IAbstractStrategyFactory20(ABC):
    '''Enterprise Abstract Strategy Factory Interface 20'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory20': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
