from data_structures.list import ListNode

from typing import Optional


class Solution:
    def intuitive(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n == 0:
            return None

        if not head.next and n >= 1:
            return None

        result = []

        current = head

        while current:
            result.append(current)
            current = current.next
        
        l = len(result)
        if l - n == 0:
            return result[1]

        for i in range(len(result) - 1):
            if i + 1 == len(result) - n:
                result[i].next = result[i + 1].next

        return result[0]

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
