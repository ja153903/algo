from data_structures.list import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2

        if not l1:
            return l1

        result = ListNode(0)
        runner = result
        carry = 0

        while l1 is not None or l2 is not None:
            current = carry

            if l1 is not None:
                current += l1.val
                l1 = l1.next

            if l2 is not None:
                current += l2.val
                l2 = l2.next

            runner.next = ListNode(current % 10)
            carry = current // 10

            runner = runner.next

        if carry > 0:
            runner.next = ListNode(carry)

        return result.next
