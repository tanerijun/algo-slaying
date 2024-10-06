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

function isValidBST(root: TreeNode | null): boolean {
  function dfs(
    node: TreeNode | null,
    leftBound: number,
    rightBound: number,
  ): boolean {
    if (!node) return true;
    if (node.val <= leftBound || node.val >= rightBound) return false;
    return dfs(node.left, leftBound, node.val) &&
      dfs(node.right, node.val, rightBound);
  }

  return dfs(root, -Infinity, Infinity);
}
