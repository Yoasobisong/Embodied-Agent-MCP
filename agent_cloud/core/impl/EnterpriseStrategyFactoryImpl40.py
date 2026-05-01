from ..interfaces.IAbstractStrategyFactory40 import IAbstractStrategyFactory40

class EnterpriseStrategyFactoryImpl40(IAbstractStrategyFactory40):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
