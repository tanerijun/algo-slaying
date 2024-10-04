export function threeSum(nums: number[]): number[][] {
  const res: number[][] = [];

  nums.sort((a, b) => a - b); // Sort list from low to high

  // We only need to loop until nums.length - 2 because
  // the last 2 spaces will checked by our l and r pointers.
  //  Ex: [-1, -1, 0, 2, 3]
  //      [        i, l, r]
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue; // Skip duplicates

    let l = i + 1;
    let r = nums.length - 1;

    while (l < r) {
      const sum = nums[i] + nums[l] + nums[r];

      if (sum === 0) {
        res.push([nums[i], nums[l], nums[r]]);

        while (l < r && nums[l + 1] === nums[l]) {
          l++;
        }

        while (l < r && nums[r - 1] === nums[r]) {
          r--;
        }

        l++;
        r--;
      } else if (sum < 0) {
        l++;
      } else {
        r--;
      }
    }
  }

  return res;
}
