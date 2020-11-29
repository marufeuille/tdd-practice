class Money:
    def __init__(self: 'Money', amount: int):
        self._amount: int = amount

    def __eq__(self: 'Money', others:'Money') -> bool:
        return self._amount == others._amount \
            and type(self) == type(others)

    @classmethod
    def dollar(cls: 'Money', amount: int) -> 'Money':
        return Money(amount)