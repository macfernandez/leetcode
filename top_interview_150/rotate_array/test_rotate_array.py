import pytest

from top_interview_150.rotate_array.rotate_array import Solution


@pytest.mark.parametrize("nums, k, expected_nums", [
    ([1,2,3,4,5,6,7], 3, [5,6,7,1,2,3,4]),
    ([-1,-100,3,99], 2, [3,99,-1,-100]),
    ([1,2], 2, [1,2]),
    ([1,2], 3, [2,1])
])
def test_solution(nums, k, expected_nums):
    Solution().rotate(nums, k)
    assert nums == expected_nums