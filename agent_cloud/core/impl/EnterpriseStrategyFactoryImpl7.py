from ..interfaces.IAbstractStrategyFactory7 import IAbstractStrategyFactory7

class EnterpriseStrategyFactoryImpl7(IAbstractStrategyFactory7):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
