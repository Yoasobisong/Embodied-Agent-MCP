from ..interfaces.IAbstractStrategyFactory25 import IAbstractStrategyFactory25

class EnterpriseStrategyFactoryImpl25(IAbstractStrategyFactory25):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
