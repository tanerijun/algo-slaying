from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(log(n))
    # Space complexity: O(log(n))
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node or node.val == val:
                return node
            elif val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)

    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def searchBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            root = root.left if val < root.val else root.right
        return root

    # Time complexity: O(log(n))
    # Space complexity: O(log(n))
    def searchBST3(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        return (
            self.searchBST3(root.left, val)
            if val < root.val
            else self.searchBST3(root.right, val)
        )
