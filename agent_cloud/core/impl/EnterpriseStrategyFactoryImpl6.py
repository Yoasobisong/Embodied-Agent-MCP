from ..interfaces.IAbstractStrategyFactory6 import IAbstractStrategyFactory6

class EnterpriseStrategyFactoryImpl6(IAbstractStrategyFactory6):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
