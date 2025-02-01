import pytest

from top_interview_150.merged_sorted_array import Solution


@pytest.mark.parametrize('nums1, m, nums2, n, expected',[
    ([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
    ([1], 1, [], 0, [1]),
    ([0], 0, [1], 1, [1]),
    ([1,0], 1, [2], 1, [1,2]),
    ([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6])
])


def test_solution(nums1, m, nums2, n, expected):
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == expected