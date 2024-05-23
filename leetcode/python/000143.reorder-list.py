from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def reorderList(self, head: Optional[ListNode]) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""
		pt1, pt2 = head, head
		while pt2 and pt2.next:
			pt1 = pt1.next
			pt2 = pt2.next.next

		reversed_half = self.reverse_list(pt1.next)
		pt1.next = None

		pt1 = head
		pt2 = reversed_half
		while pt1 and pt2:
			temp = pt1.next
			pt1.next = pt2
			pt1 = temp
			temp = pt2.next
			pt2.next = pt1
			pt2 = temp

	def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
		pt1 = None
		pt2 = head
		while pt2:
			temp = pt2.next
			pt2.next = pt1
			pt1 = pt2
			pt2 = temp
		return pt1
