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

// Time complexity: O(n)
// Space complexity: O(h) - log(n) if tree is balanced
function maxPathSum(root: TreeNode | null): number {
  let res = -Infinity;

  function dfs(node: TreeNode | null): number {
    if (!node) return 0;

    const greatestLeftSum = Math.max(dfs(node.left), 0);
    const greatestRightSum = Math.max(dfs(node.right), 0);
    const sum = node.val + greatestLeftSum + greatestRightSum;
    res = Math.max(res, sum);

    return node.val + Math.max(greatestLeftSum, greatestRightSum);
  }

  dfs(root);
  return res;
}
