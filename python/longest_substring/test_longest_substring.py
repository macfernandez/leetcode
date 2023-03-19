import pytest

from python.longest_substring.longest_substring import Solution


@pytest.mark.parametrize('s, expected_output', [
    ('abcabcbb', 3),
    ('bbbbb', 1),
    ('pwwkew', 3),
    ('jbpnbwwd', 4)
])
def test_solution(s, expected_output):
    assert Solution().lengthOfLongestSubstring(s) == expected_output