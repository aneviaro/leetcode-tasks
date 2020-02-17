import pytest

from reverse_integer.reverse_integer import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution = Solution()
    return solution


def test_reverse(init_solution):
    assert init_solution.reverse(123) == 321
    assert init_solution.reverse(-123) == -321
    assert init_solution.reverse(120) == 21
    assert init_solution.reverse(1111111123819283791823)==0
    assert init_solution.reverse(1534236469)==0
