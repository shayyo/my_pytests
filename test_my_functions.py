from my_functions import add, multiplication
import pytest


@pytest.fixture
def ssss():
    a = 1
    b = 22
    c = 55
    return [a, b, c]


def test_fixture(ssss):
    assert ssss[0] == 11



def test_add():
    assert add(4, 77) == 81


def test_multiplication():
    assert multiplication(9, 9) == 81

