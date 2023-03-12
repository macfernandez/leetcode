import pytest

from python.implement_str_str.implement_str_str import Solution


@pytest.mark.parametrize('haystack, needle, expected_start_pos',[
    ('hello','ll',2),
    ('aaaaa','bba',-1),
    ('aaaaa','',0),
    ('a','a',0),
    ("mississippi","issi",1),
    ("mississippi","issip",4)
])
def test_given_haystack_and_needle_when_implement_str_str_runs_then_returns_expected_start_pos(haystack,needle,expected_start_pos):
    assert Solution().strStr(haystack, needle) == expected_start_pos