class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, others):
        return self._amount == others._amount