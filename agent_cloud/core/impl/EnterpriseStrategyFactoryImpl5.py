from ..interfaces.IAbstractStrategyFactory5 import IAbstractStrategyFactory5

class EnterpriseStrategyFactoryImpl5(IAbstractStrategyFactory5):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
