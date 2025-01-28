# problem 88
# https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m < len(nums1):
            _ = nums1.pop()

        if not nums1:
            nums1.extend(nums2[:n])
            return

        if not nums2[:n]:
            return

        else:
            i, p1, p2 = 0, 0, 0
            while i < m+n:
                if len(nums1) == m+n:
                    break
                n1, n2 = nums1[p1], nums2[p2]
                if n1 < n2:
                    if len(nums1)-1 <= p1:
                        nums1.append(n2)
                        p2 += 1
                else:
                    nums1.insert(i, n2)
                    p2 += 1
                p1 += 1
                i += 1
