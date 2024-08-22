from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([root])
        lvl = 0
        while queue:
            lvl += 1

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return lvl

    # Recursive DFS
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_depth):
            if node is None:
                return curr_depth

            return max(dfs(node.left, curr_depth + 1), dfs(node.right, curr_depth + 1))

        return dfs(root, 0)

    # Recursive DFS
    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth3(root.left), self.maxDepth3(root.right))

    # Iterative DFS
    def maxDepth4(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth
