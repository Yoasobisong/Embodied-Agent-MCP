from abc import ABC, abstractmethod

class IAbstractStrategyFactory28(ABC):
    '''Enterprise Abstract Strategy Factory Interface 28'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory28': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
