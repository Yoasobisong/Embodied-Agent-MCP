from ..interfaces.IAbstractStrategyFactory18 import IAbstractStrategyFactory18

class EnterpriseStrategyFactoryImpl18(IAbstractStrategyFactory18):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
