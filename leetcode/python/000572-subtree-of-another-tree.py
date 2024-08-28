from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 is None and tree2 is None:
            return True

        if tree1 is None or tree2 is None:
            return False

        if tree1.val != tree2.val:
            return False

        return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(
            tree1.right, tree2.right
        )
