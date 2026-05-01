from ..interfaces.IAbstractStrategyFactory50 import IAbstractStrategyFactory50

class EnterpriseStrategyFactoryImpl50(IAbstractStrategyFactory50):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
