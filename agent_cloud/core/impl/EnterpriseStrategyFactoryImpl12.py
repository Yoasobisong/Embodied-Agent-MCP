from ..interfaces.IAbstractStrategyFactory12 import IAbstractStrategyFactory12

class EnterpriseStrategyFactoryImpl12(IAbstractStrategyFactory12):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
