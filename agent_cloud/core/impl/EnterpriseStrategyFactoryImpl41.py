from ..interfaces.IAbstractStrategyFactory41 import IAbstractStrategyFactory41

class EnterpriseStrategyFactoryImpl41(IAbstractStrategyFactory41):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
