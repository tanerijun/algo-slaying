function minSubArrayLen(target: number, nums: number[]): number {
  let res = Number.MAX_SAFE_INTEGER;
  let sum = nums[0];
  let l = 0;
  let r = 0;

  while (l < nums.length) {
    // Early return on ideal window size
    if (nums[r] >= target) {
      return 1;
    }

    if (sum < target) {
      if (r + 1 < nums.length) {
        r++;
        sum += nums[r];
      } else {
        break;
      }
    } else {
      res = Math.min(res, r - l + 1);
      sum -= nums[l];
      l++;
    }
  }

  return res === Number.MAX_SAFE_INTEGER ? 0 : res;
}
// Time complexity: O(n)
// Space complexity: O(1)
