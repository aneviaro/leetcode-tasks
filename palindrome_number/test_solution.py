
import pytest

from palindrome_number import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution=Solution()
    return solution

def test_isPalindrome(init_solution):
    assert init_solution.isPalindrome(121)==True
    assert init_solution.isPalindrome(-121)==False
    assert init_solution.isPalindrome(10)==False