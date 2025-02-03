# problem 80
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, ii, last = 0, 1, len(nums)
        while ii < last:
            e, ee = nums[i], nums[ii]
            if e != ee:
                if ii-i == 1:
                    ii += 1
                i += 1
            else:
                if ii-i == 1:
                    ii += 1
                else:
                    nums[ii:] = nums[ii+1:] + [e]
                    last -= 1
        return ii
