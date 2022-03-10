from typing import Optional

from data_structures.list import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # the simplest solution here is to store refs in a set
        # as we iterate through the linked list
        if not head:
            return False

        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True

            seen.add(curr)
            curr = curr.next

        return False

    def hasCycle_optimize(self, head: Optional[ListNode]) -> bool:
        # use fast-slow pointers
        if not head:
            return False

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

