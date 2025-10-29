/**
 * @param {number[]} nums
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var jump = function (nums) {
  let jumps = 0;
  let currentEnd = 0; // end of current's jump range
  let maxReach = 0; // farthest we can reach in current range

  for (let i = 0; i < nums.length - 1; i++) {
    maxReach = Math.max(maxReach, i + nums[i]);
    if (i === currentEnd) {
      jumps++;
      currentEnd = maxReach;
    }
  }

  return jumps;
};
