import pytest

from python.single_number.single_number import Solution

@pytest.mark.parametrize('nums, expected_single',[
    ([2,2,1], 1),
    ([4,1,2,1,2], 4),
    ([1], 1)
])
def test_given_list_when_add_longest_common_prefix_runs_then_returns_expected_common_prefix(nums, expected_single):
    assert Solution().single_number(nums) == expected_single