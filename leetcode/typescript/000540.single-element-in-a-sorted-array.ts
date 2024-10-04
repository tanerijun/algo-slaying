function singleNonDuplicate(nums: number[]): number {
  let l = 0;
  let r = nums.length;

  while (l <= r) {
    const m = Math.floor((l + r) / 2);
    // If nums[m] is not unique, the pair will be either on it's left or on it's right
    let pairIndex = nums[m] === nums[m - 1]
      ? m - 1
      : nums[m] === nums[m + 1]
      ? m + 1
      : -1;

    console.log(m, pairIndex);

    // nums[m] is unique
    if (pairIndex === -1) {
      return nums[m];
    }

    // Continue searching the side where the length is odd
    if ((Math.min(pairIndex, m) - l) % 2 === 0) {
      l = Math.max(m, pairIndex) + 1;
      console.log("Update l to", l);
    } else {
      r = Math.min(m, pairIndex) - 1;
      console.log("Update r to", r);
    }
  }

  return -1; // shouldn't happen
}
// Time complexity: O(n)
// Space complexity: O(1)
