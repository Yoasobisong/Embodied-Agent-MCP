from ..interfaces.IAbstractStrategyFactory48 import IAbstractStrategyFactory48

class EnterpriseStrategyFactoryImpl48(IAbstractStrategyFactory48):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
