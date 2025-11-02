/**
 * @param {number[]} nums
 * @return {number}
 * Time complexity: O(n)
 * Space complexity: O(1)
 */
var maxSubArray = function (nums) {
  let res = nums[0];
  let curSum = 0;
  for (const num of nums) {
    if (curSum < 0) curSum = 0;
    curSum += num;
    res = Math.max(res, curSum);
  }
  return res;
};
