import pytest

from dollar import Dollar
from franc import Franc

def test_multiplication():
    five = Dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(7)

def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
