from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(h)
    # Space complexity: O(h)
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            cur.left = root.left
            res = root.right
            del root
            return res

        return root

    # Time complexity: O(h)
    # Space complexity: O(h)
    def deleteNode1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root

    # Time complexity: O(h)
    # Space complexity: O(1)
    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        parent = None
        cur = root

        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left

        if not cur:
            return root

        # Node with <= 1 child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        else:
            # Node with 2 children
            par = None  # parent of right subtree min node
            delNode = cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left

            if par:  # if there was a left traversal
                par.left = cur.right
                cur.right = delNode.right

            cur.left = delNode.left

            if not parent:  # if we are deleting root
                return cur

            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur

        return root

    # Without changing value
    # Time complexity: O(h)
    # Space complexity: O(h)
    # Example:
    # Delete 5:
    # Before:
    #        5
    #       / \
    #      3   8
    #     / \   \
    #    1   4   10
    # After:
    #         8          ← This becomes the new root
    #        / \
    #       3   10       ← The entire left subtree (3,1,4) is now under 8
    #      / \
    #     1   4
    #
    # Delete 10:
    # Before:
    #     10
    #    /  \
    #   5    15
    #  / \   / \
    # 3   7 12  20
    # After:
    #       15
    #      /  \
    #    12    20
    #    /
    #   5
    #  / \
    # 3   7
    #
    # Delete 50
    # Before:
    #    50
    #   /  \
    # 30    70
    #      /  \
    #     60   80
    #    /  \
    #   55   65
    #        \
    #         67
    # After:
    #       70
    #      /  \
    #     60   80
    #    /  \
    #   55   65
    #  /      \
    # 30       67     ← BST property maintained
    def deleteNode3(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # <= 1 children
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 2 children
            successor = root.right
            while successor.left:
                successor = successor.left
            successor.left = root.left
            return root.right

        return root
