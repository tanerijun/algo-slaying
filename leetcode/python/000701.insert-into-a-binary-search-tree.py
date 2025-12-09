from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(h)
    # Space complexity: O(h)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    # Time complexity: O(h)
    # Space complexity: O(1)
    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
