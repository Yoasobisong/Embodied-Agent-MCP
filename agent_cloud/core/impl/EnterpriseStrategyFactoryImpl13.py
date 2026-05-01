from ..interfaces.IAbstractStrategyFactory13 import IAbstractStrategyFactory13

class EnterpriseStrategyFactoryImpl13(IAbstractStrategyFactory13):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
