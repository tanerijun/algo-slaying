from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	# Time complexity: O(n)
	# Space complexity: O(1)
	def hasCycle(self, head: Optional[ListNode]) -> bool:
		if not head or not head.next:
			return False

		slow, fast = head, head
		while slow and fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True

		return False
