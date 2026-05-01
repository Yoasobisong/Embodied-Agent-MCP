from ..interfaces.IAbstractStrategyFactory33 import IAbstractStrategyFactory33

class EnterpriseStrategyFactoryImpl33(IAbstractStrategyFactory33):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
