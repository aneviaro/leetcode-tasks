import random

import pytest
from int_to_roman.int_to_roman import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution = Solution()
    return solution

def test_int_to_roman(init_solution):
    assert init_solution.intToRoman(9)=='IX'
    assert init_solution.intToRoman(3)=='III'
    assert init_solution.intToRoman(4)=='IV'
    assert init_solution.intToRoman(5)=='V'