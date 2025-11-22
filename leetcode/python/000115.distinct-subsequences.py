class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
            cache[(i, j)] = res
            return res

        return dfs(0, 0)

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def numDistinct2(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # dp[i][j] = the number of distinct subsequences of the suffix t[j:] found inside the suffix s[i:].
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            # when j == n, the t string is empty
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # If we ignore s[i], the number of ways to form t[j:]
                # is the same as the number of ways to form it using the remaining suffix s[i+1:].
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    # If we use s[i] to match t[j], we now need to find how many ways the rest of s (s[i+1:])
                    # can form the rest of t (t[j+1:]). We add this count to our total.
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

    # Time complexity: O(m * n)
    # Space complexity: O(n)
    def numDistinct3(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(m - 1, -1, -1):
            next_dp = [0] * (n + 1)
            next_dp[n] = 1
            for j in range(n - 1, -1, -1):
                next_dp[j] = dp[j]
                if s[i] == t[j]:
                    next_dp[j] += dp[j + 1]
            dp = next_dp

        return dp[0]

    # Time complexity: O(m * n)
    # Space complexity: O(n)
    def numDistinct4(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[n] = 1  # base Case: Empty t matches anything once

        for i in range(m - 1, -1, -1):
            # This represents dp[i+1][n], which is always 1.
            # It serves as the "diagonal" for the first iteration (j=n-1).
            prev = 1
            for j in range(n - 1, -1, -1):
                # 1. Capture the "Down" value (dp[i+1][j])
                res = dp[j]
                if s[i] == t[j]:
                    res += prev

                # Before we overwrite dp[j] with the new result,
                # we store its OLD value into 'prev'.
                # This old value becomes the "Diagonal" for the next loop iteration (j-1).
                prev = dp[j]

                dp[j] = res

        return dp[0]
