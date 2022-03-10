from data_structures.list import ListNode

from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find Middle
        if not head:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        prev, curr = None, slow.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # set slow.next to None
        # so that we cut the forward moving node
        slow.next = None

        forward, backward = head, prev

        while backward:
            next = forward.next
            forward.next = backward
            forward = backward
            backward = next

