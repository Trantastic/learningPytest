import pytest

#In pytest, any tests with the test_ naming will be executed as test cases
def test_one_plus_one():
    #assert statement is native to python
    assert 1 + 1 == 2

#To run test on commandline, python3 -m pytest

#Creating a failed test to see how pytest handles test failures
#def test_one_plus_two():
#    a = 1
#    b = 2
#    c = 0
#    assert a + b == c

def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

#Test case with an exception
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)

#Parameterized test case
products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


