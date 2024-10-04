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

function diameterOfBinaryTree(root: TreeNode | null): number {
  let maxDiameter = 0;

  function dfs(root: TreeNode | null) {
    if (!root) {
      return 0;
    }

    const leftHeight = dfs(root.left);
    const rightHeight = dfs(root.right);

    maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

    return 1 + Math.max(leftHeight, rightHeight); // to parent, add parent plus whichever child is deeper.
  }

  dfs(root);

  return maxDiameter;
}
// Time complexity: O(n)
// Space complexity: O(n)
