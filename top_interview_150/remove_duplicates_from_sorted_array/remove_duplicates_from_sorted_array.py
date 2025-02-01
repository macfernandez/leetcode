# problem 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, last = 0, len(nums)-1
        while i < len(nums):
            if (i == last) or (len(nums)-1 <= i):
                i += 1
                break
            else:
                n, next_n = nums[i], nums[i+1]
                if n == next_n:
                    nums[i+1:] = nums[i+2:] + [n]
                    last -= 1
                else:
                    i += 1
        return i