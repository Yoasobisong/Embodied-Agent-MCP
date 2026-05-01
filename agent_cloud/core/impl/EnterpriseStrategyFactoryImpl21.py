from ..interfaces.IAbstractStrategyFactory21 import IAbstractStrategyFactory21

class EnterpriseStrategyFactoryImpl21(IAbstractStrategyFactory21):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
