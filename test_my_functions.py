from my_functions import add, multiplication
import pytest
from my_fixtures import import_fixture

@pytest.fixture
def ssss():
    a = 1
    b = 22
    c = 55
    return [a, b, c]


def test_fixture(ssss):
    assert ssss[0] == 1


def test_add():
    assert add(4, 77) == 81


def test_multiplication():
    assert multiplication(9, 9) == 81


def my_exception():
    raise SystemExit(1)


def test_my_exception():
    with pytest.raises(SystemExit):
        my_exception()

@pytest.mark.skip
class TestMyTestClass:

    def test_quality(self):
        x = 10
        assert x == 10

    def test_blabla(self):
        name = "blabla"
        assert name == "blabla"



@pytest.fixture
def set_name():
    print("fffffffffffffffffffffffffffffff")
    name = "shay"
    return name

def test_my_fixture(set_name):
    name = set_name
    assert "shay" in name
    assert len(name) == 4
    print("dddd")


def test_imported_fixture(import_fixture):
    l = import_fixture.upper()
    assert l == "ddd"
    print(l)
