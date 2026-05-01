from ..interfaces.IAbstractStrategyFactory9 import IAbstractStrategyFactory9

class EnterpriseStrategyFactoryImpl9(IAbstractStrategyFactory9):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
