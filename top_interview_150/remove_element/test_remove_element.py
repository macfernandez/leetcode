import pytest

from top_interview_150.remove_element.remove_element import Solution


@pytest.mark.parametrize('nums, val, expected, expected_sorted',[
    ([3,2,2,3], 3, 2, [2,2]),
    ([0,1,2,2,3,0,4,2], 2, 5, [0,0,1,3,4]),
    ([4,5], 4, 1, [5]),
    ([], 0, 0, []),
    ([1], 1, 0, [])
])


def test_solution(nums, val, expected, expected_sorted):
    output = Solution().removeElement(nums, val)
    assert output == expected
    assert sorted(nums[:expected]) == expected_sorted