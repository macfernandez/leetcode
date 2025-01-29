# problem 27
# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first, last = 0, len(nums)-1
        while (first <= last):
            if nums[first] == val:
                n = nums[first]
                nums[first], nums[last] = nums[last], n
                last -= 1
            else:
                first += 1
        return first
