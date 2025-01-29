# problem 88
# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, pointer = m-1, n-1, m+n-1
        
        while 0 <= p2:
            if (0 <= p1) and (nums2[p2] < nums1[p1]):
                nums1[pointer] = nums1[p1]
                p1 -= 1
            else:
                nums1[pointer] = nums2[p2]
                p2 -= 1
            pointer -= 1