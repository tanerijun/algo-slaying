# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        seen = []
        queue = deque([root])

        while queue:
            nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                nodes.append(node)
            seen.append(nodes[-1].val)  # the right-most node

        return seen

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ret = []
        queue = [root]
        while queue:
            ret.append(queue[-1].val)
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue

        return ret
