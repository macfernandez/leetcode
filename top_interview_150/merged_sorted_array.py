# problem 88
# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def prune(self, nums: List[int], n: int) -> None:
        while n < len(nums):
            _ = nums.pop()

    def sort(self, nums: List[int]) -> None:
        n = len(nums)
        for i in range(n):
            finished = True
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    finished = False
            if finished:
                break

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.prune(nums1, m)
        self.prune(nums2, n)
        self.sort(nums1)
