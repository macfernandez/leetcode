import pytest

from python.median_of_two_sorted_arrays.median_of_two_sorted_arrays import Solution


@pytest.mark.parametrize("nums1, nums2, expected_median", [
    ([1, 3], [2], 2.00000),
    ([1, 2], [3, 4], 2.50000),
    ([], [1], 1)
])
def test_solution(nums1, nums2, expected_median):
    assert Solution().findMedianSortedArrays(nums1, nums2) == expected_median