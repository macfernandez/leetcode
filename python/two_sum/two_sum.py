from typing import *

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
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
            needed = target - nums[i]
            masked_nums = nums[:i] + [None] + nums[i+1:]
            if needed in masked_nums:
                j = masked_nums.index(needed)
                solution = [i,j]
                return solution
