/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 * Time complexity: O(n)
 * Space complexity: O(h) - recursion stack
 */
var isBalanced = function (root) {
  function checkBalance(node) {
    if (!node) {
      return 0;
    }

    const leftHeight = checkBalance(node.left);
    if (leftHeight === -1) return -1;

    const rightHeight = checkBalance(node.right);
    if (rightHeight === -1) return -1;

    if (Math.abs(rightHeight - leftHeight) > 1) {
      return -1;
    }

    return 1 + Math.max(leftHeight, rightHeight);
  }

  return checkBalance(root) !== -1;
};
