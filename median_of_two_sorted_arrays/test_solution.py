import pytest

from median_of_two_sorted_arrays.median import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution = Solution()
    return solution

def test_findMedianSortedArrays(init_solution):
    assert init_solution.findMedianSortedArrays([1, 3], [2])==2.0
    assert init_solution.findMedianSortedArrays([1,2], [3,4])==2.5
