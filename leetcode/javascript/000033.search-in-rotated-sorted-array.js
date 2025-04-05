/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 * Time complexity: O(log(n))
 * Space complexity: O(1)
 */
var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const val = nums[mid];

    if (val === target) return mid;

    // left half is sorted
    if (nums[left] <= val) {
      if (nums[left] <= target && target < nums[mid]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    } else {
      if (nums[mid] < target && target <= nums[right]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
  }
  return -1;
};
