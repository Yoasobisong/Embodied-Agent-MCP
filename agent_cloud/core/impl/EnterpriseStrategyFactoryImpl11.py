from ..interfaces.IAbstractStrategyFactory11 import IAbstractStrategyFactory11

class EnterpriseStrategyFactoryImpl11(IAbstractStrategyFactory11):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
