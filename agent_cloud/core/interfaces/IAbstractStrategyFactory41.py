from abc import ABC, abstractmethod

class IAbstractStrategyFactory41(ABC):
    '''Enterprise Abstract Strategy Factory Interface 41'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory41': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
