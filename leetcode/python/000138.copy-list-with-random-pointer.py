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
