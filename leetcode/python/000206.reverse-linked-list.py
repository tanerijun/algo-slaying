from typing import Optional

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	# Time complexity: O(n)
	# Space complexity: O(1)
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		ptr1 = None
		ptr2 = head
		while ptr2:
			temp = ptr2.next
			ptr2.next = ptr1
			ptr1 = ptr2
			ptr2 = temp
		return ptr1
