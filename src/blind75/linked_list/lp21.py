from data_structures.list import ListNode

from typing import Optional


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
