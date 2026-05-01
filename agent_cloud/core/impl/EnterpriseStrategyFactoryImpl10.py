from ..interfaces.IAbstractStrategyFactory10 import IAbstractStrategyFactory10

class EnterpriseStrategyFactoryImpl10(IAbstractStrategyFactory10):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
