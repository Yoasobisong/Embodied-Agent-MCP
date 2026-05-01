from ..interfaces.IAbstractStrategyFactory22 import IAbstractStrategyFactory22

class EnterpriseStrategyFactoryImpl22(IAbstractStrategyFactory22):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
