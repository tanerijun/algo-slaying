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
// Space complexity: O(n)
function kthSmallest(root: TreeNode | null, k: number): number {
  const nums: number[] = [];
  function dfs(node: TreeNode | null) {
    if (!node) return;
    dfs(node.left);
    nums.push(node.val);
    dfs(node.right);
  }
  dfs(root);

  return nums[k - 1];
}

// Time complexity: O(H + k), when k is small the complexity is close to H, when k is close to n the complexity is close to n
// Space complexity: O(H)
function kthSmallest2(root: TreeNode | null, k: number): number {
  const stack: TreeNode[] = [];
  let cur: TreeNode | null = root;
  while (cur || stack) {
    while (cur) {
      stack.push(cur);
      cur = cur.left;
    }
    cur = stack.pop()!;
    k--;
    if (k == 0) return cur.val;
    cur = cur.right;
  }
  return -1; // won't happen
}
