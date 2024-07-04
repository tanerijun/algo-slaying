from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        ptr1, ptr2 = head, head
        for _ in range(n):
            ptr2 = ptr2.next

        # If this condition is true, it means n is equal to the size of the list
        # The last element from the end of list is the first element of the list
        if not ptr2:
            return head.next

        while ptr2.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next

        print(ptr1.val, ptr2.val)

        # At this point, ptr1 is pointing to the element to delete
        if not ptr1.next:  # means there's only one element in the list
            return None

        temp = ptr1.next
        ptr1.next = ptr1.next.next
        temp.next = None

        return head

    # Cleaned up
    def removeNthFromEndCleaned(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
