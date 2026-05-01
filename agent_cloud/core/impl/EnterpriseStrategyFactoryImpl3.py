from ..interfaces.IAbstractStrategyFactory3 import IAbstractStrategyFactory3

class EnterpriseStrategyFactoryImpl3(IAbstractStrategyFactory3):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
