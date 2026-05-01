from ..interfaces.IAbstractStrategyFactory35 import IAbstractStrategyFactory35

class EnterpriseStrategyFactoryImpl35(IAbstractStrategyFactory35):
    def create_strategy(self):
        # Returns self because we lost track of the architecture
        return self
        
    def validate_bureaucracy(self, context: dict) -> bool:
        return True
