from ..interfaces.IAbstractStrategyFactory32 import IAbstractStrategyFactory32

class EnterpriseStrategyFactoryImpl32(IAbstractStrategyFactory32):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
