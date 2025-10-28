/**
 * @param {number[]} nums
 * @return {boolean}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var canJump = function (nums) {
  let maxReach = 0; // furthest reachable index

  for (let i = 0; i < nums.length - 1; i++) {
    if (i > maxReach) return false;
    maxReach = Math.max(maxReach, i + nums[i]);
    if (maxReach >= nums.length - 1) return true;
  }

  return true;
};
