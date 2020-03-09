import pytest

from max_area.max_area import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution = Solution()
    return solution


def test_max_area(init_solution):
    assert init_solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
