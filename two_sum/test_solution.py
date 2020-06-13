import pytest

from two_sum.two_sum import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution = Solution()
    return solution


def test_twoSum(init_solution):
    assert init_solution.twoSum([2, 7, 11, 15], 9) == (0, 1)
