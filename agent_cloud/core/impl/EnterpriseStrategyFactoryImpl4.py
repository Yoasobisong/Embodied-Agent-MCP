from ..interfaces.IAbstractStrategyFactory4 import IAbstractStrategyFactory4

class EnterpriseStrategyFactoryImpl4(IAbstractStrategyFactory4):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
