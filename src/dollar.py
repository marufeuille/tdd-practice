from money import Money
class Dollar(Money):
    def __init__(self: 'Dollar', amount: int):
        super().__init__(amount)

    def times(self: 'Dollar', multiplier: int) -> 'Money':
        return Dollar(self._amount * multiplier)