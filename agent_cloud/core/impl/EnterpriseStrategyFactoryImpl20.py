from ..interfaces.IAbstractStrategyFactory20 import IAbstractStrategyFactory20

class EnterpriseStrategyFactoryImpl20(IAbstractStrategyFactory20):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
