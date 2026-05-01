from ..interfaces.IAbstractStrategyFactory36 import IAbstractStrategyFactory36

class EnterpriseStrategyFactoryImpl36(IAbstractStrategyFactory36):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
