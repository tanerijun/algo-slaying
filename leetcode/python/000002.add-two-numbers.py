from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	# Time complexity: O(m + n), m = len(l1), n - len(l2)
	# Space complexity: O(1)
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		dummy_head = ListNode()
		cur = dummy_head
		carry = 0
		while l1 or l2:
			x, y = 0, 0
			if l1:
				x = l1.val
				l1 = l1.next
			if l2:
				y = l2.val
				l2 = l2.next
			sum = x + y + carry
			carry = sum // 10
			cur.next = ListNode(sum % 10)
			cur = cur.next

		if carry != 0:
			cur.next = ListNode(carry)

		return dummy_head.next
