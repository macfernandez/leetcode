from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = list()
        remain = 0
        shorter_list = l1 if len(l1) < len(l2) else l2
        longer_list = l1 if len(l1) >= len(l2) else l2
        for i in range(len(longer_list)):
            if i < len(shorter_list):
                l_sum = shorter_list[i] + longer_list[i] + remain
                if l_sum >= 10:
                    solution.append(int(str(l_sum)[-1]))
                    remain = int(str(l_sum)[:-1])
                else:
                    solution.append(l_sum)
                    remain = 0
            else:
                l_sum = longer_list[i] + remain
                if l_sum >= 10:
                    solution.append(int(str(l_sum)[-1]))
                    remain = int(str(l_sum)[:-1])
                else:
                    solution.append(l_sum)
                    remain = 0
        if remain:
            solution.append(remain)
        return solution

#print(Solution().addTwoNumbers([2,4,3],[5,6,4]))
#print(Solution().addTwoNumbers([0],[0]))
#print(Solution().addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
        

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

9 | 9 | 0 | 18 | 8
9 | 9 | 1 | 19 | 9
9 | 9 | 1 | 19 | 9
9 | 9 | 1 | 19 | 9
9 | 0 | 1 | 10 | 0
9 | 0 | 1 | 10 | 0
9 | 0 | 1 | 10 | 0
0 | 0 | 1 | 1  | 1