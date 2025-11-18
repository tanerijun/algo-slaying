class Solution:
    # Time complexity: O(n * m)
    # Space complexity: O(n * m)
    def change(self, amount: int, coins: list[int]) -> int:
        # key => tuple (i, a) representing (coin_index, current_accumulated_amount)
        # value => number of ways to make the remaining amount (amount - a) using coins from index 'i' onwards
        cache = {}

        # i: The current index of the coin we are considering in the 'coins' array.
        # a: The current accumulated amount formed by the coins chosen so far.
        def dfs(i: int, a: int):
            # Base Case 1: If the accumulated amount 'a' equals the target 'amount',
            # we have found one valid combination.
            if a == amount:
                return 1
            # Base Case 2: If the accumulated amount 'a' exceeds the target 'amount',
            # this path is invalid, so return 0 ways.
            if a > amount:
                return 0
            # Base Case 3: If we have exhausted all coins (i.e., 'i' is beyond the
            # last coin index) but haven't reached the target amount, this path
            # cannot form the target, so return 0 ways.
            if i == len(coins):
                return 0
            # Memoization check: If this subproblem (i, a) has already been computed,
            # return its cached result to avoid re-calculation.
            if (i, a) in cache:
                return cache[(i, a)]

            # Recursive Step: This is where we explore two possibilities for the current coin coins[i]:
            #
            # 1. Include the current coin (dfs(i, a + coins[i])):
            #    We use coins[i] and add its value to the current accumulated amount 'a'.
            #    We remain at the same coin index 'i' because we can use the same coin
            #    multiple times to form combinations.
            #
            # 2. Exclude the current coin (dfs(i + 1, a)):
            #    We do not use coins[i]. We move to the next coin (i + 1) in the array,
            #    and the accumulated amount 'a' remains unchanged.
            #
            # The total ways for the current subproblem (i, a) is the sum of ways from these two branches.
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        # Initial call to start the DFS:
        # We begin by considering the first coin (index 0) and an initial accumulated amount of 0.
        return dfs(0, 0)

    # Time complexity: O(n * m)
    # Space complexity: O(n * m)
    def change2(self, amount: int, coins: list[int]) -> int:
        # Initialize a 2D DP table.
        # dp[a][i] will store the number of ways to make 'amount a'
        # using coins from index 'i' up to the end of the 'coins' array.
        #
        # Rows: 'amount + 1' for amounts from 0 to 'amount'.
        # Columns: 'len(coins) + 1' for coin indices from 0 to len(coins).
        # The 'len(coins)' column (i.e., dp[a][len(coins)]) will represent
        # the base case of having no more coins to consider.
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]

        # Base case initialization:
        # There is always one way to make an amount of 0 (by selecting no coins),
        # regardless of which coins are available from index 'i' onwards.
        # So, for amount 0, all cells in that row are 1.
        dp[0] = [1] * (len(coins) + 1)

        # Build up solutions for smaller amounts first.
        for a in range(1, amount + 1):
            # Iterate through coins in reverse order (from last coin to first).
            # This order is important because dp[a][i+1] (which represents not using coins[i])
            # must be computed before we calculate dp[a][i].
            for i in range(len(coins) - 1, -1, -1):
                # Option 1: Do NOT use the current coin (coins[i]).
                # In this case, the number of ways to make amount 'a' using coins
                # from index 'i' onwards is the same as the number of ways to
                # make 'a' using coins from index 'i + 1' onwards.
                dp[a][i] = dp[a][i + 1]

                # Option 2: Use the current coin (coins[i]).
                # This is only possible if the current amount 'a' is greater than
                # or equal to the coin's value.
                if a - coins[i] >= 0:
                    # If we use coins[i], we need to find the number of ways to make
                    # the remaining amount (a - coins[i]). Since we can use the
                    # same coin multiple times, we look up this value from dp[a - coins[i]][i]
                    # (i.e., still considering coins from index 'i' onwards).
                    # We add this to the ways found in Option 1.
                    dp[a][i] += dp[a - coins[i]][i]

        # The final answer is stored in dp[amount][0].
        # This represents the number of ways to make the target 'amount'
        # using coins starting from index 0 (i.e., all available coins).
        return dp[amount][0]

    # Time complexity: O(n * m)
    # Space complexity: O(n)
    def change3(self, amount: int, coins: list[int]) -> int:
        # dp[j] will store the number of ways to make amount j
        # using the coins considered up to the current point in the outer loop.
        dp = [0] * (amount + 1)

        # Base case: There is one way to make an amount of 0 (by using no coins).
        dp[0] = 1

        # Iterate through each coin available.
        # By processing coins one by one,
        # we ensure that combinations like [1, 2] and [2, 1] are not double-counted.
        for coin in coins:
            # We start from 'coin' because we can only form amounts greater than or
            # equal to the current coin's value if we use this coin.
            for j in range(coin, amount + 1):
                # The DP recurrence relation:
                # dp[j] (new) = dp[j] (old) + dp[j - coin]
                #
                # dp[j] (old): Represents the number of ways to make amount 'j'
                #              WITHOUT using the current 'coin'. These are the ways
                #              formed by previous coins.
                #
                # dp[j - coin]: Represents the number of ways to make the 'remaining'
                #               amount (j - coin). If we use the current 'coin',
                #               we need to find how many ways there are to form 'j - coin'
                #               using any of the coins processed so far (including the
                #               current 'coin' if it was used to form j - coin in
                #               a previous iteration of this inner loop, or previous coins).
                #
                # By adding these two, we get the total number of ways to make amount 'j'
                # by either NOT using the current 'coin', or by USING the current 'coin'.
                dp[j] += dp[j - coin]

        return dp[amount]
