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

// Time complexity: O(n^2)
// Space complexity: O(n)
function LengthOfLIS2(nums: number[]): number {
  const dp: number[] = Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    for (let j = 0; j < i; j++) {
      if (nums[i] > nums[j]) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }

  return Math.max(...dp);
}

// Algorithm:
// - Greedily maintain a tails array where tails[i] is the smallest possible tail element for any increasing subsequence of length i+1.
// - For each number:
//   - If it's larger than everything in tails → extend the LIS by appending it
//   - Otherwise → replace the first element in tails that is ≥ the current number
// Time complexity: O(n(log(n)))
// Space complexity: O(n)
function LengthOfLIS3(nums: number[]): number {
  const tails: number[] = [];

  for (const num of nums) {
    let l = 0;
    let r = tails.length - 1;

    while (l <= r) {
      const m = Math.floor((l + r) / 2);
      if (tails[m] < num) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    }

    tails[l] = num;
  }

  return tails.length;
}
