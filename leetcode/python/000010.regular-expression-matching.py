class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if j == len(p):
                return i == len(s)

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                # Use the * (only if match) or skip the *
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return cache[(i, j)]

            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def isMatch1(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2]
                    if match:
                        dp[i][j] = dp[i + 1][j] or dp[i][j]
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]

        return dp[0][0]

    # Time complexity: O(m * n)
    # Space complexity: O(n)
    def isMatch2(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True

        for i in range(len(s), -1, -1):
            next_dp = [False] * (len(p) + 1)
            next_dp[len(p)] = i == len(s)

            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    next_dp[j] = next_dp[j + 2]
                    if match:
                        next_dp[j] |= dp[j]
                elif match:
                    next_dp[j] = dp[j + 1]

            dp = next_dp

        return dp[0]
