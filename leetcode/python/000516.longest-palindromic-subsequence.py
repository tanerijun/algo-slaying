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
