import pytest

from atoi.atoi import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution = Solution()
    return solution


def test_myAtoi(init_solution):
    assert init_solution.myAtoi("42") == 42
    assert init_solution.myAtoi("   -42") == -42
    assert init_solution.myAtoi("4193 with words") == 4193
    assert init_solution.myAtoi("words and 987") == 0
    assert init_solution.myAtoi("-91283472332") == -2147483648
    assert init_solution.myAtoi("") == 0
    assert init_solution.myAtoi("+") == 0
    assert init_solution.myAtoi("++++++") ==0
    assert init_solution.myAtoi("2147483648") ==2147483647
