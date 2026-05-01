from ..interfaces.IAbstractStrategyFactory43 import IAbstractStrategyFactory43

class EnterpriseStrategyFactoryImpl43(IAbstractStrategyFactory43):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
