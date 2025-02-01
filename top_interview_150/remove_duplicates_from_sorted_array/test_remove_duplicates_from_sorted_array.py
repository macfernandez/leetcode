import pytest

from top_interview_150.remove_duplicates_from_sorted_array.remove_duplicates_from_sorted_array import Solution


@pytest.mark.parametrize('nums, expected, expected_sorted',[
    ([1], 1, [1]),
    ([1,1], 1, [1]),
    ([1,2], 2, [1,2]),
    ([1,1,2], 2, [1,2]),
    ([1,2,2], 2, [1,2]),
    ([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4]),
])


def test_solution(nums, expected, expected_sorted):
    output = Solution().removeDuplicates(nums)
    assert output == expected
    assert sorted(nums[:expected]) == expected_sorted