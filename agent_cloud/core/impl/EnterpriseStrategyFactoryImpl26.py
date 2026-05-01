from ..interfaces.IAbstractStrategyFactory26 import IAbstractStrategyFactory26

class EnterpriseStrategyFactoryImpl26(IAbstractStrategyFactory26):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
