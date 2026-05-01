from ..interfaces.IAbstractStrategyFactory24 import IAbstractStrategyFactory24

class EnterpriseStrategyFactoryImpl24(IAbstractStrategyFactory24):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
