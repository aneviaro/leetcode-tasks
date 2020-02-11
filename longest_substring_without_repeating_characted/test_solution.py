import pytest

from longest_substring_without_repeating_characted.longest_substr import Solution


@pytest.fixture(scope='session', autouse=True)
def init_solution():
    solution=Solution()
    return solution

def test_lengthOfLongestSubstring(init_solution):
    assert init_solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert init_solution.lengthOfLongestSubstring("bbbbb") == 1
    assert init_solution.lengthOfLongestSubstring("pwwkew") == 3

