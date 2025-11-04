/**
 * @param {number[]} nums
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(1)
 * There are two cases for where the maximum sum subarray can be:
 * 1. The max subarray is in the middle (like a normal array)
 * 2. The max subarray wraps around the edges
 * If the subarray wraps around, then the elements we DON'T include form a minimum subarray in the middle!
 * Intuition: To maximize prefix + suffix, we have to minimize the middle array. Therefore, total - min subarray.
 * Edge case: If all numbers are negative, `total - minSum` would give 0 (we'd be removing everything),
 * but the answer should be the least negative number. So we return `maxSum` instead.
 */
var maxSubarraySumCircular = function (nums) {
  let total = 0;
  let maxSum = nums[0];
  let minSum = nums[0];
  let curMax = 0;
  let curMin = 0;
  for (const num of nums) {
    curMax = Math.max(curMax + num, num);
    maxSum = Math.max(maxSum, curMax);
    curMin = Math.min(curMin + num, num);
    minSum = Math.min(minSum, curMin);
    total += num;
  }
  return maxSum > 0 ? Math.max(maxSum, total - minSum) : maxSum;
};
