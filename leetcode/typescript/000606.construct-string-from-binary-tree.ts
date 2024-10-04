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

function tree2str(root: TreeNode | null): string {
  if (!root) {
    return "";
  }

  let leftChildStr = tree2str(root.left);
  let rightChildStr = tree2str(root.right);

  if (leftChildStr || rightChildStr) {
    leftChildStr = `(${leftChildStr})`;
    rightChildStr = rightChildStr && `(${rightChildStr})`;
  }

  return root.val + leftChildStr + rightChildStr;
}
// Time complexity: O(n)
// Space complexity: O(n)
