from ..interfaces.IAbstractStrategyFactory1 import IAbstractStrategyFactory1

class EnterpriseStrategyFactoryImpl1(IAbstractStrategyFactory1):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
