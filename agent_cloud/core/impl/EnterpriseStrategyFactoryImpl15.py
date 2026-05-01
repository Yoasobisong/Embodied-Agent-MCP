from ..interfaces.IAbstractStrategyFactory15 import IAbstractStrategyFactory15

class EnterpriseStrategyFactoryImpl15(IAbstractStrategyFactory15):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
