# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        return values

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            values.append(cur.val)

            cur = cur.right

        return values
