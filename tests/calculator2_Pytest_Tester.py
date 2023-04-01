import pytest
from calculator2 import square

# assert é a mesma coisa que um if, porém para verficar se é verdade

# "pytest .\python\calculator2_Pytest_Tester.py" - para executar teste

"""
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
"""
# ------------------------------------------------------------------------------------------------------------------


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
