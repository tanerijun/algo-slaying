from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node):
            if node is None:
                return 0

            leftH, rightH = dfs(node.left), dfs(node.right)

            height_diff = abs(leftH - rightH)
            print(height_diff)
            if height_diff > 1:
                nonlocal balanced
                balanced = False

            return 1 + max(leftH, rightH)

        dfs(root)
        return balanced
