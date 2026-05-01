from ..interfaces.IAbstractStrategyFactory23 import IAbstractStrategyFactory23

class EnterpriseStrategyFactoryImpl23(IAbstractStrategyFactory23):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
