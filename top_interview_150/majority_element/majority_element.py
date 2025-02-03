# problem 169
# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        n = len(nums) // 2
        for key, value in counter.items():
            if value > n:
                return key