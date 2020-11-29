class Franc:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def __eq__(self, others):
        return self.amount == others.amount