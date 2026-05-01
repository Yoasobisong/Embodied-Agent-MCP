from ..interfaces.IAbstractStrategyFactory44 import IAbstractStrategyFactory44

class EnterpriseStrategyFactoryImpl44(IAbstractStrategyFactory44):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
