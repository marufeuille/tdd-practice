import pytest

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent / "src"))
from init import init

def test_multiplication(init):
    from dollar import Dollar
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount