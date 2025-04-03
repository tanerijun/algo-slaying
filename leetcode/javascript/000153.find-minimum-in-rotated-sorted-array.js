/**
 * @param {number[]} nums
 * @return {number}
 * Time complexity: O(log(n))
 * Space complexity: O(1)
 */
var findMin = function (nums) {
  let l = 0;
  let r = nums.length - 1;

  if (nums[l] < nums[r]) {
    return nums[l];
  }

  if (nums.length === 1) {
    return nums[0];
  }

  while (l <= r) {
    const m = Math.floor((l + r) / 2);
    if (m < nums.length && nums[m + 1] < nums[m]) {
      return nums[m + 1];
    }
    if (m > 0 && nums[m - 1] > nums[m]) {
      return nums[m];
    }
    if (nums[m] > nums[l]) {
      l = m + 1;
    } else if (nums[m] < nums[l]) {
      r = m - 1;
    }
  }
};
