class Solution:
    # Time complexity: O(n^3) - For each state (O(n)), we handle the subarray (O(n^2))
    # Space complexity: O(n^2) - Memoization table
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]  # handle out of bounds
        dp = {}  # store dfs(l, r) -> key: (l, r), value: max coins

        # DFS function returns the max coins obtained from bursting all balloons in the range (l, r).
        def dfs(l, r):
            # Cached
            if (l, r) in dp:
                return dp[(l, r)]

            # No balloons exist here
            if l > r:
                return 0

            dp[(l, r)] = 0

            # We assume i is the last balloon to burst in this specific range
            for i in range(l, r + 1):
                # Calculate coins gained:
                # 1. nums[l-1] * nums[i] * nums[r+1]:
                #    Since 'i' is the LAST to burst, the balloons strictly inside (l, i)
                #    and (i, r) are already gone.
                #    So, 'i' is effectively adjacent to the fixed boundaries 'l-1' and 'r+1'.
                # 2. dfs(l, i - 1): Max coins from the left sub-problem (before 'i' bursts).
                # 3. dfs(i + 1, r): Max coins from the right sub-problem (before 'i' bursts).
                coins = (
                    nums[l - 1] * nums[i] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r)
                )
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        # remember that the array was padded
        return dfs(1, len(nums) - 2)

    # Time complexity: O(n^3)
    # Space complexity: O(n^2)
    def maxCoins2(self, nums: list[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]

        # dp[l][r] represents max coins for range starting at l and ending at r
        # The size is n + 2 to accommodate the padded indices
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # We need to populate the DP table.
        # In Interval DP, we must calculate smaller ranges before larger ranges.
        #
        # Outer Loop 'l': Iterate backwards from the last balloon to the first.
        # Why backwards? Because to solve for range (l, r), we need the results
        # of inner ranges like (l+1, r). By going backwards, we ensure rows
        # below us (larger indices) are already filled.
        for l in range(n, 0, -1):
            # Middle Loop 'r': Iterate from 'l' to the end.
            # This defines the right boundary of our current window [l, r].
            for r in range(l, n + 1):
                # Inner Loop 'i': The pivot choice.
                # We try every balloon 'i' inside [l, r] as the LAST one to burst.
                for i in range(l, r + 1):
                    coins = (
                        # The coins we get from bursting 'i' last.
                        # It sees boundaries l-1 and r+1.
                        new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                        # Add max coins from the sub-range to the left of i
                        + dp[l][i - 1]
                        # Add max coins from the sub-range to the right of i
                        + dp[i + 1][r]
                    )
                    # Store the maximum coins obtainable for range [l, r]
                    dp[l][r] = max(dp[l][r], coins)

        # Return the result for the full range [1, n]
        return dp[1][n]
