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

function sortedArrayToBST(nums: number[]): TreeNode | null {
  function helper(l: number, r: number) {
    if (l > r) {
      return null;
    }

    const m = Math.floor((l + r) / 2);
    const root = new TreeNode(nums[m]);
    root.left = helper(l, m - 1);
    root.right = helper(m + 1, r);

    return root;
  }

  return helper(0, nums.length - 1);
}
// Time complexity: O(n)
// Space complexity: O(n)
