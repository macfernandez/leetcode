import pytest

from python.longest_palindromic_substring.longest_palindromic_substring import Solution


@pytest.mark.parametrize('s, expected_substring', [
    ('babad', ['aba', 'bab']),
    ('cbbd', ['bb']),
    ('abbaa', ['abba']),
    ('nnabba', ['abba'])
])
def test_solution(s, expected_substring):
    assert Solution().longestPalindrome(s) in expected_substring