from money import Money
class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, others):
        return self._amount == others._amount