function search(nums: number[], target: number): number {
  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    const m = Math.floor((l + r) / 2);

    if (target === nums[m]) {
      return m;
    }

    if (nums[m] >= nums[l]) {
      // If m is part of left sorted array. Ex: 4 5 6 7 0 1 2
      if (target < nums[l] || target > nums[m]) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    } else {
      // If m is part of right sorted array. Ex: 6 7 0 1 2 4 5
      if (target > nums[m] && target <= nums[r]) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    }
  }

  return -1;
}
// Time complexity: O(log(n))
// Space complexity: O(1)
