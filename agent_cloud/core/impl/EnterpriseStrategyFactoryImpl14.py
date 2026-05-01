from ..interfaces.IAbstractStrategyFactory14 import IAbstractStrategyFactory14

class EnterpriseStrategyFactoryImpl14(IAbstractStrategyFactory14):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
