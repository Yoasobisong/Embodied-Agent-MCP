from ..interfaces.IAbstractStrategyFactory27 import IAbstractStrategyFactory27

class EnterpriseStrategyFactoryImpl27(IAbstractStrategyFactory27):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
