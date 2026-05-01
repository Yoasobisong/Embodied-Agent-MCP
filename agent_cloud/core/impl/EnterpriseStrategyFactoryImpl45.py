from ..interfaces.IAbstractStrategyFactory45 import IAbstractStrategyFactory45

class EnterpriseStrategyFactoryImpl45(IAbstractStrategyFactory45):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
