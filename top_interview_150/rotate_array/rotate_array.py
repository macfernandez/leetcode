# problem 189
# https://leetcode.com/problems/rotate-array/description/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k != len(nums):
            k = k%len(nums)
            nums[:] = nums[-k:] + nums[:-k]
