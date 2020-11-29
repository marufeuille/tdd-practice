class Money:
    def __init__(self: 'Money', amount: int, currency: str):
        self._amount: int = amount
        self._currency: str = currency

    def __eq__(self: 'Money', others:'Money') -> bool:
        return self._amount == others._amount \
            and type(self) == type(others)

    @classmethod
    def dollar(cls: 'Money', amount: int) -> 'Money':
        return Money(amount, "USD")

    @classmethod
    def franc(cls: 'Money', amount: int) -> 'Money':
        return Money(amount, "CHF")