# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h) - log(n) if tree is balanced
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            greatest_left_sum = max(dfs(node.left), 0)  # if negative, we just
            greatest_right_sum = max(dfs(node.right), 0)  # reset to 0 (not adding it)
            sum_if_node_is_root = node.val + greatest_left_sum + greatest_right_sum

            nonlocal max_path_sum
            max_path_sum = max(max_path_sum, sum_if_node_is_root)

            return node.val + max(greatest_left_sum, greatest_right_sum)

        dfs(root)
        return int(max_path_sum)
