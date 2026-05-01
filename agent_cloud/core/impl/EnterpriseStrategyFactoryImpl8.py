from ..interfaces.IAbstractStrategyFactory8 import IAbstractStrategyFactory8

class EnterpriseStrategyFactoryImpl8(IAbstractStrategyFactory8):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
