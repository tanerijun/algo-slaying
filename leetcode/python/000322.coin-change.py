class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return -1 if dp[amount] == float('inf') else dp[amount]
