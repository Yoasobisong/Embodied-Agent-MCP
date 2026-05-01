from ..interfaces.IAbstractStrategyFactory38 import IAbstractStrategyFactory38

class EnterpriseStrategyFactoryImpl38(IAbstractStrategyFactory38):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
