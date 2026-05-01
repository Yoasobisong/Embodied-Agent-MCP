from abc import ABC, abstractmethod

class IAbstractStrategyFactory21(ABC):
    '''Enterprise Abstract Strategy Factory Interface 21'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory21': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
