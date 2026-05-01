from ..interfaces.IAbstractStrategyFactory30 import IAbstractStrategyFactory30

class EnterpriseStrategyFactoryImpl30(IAbstractStrategyFactory30):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
