from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: "Optional[Node]" = None, random: "Optional[Node]" = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
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
    def copyRandomList2(self, head: "Optional[Node]") -> "Optional[Node]":
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
            if cur.next:
                cur.next = cur.next.next
            cur = cur.next

        return head.next

    # Time complexity: O(n)
    # Space complexity: O(n)
    def copyRandomList3(self, head: "Optional[Node]") -> "Optional[Node]":
        cloned = {}

        def dfs(node: "Optional[Node]") -> "Optional[Node]":
            if node is None:
                return None
            if node in cloned:
                return cloned[node]

            clone = Node(node.val)
            cloned[node] = clone
            clone.next = dfs(node.next)
            clone.random = dfs(node.random)

            return clone

        return dfs(head)


class Solution2:
    def __init__(self):
        self.visited = {}

    def getNode(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                new_node = Node(node.val)
                self.visited[node] = new_node
                return new_node
        return None

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        old_node = head
        new_node = self.getNode(old_node)

        while old_node:
            new_node.next = self.getNode(old_node.next)
            new_node.random = self.getNode(old_node.random)

            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]
