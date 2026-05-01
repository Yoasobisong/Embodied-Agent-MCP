from ..interfaces.IAbstractStrategyFactory34 import IAbstractStrategyFactory34

class EnterpriseStrategyFactoryImpl34(IAbstractStrategyFactory34):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
