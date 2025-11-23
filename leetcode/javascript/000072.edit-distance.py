class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        cache = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in cache:
                return cache[(i, j)]
            if word1[i] == word2[j]:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = 1 + min(dfs(i, j + 1), dfs(i + 1, j), dfs(i + 1, j + 1))
            return cache[(i, j)]

        return dfs(0, 0)

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def minDistance1(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[m][j] = n - j
        for i in range(m + 1):
            dp[i][n] = m - i

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])

        return int(dp[0][0])

    # Time complexity: O(m * n)
    # Space complexity: O(n)
    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [float("inf")] * (n + 1)

        for j in range(n + 1):
            dp[j] = n - j

        for i in range(m - 1, -1, -1):
            next_dp = [float("inf")] * (n + 1)
            next_dp[n] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    next_dp[j] = dp[j + 1]
                else:
                    next_dp[j] = 1 + min(next_dp[j + 1], dp[j], dp[j + 1])
            dp = next_dp

        return int(dp[0])

    # Time complexity: O(m * n)
    # Space complexity: O(min(m, n))
    def minDistance3(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return self.minDistance3(word2, word1)

        m, n = len(word1), len(word2)
        dp = [float("inf")] * (n + 1)

        for j in range(n + 1):
            dp[j] = n - j

        for i in range(m - 1, -1, -1):
            next_dp = [float("inf")] * (n + 1)
            next_dp[n] = m - i
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    next_dp[j] = dp[j + 1]
                else:
                    next_dp[j] = 1 + min(next_dp[j + 1], dp[j], dp[j + 1])
            dp = next_dp

        return int(dp[0])
