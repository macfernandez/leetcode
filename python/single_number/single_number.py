from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        '''
            Take a list of integers and return the only number that appears once.

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
        nums_set = set(nums)
        for n in nums_set:
            n_count = nums.count(n)
            if n_count == 1:
                single = n
        return single
