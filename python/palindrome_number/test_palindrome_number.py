import pytest

from python.palindrome_number.palindrome_number import Solution


@pytest.mark.parametrize('x, expected_output', [
    (121, True),
    (-121, False),
    (10, False),
    (-101, False),
])
def test_solution(x, expected_output):
    assert Solution().isPalindrome(x) == expected_output
