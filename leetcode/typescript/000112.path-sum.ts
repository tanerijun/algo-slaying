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

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
  function helper(root: TreeNode | null, currentSum: number) {
    if (!root) {
      return false;
    }

    const sum = currentSum + root.val;

    if (!root.left && !root.right) {
      return sum === targetSum;
    }

    return helper(root.left, sum) || helper(root.right, sum);
  }

  return helper(root, 0);
}
// Time complexity: O(n)
// Space complexity: O(n)
