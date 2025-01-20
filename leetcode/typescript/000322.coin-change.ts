// Time complexity: O(n)
// Space complexity: O(n)
function coinChange(coins: number[], amount: number): number {
  const dp = [0]; // represents least coin needed for i amount
  for (let i = 1; i <= amount; i++) {
    dp[i] = Infinity;
    for (const coin of coins) {
      if (coin > i) continue;
      dp[i] = Math.min(dp[i], 1 + dp[i - coin]);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}
