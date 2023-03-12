import pytest

from python.longest_common_prefix.longest_common_prefix import Solution

@pytest.mark.parametrize('strs, expected_prefix',[
    ([""], ''),
    (["flower","flow","flight"], 'fl'),
    (["dog","racecar","car"], '')
])
def test_given_list_when_add_longest_common_prefix_runs_then_returns_expected_common_prefix(strs, expected_prefix):
    assert Solution().longestCommonPrefix(strs) == expected_prefix