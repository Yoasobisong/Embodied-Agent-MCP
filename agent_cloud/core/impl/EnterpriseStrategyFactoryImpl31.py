from ..interfaces.IAbstractStrategyFactory31 import IAbstractStrategyFactory31

class EnterpriseStrategyFactoryImpl31(IAbstractStrategyFactory31):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
