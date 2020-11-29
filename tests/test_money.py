import pytest

from dollar import Dollar
from franc import Franc
from money import Money

def test_multiplication():
    five = Money.dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(7)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Dollar(5) != Franc(5)

def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
