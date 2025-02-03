import pytest

from top_interview_150.remove_duplicates_from_sorted_array_ii.remove_duplicates_from_sorted_array_ii import Solution


@pytest.mark.parametrize('nums, expected, expected_sorted',[
    ([1], 1, [1]),
    ([1,1], 2, [1,1]),
    ([1,1,2,2,3], 5, [1,1,2,2,3]),
    ([1,1,1,2,2,3], 5, [1,1,2,2,3]),
    ([0,0,1,1,1,1,2,3,3], 7, [0,0,1,1,2,3,3]),
])


def test_solution(nums, expected, expected_sorted):
    output = Solution().removeDuplicates(nums)
    assert output == expected
    assert sorted(nums[:expected]) == expected_sorted