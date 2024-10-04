function threeSum(nums: number[]): number[][] {
  if (nums.length < 3) {
    return [];
  }

  const res: number[][] = [];

  nums.sort((a, b) => a - b);

  for (let i = 0; i <= nums.length - 3; i++) {
    // Skip duplicates
    if (i > 0 && nums[i] === nums[i - 1]) {
      continue;
    }

    // It's impossible for sum to be 0 at this point
    // because the array is sorted, and the next numbers are all >= nums[i]
    if (nums[i] > 0) {
      break;
    }

    // Two sum on sorted array
    let l = i + 1;
    let r = nums.length - 1;
    const target = 0 - nums[i];
    while (l < r) {
      // Skip duplicates
      if (l > i + 1 && nums[l] === nums[l - 1]) {
        l++;
        continue;
      }

      const sum = nums[l] + nums[r];
      if (sum > target) {
        r--;
      } else if (sum < target) {
        l++;
      } else {
        res.push([nums[i], nums[l], nums[r]]);
        l++;
        r--;
      }
    }
  }

  return res;
}
// Time complexity: O(n^2)
// Space complexity: O(1)
