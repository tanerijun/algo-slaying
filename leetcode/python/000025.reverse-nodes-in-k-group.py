from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        group_prev = dummy_node

        while True:
            kth = self.get_kth(group_prev, k)

            if not kth:
                break

            group_next = kth.next

            # Reverse
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy_node.next

    def get_kth(self, node: Optional[ListNode], k: int) -> Optional[ListNode]:
        while node and k:
            node = node.next
            k -= 1
        return node
