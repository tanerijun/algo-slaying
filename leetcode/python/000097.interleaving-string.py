class Solution:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # Key: A tuple (i, j) representing the current indices in s1 and s2.
        # Value: A boolean indicating whether s3[i+j:] can be formed by interleaving s1[i:] and s2[j:].
        cache = {}

        def dfs(i, j):
            # If we have exhausted both s1 and s2, it means s3 has been successfully
            # formed by interleaving s1 and s2 up to this point.
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in cache:
                return cache[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True
            cache[(i, j)] = False
            return False

        return dfs(0, 0)

    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        # dp[i][j] will represent if s1[:i] and s2[:j] can form s3[:i+j]
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]
