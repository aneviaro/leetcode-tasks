import pytest

from zigzag import ZigZag

@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution=ZigZag()
    return solution
def test_convert(init_solution):
    assert init_solution.convert("AB", 1)=="AB"
    assert init_solution.convert("PAYPALISHIRING", 3)=="PAHNAPLSIIGYIR"