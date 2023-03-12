from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            Given two non-empty linked lists representing two non-negative
            integers, return the sum as a linked list.

            Parameters
            ----------
            l1: ListNode
                List with integers.
                
            l2: ListNode
                List with integers.

            Returns
            -------
            solution: list
                List with the sum.
        '''
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
