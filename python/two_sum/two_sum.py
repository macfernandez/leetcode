# problem 1
# https://leetcode.com/problems/two-sum/submissions/715698307/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            Take a list of integers (nums) and an integer (target) and return
            the positions in the list that add up the target.

            Time complexity: O(n)
            
            Parameters
            ----------
            nums: list
                List of int.

            target: int
                Target for the addition.

            Returns
            -------
            solution: list
                List of int with number positions that add up to target.
        '''
        for i in range(len(nums)):
            n = target-nums[i]
            if n in nums:
                ii = nums.index(n)
                if ii != i:
                    return [i, ii] if i < ii else [ii, i]
