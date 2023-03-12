from typing import List


class Solution:
    def single_number(self, nums: List[int]) -> int:
        '''
            Take a list of integers and return the only number that appears
            once.

            Parameters
            ----------
            nums: list
                List of int.

            Returns
            -------
            single: int
                Integer that only appears once in the list.
        '''
        nums_set = set(nums)
        for n in nums_set:
            n_count = nums.count(n)
            if n_count == 1:
                single = n
        return single
