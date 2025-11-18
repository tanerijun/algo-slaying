class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxProfit(self, prices: list[int]) -> int:
        # Store: How much maxProfit if buying/skipping prices[i]
        dp = {}  # key = (i, state), val = maxProfit

        # State can either be buying or selling.
        # When state is buying, we have options to buy stock or cooldown.
        # When state is selling, we have options to sell or cooldown.
        # When state is buy or cooldown, we increment next i buy 1.
        # WHen state is sell, we increment next i buy 2 (because we're forced to cooldown).
        def dfs(i: int, buying: bool):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            # If we cooldown
            cooldown = dfs(i + 1, buying)

            if buying:
                # If we buy
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                # If we sell
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        return dfs(0, True)
