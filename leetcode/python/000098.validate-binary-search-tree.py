# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_bound, right_bound):
            if node is None:
                return True
            if not left_bound < node.val < right_bound:
                return False
            return dfs(node.left, left_bound, node.val) and dfs(
                node.right, node.val, right_bound
            )

        return dfs(root, float("-inf"), float("inf"))

    # Time complexity: O(n)
    # Space complexity: O(n)
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        values = []

        def dfs(root):  # inorder traversal
            if not root:
                return
            dfs(root.left)
            nonlocal values
            values.append(root.val)
            dfs(root.right)

        dfs(root)

        for i in range(1, len(values)):
            if values[i] < values[i - 1]:
                return False

        return True
