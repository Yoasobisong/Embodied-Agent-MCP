from ..interfaces.IAbstractStrategyFactory46 import IAbstractStrategyFactory46

class EnterpriseStrategyFactoryImpl46(IAbstractStrategyFactory46):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
