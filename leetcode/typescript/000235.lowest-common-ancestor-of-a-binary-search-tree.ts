/**
 * Definition for a binary tree node.
 */
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

// Time complexity: O(log(n))
// Space complexity: O(1)
function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null,
): TreeNode | null {
  if (root && p && q && root.val > p.val && root.val > q.val) {
    return lowestCommonAncestor(root.left, p, q);
  }
  if (root && p && q && root.val < p.val && root.val < q.val) {
    return lowestCommonAncestor(root.right, p, q);
  }
  return root;
}
