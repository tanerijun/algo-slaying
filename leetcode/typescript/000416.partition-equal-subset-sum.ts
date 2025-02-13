// Time complexity: O(2^n)
// Space complexity: O(n)
function canPartition(nums: number[]): boolean {
  const sum = nums.reduce((a, b) => a + b);
  if (sum % 2 !== 0) return false;

  function dfs(nums: number[], i: number, target: number): boolean {
    if (i === nums.length) return target === 0;

    if (target < 0) return false;

    return dfs(nums, i + 1, target) || dfs(nums, i + 1, target - nums[i]);
  }

  return dfs(nums, 0, sum / 2);
}

// Time complexity: O(n * target)
// Space complexity: O(n * target)
function canPartition2(nums: number[]): boolean {
  const sum = nums.reduce((a, b) => a + b);
  if (sum % 2 !== 0) return false;
  const n = nums.length;
  const memo = Array.from(Array(n + 1), () => Array(sum / 2 + 1).fill(null));

  function dfs(nums: number[], i: number, target: number): boolean {
    if (i === nums.length) return target === 0;

    if (target < 0) return false;

    if (memo[i][target] !== null) return memo[i][target];

    memo[i][target] = dfs(nums, i + 1, target) ||
      dfs(nums, i + 1, target - nums[i]);

    return memo[i][target];
  }

  return dfs(nums, 0, sum / 2);
}

// Time complexity: O(n * target)
// Space complexity: O(n * target)
function canPartition3(nums: number[]): boolean {
  const sum = nums.reduce((a, b) => a + b, 0);
  if (sum % 2 !== 0) return false;
  const target = sum / 2;
  const n = nums.length;

  const dp = Array.from(Array(n + 1), () => Array(target + 1).fill(false));

  for (let i = 0; i <= n; i++) {
    dp[i][0] = true;
  }

  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= target; j++) {
      if (nums[i - 1] <= j) {
        dp[i][j] = dp[i - 1][j] ||
          dp[i - 1][j - nums[i - 1]];
      } else {
        dp[i][j] = dp[i - 1][j];
      }
    }
  }

  return dp[n][target];
}

// Time complexity: O(n * target)
// Space complexity: O(n * target)
function canPartition4(nums: number[]): boolean {
  const sum = nums.reduce((a, b) => a + b, 0);
  if (sum % 2 !== 0) return false;
  const target = sum / 2;

  let dp = new Set<number>([0]);

  for (let i = 0; i < nums.length; i++) {
    const nextDp = new Set<number>();
    for (const t of dp) {
      nextDp.add(t + nums[i]);
      nextDp.add(t);
    }
    dp = nextDp;
  }

  return dp.has(target);
}

// Time complexity: O(n * target)
// Space complexity: O(n * target)
function canPartition5(nums: number[]): boolean {
  const sum = nums.reduce((a, b) => a + b, 0);
  if (sum % 2 !== 0) return false;
  const target = sum / 2;

  let dp = new Set<number>([0]);

  for (let i = 0; i < nums.length; i++) {
    const nextDp = new Set<number>();
    for (const t of dp) {
      if (t + nums[i] === target) return true;
      nextDp.add(t + nums[i]);
      nextDp.add(t);
    }
    dp = nextDp;
  }

  return false;
}
