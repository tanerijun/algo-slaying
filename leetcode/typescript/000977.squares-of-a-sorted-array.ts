function sortedSquares(nums: number[]): number[] {
  const ans: number[] = Array(nums.length).fill(0);
  let l = 0;
  let r = nums.length - 1;
  let i = nums.length - 1;
  while (i >= 0) {
    if (nums[r] > Math.abs(nums[l])) {
      ans[i] = nums[r] * nums[r];
      r--;
    } else {
      ans[i] = nums[l] * nums[l];
      l++;
    }
    i--;
  }
  return ans;
}
// Time complexity: O(n)
// Space complexity: O(1)
