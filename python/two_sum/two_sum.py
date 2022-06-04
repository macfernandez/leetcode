from typing import *

class Solution:
    #def two_sum(self, nums: List[int], target: int) -> List[int]:
    #    '''
    #        Take a list of integers (nums) and an integer (target) and return
    #        the positions in the list that add up the target.
    #
    #        Time complexity: O(n^2)
    #
    #        Parameters
    #        ----------
    #        nums: list
    #            List of int.
    #
    #        target: int
    #            Target for the addition.
    #
    #        Returns
    #        -------
    #        solution: list
    #            List of int with number positions that add up to target.
    #    '''
    #    solution = list()
    #    for i in range(len(nums)):
    #        for j in range(len(nums)):
    #            if i < j:
    #                if (nums[i] + nums[j] == target):
    #                    solution.append(i)
    #                    solution.append(j)
    #                    break
    #    return solution

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        '''
            Take a list of integers (nums) and an integer (target) and return
            the positions in the list that add up the target.

            Time complexity: (n * (n-1))/2 -> O(n^2)

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
        solution = list()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    solution.append(i)
                    solution.append(j)
                    break
        return solution

# 0 - 0  x||   1 - 0 x ||   2 - 0 x ||   3 - 0 x || 4 - 0 x ||   5 - 0 x ||    6 - 0 x
# 0 - 1   ||   1 - 1 x ||   2 - 1 x ||   3 - 1 x || 4 - 1 x ||   5 - 1 x ||    6 - 1 x
# 0 - 2   ||   1 - 2   ||   2 - 2 x ||   3 - 2 x || 4 - 2 x ||   5 - 2 x ||    6 - 2 x
# 0 - 3   ||   1 - 3   ||   2 - 3   ||   3 - 3 x || 4 - 3 x ||   5 - 3 x ||    6 - 3 x
# 0 - 4   ||   1 - 4   ||   2 - 4   ||   3 - 4   || 4 - 4 x ||   5 - 4 x ||    6 - 4 x
# 0 - 5   ||   1 - 5   ||   2 - 5   ||   3 - 5   || 4 - 5   ||   5 - 5 x ||    6 - 5 x
# 0 - 6   ||   1 - 6   ||   2 - 6   ||   3 - 6   || 4 - 6   ||   5 - 6   ||    6 - 6 x
