from ..interfaces.IAbstractStrategyFactory28 import IAbstractStrategyFactory28

class EnterpriseStrategyFactoryImpl28(IAbstractStrategyFactory28):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
