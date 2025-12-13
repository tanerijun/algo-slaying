from functools import lru_cache


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def longestPalindromeSubseq(self, s: str) -> int:
        def longestCommonSubsequence(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if s1[i] == s2[j]:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

            return dp[0][0]

        return longestCommonSubsequence(s, s[::-1])

    # Time complexity: O(n^2)
    # Space complexity: O(n^2)
    def longestPalindromeSubseq1(self, s: str) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            if l == r:
                return 1  # single character is always a palindrome
            if s[l] == s[r]:
                # Characters match! Include both and recurse on the inner substring
                return 2 + dfs(l + 1, r - 1)
            else:
                # Characters don't match. Try skipping either the left or right character
                return max(dfs(l + 1, r), dfs(l, r - 1))

        return dfs(0, len(s) - 1)
