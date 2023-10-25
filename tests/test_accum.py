import pytest

from stuff.accum import Accumulator

#Verifies the new instance of Accumulator has a starting count of 0
def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0

#Verifies when add() is called with no other arguments the count increments by 1
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

#Verifies when add() is called with an argument of 3 the count increments to 3
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3

#Verifies when add() is called twice, count increments to 2
def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

#Verifies the count attribute cannot be assigned directly because it's a read only property
def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter"):
        accum.count = 10