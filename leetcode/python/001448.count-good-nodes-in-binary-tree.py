class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h), h: height of tree
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, curr_max):
            if node is None:
                return

            if node.val >= curr_max:
                curr_max = node.val
                nonlocal res
                res += 1

            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, float("-inf"))

        return res

    def goodNodes2(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if node is None:
                return 0

            res = 1 if node.val >= curr_max else 0
            curr_max = max(curr_max, node.val)
            res += dfs(node.left, curr_max)
            res += dfs(node.right, curr_max)

            return res

        return dfs(root, root.val)
