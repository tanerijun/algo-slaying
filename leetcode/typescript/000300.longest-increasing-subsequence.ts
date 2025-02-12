// Time complexity: O(n^2)
// Space complexity: O(n)
function lengthOfLIS(nums: number[]): number {
  // Init dp array with 1 (min subsequence length starting at that number)
  const dp: number[] = Array(nums.length).fill(1);

  for (let i = nums.length - 2; i >= 0; i--) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] > nums[i]) {
        dp[i] = Math.max(dp[i], 1 + dp[j]);
      }
    }
  }

  return Math.max(...dp);
}
