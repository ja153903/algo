from data_structures.list import ListNode

from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        copy = self.clone(head)
        reverse_node = self.reverse(copy)

        while head and reverse_node:
            if head.val != reverse_node.val:
                return False

            head = head.next
            reverse_node = reverse_node.next

        return True

    def clone(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return None

        result = ListNode(-1)

        curr, runner = node, result

        while curr:
            runner.next = ListNode(curr.val)
            runner = runner.next
            curr = curr.next

        return result.next

    def reverse(self, head: Optional[ListNode]) -> bool:
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev
