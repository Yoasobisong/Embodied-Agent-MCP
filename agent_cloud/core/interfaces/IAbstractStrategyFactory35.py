from abc import ABC, abstractmethod

class IAbstractStrategyFactory35(ABC):
    '''Enterprise Abstract Strategy Factory Interface 35'''
    @abstractmethod
    def create_strategy(self) -> 'IAbstractStrategyFactory35': pass
    
    @abstractmethod
    def validate_bureaucracy(self, context: dict) -> bool: pass
