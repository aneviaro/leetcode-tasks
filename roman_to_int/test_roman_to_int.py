
import pytest
from roman_to_int.roman_to_int import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution = Solution()
    return solution

def test_roman_to_int(init_solution):
    assert init_solution.romanToInt('IX')==9
    assert init_solution.romanToInt('III')==3
    assert init_solution.romanToInt('IV')==4
    assert init_solution.romanToInt('V')==5
    # assert init_solution.romanToInt(3)=='III'
    # assert init_solution.romanToInt(4)=='IV'
    # assert init_solution.romanToInt(5)=='V'