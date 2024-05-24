from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
	# Time complexity: O(n)
	# Space complexity: O(n)
	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		if not head:
			return None

		cloned = {}

		cur = head
		while cur:
			cloned[cur] = Node(cur.val)
			cur = cur.next

		cur = head
		while cur:
			cloned[cur].next = cloned[cur.next] if cur.next else None
			cloned[cur].random = cloned[cur.random] if cur.random else None
			cur = cur.next

		return cloned[head]

	# Time complexity: O(n)
	# Space complexity: O(1)
	def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
		if not head:
			return None

		# Create cloned nodes next to real nodes
		cur = head
		while cur:
			temp = Node(cur.val)
			temp.next = cur.next
			cur.next = temp
			cur = temp.next

		# Handle the node.random val for the cloned nodes
		cur = head
		while cur and cur.next:
			if cur.random:
				cur.next.random = cur.random.next
			cur = cur.next.next

		# Connect the cloned nodes
		cur = head.next
		while cur:
			cur.next = cur.next.next if cur.next
			cur = cur.next

		return head.next
