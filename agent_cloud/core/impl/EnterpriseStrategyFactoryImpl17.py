from ..interfaces.IAbstractStrategyFactory17 import IAbstractStrategyFactory17

class EnterpriseStrategyFactoryImpl17(IAbstractStrategyFactory17):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
