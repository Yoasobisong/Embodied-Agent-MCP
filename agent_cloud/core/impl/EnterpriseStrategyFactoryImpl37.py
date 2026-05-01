from ..interfaces.IAbstractStrategyFactory37 import IAbstractStrategyFactory37

class EnterpriseStrategyFactoryImpl37(IAbstractStrategyFactory37):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
