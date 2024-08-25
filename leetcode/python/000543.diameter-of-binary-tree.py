from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            leftH = dfs(node.left)
            rightH = dfs(node.right)
            diameter = leftH + rightH

            nonlocal maxDiameter
            maxDiameter = max(maxDiameter, diameter)  # updates maxDiameter

            return max(leftH, rightH) + 1  # returns the higher height, + 1 for self

        dfs(root)
        return maxDiameter
