from money import Money
class Franc(Money):
    def __init__(self: 'Franc', amount: int):
        super().__init__(amount)

    def times(self: 'Franc', multiplier: int):
        return Franc(self._amount * multiplier)