# problem 88
# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def _merge(self, nums_x: List[int], x: int, nums_y: List[int], y: int) -> None:
        pointer_y = 0
        while pointer_y < y:
            ny = nums_y[pointer_y] # 2
            print(ny)
            pointer_y += 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m < len(nums1):
            _ = nums1.pop()

        if not nums1:
            nums1.extend(nums2)
        
        else:
            p1 = 0
            for p2 in range(len(nums2[:n])):
                if nums2[p2] <= nums1[p1]:
                    nums1.insert(p1, nums2[p2])
                    p1 += 1
                else:
                    try:
                        while nums1[p1] < nums2[p2]:
                            p1 += 1
                        nums1.insert(p1, nums2[p2])
                        p1 += 1
                    except IndexError:
                        p1 -= 1
                        nums1.append(nums2[p2])
