class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] += dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]

    # Time complexity: O(m * n)
    # Space complexity: O(n)
    def uniquePaths1(self, m: int, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n - 1] = 1
        for i in range(m - 1, -1, -1):
            next_dp = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                next_dp[j] += dp[j] + next_dp[j + 1]
            dp = next_dp
        return dp[0]

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def uniquePaths2(self, m: int, n: int) -> int:
        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r == m - 1 and c == n - 1:
                return 1
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]

        return dfs(0, 0)
