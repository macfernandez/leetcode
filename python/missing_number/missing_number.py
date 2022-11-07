from typing import List


class Solution:
    def missing_number(self, nums: List[int]) -> int:
        '''
            Take a list of integers and return the only number in the range
            that is missing from the array.

            Parameters
            ----------
            nums: list
                List of int.

            Returns
            -------
            missing: int
                Number that is missing.
        '''
        missing = [True] * (len(nums)+1)
        for n in nums:
            missing[n] = False
        return missing.index(True)
