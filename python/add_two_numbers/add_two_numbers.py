# problem #2
# https://leetcode.com/problems/add-two-numbers/description/


from typing import Optional

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
        l1_int, l2_int = self.getVals(l1), self.getVals(l2)
        addition = l1_int + l2_int
        for i, digit in enumerate(str(addition)):
            if i == 0:
                list_node = ListNode(val=int(digit))
            else:
                list_node = ListNode(val=int(digit), next=list_node)
        return list_node
        
    def getVals(self, node: ListNode):
        vals = ''
        while node != None:
            vals = f'{node.val}{vals}'
            node = node.next
        return int(vals)
