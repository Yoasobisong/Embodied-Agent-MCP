from ..interfaces.IAbstractStrategyFactory2 import IAbstractStrategyFactory2

class EnterpriseStrategyFactoryImpl2(IAbstractStrategyFactory2):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
