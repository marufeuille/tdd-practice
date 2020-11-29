import pytest

from money import Money

def test_multiplication():
    five = Money.dollar(5)
    assert Money(10, "USD") == five.times(2)
    assert Money(15, "USD") == five.times(3)

def test_equality():
    assert Money(5, "USD") == Money(5, "USD")
    assert Money(5, "USD") != Money(7, "USD")
    assert Money(5, "CHF") == Money(5, "CHF")
    assert Money(5, "CHF") != Money(6, "CHF")
    assert Money(5, "USD") != Money(5, "CHF")

def test_franc_multiplication():
    five = Money.franc(5)
    assert Money(10, "CHF") == five.times(2)
    assert Money(15, "CHF") == five.times(3)
