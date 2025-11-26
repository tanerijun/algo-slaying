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

        # Initially, we are always in a 'buying' state
        # (We don't own any stock and can only buy / cooldown)
        return dfs(0, True)

    # Time complexity: O(n)
    # Space complexity: O(n)
    def maxProfit2(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # dp[i][0]: max profit up to i, not holding, not in cooldown
        # dp[i][1]: max profit up to i, holding
        # dp[i][2]: max profit up to i, not holding, in cooldown
        dp = [[0] * 3 for _ in range(n)]

        # Base case for day 0
        dp[0][0] = 0  # not holding
        dp[0][1] = -prices[0]  # holding (bought today)
        dp[0][2] = float("-inf")  # can't be in cooldown on day 0

        for i in range(1, n):
            # not holding: either stayed not holding or came out of cooldown
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2])
            # holding: either kept holding or bought today
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            # cooldown: sold today
            dp[i][2] = dp[i - 1][1] + prices[i]

        # Max profit is either not holding (not in cooldown) or not holding (in cooldown, but cooldown ends)
        return max(dp[n - 1][0], dp[n - 1][2])

    # Time complexity: O(n)
    # Space complexity: O(1)
    def maxProfit3(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # prev0: max profit up to prev day, not holding, not in cooldown
        # prev1: max profit up to prev day, holding
        # prev2: max profit up to prev day, not holding, in cooldown
        prev0 = 0
        prev1 = -prices[0]
        prev2 = float("-inf")  # Can't be in cooldown on day 0

        for i in range(1, n):
            curr0 = max(prev0, prev2)
            curr1 = max(prev1, prev0 - prices[i])
            curr2 = prev1 + prices[i]
            prev0, prev1, prev2 = curr0, curr1, curr2

        # Max profit is either not holding (not in cooldown) or not holding (in cooldown)
        return max(prev0, prev2)
